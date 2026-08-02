#!/usr/bin/env python3
"""Extract field-level schemas (data dictionaries) from ArcGIS feature/map services.

Usage:
    ./extract_fields.py <items.json> <output.json> [--filter REGEX]

Reads a harvested item file, hits each service's layer endpoints, and records
field names, types, aliases, coded-value domains, and live record counts.
Coded-value domains are the useful part: they turn opaque integer columns into
documented categories.
"""
import json
import re
import sys
import time
import urllib.request

def get(url, timeout=45):
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}f=json", headers={"User-Agent": "dayton-data-inventory/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def count_records(layer_url):
    try:
        d = get(f"{layer_url}/query?where=1%3D1&returnCountOnly=true")
        return d.get("count")
    except Exception:
        return None


def describe_layer(layer_url):
    d = get(layer_url)
    fields = []
    for f in d.get("fields") or []:
        rec = {"name": f.get("name"), "alias": f.get("alias"), "type": f.get("type"),
               "nullable": f.get("nullable"), "length": f.get("length")}
        dom = f.get("domain")
        if dom and dom.get("type") == "codedValue":
            rec["domain"] = {c.get("code"): c.get("name") for c in dom.get("codedValues", [])}
        elif dom and dom.get("type") == "range":
            rec["domain_range"] = dom.get("range")
        fields.append(rec)
    return {
        "name": d.get("name"),
        "description": d.get("description") or "",
        "geometryType": d.get("geometryType"),
        "recordCount": count_records(layer_url),
        "lastEditDate": (d.get("editingInfo") or {}).get("lastEditDate"),
        "fields": fields,
    }


# Tile caches and imagery have no queryable features; probing them wastes a long
# crawl on a slow server for nothing.
TILE_FOLDERS = {"Orthos", "Basemap", "Basemaps", "Basemaps_105_1", "Imagery"}


def load_items(path):
    """Accept either an ArcGIS Online item harvest or an ArcGIS Server crawl.

    The server crawl has a different shape (services/name/folder rather than
    items/title/id), so it is normalized to the item shape here instead of
    duplicating the extraction logic.
    """
    data = json.load(open(path))
    if "items" in data:
        return data["items"]
    items = []
    for s in data.get("services", []):
        if s.get("type") not in ("FeatureServer", "MapServer"):
            continue
        if s.get("folder") in TILE_FOLDERS:
            continue
        label = f"{s['folder']}/{s['name'].split('/')[-1]}" if s.get("folder") else s["name"]
        items.append({
            "id": label.replace("/", "_"),
            "title": label,
            "type": "Feature Service" if s["type"] == "FeatureServer" else "Map Service",
            "url": s["url"],
            "owner": "City of Dayton GIS (on-premise)",
            "snippet": s.get("description") or "",
            "description": s.get("description") or "",
            "tags": [s.get("folder")] if s.get("folder") else [],
            "created": None, "modified": None,
        })
    return items


def main(itemfile, outpath, pattern=None):
    items = load_items(itemfile)
    if pattern:
        rx = re.compile(pattern, re.I)
        items = [i for i in items if rx.search(i.get("title", ""))]

    out = []
    for it in items:
        url = it.get("url")
        if not url or it["type"] not in ("Feature Service", "Map Service"):
            continue
        rec = {"id": it["id"], "title": it["title"], "type": it["type"], "url": url,
               "owner": it.get("owner"), "snippet": it.get("snippet"),
               "description": it.get("description"), "tags": it.get("tags"),
               "created": it.get("created"), "modified": it.get("modified"),
               "numViews": it.get("numViews"), "licenseInfo": it.get("licenseInfo"),
               "layers": []}
        try:
            svc = get(url)
            targets = [(l["id"], l.get("name")) for l in (svc.get("layers") or [])]
            targets += [(t["id"], t.get("name")) for t in (svc.get("tables") or [])]
            for lid, lname in targets:
                try:
                    rec["layers"].append({"id": lid, **describe_layer(f"{url}/{lid}")})
                except Exception as e:
                    rec["layers"].append({"id": lid, "name": lname, "error": str(e)})
                time.sleep(0.1)
        except Exception as e:
            rec["error"] = str(e)
        nf = sum(len(l.get("fields", [])) for l in rec["layers"])
        nrec = sum(l.get("recordCount") or 0 for l in rec["layers"])
        print(f"  {rec['title'][:55]:<55} {len(rec['layers'])}L {nf}F {nrec}rows", file=sys.stderr)
        out.append(rec)
        time.sleep(0.2)

    with open(outpath, "w") as f:
        json.dump({"source": itemfile, "harvested": time.strftime("%Y-%m-%d"),
                   "count": len(out), "datasets": out}, f, indent=2)
    print(f"wrote {len(out)} datasets to {outpath}", file=sys.stderr)


if __name__ == "__main__":
    pat = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == "--filter" else None
    main(sys.argv[1], sys.argv[2], pat)
