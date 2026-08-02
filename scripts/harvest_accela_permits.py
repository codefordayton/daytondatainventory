#!/usr/bin/env python3
"""Harvest City of Dayton permit records from Accela Citizen Access.

Usage:
    ./harvest_accela_permits.py <out.json> --start MM/DD/YYYY --end MM/DD/YYYY
                                [--types "a,b"] [--list-types] [--delay 2.0]

Generalizes Code for Dayton's demolition_checker (which covers the two wrecking
types) to all 49 Building record types. Stdlib only — no Scrapy — to match the
rest of this repository.

ACA is an ASP.NET WebForms UI, not an API:
  * Every control on the page must be posted back, not just the search fields —
    posting a subset lands on an error page.
  * Results are paginated by further postbacks carrying a fresh __VIEWSTATE.
  * A search returning exactly one record redirects to the detail page instead
    of rendering the results grid.
  * Page shape is asserted; a layout change raises rather than silently
    returning zero records.

This is a live permitting system used by residents and contractors. Requests are
serialized with a delay between them; do not parallelize.
"""
import argparse
import html
import http.cookiejar
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

BASE = "https://aca-prod.accela.com/DAYTON/Cap/CapHome.aspx"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
PFX = "ctl00$PlaceHolderMain$generalSearchForm$"
GRID_ID = "ctl00_PlaceHolderMain_dgvPermitList_gdvPermitList"


class FormScraper(HTMLParser):
    """Collect every submittable control, the way a browser would serialize a form."""

    def __init__(self):
        super().__init__()
        self.fields = []
        self._sel = None
        self._sel_val = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "input":
            name, typ = a.get("name"), (a.get("type") or "text").lower()
            if not name or typ in ("submit", "button", "image", "reset"):
                return
            if typ in ("checkbox", "radio") and "checked" not in a:
                return
            self.fields.append((name, a.get("value", "")))
        elif tag == "select":
            self._sel, self._sel_val = a.get("name"), None
        elif tag == "option" and self._sel:
            if "selected" in a:
                self._sel_val = a.get("value", "")
            elif self._sel_val is None:
                self._sel_val = a.get("value", "")
        elif tag == "textarea" and a.get("name"):
            self.fields.append((a["name"], ""))

    def handle_endtag(self, tag):
        if tag == "select" and self._sel:
            self.fields.append((self._sel, self._sel_val or ""))
            self._sel = None


class GridScraper(HTMLParser):
    """Pull rows from the results grid, tracking nesting.

    The grid contains nested tables (pagination chrome), so only <tr> elements
    at the grid's own depth are data rows.
    """

    def __init__(self, grid_id):
        super().__init__()
        self.grid_id = grid_id
        self.rows = []
        self._depth = 0        # table depth once inside the grid
        self._in = False
        self._row = None
        self._cell = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table":
            if not self._in and a.get("id") == self.grid_id:
                self._in, self._depth = True, 1
            elif self._in:
                self._depth += 1
        elif self._in and self._depth == 1:
            if tag == "tr":
                self._row = []
            elif tag in ("td", "th") and self._row is not None:
                self._cell = []

    def handle_data(self, d):
        if self._cell is not None:
            self._cell.append(d)

    def handle_endtag(self, tag):
        if tag == "table" and self._in:
            self._depth -= 1
            if self._depth == 0:
                self._in = False
        elif self._in and self._depth == 1:
            if tag in ("td", "th") and self._cell is not None:
                txt = re.sub(r"\s+", " ", html.unescape("".join(self._cell))).strip()
                self._row.append(txt)
                self._cell = None
            elif tag == "tr" and self._row is not None:
                if any(self._row):
                    self.rows.append(self._row)
                self._row = None


class ACA:
    def __init__(self, module="Building", delay=2.0):
        self.url = f"{BASE}?module={module}&TabName={module}"
        self.delay = delay
        cj = http.cookiejar.CookieJar()
        self.op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        self.op.addheaders = [("User-Agent", UA)]

    def get(self):
        time.sleep(self.delay)
        return self.op.open(self.url, timeout=120).read().decode("utf-8", "replace")

    def post(self, page, overrides):
        f = FormScraper()
        f.feed(page)
        pairs = [(k, overrides.get(k, v)) for k, v in f.fields]
        have = {k for k, _ in pairs}
        pairs += [(k, v) for k, v in overrides.items() if k not in have]
        req = urllib.request.Request(
            self.url, data=urllib.parse.urlencode(pairs).encode(),
            headers={"Content-Type": "application/x-www-form-urlencoded",
                     "Referer": self.url})
        time.sleep(self.delay)
        r = self.op.open(req, timeout=240)
        return r.read().decode("utf-8", "replace"), r.url

    def permit_types(self):
        page = self.get()
        m = re.search(r'id="ctl00_PlaceHolderMain_generalSearchForm_ddlGSPermitType".*?</select>',
                      page, re.S)
        if not m:
            raise SystemExit("permit-type dropdown not found — page layout changed")
        out = []
        for v, t in re.findall(r'<option[^>]*value="([^"]*)"[^>]*>(.*?)</option>', m.group(0), re.S):
            label = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()
            if v:
                out.append({"value": v, "label": label})
        return out


