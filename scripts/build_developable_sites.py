#!/usr/bin/env python3
"""Build a developable-sites layer for Dayton.

Usage:
    ./build_developable_sites.py <taxroll.csv> <hcs_grades.json>
                                 <address_bridge.json> <outdir>

Two site types, per the 2026 Bowen recommendation to "inventory developable
sites — undeveloped land and underutilized structures":

  vacant_land       County land use codes 300/400/500 (industrial, commercial,
                    residential vacant land), any owner
  vacant_structure  Church, school or warehouse parcels carrying a building
                    that the Housing Condition Survey records as vacant

No size or condition filter is applied. The universe is large — roughly 11,900
parcels — and most residential vacant lots are scattered infill rather than
development sites. Filtering criteria are a policy decision, so this emits the
full set with the attributes needed to filter it, plus a size distribution to
inform that conversation.

Owner portfolio counts are included because contiguous parcels under one owner
are the practical route to a site larger than a single lot.
"""
import argparse
import collections
import csv
import json
import os
import re

VACANT_LAND = {"300": "Industrial, vacant land",
               "400": "Commercial vacant land",
               "500": "Residential vacant land, lot"}
# Non-residential uses named in the Bowen recommendation as adaptive-reuse
# candidates. Only counted when the parcel carries a building AND the condition
# survey records it vacant.
REUSE = {"340": "Warehouse (industrial)", "440": "Warehouse", "445": "Warehouse",
         "447": "Warehouse / storage", "650": "Educational",
         "660": "Charitable / educational", "685": "Church / public worship"}
VACANT_STATUS = {"VB": "Vacant & boarded", "VS": "Vacant & secure",
                 "VTO": "Vacant, too damaged to board", "DEMO": "Demolition"}

LANDBANK = re.compile(r"LAND REUTILIZ|LAND BANK|LANDBANK", re.I)
CITY = re.compile(r"^\s*(THE\s+)?CITY OF DAYTON\b|^\s*DAYTON,?\s*(OH(IO)?)?,?\s*CITY OF\b", re.I)
PUBLIC = re.compile(r"BOARD OF EDUCATION|BD OF ED|COUNTY|STATE OF OHIO|UNITED STATES|"
                    r"HOUSING AUTH|METRO|PORT AUTH", re.I)


def num(v):
    try:
        return float(str(v).strip().lstrip("0") or 0)
    except (TypeError, ValueError):
        return 0.0


