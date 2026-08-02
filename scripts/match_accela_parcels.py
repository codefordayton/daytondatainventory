#!/usr/bin/env python3
"""Join Dayton code enforcement incidents to parcel ids via the address bridge.

Usage:
    ./match_accela_parcels.py <accela.json> <address_bridge.json> <out.json>

Two-stage match, most reliable first:

  1. ADDRKEY  - exact integer key shared by Accela and the City address layer.
  2. normalized address - street number + directionals + name + suffix, folded
     to a common vocabulary, as a fallback when the key misses.

Anything still unmatched is reported rather than force-matched; a wrong parcel
is worse than a null in this context.
"""
import collections
import json
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from build_address_bridge import norm_addr  # noqa: E402


def main(accela_path, bridge_path, out_path):
    inc = json.load(open(accela_path))["incidents"]
    bridge = json.load(open(bridge_path))
    by_key = bridge["by_addrkey"]
    by_addr = bridge["by_norm_address"]

    out, stats = [], collections.Counter()
    for r in inc:
        parcel, method = None, "unmatched"

        k = r.get("ADDRKEY")
        if k is not None:
            hit = by_key.get(str(int(k)))
            if hit and hit["parcel"]:
                parcel, method = hit["parcel"], "addrkey"

        if not parcel:
            na = norm_addr(r.get("STR_NO"), r.get("STR_DIR"), r.get("STR_NAME"),
                           r.get("STR_SUFFIX"), r.get("STR_DIR_SUFFIX"))
            hit = by_addr.get(na)
            if hit and hit["parcel"]:
                parcel, method = hit["parcel"], "normalized_address"

        stats[method] += 1
        out.append({"complaint_no": r.get("COMPLAINT_NO"),
                    "record_date": r.get("RECORD_DATE"),
                    "status": r.get("STATUS"),
                    "neighborhood": (r.get("NEIGHBORHOOD") or "").strip(),
                    "address": (r.get("ADDRESS") or "").strip(),
                    "addrkey": r.get("ADDRKEY"),
                    "parcel": parcel, "match_method": method})

    total = len(out)
    matched = total - stats["unmatched"]
    json.dump({"source_incidents": accela_path, "bridge": bridge_path,
               "count": total, "matched": matched,
               "match_rate_pct": round(matched / total * 100, 1) if total else 0,
               "by_method": dict(stats),
               "distinct_parcels": len({o["parcel"] for o in out if o["parcel"]}),
               "incidents": out}, open(out_path, "w"), indent=2)

    print(f"incidents        : {total:,}")
    print(f"matched to parcel: {matched:,} ({matched / total * 100:.1f}%)")
    for m, n in stats.most_common():
        print(f"  {m:<20}{n:>8,}")
    print(f"distinct parcels : {len({o['parcel'] for o in out if o['parcel']}):,}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