# Observed grid layout. Column 0 is the row-select checkbox and is always empty,
# which is why a naive positional mapping lands one column to the left.
COLS = ["_select", "date", "record_number", "record_type", "project_name",
        "address", "action"]
HEADER = {"date", "record number", "record type", "project name", "address", "action"}


def parse_rows(page):
    g = GridScraper(GRID_ID)
    g.feed(page)
    out = []
    for r in g.rows:
        if len(r) < 5:
            continue
        if any(c.startswith("Showing ") for c in r):
            continue
        # The header repeats per page; detect it by content, not position.
        if len({c.strip().lower() for c in r} & HEADER) >= 3:
            continue
        out.append(r)
    return out


def search(aca, ptype, start, end):
    """Run one search and page through the results."""
    page = aca.get()
    over = {"__EVENTTARGET": "ctl00$PlaceHolderMain$btnNewSearch", "__EVENTARGUMENT": "",
            PFX + "ddlGSPermitType": ptype,
            PFX + "txtGSStartDate": start, PFX + "txtGSEndDate": end}
    page, final = aca.post(page, over)

    if "ErrorId=" in final:
        raise RuntimeError(f"ACA returned an error page for {ptype} — form fields rejected")

    # A single hit redirects to the record detail page rather than the grid.
    if "CapDetail" in final:
        num = re.search(r'id="ctl00_PlaceHolderMain_lblPermitNumber"[^>]*>([^<]*)', page)
        return [{"record_number": (num.group(1).strip() if num else ""),
                 "detail_url": final, "single_result": True}], False

    grid = GRID_ID in page
    empty = "noDataMessageForSearchResultList" in page
    # Assert the page is one of the two shapes we understand.
    if not grid and not empty:
        raise RuntimeError(f"unrecognized page shape for {ptype} — ACA layout likely changed")
    if empty:
        return [], False

    # ACA reports "Showing 1-10 of 100+" for any result set over 100 — it never
    # shows a true total, so that string says nothing about completeness.
    # (Verified: a half-year run and the sum of its two quarters both return 615
    # for Residential Gas.) Completeness is established by pagination running out
    # of Next links, which is what the loop below tracks.
    rows, pages = parse_rows(page), 1

    while True:
        nxt = re.search(r'href="javascript:__doPostBack\(&#39;([^&]+)&#39;,&#39;&#39;\)"[^>]*>\s*Next',
                        page)
        if not nxt:
            break
        page, final = aca.post(page, {"__EVENTTARGET": html.unescape(nxt.group(1)),
                                      "__EVENTARGUMENT": ""})
        new = parse_rows(page)
        if not new:
            break
        rows.extend(new)
        pages += 1
    return rows, pages


def to_record(row, ptype):
    rec = {"searched_type": ptype}
    for i, c in enumerate(COLS):
        if c.startswith("_"):
            continue
        rec[c] = row[i] if i < len(row) else ""
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out", nargs="?")
    ap.add_argument("--start", default="01/01/2026")
    ap.add_argument("--end", default="06/30/2026")
    ap.add_argument("--types", help="comma-separated ddlGSPermitType values; default all")
    ap.add_argument("--list-types", action="store_true")
    ap.add_argument("--delay", type=float, default=2.0)
    a = ap.parse_args()

    aca = ACA(delay=a.delay)
    types = aca.permit_types()
    if a.list_types:
        for t in types:
            print(f"{t['value']:<48}{t['label']}")
        return
    if not a.out:
        ap.error("out path required unless --list-types")

    wanted = ([t for t in types if t["value"] in set(a.types.split(","))]
              if a.types else types)
    print(f"{len(wanted)} record types, {a.start} to {a.end}, {a.delay}s between requests",
          file=sys.stderr)

    records, page_counts, failed = [], {}, []
    for n, t in enumerate(wanted, 1):
        try:
            rows, pages = search(aca, t["value"], a.start, a.end)
        except Exception as e:
            failed.append({"type": t["value"], "error": str(e)})
            print(f"  !! {n}/{len(wanted)} {t['label'][:44]:<46}{e}", file=sys.stderr)
            continue
        for r in rows:
            records.append({**(r if isinstance(r, dict) else to_record(r, t["value"])),
                            "type_label": t["label"]})
        page_counts[t["value"]] = pages
        print(f"  {n}/{len(wanted)} {t['label'][:44]:<46}{len(rows):>5} records "
              f"({pages} page{'s' if pages != 1 else ''})", file=sys.stderr)

    json.dump({"source": BASE, "module": "Building",
               "start": a.start, "end": a.end,
               "harvested": time.strftime("%Y-%m-%d"),
               "types_searched": len(wanted), "count": len(records),
               "pages_per_type": page_counts, "failed_types": failed,
               "note": "Completeness comes from pagination exhausting its Next links. "
                       "ACA's 'of 100+' label is a display artifact and does not "
                       "indicate a result cap.",
               "records": records}, open(a.out, "w"), indent=2)
    print(f"\n{len(records)} records -> {a.out}", file=sys.stderr)
    if failed:
        print(f"WARNING: {len(failed)} types failed", file=sys.stderr)


if __name__ == "__main__":
    main()
