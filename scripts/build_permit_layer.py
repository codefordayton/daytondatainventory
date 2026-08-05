#!/usr/bin/env python3
"""Build a parcel-linkable permit layer from Accela records.

Usage:
    ./build_permit_layer.py <accela.json> <address_bridge.json> <outdir>
                            [--linked linked.json]

Emits three files, all open formats, no GIS software required:

  permits_parcel.csv        one row per permit, keyed on parcel id
  parcel_permit_summary.csv one row per parcel — counts, types, valuation
  permits.geojson           point geometry for mapping

The parcel-keyed CSVs are the point. Parcel-based analytics platforms join on
parcel id, so a permit table carrying one sits alongside condition, tenure and
census data without any spatial work. The GeoJSON is a convenience for desktop
GIS and web maps.

Parcel ids are resolved by two independent routes, best first:
  1. permit-number link to County CAMA (exact; see scripts/link_permits.py)
  2. address match through the City address layer
Method is recorded per row so downstream users can filter by confidence.
"""
import argparse
import collections
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_address_bridge import norm_addr  # noqa: E402

SUFFIX_WORDS = {
    "AVENUE": "AVE", "AV": "AVE", "STREET": "ST", "DRIVE": "DR", "ROAD": "RD",
    "BOULEVARD": "BLVD", "COURT": "CT", "PLACE": "PL", "LANE": "LN",
    "TERRACE": "TER", "PARKWAY": "PKWY", "CIRCLE": "CIR", "TRAIL": "TRL",
    "HIGHWAY": "HWY", "SQUARE": "SQ", "PIKE": "PIKE", "WAY": "WAY",
}
SUFFIXES = set(SUFFIX_WORDS) | set(SUFFIX_WORDS.values())
DIRS = {"N", "S", "E", "W", "NE", "NW", "SE", "SW"}


def parse_aca_address(raw):
    """Turn 'ottawa st, DAYTON OH 45402 United States' into a bridge key.

    Accela returns a single free-text field with city, state, ZIP and sometimes
    'United States' appended, plus optional unit designators mid-string.
    """
    if not raw:
        return None
    a = raw.upper().split(",")[0].strip()
    a = re.sub(r"\b(UNIT|APT|STE|SUITE|BLDG|#)\b.*$", "", a).strip()
    a = re.sub(r"\s+", " ", a)
    m = re.match(r"^(\d+)\s+(.*)$", a)
    if not m:
        return None
    num, rest = m.group(1), m.group(2).split()
    if not rest:
        return None
    pre = rest.pop(0) if rest[0] in DIRS else ""
    post = ""
    if rest and rest[-1] in DIRS and len(rest) > 1:
        post = rest.pop()
    suf = ""
    if rest and rest[-1] in SUFFIXES:
        suf = SUFFIX_WORDS.get(rest[-1], rest[-1])
        rest = rest[:-1]
    if not rest:
        return None
    return norm_addr(num, pre, " ".join(rest), suf, post)


def to_int(v):
    try:
        return int(str(v).strip() or 0)
    except (TypeError, ValueError):
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("accela")
    ap.add_argument("bridge")
    ap.add_argument("outdir")
    ap.add_argument("--linked", help="output of link_permits.py, for CAMA parcel ids")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)

    bridge = json.load(open(a.bridge))
    by_addr = bridge["by_norm_address"]
    records = json.load(open(a.accela))["records"]

    # Route 1: exact parcel ids recovered from the CAMA permit-number link.
    from_cama = {}
    if a.linked and os.path.exists(a.linked):
        for r in json.load(open(a.linked))["records"]:
            if r.get("parcel"):
                from_cama[r["record_number"]] = r

    rows, stats = [], collections.Counter()
    for r in records:
        num = r.get("record_number")
        parcel = lat = lon = None
        method = "unmatched"

        hit = from_cama.get(num)
        if hit and hit.get("parcel"):
            parcel, method = hit["parcel"], "permit_number"

        key = parse_aca_address(r.get("address"))
        addr_hit = by_addr.get(key) if key else None
        if addr_hit:
            if not parcel:
                parcel, method = addr_hit["parcel"], "address"
            lat, lon = addr_hit.get("lat"), addr_hit.get("lon")

        stats[method] += 1
        rows.append({
            "permit_number": num,
            "parcel": parcel or "",
            "match_method": method,
            "permit_date": r.get("date", ""),
            "permit_type": r.get("record_type", ""),
            "type_code": (num.split("2")[0] if num and "2" in num else ""),
            "project_name": r.get("project_name", ""),
            "address": r.get("address", ""),
            "valuation": (hit or {}).get("cama_amount") or "",
            "cama_category": (hit or {}).get("cama_why") or "",
            "lat": lat if lat is not None else "",
            "lon": lon if lon is not None else "",
        })

    # --- permit-level table -------------------------------------------------
    cols = list(rows[0].keys())
    with open(os.path.join(a.outdir, "permits_parcel.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    # --- parcel-level rollup: what a parcel platform actually joins ---------
    per = collections.defaultdict(lambda: {"permits": 0, "types": collections.Counter(),
                                           "valuation": 0, "first": "", "last": "",
                                           "lat": "", "lon": "", "address": ""})
    for r in rows:
        if not r["parcel"]:
            continue
        p = per[r["parcel"]]
        p["permits"] += 1
        if r["permit_type"]:
            p["types"][r["permit_type"]] += 1
        p["valuation"] += to_int(r["valuation"])
        d = r["permit_date"]
        if d:
            iso = f"{d[6:]}-{d[:2]}-{d[3:5]}" if len(d) == 10 else d
            p["first"] = min(p["first"] or iso, iso)
            p["last"] = max(p["last"], iso)
        if r["lat"] and not p["lat"]:
            p["lat"], p["lon"] = r["lat"], r["lon"]
        if r["address"] and not p["address"]:
            p["address"] = r["address"]

    with open(os.path.join(a.outdir, "parcel_permit_summary.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["parcel", "permit_count", "distinct_types", "top_type",
                    "total_valuation", "first_permit", "last_permit",
                    "address", "lat", "lon"])
        for pid, v in sorted(per.items()):
            top = v["types"].most_common(1)
            w.writerow([pid, v["permits"], len(v["types"]),
                        top[0][0] if top else "", v["valuation"],
                        v["first"], v["last"], v["address"], v["lat"], v["lon"]])

    # --- geojson ------------------------------------------------------------
    feats = []
    for r in rows:
        if r["lat"] == "" or r["lon"] == "":
            continue
        props = {k: v for k, v in r.items() if k not in ("lat", "lon")}
        feats.append({"type": "Feature",
                      "geometry": {"type": "Point",
                                   "coordinates": [round(float(r["lon"]), 6),
                                                   round(float(r["lat"]), 6)]},
                      "properties": props})
    with open(os.path.join(a.outdir, "permits.geojson"), "w") as f:
        json.dump({"type": "FeatureCollection",
                   "crs": {"type": "name",
                           "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
                   "features": feats}, f)

    total = len(rows)
    matched = total - stats["unmatched"]
    print(f"permits            : {total:,}")
    print(f"  parcel resolved  : {matched:,} ({matched / total * 100:.0f}%)")
    for m, n in stats.most_common():
        print(f"    {m:<16}{n:>7,}")
    print(f"  distinct parcels : {len(per):,}")
    print(f"  mappable points  : {len(feats):,}")
    print(f"\nwrote 3 files to {a.outdir}/")


if __name__ == "__main__":
    main()
