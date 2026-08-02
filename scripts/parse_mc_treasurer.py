#!/usr/bin/env python3
"""Parse the Montgomery County Treasurer bulk-download listings into a manifest.

The listing pages emit unquoted, backslash-separated hrefs (legacy ColdFusion),
so the href regex deliberately accepts bare attribute values.

Usage:
    ./parse_mc_treasurer.py <dir_of_html> <output.json>
"""
import glob
import html
import json
import os
import re
import sys
import time

BASE = "https://go.mcohio.org/applications/treasurer/search/"

TYPES = {
    "WS": "Weekly Sales", "MS": "Monthly Sales", "YS": "Yearly Sales",
    "TR": "Taxroll", "DQ": "Delinquent Files", "ST": "Street Light Districts",
    "CC": "CAMA Characteristics", "RF": "Available Tax Refunds",
    "NC": "Neighborhood Codes",
}

# Anchors are matched on their own rather than as part of one row-spanning
# regex: a combined pattern lets a non-file anchor (e.g. javascript:window.close)
# consume the row that follows it, silently dropping the newest file.
# Attributes may precede href (e.g. target='_blank'), and hrefs are often
# unquoted with backslash separators, so both forms are accepted.
ANCHOR = re.compile(
    r"<a\s[^>]*?href\s*=\s*(?P<href>\"[^\"]*\"|'[^']*'|[^\s>]+)[^>]*>(?P<label>.*?)</a>",
    re.S | re.I,
)
CELL = re.compile(r"<td[^>]*>(.*?)</td>", re.S | re.I)
FILE_EXT = re.compile(r"\.(zip|txt|csv|dat|pdf|html?)$", re.I)


def _text(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def parse(path):
    s = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for m in ANCHOR.finditer(s):
        href = html.unescape(m.group("href")).strip('"')
        if not FILE_EXT.search(href):
            continue
        # The creation date and byte size live in the next two <td> cells.
        cells = [_text(c.group(1)) for c in CELL.finditer(s, m.end())][:2]
        created = next((c for c in cells if re.fullmatch(r"[\d/]+", c)), None)
        size = next((c for c in cells if re.fullmatch(r"[\d,]+", c)), None)
        out.append({
            "label": _text(m.group("label")),
            "created": created,
            "size_bytes": int(size.replace(",", "")) if size else None,
            "url": BASE + href.replace("\\", "/"),
        })
    return out


if __name__ == "__main__":
    srcdir, outpath = sys.argv[1], sys.argv[2]
    datasets = []
    for path in sorted(glob.glob(os.path.join(srcdir, "*.html"))):
        code = os.path.basename(path)[:-5]
        files = parse(path)
        datasets.append({"code": code, "name": TYPES.get(code, code),
                         "file_count": len(files), "files": files})
        print(f"  {TYPES.get(code, code):<25} {len(files):>4} files", file=sys.stderr)
    with open(outpath, "w") as f:
        json.dump({"source": BASE + "filedownloads.cfm",
                   "harvested": time.strftime("%Y-%m-%d"), "datasets": datasets}, f, indent=2)
    print(f"wrote {outpath}", file=sys.stderr)
