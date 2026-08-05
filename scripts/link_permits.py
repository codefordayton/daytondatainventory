#!/usr/bin/env python3
"""Link Accela permit records to County CAMA permits to recover parcel ids.

Usage:
    ./link_permits.py <accela.json> <PERMIT.DAT> <cama_spec.json> <out.json> [year]

Accela is the City's live permitting system and carries no parcel id. The
County's CAMA extract carries one, and both systems record the *same* permit
number in different notation:

    CAMA   MECR26-0135        TYPE + R/C + YY   + SEQ
    Accela MEC2026R-00135     TYPE + YYYY + R/C + SEQ

Normalizing both to (type, R|C, 2-digit year, sequence) lifts the match rate
from 6% to 43%. The remainder is not a matching failure — see docs/PERMIT_LINKING.md.
CAMA only records permits that bear on assessed value, so plumbing, water,
sewer and fire-protection permits are absent from it entirely and can only be
enriched from Accela's own record detail pages.
"""
import datetime
import json
import re
import sys
import collections

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from cama import read_rows  # noqa: E402

MONTHS = {m: i + 1 for i, m in enumerate(
    ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"])}

# CAMA writes electrical permits as ELE*, Accela as ELC. Other shared types
# (BLD, MEC, GAS, WRK) use the same base code in both systems.
TYPE_ALIAS = {"ELE": "ELC"}


def parse_date(s):
    try:
        d, m, y = s.split("-")
        y = int(y)
        return datetime.date(y + (2000 if y < 50 else 1900), MONTHS[m], int(d))
    except Exception:
        return None


def norm_permit(number):
    """Reduce either system's permit number to (type, R|C, yy, sequence)."""
    s = re.sub(r"[^A-Z0-9]", "", (number or "").upper())
    m = re.match(r"^([A-Z]+?)(\d{4})([RC])(\d+)$", s)          # Accela order
    if m:
        t, yy, rc, seq = m.group(1), int(m.group(2)) % 100, m.group(3), int(m.group(4))
    else:
        m = re.match(r"^([A-Z]+?)([RC])(\d{2})(\d+)$", s)      # CAMA order
        if not m:
            return None
        t, rc, yy, seq = m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
    return (TYPE_ALIAS.get(t, t), rc, yy, seq)


def load_cama(path, spec, year):
    out = {}
    for r in read_rows(spec, "PERMIT", path):
        d = parse_date(r["PERMDT"])
        if year and (not d or d.year != year):
            continue
        k = norm_permit(r["NUM"])
        if not k:
            continue
        out[k] = {"cama_number": r["NUM"].strip(), "parcel": r["PARID"].strip(),
                  "permit_date": d.isoformat() if d else None,
                  "amount": r["AMOUNT"].strip(), "why": r["WHY"].strip(),
                  "note": r["NOTE1"].strip()}
    return out


def main(aca_path, permit_dat, spec_path, out_path, year=2026):
    spec = json.load(open(spec_path))
    cama = load_cama(permit_dat, spec, year)
    records = json.load(open(aca_path))["records"]

    linked, by_type = [], collections.defaultdict(lambda: [0, 0])
    for r in records:
        k = norm_permit(r.get("record_number"))
        hit = cama.get(k) if k else None
        if k:
            by_type[k[0]][0] += 1
            if hit:
                by_type[k[0]][1] += 1
        linked.append({**r,
                       "match_key": "|".join(map(str, k)) if k else None,
                       "parcel": hit["parcel"] if hit else None,
                       "cama_amount": hit["amount"] if hit else None,
                       "cama_why": hit["why"] if hit else None,
                       "linked": bool(hit)})

    n = sum(1 for x in linked if x["linked"])
    rates = {t: {"accela": a, "matched": m, "rate_pct": round(m / a * 100, 1) if a else 0}
             for t, (a, m) in sorted(by_type.items(), key=lambda x: -x[1][0])}
    json.dump({"accela_source": aca_path, "cama_source": permit_dat, "year": year,
               "accela_records": len(records), "cama_permits": len(cama),
               "linked": n,
               "link_rate_pct": round(n / len(records) * 100, 1) if records else 0,
               "by_type": rates,
               "note": "Types at 0% are absent from CAMA, not mismatched — the County "
                       "records permits that bear on assessed value. Enrich those from "
                       "Accela record detail pages instead.",
               "records": linked}, open(out_path, "w"), indent=2)

    print(f"accela {len(records):,} | cama {len(cama):,} | linked {n:,} "
          f"({n / len(records) * 100:.0f}%)", file=sys.stderr)
    print(f"{'type':<8}{'accela':>8}{'matched':>9}{'rate':>7}", file=sys.stderr)
    for t, v in list(rates.items())[:12]:
        print(f"  {t:<6}{v['accela']:>8}{v['matched']:>9}{v['rate_pct']:>6.0f}%", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4],
         int(sys.argv[5]) if len(sys.argv) > 5 else 2026)
