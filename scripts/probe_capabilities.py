#!/usr/bin/env python3
"""Probe ArcGIS services for Query capability.

Usage:
    ./probe_capabilities.py <items.json> <out.json>

Not every Feature Service holds readable data. Survey123 "_form" views are
write-only submission endpoints (capabilities: Create,Editing) — opening one in
a map viewer fails with "layer view requires a layer with query capability".
Cataloguing them as datasets sends people to dead links, so this records the
declared capabilities and whether a count query actually succeeds.
"""
import json
import sys
import time
import urllib.parse
import urllib.request


def get(url, timeout=30):
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}f=json",
                                 headers={"User-Agent": "dayton-data-inventory/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def probe(url):
    out = {"capabilities": None, "queryable": False, "note": ""}
    try:
        d = get(url)
    except Exception as e:
        out["note"] = f"service unreachable: {e}"
        return out
    if "error" in d:
        out["note"] = str(d["error"].get("message") or d["error"])
        return out
    caps = d.get("capabilities") or ""
    out["capabilities"] = caps
    if "Query" not in caps:
        out["note"] = "no Query capability — not readable as data"
        return out
    layers = (d.get("layers") or []) + (d.get("tables") or [])
    if not layers:
        out["note"] = "Query declared but no layers or tables"
        return out
    lid = layers[0].get("id", 0)
    try:
        c = get(f"{url}/{lid}/query?where=1%3D1&returnCountOnly=true")
        if "error" in c:
            out["note"] = str(c["error"].get("message") or "query rejected")
        else:
            out["queryable"] = True
            out["count"] = c.get("count")
    except Exception as e:
        out["note"] = f"query failed: {e}"
    return out


if __name__ == "__main__":
    items = json.load(open(sys.argv[1]))["items"]
    svcs = [i for i in items if i["type"] in ("Feature Service", "Map Service") and i.get("url")]
    res = {}
    for n, i in enumerate(svcs, 1):
        r = probe(i["url"])
        res[i["id"]] = {"title": i["title"], "url": i["url"], **r}
        flag = "ok " if r["queryable"] else "NO "
        print(f"  {flag}{n}/{len(svcs)} {i['title'][:52]:<54}{r['capabilities'] or r['note'][:30]}",
              file=sys.stderr)
        time.sleep(0.1)
    ok = sum(1 for v in res.values() if v["queryable"])
    json.dump({"probed": len(res), "queryable": ok,
               "harvested": time.strftime("%Y-%m-%d"), "services": res},
              open(sys.argv[2], "w"), indent=2)
    print(f"\n{ok}/{len(res)} queryable -> {sys.argv[2]}", file=sys.stderr)
