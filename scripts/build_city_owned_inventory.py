#!/usr/bin/env python3
"""Reconcile City of Dayton property ownership across the City and County records.

Usage:
    ./build_city_owned_inventory.py <taxroll.csv> <city_owned_parcels.json>
                                    <address_bridge.json> <outdir>

Neither source alone answers "what does the City own":

  * The City's own GIS layer carries intent (DEPARTMENT, INTENDEDUSE) but was
    last edited in July 2021 and holds 1,912 parcels.
  * The County tax roll is authoritative for ownership and refreshed daily, but
    has no field describing what the City holds a parcel *for*.

They agree on only 1,688 parcels. This joins them, records which source each
parcel came from, and flags development candidates using the County's own land
use coding rather than a heuristic.

Owner-name matching is deliberately conservative: a naive "city" + "dayton"
string match pulls in 123 parcels belonging to other entities, 107 of them the
school district, which is a separate legal body.
"""
import argparse
import collections
import csv
import json
import os
import re

# Entities whose owner name contains both words but which are not the municipal
# corporation. The school district is the big one.
NOT_CITY = re.compile(
    r"BOARD OF EDUCATION|BD OF ED|CITY SCH|SCHOOL|CHURCH|MINISTR|\bLLC\b|\bINC\b|"
    r"NON PROFIT|CORP\b|BD OF CO COMM|COUNTY|UNIVERSITY|HOSPITAL|HOUSING AUTH|METRO",
    re.I)
# The municipal corporation, in the spellings the tax roll actually uses.
IS_CITY = re.compile(
    r"^\s*(THE\s+)?CITY OF DAYTON\b|^\s*DAYTON,?\s*(OH(IO)?)?,?\s*CITY OF\b|"
    r"^\s*DAYTON CITY OH OF\b", re.I)

LUC_DESC = {
    "300": "Industrial, vacant land", "400": "Commercial vacant land",
    "500": "Residential vacant land, lot", "600": "Exempt, owned by USA",
    "613": "Exempt land only", "620": "Exempt, owned by counties",
    "640": "Exempt, owned by municipals", "665": "Exempt (unspecified)",
    "685": "Churches etc, public worship",
}
# Vacant land classes — the County's own coding, not an inference.
VACANT_LUC = {"300", "400", "500"}


def num(v):
    try:
        return float(str(v).strip().lstrip("0") or 0)
    except (TypeError, ValueError):
        return 0.0


def load_taxroll(path):
    out = {}
    with open(path, newline="", encoding="utf-8", errors="replace") as f:
        r = csv.reader(f)
        hdr = [h.strip() for h in next(r)]
        ix = {k: hdr.index(k) for k in
              ("PARCELID", "OWNERNAME1", "OWNERNAME2", "CLS", "LUC", "ASMTBLDG",
               "ASMTLAND", "ASMTTOTAL", "PARCELLOCATION", "CITY/TOWNSHIP",
               "ACRES", "CENSUS TRACT", "NBHD")}
        for row in r:
            if len(row) <= max(ix.values()):
                continue
            owner = row[ix["OWNERNAME1"]].strip()
            if not IS_CITY.search(owner) or NOT_CITY.search(
                    owner + " " + row[ix["OWNERNAME2"]]):
                continue
            out[row[ix["PARCELID"]].strip()] = {
                k.lower().replace("/", "_").replace(" ", "_"): row[i].strip()
                for k, i in ix.items()}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("taxroll")
    ap.add_argument("city_layer")
    ap.add_argument("bridge")
    ap.add_argument("outdir")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)

    county = load_taxroll(a.taxroll)
    city = {}
    for p in json.load(open(a.city_layer))["parcels"]:
        pid = (p.get("PARCELID") or "").strip()
        if pid:
            city[pid] = p

    # Address points cover addressed parcels; many City holdings are vacant lots
    # and rights-of-way with no address, so parcel centroids fill the gap.
    bridge = json.load(open(a.bridge))
    coords = {}
    for rec in bridge["by_addrkey"].values():
        if rec.get("parcel") and rec.get("lat") and rec["parcel"] not in coords:
            coords[rec["parcel"]] = (rec["lat"], rec["lon"])
    cpath = os.path.join(os.path.dirname(a.bridge), "parcel_centroids.json")
    if os.path.exists(cpath):
        for pid, (lat, lon) in json.load(open(cpath)).items():
            coords.setdefault(pid, (lat, lon))

    rows = []
    for pid in sorted(set(county) | set(city)):
        c, g = county.get(pid), city.get(pid)
        source = ("both" if c and g else "county_only" if c else "city_layer_only")
        luc = (c or {}).get("luc", "")
        bldg = num((c or {}).get("asmtbldg"))
        intended = str((g or {}).get("INTENDEDUSE") or "").strip()
        dept = str((g or {}).get("DEPARTMENT") or "").strip()

        # Development candidate: County classes it as vacant land, or the City
        # has explicitly flagged it Surplus/Development. Anything with a
        # building is excluded — that is a facility, not a site.
        candidate = bool(
            (luc in VACANT_LUC or intended in ("Surplus", "Development"))
            and bldg == 0)

        lat, lon = coords.get(pid, ("", ""))
        rows.append({
            "parcel": pid,
            "source": source,
            "owner_name": (c or {}).get("ownername1", ""),
            "address": (c or {}).get("parcellocation", ""),
            "jurisdiction": (c or {}).get("city_township", ""),
            "luc": luc,
            "luc_desc": LUC_DESC.get(luc, ""),
            "parcel_class": (c or {}).get("cls", ""),
            "acres": (c or {}).get("acres", ""),
            "assessed_land": (c or {}).get("asmtland", ""),
            "assessed_bldg": (c or {}).get("asmtbldg", ""),
            "has_building": "Y" if bldg > 0 else "N",
            "city_department": dept,
            "city_intended_use": intended,
            "development_candidate": "Y" if candidate else "N",
            "census_tract": (c or {}).get("census_tract", ""),
            "lat": lat, "lon": lon,
        })

    path = os.path.join(a.outdir, "city_owned_properties.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    cand = [r for r in rows if r["development_candidate"] == "Y"]
    with open(os.path.join(a.outdir, "city_owned_development_candidates.csv"),
              "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(cand)

    feats = [{"type": "Feature",
              "geometry": {"type": "Point",
                           "coordinates": [round(float(r["lon"]), 6),
                                           round(float(r["lat"]), 6)]},
              "properties": {k: v for k, v in r.items() if k not in ("lat", "lon")}}
             for r in rows if r["lat"] != ""]
    with open(os.path.join(a.outdir, "city_owned_properties.geojson"), "w") as f:
        json.dump({"type": "FeatureCollection", "features": feats}, f)

    src = collections.Counter(r["source"] for r in rows)
    print(f"reconciled parcels        : {len(rows):,}")
    for k in ("both", "county_only", "city_layer_only"):
        print(f"    {k:<18}{src[k]:>7,}")
    print(f"  with a building         : {sum(1 for r in rows if r['has_building']=='Y'):,}")
    print(f"  development candidates  : {len(cand):,}")
    print(f"  geocoded                : {len(feats):,}")
    print(f"\nwrote 3 files to {a.outdir}/")


if __name__ == "__main__":
    main()
