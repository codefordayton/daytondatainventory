#!/usr/bin/env python3
"""Harvest HUD assisted multifamily properties (project-based Section 8) for a county.

Usage:
    ./harvest_hud_assisted.py <output.json> [county] [state_fips]

Unlike the LIHTC database, this source carries PUBLISHED contract expiration
dates (EXPIRATION_DATE1/2) rather than derived horizons. HUD refreshes it
monthly. Note that a project-based rental assistance contract expiring is not
the same event as a LIHTC extended-use period ending — a property can have
both, on different clocks.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

URL = ("https://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services"
       "/Multifamily_Properties_Assisted/FeatureServer/0/query")

FIELDS = ("PROPERTY_NAME_TEXT,ADDRESS_LINE1_TEXT,PLACED_BASE_CITY_NAME_TEXT,"
          "STD_CITY,PROPERTY_CATEGORY_NAME,CLIENT_GROUP_NAME,"
          "TOTAL_UNIT_COUNT,TOTAL_ASSISTED_UNIT_COUNT,PCT_OCCUPIED,"
          "CONTRACT1,CONTRACT2,CONTRACT_COUNT,MAXIMUM_CONTRACT_UNIT_COUNT,UNITS1,UNITS2,"
          "EXPIRATION_DATE1,EXPIRATION_DATE2,IS_SUBSIDIZED_IND,"
          "HAS_ACTIVE_ASSISTANCE_IND,WAS_EVER_ASSISTED_IND,"
          "CURCNTY_NM,TRACT2KX,LAT,LON")


def fetch(where):
    out, offset = [], 0
    while True:
        params = {"where": where, "outFields": FIELDS, "returnGeometry": "false",
                  "resultOffset": offset, "resultRecordCount": 1000, "f": "json"}
        with urllib.request.urlopen(f"{URL}?{urllib.parse.urlencode(params)}", timeout=120) as r:
            d = json.load(r)
        if "error" in d:
            raise SystemExit(f"API error: {d['error']}")
        feats = d.get("features", [])
        out.extend(a["attributes"] for a in feats)
        if len(feats) < 1000:
            return out
        offset += 1000
        time.sleep(0.3)


if __name__ == "__main__":
    outpath = sys.argv[1]
    county = sys.argv[2] if len(sys.argv) > 2 else "Montgomery"
    st = sys.argv[3] if len(sys.argv) > 3 else "39"
    where = f"STATE2KX='{st}' AND CURCNTY_NM LIKE '%{county}%'"
    rows = fetch(where)
    json.dump({"source": "HUD Multifamily Properties - Assisted "
                         "(services.arcgis.com/VTyQ9soqVukalItT)",
               "where": where, "harvested": time.strftime("%Y-%m-%d"),
               "note": "EXPIRATION_DATE1/2 are published contract expiration dates, "
                       "not derived. Distinct from LIHTC extended-use expiry.",
               "count": len(rows), "properties": rows},
              open(outpath, "w"), indent=2)
    print(f"wrote {len(rows)} assisted properties to {outpath}", file=sys.stderr)
