#!/usr/bin/env python3
"""Parse the OHFA "Projects Exiting LIHTC Program Affordability Period" export
and cross-check it against the HUD-derived affordability horizons.

Usage:
    ./parse_ohfa.py <ohfa_export.csv> <lihtc.json> <out.json> [county]

The OHFA export is a manual browser download from the Tableau dashboard
(the .csv URL suffix returns only a filter sheet — see docs/CAVEATS.md).
It arrives UTF-16 encoded and TAB delimited despite the .csv extension.

OHFA is Ohio's LIHTC allocating agency, so its exit years reflect recorded
extended use agreements — including re-syndications that HUD's placed-in-service
year cannot capture. Its column is still labelled "Est. Program Exit", so treat
it as authoritative-but-estimated rather than a legal date.
"""
import collections
import csv
import json
import re
import statistics
import sys


def norm(name):
    """Normalize a project name for matching. Phase numerals are deliberately
    KEPT — 'Foo II' is a different project from 'Foo' with different dates."""
    s = (name or "").upper()
    s = re.sub(r"\b(APARTMENTS|APARTMENT|APTS|APT)\b", "", s)
    s = re.sub(r"\b(LP|LTD|LLC)\b", "", s)
    return re.sub(r"[^A-Z0-9]", "", s)


def load_ohfa(path, county=None):
    with open(path, encoding="utf-16", newline="") as f:
        r = csv.reader(f, delimiter="\t")
        hdr = next(r)
        rows = [dict(zip(hdr, x)) for x in r]
    if county:
        rows = [x for x in rows if x.get("County", "").strip().lower() == county.lower()]
    return rows


def as_int(v):
    try:
        return int(str(v).replace(",", "").strip())
    except (TypeError, ValueError):
        return None


def main(ohfa_path, lihtc_path, out_path, county="Montgomery"):
    ohfa = load_ohfa(ohfa_path, county)
    hud = json.load(open(lihtc_path))["properties"]

    by_name = collections.defaultdict(list)
    for x in ohfa:
        by_name[norm(x["Project Name"])].append(x)

    matches, diffs = [], []
    for h in hud:
        k = norm(h.get("PROJECT"))
        cands = by_name.get(k, [])
        # Ambiguous names are skipped rather than guessed at.
        if len(cands) != 1 or not h.get("extended_use_ends_est"):
            continue
        oy = as_int(cands[0]["Est. Program Exit"])
        if oy is None:
            continue
        diff = oy - h["extended_use_ends_est"]
        diffs.append(diff)
        matches.append({
            "project": h["PROJECT"], "yr_pis": h.get("YR_PIS"),
            "li_units": h.get("LI_UNITS"),
            "derived_exit": h["extended_use_ends_est"],
            "ohfa_exit": oy, "diff_years": diff,
            "ohfa_total_units": as_int(cands[0].get("Total Units")),
            "ohfa_population": cands[0].get("Population", "").strip(),
        })

    exits = collections.Counter()
    units = collections.Counter()
    for x in ohfa:
        y, u = as_int(x["Est. Program Exit"]), as_int(x["Total Units"]) or 0
        if y:
            exits[y] += 1
            units[y] += u

    out = {
        "source": "OHFA Projects Exiting LIHTC Program Affordability Period (Tableau export)",
        "dashboard": "https://analytics.das.ohio.gov/t/OHFAPUB/views/"
                     "ExitingAffordabilityPublic/ExitingAffordability",
        "county": county,
        "note": "OHFA column is 'Est. Program Exit' — authoritative source, still an estimate.",
        "project_count": len(ohfa),
        "total_units": sum(as_int(x.get("Total Units")) or 0 for x in ohfa),
        "exits_by_year": {str(y): {"projects": exits[y], "units": units[y]} for y in sorted(exits)},
        "validation": {
            "matched": len(matches),
            "ohfa_later": sum(1 for d in diffs if d > 0),
            "ohfa_earlier": sum(1 for d in diffs if d < 0),
            "equal": sum(1 for d in diffs if d == 0),
            "median_diff_years": statistics.median(diffs) if diffs else None,
            "within_1_year_pct": round(sum(1 for d in diffs if abs(d) <= 1) / len(diffs) * 100, 1)
                                 if diffs else None,
        },
        "matches": sorted(matches, key=lambda m: -abs(m["diff_years"])),
        "projects": ohfa,
    }
    json.dump(out, open(out_path, "w"), indent=2)
    v = out["validation"]
    print(f"{len(ohfa)} {county} projects, {out['total_units']:,} units", file=sys.stderr)
    print(f"matched {v['matched']}; {v['within_1_year_pct']}% within +/-1yr of derived",
          file=sys.stderr)
    print(f"wrote {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3],
         sys.argv[4] if len(sys.argv) > 4 else "Montgomery")
