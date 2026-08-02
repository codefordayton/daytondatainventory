#!/usr/bin/env python3
"""Generate markdown data dictionaries from harvested ArcGIS field schemas.

Usage:
    ./build_dictionaries.py <fields.json> <output_dir>

One file per dataset. Coded-value domains are rendered inline so a reader can
decode categorical columns without touching the API.
"""
import datetime
import json
import os
import re
import sys

# Columns that are ArcGIS plumbing rather than substantive content. They are
# still listed, but pushed into a collapsed section to keep dictionaries usable.
PLUMBING = re.compile(
    r"^(OBJECTID|GlobalID|Shape__|Shape_|SHAPE|FID|ESRI_OID)", re.I
)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def ms_to_date(ms):
    if not ms:
        return None
    try:
        return datetime.datetime.fromtimestamp(ms / 1000).strftime("%Y-%m-%d")
    except Exception:
        return None


def field_rows(fields):
    rows = []
    for f in fields:
        t = (f.get("type") or "").replace("esriFieldType", "")
        notes = []
        if f.get("domain"):
            items = list(f["domain"].items())
            shown = "; ".join(f"`{k}` = {v}" for k, v in items[:12])
            if len(items) > 12:
                shown += f"; …(+{len(items) - 12} more)"
            notes.append(f"**Values:** {shown}")
        if f.get("domain_range"):
            notes.append(f"**Range:** {f['domain_range']}")
        if f.get("length") and t == "String":
            notes.append(f"len {f['length']}")
        alias = f.get("alias") or ""
        alias = "" if alias == f.get("name") else alias
        rows.append((f.get("name"), t, alias, " · ".join(notes)))
    return rows


def render(ds):
    out = [f"# {ds['title']}\n"]
    if ds.get("snippet"):
        out.append(f"> {ds['snippet']}\n")

    out.append("## Source\n")
    out.append(f"- **Publisher:** City of Dayton (ArcGIS Online, owner `{ds.get('owner')}`)")
    out.append(f"- **Service type:** {ds.get('type')}")
    out.append(f"- **Service URL:** {ds.get('url')}")
    out.append(f"- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id={ds['id']}")
    out.append(f"- **Created:** {ms_to_date(ds.get('created'))}  ·  **Item modified:** {ms_to_date(ds.get('modified'))}")
    if ds.get("tags"):
        out.append(f"- **Tags:** {', '.join(ds['tags'])}")
    if ds.get("licenseInfo"):
        lic = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", ds["licenseInfo"])).strip()
        out.append(f"- **License/terms:** {lic[:300]}")
    out.append("")

    desc = ds.get("description")
    if desc:
        clean = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", desc)).strip()
        if clean:
            out.append(f"## Publisher description\n\n{clean}\n")

    for layer in ds.get("layers", []):
        if layer.get("error"):
            out.append(f"## Layer {layer['id']}: {layer.get('name')}\n\n*Not readable: {layer['error']}*\n")
            continue
        out.append(f"## Layer {layer['id']}: {layer.get('name')}\n")
        meta = [f"- **Records:** {layer.get('recordCount'):,}" if isinstance(layer.get("recordCount"), int)
                else "- **Records:** unknown"]
        if layer.get("geometryType"):
            meta.append(f"- **Geometry:** {layer['geometryType'].replace('esriGeometry', '')}")
        if ms_to_date(layer.get("lastEditDate")):
            meta.append(f"- **Last edited:** {ms_to_date(layer['lastEditDate'])}")
        out.extend(meta)
        ldesc = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", layer.get("description") or "")).strip()
        if ldesc and ldesc.lower() != "null":
            out.append(f"\n{ldesc}")
        out.append("")

        rows = field_rows(layer.get("fields", []))
        substantive = [r for r in rows if not PLUMBING.match(r[0] or "")]
        plumbing = [r for r in rows if PLUMBING.match(r[0] or "")]

        out.append("| Field | Type | Alias | Notes |")
        out.append("|---|---|---|---|")
        for n, t, a, note in substantive:
            out.append(f"| `{n}` | {t} | {a} | {note} |")
        out.append("")
        if plumbing:
            out.append("<details><summary>System/geometry fields</summary>\n")
            out.append("| Field | Type | Alias | Notes |")
            out.append("|---|---|---|---|")
            for n, t, a, note in plumbing:
                out.append(f"| `{n}` | {t} | {a} | {note} |")
            out.append("\n</details>\n")
    return "\n".join(out)


if __name__ == "__main__":
    src, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    data = json.load(open(src))
    written = 0
    seen = set()
    for ds in data["datasets"]:
        if not ds.get("layers") or all(l.get("error") for l in ds["layers"]):
            continue
        if not any(l.get("recordCount") for l in ds["layers"]):
            continue
        # Titles differing only in case/punctuation (e.g. "Dayton Neighborhoods"
        # vs "DAYTON_NEIGHBORHOODS") slugify identically but are distinct
        # services, so a colliding name gets the item id appended.
        base = slug(ds["title"])
        path = os.path.join(outdir, f"{base}.md")
        if os.path.exists(path) and base in seen:
            path = os.path.join(outdir, f"{base}-{ds['id'][:8]}.md")
        seen.add(base)
        with open(path, "w") as f:
            f.write(render(ds) + "\n")
        written += 1
    print(f"wrote {written} dictionaries to {outdir}", file=sys.stderr)
