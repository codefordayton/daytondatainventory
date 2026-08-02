# Montgomery County CAMA Characteristics (bulk extract)

> The Auditor's full mass-appraisal database: 35 relational tables, ~2.3 GB uncompressed,
> monthly back to January 2011. Structural condition, year built, room counts, **building
> permits**, and **apartment rents** — the structural counterpart to the City's exterior
> Housing Condition Survey.

## Source

- **Publisher:** Montgomery County Auditor (via Treasurer downloads)
- **Index:** https://go.mcohio.org/applications/treasurer/search/filedownloads.cfm (type `CC`)
- **File:** `Cama_Files_20260630.zip` — 126 MB zipped, **2.26 GB / 35 files** unzipped
- **Archive:** 76 monthly files, 2011-01 → 2026-06
- **Layout:** `docs/mc_file_layouts/Cama_Data_Layout.pdf` (33 tables, 750 columns)
- **Format:** fixed-width `.DAT`, CRLF, joined on `PARID`
- **Parser:** [`scripts/cama.py`](../scripts/cama.py)
- **Verified 2026-08-01:** downloaded and parsed in full

```bash
pdftotext -layout docs/mc_file_layouts/Cama_Data_Layout.pdf layout.txt
python3 scripts/cama.py spec layout.txt cama_spec.json
python3 scripts/cama.py freq cama_spec.json DWELDAT DWELL.DAT GRADE CDU
```

## Tables that matter for housing policy

| File | Rows | What it holds |
|---|---|---|
| `PARDAT.DAT` | 259,815 | Parcel master — **`LIVUNIT` living-unit count**, class, land use, neighborhood |
| `DWELL.DAT` | 189,389 | Residential dwellings — year built, **condition (`CDU`)**, **quality (`GRADE`)**, rooms, baths, heat, basement, living area |
| `PERMIT.DAT` | 251,570 | **Building permits** — parcel, number, date, type, valuation, status |
| `COMAPT.DAT` | 6,834 | **Apartment units and rents** by bedroom count |
| `SALES.DAT` | — | Sales history |
| `OBY.DAT` | — | Outbuildings / yard items |
| `COMDAT.DAT` | — | Commercial buildings |
| `HMSD.DAT` | — | Homestead exemption detail |
| `NBHD.DAT` | 812 KB | **Neighborhood code → name lookup** |
| `GRADE/EXTWALL/HEAT/BSMT/ATTIC/SHFACT/CICDU.DAT` | small | **Code lookup tables — the embedded data dictionary** |

## Housing stock — `PARDAT.LIVUNIT` (259,815 parcels)

| Living units | Parcels |
|---|---|
| 0 (vacant/non-residential) | 63,500 |
| 1 | 186,734 |
| 2 | 5,167 |
| 3–4 | 2,756 |
| 5–19 | 1,007 |
| 20+ | 651 |

This is the missing stock-by-units denominator. Note 1,658 parcels carry 5+ units — small
in count, large in unit terms.

## Condition and quality — `DWELL.DAT` (189,389 dwellings)

**`CDU` — condition/desirability/utility** (codes confirmed against `CICDU.DAT`):

| Code | Meaning | Count |
|---|---|---|
| AV | Average | 148,976 |
| FR | Fair | 17,073 |
| GD | Good | 15,789 |
| VG | Very Good | 3,518 |
| PR | Poor | 3,069 |
| UN | Unsound | 801 |
| VP | Very Poor | 1 |

**`GRADE` — construction quality** (letters decode via `GRADE.DAT`: A very good,
B custom, C average, D below average, E poor, X excellent, XX exceptional):

C 70,516 · C+ 47,635 · C- 23,530 · D+ 12,396 · B- 10,358 · B 7,484 · D 7,108 ·
B+ 3,469 · A 1,597 · A- 1,513 · D- 1,375 · A+ 1,079 · X- 479 · E+ 275

**Year built** — a genuinely old stock, 48% pre-1960:

| Era | Dwellings | Share |
|---|---|---|
| pre-1940 | 38,234 | 20% |
| 1940–59 | 53,678 | 28% |
| 1960–79 | 57,546 | 30% |
| 1980–99 | 22,262 | 12% |
| 2000+ | 17,669 | 9% |

