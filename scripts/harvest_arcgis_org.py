#!/usr/bin/env python3
"""Harvest every public item from an ArcGIS Online organization.

Usage:
    ./harvest_arcgis_org.py <orgid> <output.json> [--label NAME]

Pages through the ArcGIS Online search API (100 items/page, the API max) and
writes the raw item records to disk. Raw output is kept verbatim so the
normalization step downstream can be re-run without re-fetching.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

SEARCH_URL = "https://www.arcgis.com/sharing/rest/search"


def fetch_page(orgid, start, num=100):
    params = {
        "q": f"orgid:{orgid}",
        "f": "json",
        "num": num,
        "start": start,
        "sortField": "title",
        "sortOrder": "asc",
    }
    url = f"{SEARCH_URL}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.load(resp)


def harvest(orgid):
    items, start = [], 1
    while start > 0:
        page = fetch_page(orgid, start)
        items.extend(page.get("results", []))
        print(f"  fetched {len(items)}/{page.get('total')}", file=sys.stderr)
        start = page.get("nextStart", -1)
        time.sleep(0.3)
    return items


if __name__ == "__main__":
    orgid, outpath = sys.argv[1], sys.argv[2]
    label = sys.argv[4] if len(sys.argv) > 4 else orgid
    results = harvest(orgid)
    with open(outpath, "w") as f:
        json.dump({"orgid": orgid, "label": label, "harvested": time.strftime("%Y-%m-%d"),
                   "count": len(results), "items": results}, f, indent=2)
    print(f"wrote {len(results)} items to {outpath}", file=sys.stderr)
