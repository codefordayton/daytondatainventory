#!/usr/bin/env python3
"""Emit the developable-sites map's data files.

Usage:
    ./build_map_data.py <derived_dir> <neighborhoods.geojson> <map_data_dir>

Writes JS files that assign to a window global rather than plain .geojson, so
the map works from file:// without a local server — same convention as the
voterimpact project.

Properties are trimmed to what the map filters or displays; the full attribute
set stays in data/derived/developable_sites.csv.
"""
import csv
import json
import os
import sys


def num(v):
    try:
        return float(str(v).strip() or 0)
    except (TypeError, ValueError):
        return 0.0


def main(derived, hoods, outdir):
    os.makedirs(outdir, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(derived, "developable_sites.csv"))))

    feats = []
    for r in rows:
        if not r["lat"] or not r["lon"]:
            continue
        ac = num(r["acres_best"])
        feats.append({
            "type": "Feature",
            "geometry": {"type": "Point",
                         "coordinates": [round(float(r["lon"]), 6),
                                         round(float(r["lat"]), 6)]},
            "properties": {
                "p": r["parcel"],
                "t": "S" if r["site_type"] == "vacant_structure" else "L",
                "u": r["use_desc"],
                "a": round(ac, 3) if ac else None,
                "ad": r["address"],
                "o": r["owner_name"],
                "ot": r["owner_type"],
                "om": r["owner_mailing"],
                "v": num(r["assessed_total"]) or None,
                "vl": num(r["assessed_land"]) or None,
                "yb": r["year_built"] or None,
                "hs": r["hcs_status"] or None,
                "hg": r["hcs_grade"] or None,
                "oc": int(r["owner_site_count"] or 0),
                "oa": num(r["owner_site_acres"]) or None,
                "ct": r["census_tract"],
            },
        })

    def write(path, varname, payload):
        with open(path, "w") as f:
            f.write(f"window.{varname} = ")
            json.dump(payload, f, separators=(",", ":"))
            f.write(";\n")
        return os.path.getsize(path)

    n1 = write(os.path.join(outdir, "sites_geojson.js"), "SITES_GEOJSON",
               {"type": "FeatureCollection", "features": feats})

    hg = json.load(open(hoods))
    slim = [{"type": "Feature", "geometry": g["geometry"],
             "properties": {"name": g["properties"].get("NAME", "")}}
            for g in hg["features"]]
    n2 = write(os.path.join(outdir, "neighborhoods_geojson.js"), "NEIGHBORHOODS_GEOJSON",
               {"type": "FeatureCollection", "features": slim})

    # Counts the sidebar shows before any filtering, computed here so the page
    # does not have to derive them on load.
    stats = {
        "total_rows": len(rows),
        "mapped": len(feats),
        "structures": sum(1 for f in feats if f["properties"]["t"] == "S"),
        "land": sum(1 for f in feats if f["properties"]["t"] == "L"),
    }
    n3 = write(os.path.join(outdir, "stats.js"), "SITE_STATS", stats)

    print(f"sites          : {len(feats):,} of {len(rows):,} rows  ({n1/1024:.0f} KB)")
    print(f"neighborhoods  : {len(slim)}  ({n2/1024:.0f} KB)")
    print(f"stats          : {n3} bytes")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
