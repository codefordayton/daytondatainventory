#!/usr/bin/env python3
"""Recursively enumerate services and layers on an ArcGIS Server REST directory.

Usage:
    ./harvest_arcgis_server.py <rest_services_url> <output.json>

Walks every folder, then every service, then pulls each service's layer list so
the inventory records field-level detail without a second crawl.
"""
import json
import sys
import time
import urllib.request

def get(url, timeout=45):
    sep = "&" if "?" in url else "?"
    with urllib.request.urlopen(f"{url}{sep}f=json", timeout=timeout) as r:
        return json.load(r)


def walk(root, folder=""):
    base = f"{root}/{folder}" if folder else root
    try:
        info = get(base)
    except Exception as e:
        print(f"  !! {base}: {e}", file=sys.stderr)
        return []

    out = []
    for svc in info.get("services", []):
        name, stype = svc["name"], svc["type"]
        svc_url = f"{root}/{name}/{stype}"
        rec = {"name": name, "type": stype, "url": svc_url, "folder": folder}
        try:
            detail = get(svc_url)
            rec["description"] = detail.get("serviceDescription") or detail.get("description") or ""
            rec["copyright"] = detail.get("copyrightText", "")
            rec["spatialReference"] = (detail.get("spatialReference") or {}).get("latestWkid")
            rec["layers"] = [
                {"id": l.get("id"), "name": l.get("name"), "geometryType": l.get("geometryType")}
                for l in (detail.get("layers") or [])
            ]
            rec["tables"] = [t.get("name") for t in (detail.get("tables") or [])]
        except Exception as e:
            rec["error"] = str(e)
        out.append(rec)
        print(f"  {name} ({stype}) - {len(rec.get('layers', []))} layers", file=sys.stderr)
        time.sleep(0.15)

    for sub in info.get("folders", []):
        out.extend(walk(root, sub))
    return out


if __name__ == "__main__":
    root, outpath = sys.argv[1].rstrip("/"), sys.argv[2]
    services = walk(root)
    with open(outpath, "w") as f:
        json.dump({"root": root, "harvested": time.strftime("%Y-%m-%d"),
                   "count": len(services), "services": services}, f, indent=2)
    print(f"wrote {len(services)} services to {outpath}", file=sys.stderr)
