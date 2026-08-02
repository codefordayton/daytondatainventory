#!/usr/bin/env python3
"""Build an address -> parcel bridge for joining Dayton code enforcement to parcel data.

Usage:
    ./build_address_bridge.py <out.json>

Accela code enforcement incidents carry no parcel id, only an address and an
ADDRKEY. The City's "Dayton Used Address" layer carries the same ADDRKEY plus
TAXPINNO (the county-format parcel id), so the join is an exact integer key
lookup rather than fuzzy address matching.

A normalized address string is emitted alongside it as a fallback for records
whose ADDRKEY misses.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

ADDR_URL = ("https://maps.daytonohio.gov/gisservices/rest/services/Basemaps/"
            "Dayton_Used_Address/MapServer/0/query")

FIELDS = ("ADDRKEY,TAXPINNO,K_PID,STNO,PREDIR,STNAME,SUFFIX,POSTDIR,CITY,ZIP,"
          "USEDADDRESS,FullAddress,LUC_Description")

# Accela writes suffixes in short form (AVE/ST/DR); the address layer is mostly
# consistent but not entirely, so both sides are folded to a common vocabulary.
SUFFIX = {
    "AVENUE": "AVE", "AV": "AVE", "STREET": "ST", "DRIVE": "DR", "ROAD": "RD",
    "BOULEVARD": "BLVD", "COURT": "CT", "PLACE": "PL", "LANE": "LN",
    "TERRACE": "TER", "PARKWAY": "PKWY", "CIRCLE": "CIR", "TRAIL": "TRL",
    "HIGHWAY": "HWY", "SQUARE": "SQ", "WAY": "WAY",
}
DIR = {"NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W"}


def norm_addr(stno, predir, stname, suffix, postdir=None):
    """Normalize address parts into a comparable key."""
    parts = []
    stno = re.sub(r"\D", "", str(stno or ""))
    if stno:
        parts.append(str(int(stno)))
    for d in (predir,):
        d = (d or "").strip().upper()
        if d:
            parts.append(DIR.get(d, d))
    name = re.sub(r"[^A-Z0-9 ]", "", (stname or "").strip().upper())
    name = re.sub(r"\s+", " ", name)
    if name:
        parts.append(name)
    s = (suffix or "").strip().upper().rstrip(".")
    if s:
        parts.append(SUFFIX.get(s, s))
    for d in (postdir,):
        d = (d or "").strip().upper()
        if d:
            parts.append(DIR.get(d, d))
    return " ".join(parts)


def fetch_all(url, fields, where="1=1", page=1000):
    """Page through a feature service.

    The server silently caps resultRecordCount at its own maxRecordCount, so a
    requested page size larger than that comes back short and a naive
    `len(feats) < page` test reads a full page as the final one. Termination is
    driven by exceededTransferLimit, falling back to an empty page.
    """
    out, off = [], 0
    while True:
        q = {"where": where, "outFields": fields, "returnGeometry": "false",
             "resultOffset": off, "resultRecordCount": page, "f": "json",
             "orderByFields": "OBJECTID"}
        with urllib.request.urlopen(f"{url}?{urllib.parse.urlencode(q)}", timeout=180) as r:
            d = json.load(r)
        if "error" in d:
            raise SystemExit(f"API error: {d['error']}")
        feats = d.get("features", [])
        out.extend(f["attributes"] for f in feats)
        print(f"  {len(out):,}", file=sys.stderr)
        more = d.get("exceededTransferLimit") or d.get("properties", {}).get("exceededTransferLimit")
        if not feats or not more:
            return out
        off += len(feats)
        time.sleep(0.2)


if __name__ == "__main__":
    rows = fetch_all(ADDR_URL, FIELDS)

    by_key, by_addr = {}, {}
    with_parcel = 0
    for r in rows:
        pid = (r.get("TAXPINNO") or "").strip()
        rec = {"parcel": pid, "k_pid": (r.get("K_PID") or "").strip(),
               "address": (r.get("USEDADDRESS") or r.get("FullAddress") or "").strip(),
               "luc": (r.get("LUC_Description") or "").strip()}
        if pid:
            with_parcel += 1
        key = r.get("ADDRKEY")
        if key is not None:
            by_key[str(int(key))] = rec
        na = norm_addr(r.get("STNO"), r.get("PREDIR"), r.get("STNAME"),
                       r.get("SUFFIX"), r.get("POSTDIR"))
        if na and pid:
            by_addr.setdefault(na, rec)

    out = {"source": ADDR_URL, "harvested": time.strftime("%Y-%m-%d"),
           "address_records": len(rows),
           "with_parcel_id": with_parcel,
           "addrkey_entries": len(by_key),
           "normalized_address_entries": len(by_addr),
           "by_addrkey": by_key, "by_norm_address": by_addr}
    json.dump(out, open(sys.argv[1], "w"))
    print(f"{len(rows):,} addresses; {with_parcel:,} with parcel id; "
          f"{len(by_key):,} ADDRKEY entries; {len(by_addr):,} normalized addresses",
          file=sys.stderr)
