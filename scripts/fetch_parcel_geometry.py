#!/usr/bin/env python3
"""Fetch parcel centroids for a list of parcel ids, City layer then County.

Usage:
    ./fetch_parcel_geometry.py <parcels.csv> <parcel_id_column> <centroids.json>

Written after a derived layer shipped with half its rows unmapped: the shared
centroids file had only ever been populated for a different analysis, and the
gap looked like missing source data rather than an unfetched batch.

Tries DaytonParcels first (City, current), then Montgomery County's
mc_parcel_polygon for parcels the City layer does not carry. Existing entries
are preserved, so this is safe to re-run and cheap to top up.
"""
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

SOURCES = [
    ("City DaytonParcels",
     "https://services2.arcgis.com/3dDB2Kk6kuA2gIGw/arcgis/rest/services/"
     "DaytonParcels/FeatureServer/0/query", 150),
    ("County mc_parcel_polygon",
     "https://gis.mcohio.org/server/rest/services/TestData/"
     "mc_parcel_polygon/MapServer/0/query", 60),
]


def centroid(feature):
    c = feature.get("centroid") or {}
    if c.get("x") is not None:
        return [c["y"], c["x"]]
    rings = (feature.get("geometry") or {}).get("rings")
    if not rings:
        return None
    pts = [p for ring in rings for p in ring]
    return [sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)]


def fetch(url, batch, ids):
    found = {}
    for i in range(0, len(ids), batch):
        chunk = ids[i:i + batch]
        where = "TAXPINNO IN (" + ",".join(
            "'" + p.replace("'", "''") + "'" for p in chunk) + ")"
        # POST: a GET url with this many ids exceeds server length limits.
        data = urllib.parse.urlencode({
            "where": where, "outFields": "TAXPINNO", "returnGeometry": "true",
            "returnCentroid": "true", "outSR": 4326, "f": "json"}).encode()
        req = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=180))
        except Exception as e:
            print(f"    batch {i} failed: {e}", file=sys.stderr)
            continue
        if "error" in d:
            print(f"    batch {i}: {str(d['error'])[:80]}", file=sys.stderr)
            continue
        for f in d.get("features", []):
            pid = (f["attributes"].get("TAXPINNO") or "").strip()
            c = centroid(f)
            if pid and c:
                found[pid] = c
        time.sleep(0.15)
    return found


if __name__ == "__main__":
    src, col, out = sys.argv[1], sys.argv[2], sys.argv[3]
    want = {r[col].strip() for r in csv.DictReader(open(src)) if r.get(col, "").strip()}
    have = json.load(open(out)) if os.path.exists(out) else {}
    missing = sorted(want - set(have))
    print(f"{len(want):,} parcels requested; {len(want) - len(missing):,} already known; "
          f"{len(missing):,} to fetch")

    for name, url, batch in SOURCES:
        if not missing:
            break
        print(f"  {name}...")
        got = fetch(url, batch, missing)
        have.update(got)
        missing = sorted(set(missing) - set(got))
        print(f"    +{len(got):,} — {len(missing):,} still missing")

    json.dump(have, open(out, "w"))
    print(f"\ncentroids file: {len(have):,} parcels")
    if missing:
        print(f"{len(missing):,} parcels have no geometry in either layer — "
              f"typically rights-of-way and remnant strips carried on the tax roll "
              f"without a mapped polygon.")
