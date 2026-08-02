#!/usr/bin/env python3
"""Harvest Dayton Accela housing code enforcement incidents.

Usage:
    ./harvest_accela.py <out.json>

Uses the _UPDATE service: the non-_UPDATE sibling exposes the same schema but
its query endpoint returns 503. Coverage is current-year only.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

URL = ("https://maps.daytonohio.gov/gisservices/rest/services/Accela_UPDATES/"
       "AccelaIncidents_UPDATE/MapServer/0/query")

FIELDS = ("OBJECTID,COMPLAINT_NO,COMPLAINT_TYPE,RECORD_DATE,STATUS,ACTION_TAKEN,"
          "ASSIGNED,DESCRIPTION,ADDRESS,ADDRKEY,STR_NO,STR_DIR,STR_NAME,"
          "STR_SUFFIX,STR_DIR_SUFFIX,UNIT_TYPE,UNIT,NEIGHBORHOOD,PRI_BOARD,"
          "X_COORDINATE,Y_COORDINATE")


def fetch(page=1000):
    out, off = [], 0
    while True:
        q = {"where": "1=1", "outFields": FIELDS, "returnGeometry": "false",
             "resultOffset": off, "resultRecordCount": page, "f": "json",
             "orderByFields": "OBJECTID"}
        for attempt in range(3):
            try:
                with urllib.request.urlopen(f"{URL}?{urllib.parse.urlencode(q)}", timeout=180) as r:
                    d = json.load(r)
                break
            except Exception as e:
                if attempt == 2:
                    raise SystemExit(f"failed at offset {off}: {e}")
                time.sleep(5)
        if "error" in d:
            raise SystemExit(f"API error: {d['error']}")
        feats = d.get("features", [])
        out.extend(f["attributes"] for f in feats)
        print(f"  {len(out):,}", file=sys.stderr)
        # The server caps resultRecordCount at its own maxRecordCount, so a
        # short page does not reliably mean the last page. Trust the flag.
        more = d.get("exceededTransferLimit") or d.get("properties", {}).get("exceededTransferLimit")
        if not feats or not more:
            return out
        off += len(feats)
        time.sleep(0.5)


if __name__ == "__main__":
    rows = fetch()
    json.dump({"source": URL, "harvested": time.strftime("%Y-%m-%d"),
               "count": len(rows), "incidents": rows}, open(sys.argv[1], "w"))
    print(f"wrote {len(rows)} incidents", file=sys.stderr)
