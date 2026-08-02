#!/usr/bin/env python3
"""Harvest Montgomery County residential rental property registrations.

Usage:
    ./harvest_rental_registrations.py <out.json> [--districts R72,P70] [--keep-csv DIR]

The Auditor publishes one CSV per taxing district (67 of them; R72 is the City
of Dayton). Each row is a registered rental parcel with the responsible agent,
their mailing address and phone, and a unit count — the roster behind the
taxroll's RENTALREG Y/N flag.

The listing page uses the same legacy ColdFusion markup as the Treasurer's bulk
downloads: unquoted, backslash-separated hrefs. See parse_mc_treasurer.py.
"""
import argparse
import csv
import html
import io
import json
import re
import sys
import time
import urllib.request

LIST_URL = ("https://go.mcohio.org/ApplicationS/auditor/rentalreg/"
            "RENTAL_REGISTRATION_LIST.CFM")
ROOT = "https://go.mcohio.org/"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

ANCHOR = re.compile(r'<a\s[^>]*?href\s*=\s*("[^"]*"|\'[^\']*\'|[^\s>]+)[^>]*>(.*?)</a>', re.S | re.I)
CELL = re.compile(r"<td[^>]*>(.*?)</td>", re.S | re.I)


def get(url, timeout=180):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _text(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", x))).strip()


def list_files():
    page = get(LIST_URL).decode("utf-8", "replace")
    out = []
    for m in ANCHOR.finditer(page):
        href = html.unescape(m.group(1)).strip("\"'")
        if not href.lower().endswith(".csv"):
            continue
        cells = [_text(c.group(1)) for c in CELL.finditer(page, m.end())][:2]
        created = next((c for c in cells if re.fullmatch(r"[\d/]+", c)), None)
        size = next((c for c in cells if re.fullmatch(r"[\d,]+", c)), None)
        label = _text(m.group(2))
        district = re.sub(r"^rental_reg_|\.csv$", "", label, flags=re.I)
        out.append({"district": district, "file": label, "created": created,
                    "size_bytes": int(size.replace(",", "")) if size else None,
                    "url": ROOT + href.replace("\\", "/").lstrip("/")})
    return out


def as_int(v):
    try:
        return int(str(v).strip() or 0)
    except ValueError:
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--districts", help="comma-separated district codes; default all")
    ap.add_argument("--keep-csv", help="directory to also write the raw CSVs into")
    a = ap.parse_args()

    files = list_files()
    if a.districts:
        want = {d.strip().upper() for d in a.districts.split(",")}
        files = [f for f in files if f["district"].upper() in want]
    print(f"{len(files)} district files", file=sys.stderr)

    records, per_district = [], []
    for n, f in enumerate(files, 1):
        try:
            raw = get(f["url"])
        except Exception as e:
            print(f"  !! {f['district']}: {e}", file=sys.stderr)
            per_district.append({**f, "rows": 0, "error": str(e)})
            continue
        if a.keep_csv:
            open(f"{a.keep_csv}/{f['file']}", "wb").write(raw)
        text = raw.decode("utf-8", "replace")
        rows = list(csv.DictReader(io.StringIO(text)))
        for r in rows:
            rec = {k.strip().lower().replace(" ", "_"): (v or "").strip()
                   for k, v in r.items() if k}
            rec["number_units"] = as_int(rec.get("number_units"))
            records.append(rec)
        per_district.append({**f, "rows": len(rows),
                             "units": sum(as_int(r.get("NUMBER UNITS")) for r in rows)})
        print(f"  {n}/{len(files)} {f['district']:<6}{len(rows):>6} rows", file=sys.stderr)
        time.sleep(0.3)

    json.dump({"source": LIST_URL, "harvested": time.strftime("%Y-%m-%d"),
               "districts": len(per_district), "count": len(records),
               "units": sum(r["number_units"] for r in records),
               "note": "One row per registered rental parcel. Agent names are free text "
                       "and appear in multiple spellings — normalize before aggregating "
                       "portfolios. Blank agent_name is common where AGENT TYPE is "
                       "'SAME AS OWNER'.",
               "per_district": per_district, "records": records},
              open(a.out, "w"), indent=2)
    print(f"\n{len(records):,} registrations, "
          f"{sum(r['number_units'] for r in records):,} units -> {a.out}", file=sys.stderr)


if __name__ == "__main__":
    main()
