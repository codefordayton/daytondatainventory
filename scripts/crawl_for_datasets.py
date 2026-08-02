#!/usr/bin/env python3
"""Crawl a government site for pages that publish datasets.

Usage:
    ./crawl_for_datasets.py <out.json> --seeds URL[,URL...] --hosts h1,h2
                            [--max-pages 300] [--depth 3] [--delay 1.0]

Written after the rental registration roster turned up in an
`applications/auditor/` subdirectory that no navigation page linked to. Portals
bury data behind departmental subpages, so this walks the site and flags any
page that links to a downloadable file or looks like a file listing.

Polite by construction: one request at a time, a delay between them, bounded
depth and page count, and it stays on the hosts you name.
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

# Unquoted, backslash-separated hrefs are common in this county's legacy
# ColdFusion pages, so the pattern accepts bare attribute values too.
ANCHOR = re.compile(r'<a\s[^>]*?href\s*=\s*("[^"]*"|\'[^\']*\'|[^\s>]+)[^>]*>(.*?)</a>', re.S | re.I)
# A file link is not always a file extension. CivicPlus (both daytonohio.gov and
# mcohio.org) serves documents from extensionless paths like
# /DocumentCenter/View/1895, so matching on extension alone reports a site with
# thousands of documents as having none.
DATA_EXT = re.compile(
    r"\.(csv|zip|xlsx?|txt|dat|json|geojson|shp|pdf|mdb|accdb)(\?|$)"
    r"|/DocumentCenter/View/\d+"
    r"|/Archive\.aspx\?ADID=\d+"
    r"|(?:Download|Export)(?:File|Document)?\.aspx\?", re.I)
DATA_HINT = re.compile(r"download|data|export|report|list|file|layout|dataset|gis|"
                       r"registrat|roll|delinq|sales|abstract|statistic", re.I)
SKIP = re.compile(r"\.(jpg|jpeg|png|gif|svg|css|js|ico|woff2?|mp4)(\?|$)|"
                  r"^(mailto|tel|javascript):", re.I)


def fetch(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        ct = r.headers.get("Content-Type", "")
        if "html" not in ct.lower():
            return None
        return r.read().decode("utf-8", "replace")


def links(page, base):
    out = []
    for m in ANCHOR.finditer(page):
        href = html.unescape(m.group(1)).strip("\"'").strip()
        if not href or SKIP.search(href):
            continue
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))).strip()
        out.append((urllib.parse.urljoin(base, href.replace("\\", "/")), text))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--seeds", required=True)
    ap.add_argument("--hosts", required=True)
    ap.add_argument("--max-pages", type=int, default=300)
    ap.add_argument("--depth", type=int, default=3)
    ap.add_argument("--delay", type=float, default=1.0)
    a = ap.parse_args()

    hosts = {h.strip().lower() for h in a.hosts.split(",")}
    queue = [(s.strip(), 0) for s in a.seeds.split(",") if s.strip()]
    seen, pages, findings = set(), 0, []

    while queue and pages < a.max_pages:
        url, depth = queue.pop(0)
        key = url.split("#")[0]
        if key in seen:
            continue
        seen.add(key)
        try:
            page = fetch(key)
        except Exception as e:
            continue
        if not page:
            continue
        pages += 1
        time.sleep(a.delay)

        found = []
        for link, text in links(page, key):
            host = urllib.parse.urlparse(link).netloc.lower()
            if DATA_EXT.search(link):
                found.append({"url": link, "text": text[:120]})
            elif host in hosts and depth < a.depth and link.split("#")[0] not in seen:
                # Follow same-host pages generally — a CMS buries data behind
                # ordinary department navigation that no keyword would match.
                # DATA_HINT only decides ordering, not whether to follow.
                if DATA_HINT.search(link + " " + text):
                    queue.insert(0, (link, depth + 1))
                else:
                    queue.append((link, depth + 1))

        if found:
            title = re.search(r"<title>(.*?)</title>", page, re.S | re.I)
            findings.append({
                "page": key, "depth": depth,
                "title": re.sub(r"\s+", " ", html.unescape(title.group(1))).strip() if title else "",
                "file_count": len(found),
                "files": found[:60],
            })
            print(f"  [{len(found):>4} files] {key}", file=sys.stderr)
        elif pages % 25 == 0:
            print(f"  ...{pages} pages crawled, {len(queue)} queued", file=sys.stderr)

    json.dump({"seeds": a.seeds, "hosts": sorted(hosts),
               "harvested": time.strftime("%Y-%m-%d"),
               "pages_crawled": pages, "pages_with_files": len(findings),
               "findings": sorted(findings, key=lambda f: -f["file_count"])},
              open(a.out, "w"), indent=2)
    print(f"\n{pages} pages crawled, {len(findings)} with downloadable files -> {a.out}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
