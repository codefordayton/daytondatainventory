#!/usr/bin/env python3
"""Harvest HUD public housing developments and the PHA record for a county.

Usage:
    ./harvest_hud_public_housing.py <out.json> [county] [state_fips]

Public housing owned by a housing authority is a DIFFERENT inventory from the
project-based Section 8 properties in harvest_hud_assisted.py — only 2 of 13
known GDPM developments appear in that dataset. This fills the gap with
structured data (unit counts, occupancy, bedroom mix, coordinates) rather than
scraping the authority's website.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

BASE = "https://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services"

DEV_FIELDS = ("PARTICIPANT_CODE,FORMAL_PARTICIPANT_NAME,DEVELOPMENT_CODE,PROJECT_NAME,"
              "STD_ADDR,STD_CITY,STD_ST,STD_ZIP5,TOTAL_DWELLING_UNITS,ACC_UNITS,"
              "TOTAL_OCCUPIED,PCT_OCCUPIED,PEOPLE_TOTAL,PEOPLE_PER_UNIT,HH_INCOME,"
              "PCT_BED1,PCT_BED2,PCT_BED3,SCATTERED_SITE_IND,CURCNTY_NM,TRACT2KX,LAT,LON")

PHA_FIELDS = ("PARTICIPANT_CODE,FORMAL_PARTICIPANT_NAME,STD_ADDR,STD_CITY,STD_ST,"
              "TOTAL_UNITS,PHA_TOTAL_UNITS,ACC_UNITS,TOTAL_OCCUPIED,PCT_OCCUPIED,"
              "PEOPLE_TOTAL,HH_INCOME,CURCNTY_NM")


def fetch(service, fields, where):
    url = f"{BASE}/{service}/FeatureServer/0/query"
    out, off = [], 0
    while True:
        q = {"where": where, "outFields": fields, "returnGeometry": "false",
             "resultOffset": off, "resultRecordCount": 1000, "f": "json"}
        with urllib.request.urlopen(f"{url}?{urllib.parse.urlencode(q)}", timeout=120) as r:
            d = json.load(r)
        if "error" in d:
            raise SystemExit(f"{service}: {d['error']}")
        feats = d.get("features", [])
        out.extend(f["attributes"] for f in feats)
        more = d.get("exceededTransferLimit")
        if not feats or not more:
            return out
        off += len(feats)
        time.sleep(0.3)


if __name__ == "__main__":
    outpath = sys.argv[1]
    county = sys.argv[2] if len(sys.argv) > 2 else "Montgomery"
    st = sys.argv[3] if len(sys.argv) > 3 else "39"
    where = f"STATE2KX='{st}' AND CURCNTY_NM LIKE '%{county}%'"

    devs = fetch("Public_Housing_Developments", DEV_FIELDS, where)

    # The authority layer is not reliably tagged with the county of its
    # developments, so it is looked up by the authority names the developments
    # actually name rather than by geography.
    phas = []
    seen = set()
    for name in {(d.get("FORMAL_PARTICIPANT_NAME") or "").strip() for d in devs}:
        if not name or name in seen:
            continue
        seen.add(name)
        safe = name.replace("'", "''")
        phas.extend(fetch("Public_Housing_Authorities", "*",
                          f"FORMAL_PARTICIPANT_NAME = '{safe}'"))

    json.dump({"source": BASE, "county": county, "state_fips": st,
               "harvested": time.strftime("%Y-%m-%d"),
               "note": "Public housing is a separate inventory from project-based "
                       "Section 8 — do not merge counts without deduplicating.",
               "development_count": len(devs), "developments": devs,
               "authority_count": len(phas), "authorities": phas},
              open(outpath, "w"), indent=2)
    units = sum(d.get("TOTAL_DWELLING_UNITS") or 0 for d in devs)
    print(f"{len(devs)} developments, {units:,} dwelling units; {len(phas)} authorities",
          file=sys.stderr)