def owner_type(name):
    if LANDBANK.search(name):
        return "land bank"
    if CITY.search(name):
        return "city"
    if PUBLIC.search(name):
        return "other public"
    if re.search(r"\bLLC\b|\bINC\b|\bLTD\b|CORP\b|COMPANY|\bLP\b|TRUST|\bTR\b", name, re.I):
        return "company / trust"
    return "individual"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("taxroll")
    ap.add_argument("hcs")
    ap.add_argument("bridge")
    ap.add_argument("outdir")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)

    hcs = {}
    for r in json.load(open(a.hcs)):
        p = (r.get("PARCELID") or "").strip()
        if p:
            hcs[p] = r

    coords = {}
    bridge = json.load(open(a.bridge))
    for rec in bridge["by_addrkey"].values():
        if rec.get("parcel") and rec.get("lat"):
            coords.setdefault(rec["parcel"], (rec["lat"], rec["lon"]))
    # Centroids are shared across scripts, so coverage cannot be assumed: this
    # file was originally built for the city-owned analysis and silently left
    # half the developable sites unmapped. Missing parcels are reported so the
    # gap is visible rather than looking like a property of the data.
    cpath = os.path.join(os.path.dirname(a.bridge), "parcel_centroids.json")
    centroids = json.load(open(cpath)) if os.path.exists(cpath) else {}
    for pid, (lat, lon) in centroids.items():
        coords.setdefault(pid, (lat, lon))

    rows = []
    with open(a.taxroll, newline="", encoding="utf-8", errors="replace") as f:
        rd = csv.reader(f)
        hdr = [h.strip() for h in next(rd)]
        ix = {k: hdr.index(k) for k in
              ("PARCELID", "LUC", "CLS", "ACRES", "ASMTLAND", "ASMTBLDG", "ASMTTOTAL",
               "PARCELLOCATION", "OWNERNAME1", "OWNERNAME2", "PADDR1", "PADDR3",
               "CITY/TOWNSHIP", "CENSUS TRACT", "NBHD", "YRBL")}
        for row in rd:
            if len(row) <= max(ix.values()):
                continue
            if row[ix["CITY/TOWNSHIP"]].strip().upper() != "DAYTON":
                continue
            luc = row[ix["LUC"]].strip()
            pid = row[ix["PARCELID"]].strip()
            bldg = num(row[ix["ASMTBLDG"]])
            h = hcs.get(pid) or {}
            status = (h.get("STATUS") or "").strip()

            if luc in VACANT_LAND:
                kind, desc = "vacant_land", VACANT_LAND[luc]
            elif luc in REUSE and bldg > 0 and status in VACANT_STATUS:
                kind, desc = "vacant_structure", REUSE[luc]
            else:
                continue

            owner = row[ix["OWNERNAME1"]].strip()
            lat, lon = coords.get(pid, ("", ""))
            rows.append({
                "parcel": pid,
                "site_type": kind,
                "use_desc": desc,
                "acres": row[ix["ACRES"]].strip(),
                "address": row[ix["PARCELLOCATION"]].strip(),
                "owner_name": owner,
                "owner_type": owner_type(owner),
                "owner_mailing": (row[ix["PADDR1"]].strip() + ", "
                                  + row[ix["PADDR3"]].strip()).strip(", "),
                "luc": luc,
                "parcel_class": row[ix["CLS"]].strip(),
                "assessed_land": row[ix["ASMTLAND"]].strip(),
                "assessed_bldg": row[ix["ASMTBLDG"]].strip(),
                "assessed_total": row[ix["ASMTTOTAL"]].strip(),
                "year_built": row[ix["YRBL"]].strip(),
                "hcs_grade": h.get("GRADE_DESC") or "",
                "hcs_status": VACANT_STATUS.get(status, status),
                "census_tract": row[ix["CENSUS TRACT"]].strip(),
                "neighborhood_code": row[ix["NBHD"]].strip(),
                "lat": lat, "lon": lon,
            })

    # The tax roll's ACRES field is unpopulated on 89% of Dayton parcels — zero
    # there means "not recorded", not "small". Parcel geometry is the reliable
    # size measure. The factor below converts DaytonParcels' Shape__Area to
    # acres and was calibrated against 271 parcels that DO carry a taxroll
    # acreage, matching to three decimal places.
    AREA_TO_ACRES = 0.000146
    apath = os.path.join(os.path.dirname(a.bridge), "parcel_areas.json")
    areas = json.load(open(apath)) if os.path.exists(apath) else {}
    for r in rows:
        geo = areas.get(r["parcel"])
        r["acres_geometry"] = round(geo * AREA_TO_ACRES, 4) if geo else ""
        r["acres_best"] = (r["acres_geometry"] if r["acres_geometry"] != ""
                           else (round(num(r["acres"]), 4) or ""))

    # Contiguous holdings under one owner are the practical route to a site
    # larger than a single lot, so portfolio size travels with each row.
    port = collections.Counter(r["owner_name"] for r in rows if r["owner_name"])
    acre_by_owner = collections.defaultdict(float)
    for r in rows:
        acre_by_owner[r["owner_name"]] += num(r["acres_best"])
    for r in rows:
        r["owner_site_count"] = port.get(r["owner_name"], 0)
        r["owner_site_acres"] = round(acre_by_owner.get(r["owner_name"], 0), 2)

    cols = list(rows[0].keys())
    with open(os.path.join(a.outdir, "developable_sites.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    feats = [{"type": "Feature",
              "geometry": {"type": "Point",
                           "coordinates": [round(float(r["lon"]), 6),
                                           round(float(r["lat"]), 6)]},
              "properties": {k: v for k, v in r.items() if k not in ("lat", "lon")}}
             for r in rows if r["lat"] != ""]
    with open(os.path.join(a.outdir, "developable_sites.geojson"), "w") as f:
        json.dump({"type": "FeatureCollection", "features": feats}, f)

    # Size distribution — the input to deciding what counts as a site.
    bands = [(0.25, "under 1/4 acre"), (0.5, "1/4 to 1/2"), (1, "1/2 to 1"),
             (2, "1 to 2"), (5, "2 to 5"), (float("inf"), "5+ acres")]
    dist = collections.Counter()
    for r in rows:
        if r["acres_best"] == "":
            dist["size unknown"] += 1
            continue
        ac = num(r["acres_best"])
        for lim, label in bands:
            if ac < lim:
                dist[label] += 1
                break
    unmapped = [r for r in rows if r["lat"] == ""]
    if unmapped:
        print(f"NOTE: {len(unmapped):,} parcels have no geometry in either the City or "
              f"County parcel layer.\n      Refresh with scripts/fetch_parcel_geometry.py "
              f"before assuming this is a data limit.\n")

    print(f"developable sites: {len(rows):,}")
    for k, v in collections.Counter(r["site_type"] for r in rows).most_common():
        print(f"    {k:<18}{v:>7,}")
    print(f"  geocoded         : {len(feats):,}\n")
    print("  size distribution:")
    for _, label in bands:
        print(f"    {label:<18}{dist[label]:>7,}")
    if dist["size unknown"]:
        print(f"    {'size unknown':<18}{dist['size unknown']:>7,}")
    print("\n  owner type:")
    for k, v in collections.Counter(r["owner_type"] for r in rows).most_common():
        print(f"    {k:<18}{v:>7,}")
    print(f"\nwrote 2 files to {a.outdir}/")


if __name__ == "__main__":
    main()