Other useful `DWELL` fields: `RMTOT`, `RMBED`, `FIXBATH`, `FIXHALF`, `STORIES`, `STYLE`,
`EXTWALL`, `HEAT`, `FUEL`, `BSMT`, `SFLA` (total living area), `REMKIT` / `REMBATH`
(kitchen/bath remodeled), `INTEXT` (interior condition relative to exterior).

## Building permits — `PERMIT.DAT` (251,570 permits)

Parcel-linked, **1960 → 2026**, ~10,000/year recently. Fields: `PARID`, `NUM`, `PERMDT`,
`WHY` (type), `AMOUNT`, `FLAG` (status), `NOTE1-3`.

**Type (`WHY`):** ELECTRIC 24,536 · AC 22,587 · DWLG 17,865 · FURNACE 16,821 ·
GAS LINE 15,679 · ALT 13,697 · ADDN 10,862 · **DEMO 9,548** · MISC 8,120 ·
REMODEL 8,029 · FENCING 5,179 · SHED 5,034 · SIGNS 4,931 · (blank) 20,105

**Status (`FLAG`):** C closed 227,514 · O open 23,515 · R 9

**Volume by year:** 2016 8,556 · 2017 7,979 · 2018 8,567 · **2019 12,671** · 2020 9,935 ·
2021 10,757 · 2022 9,805 · 2023 6,051 · 2024 10,904 · 2025 9,484 · 2026 3,533 (partial)

Demolition permits run 122–442/year; the 2019 spike in both total permits and demolitions
is the Memorial Day tornado outbreak.

118,033 permits carry `AMOUNT` > 0 — median $10,100, **$20.0 B total**.

## Apartments and rents — `COMAPT.DAT` (6,834 rows)

**44,771 units across 3,640 parcels**, broken out by unit type with a recorded rent.

| Bedrooms | Units | With rent | Median annual | ≈ monthly |
|---|---|---|---|---|
| 0 (studio) | 3,251 | 272 | $4,320 | $360 |
| 1 | 19,497 | 2,422 | $4,920 | $410 |
| 2 | 19,242 | 3,447 | $6,000 | $500 |
| 3 | 2,300 | 595 | $6,900 | $575 |
| 4 | 265 | 43 | $5,940 | $495 |

⚠️ **These are assessor-recorded rents for valuation, not market rents.** $500/month for a
2-bedroom is far below Dayton market, so these are scheduled/economic rents used in the
income approach and may be stale. **Do not present them as market rent.** They are useful
for *relative* comparison and for identifying the multifamily inventory, not for
affordability levels — use ACS/HUD FMR for that.

## Parsing gotchas — read before writing code

**1. `DWELL.DAT` records span three physical lines.** A 643-char data line, then a wrapped
9-char date, then a blank. Reading line-by-line yields **568,167 rows instead of 189,389**
and invents 378,778 phantom blank records — a 3x overcount that looks plausible.
`scripts/cama.py` stitches records back together.

**2. The layout PDF is off by one from `GRADE` onward.** In `DWELDAT`, columns at start
≤ 92 (`HEAT`) match the delivered file; everything from start 95 (`GRADE`) on sits **one
byte later** than documented. Verified: with the shift, `CDU` matches the documented code
set for 99.9% of 189,389 records and `GRADE` resolves to valid letter grades; without it,
neither matches at all (0.0%). Encoded as `OFFSET_FIXES` in `scripts/cama.py`.

**3. Lookup files are the embedded dictionary.** `GRADE.DAT`, `EXTWALL.DAT`, `HEAT.DAT`,
`BSMT.DAT`, `ATTIC.DAT`, `SHFACT.DAT`, `CICDU.DAT`, `NBHD.DAT` decode the coded columns.
Don't guess at codes — these ship with the data.

**4. `DWELL` has multiple cards per parcel.** `CARD` = 1 for 188,367; 2–6 for the rest
(multiple structures). Aggregate by `PARID`, don't assume one row per parcel.

**5. Dates are `DD-MON-YY`** Oracle style. `PERMIT.PERMDT` has 1 record dated 2027 —
data entry error; filter implausible dates.

**6. Countywide, not Dayton.** Filter to Dayton parcels before reporting city figures.

**7. Some layout descriptions are wrong.** `PERMIT.NUM` is described as "Tax Year" and
`PERMIT.PERMDT` as "User ID of last maintenance"; both are mislabeled — they are the
permit number and permit date. Trust the data over the description.
