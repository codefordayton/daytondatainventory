#!/usr/bin/env python3
"""Harvest HUD LIHTC properties for a county and derive affordability horizons.

Usage:
    ./harvest_lihtc.py <output.json> [county] [state]

IMPORTANT: HUD's LIHTC database carries no expiration field — only YR_PIS (year
placed in service) and YR_ALLOC. The compliance/extended-use horizons written
here are DERIVED from statute, not published dates:

  * 15-year initial compliance period (IRC §42(i)(1))
  * +15-year minimum extended use period (IRC §42(h)(6)) => 30 years total
  * Pre-1990 allocations predate the extended-use requirement, so their
    restrictions may have ended after 15 years.

Actual expiration depends on the recorded extended use agreement, which is
often longer than the statutory minimum, and can be cut short by the Qualified
Contract process. Treat these as a screening horizon and confirm
property-by-property against the National Housing Preservation Database or
OHFA's recorded agreements before making any claim about a specific property.
"""
import json
import sys
import time
import urllib.parse
import urllib.request

URL = ("https://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services"
       "/LIHTC/FeatureServer/0/query")

FIELDS = ("HUD_ID,PROJECT,PROJ_ADD,PROJ_CTY,PROJ_ST,PROJ_ZIP,YR_PIS,YR_ALLOC,"
          "N_UNITS,LI_UNITS,N_0BR,N_1BR,N_2BR,N_3BR,N_4BR,TYPE,CREDIT,BOND,"
          "TRGT_POP,TRGT_FAM,TRGT_ELD,TRGT_DIS,TRGT_HML,RENTASSIST,MFF_RA,"
          "FMHA_515,HOME,CDBG,HOPEVI,NON_PROF,INC_CEIL,LOW_CEIL,ALLOCAMT,"
          "CURCNTY_NM,TRACT2KX,PLACE_NM2KX,LAT,LON,DATANOTE")

COMPLIANCE_YEARS = 15
EXTENDED_USE_YEARS = 15


def fetch(county, state):
    where = f"PROJ_ST='{state}' AND CURCNTY_NM LIKE '%{county}%'"
    out, offset = [], 0
    while True:
        params = {"where": where, "outFields": FIELDS, "returnGeometry": "false",
                  "resultOffset": offset, "resultRecordCount": 1000, "f": "json"}
        with urllib.request.urlopen(f"{URL}?{urllib.parse.urlencode(params)}", timeout=120) as r:
            d = json.load(r)
        feats = d.get("features", [])
        out.extend(a["attributes"] for a in feats)
        if len(feats) < 1000:
            break
        offset += 1000
        time.sleep(0.3)
    return out


def derive(rec):
    """Attach derived horizons. See module docstring for why these are estimates."""
    try:
        pis = int(rec.get("YR_PIS") or 0)
    except (TypeError, ValueError):
        pis = 0
    if not (1980 < pis < 2100):
        rec["compliance_ends"] = None
        rec["extended_use_ends_est"] = None
        rec["horizon_basis"] = "no valid YR_PIS"
        return rec
    rec["compliance_ends"] = pis + COMPLIANCE_YEARS
    try:
        alloc = int(rec.get("YR_ALLOC") or 0)
    except (TypeError, ValueError):
        alloc = 0
    if alloc and alloc < 1990:
        rec["extended_use_ends_est"] = pis + COMPLIANCE_YEARS
        rec["horizon_basis"] = "pre-1990 allocation: extended use not required"
    else:
        rec["extended_use_ends_est"] = pis + COMPLIANCE_YEARS + EXTENDED_USE_YEARS
        rec["horizon_basis"] = "statutory minimum 15+15"
    return rec


if __name__ == "__main__":
    outpath = sys.argv[1]
    county = sys.argv[2] if len(sys.argv) > 2 else "Montgomery"
    state = sys.argv[3] if len(sys.argv) > 3 else "OH"
    rows = [derive(r) for r in fetch(county, state)]
    json.dump({"source": "HUD LIHTC Database (services.arcgis.com/VTyQ9soqVukalItT)",
               "county": county, "state": state,
               "harvested": time.strftime("%Y-%m-%d"),
               "caveat": "compliance_ends / extended_use_ends_est are DERIVED from "
                         "statute, not published expiration dates. Confirm against NHPD "
                         "or OHFA recorded agreements before citing any single property.",
               "count": len(rows), "properties": rows},
              open(outpath, "w"), indent=2)
    print(f"wrote {len(rows)} LIHTC properties to {outpath}", file=sys.stderr)
