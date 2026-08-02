# Montgomery County Taxroll (bulk file)

> The single highest-value file in this inventory. One row per parcel, countywide,
> covering ownership, tenure, condition proxies, delinquency, and foreclosure — with a
> census tract already attached.

## Source

- **Publisher:** Montgomery County Treasurer
- **Index page:** https://go.mcohio.org/applications/treasurer/search/filedownloads.cfm (type `TR`)
- **Newest file:** `TAXROLL_20260731.zip` — 32.9 MB zipped, **656 MB** CSV
- **Archive:** 1,572 files, 2019-03 → 2026-07
- **Official layout:** `docs/mc_file_layouts/taxroll_file_layout.pdf`
- **Access:** public HTTP, no auth
- **Verified 2026-08-01:** downloaded and parsed in full — **254,693 rows · 82 columns**

## Why it matters

This one file speaks to most of the subcommittee's priority themes:

| Theme | Fields |
|---|---|
| Tenure | `OWNOCC`, `RENTALREG`, `HMSDFLAG` |
| Ownership / absentee | `OWNERNAME1/2`, `MAILINGNAME1/2`, `PADDR1-3`, `CITYNAME`, `MORTCO` |
| Tax delinquency | `NETDELQ`, `HLF1DELQ`, `HLF1PEN`, `HLF2PEN` |
| Foreclosure | `FRCLSR` |
| Stock / age | `YRBL`, `SQ. FT.`, `ACRES`, `CLS`, `LUC` |
| Valuation | `ASMTLAND/BLDG/TOTAL`, `TAXABLELAND/BLDG/TOTAL`, `AET*`, `C*` |
| Geography | `CENSUS TRACT`, `NBHD`, `CITY/TOWNSHIP`, `SCHOOL DISTRICT`, `PARCEL LOCATION ZIP` |

**`CENSUS TRACT` is on every row** (419 distinct tracts) — you can join to ACS without
geocoding anything.

## Verified distributions (2026-07-31 file, all 254,693 rows)

**`OWNOCC` — owner occupancy credit**
| Value | Count |
|---|---|
| Y | 135,858 |
| N | 118,834 |
| X | 1 |

**`RENTALREG` — Rental Registration Program**
| Value | Count |
|---|---|
| N | 237,239 |
| **Y** | **17,454** |

**`HMSDFLAG` — homestead exemption**
| Value | Count |
|---|---|
| N | 221,628 |
| Y | 33,065 |

**`CLS` — parcel class**
| Code | Meaning | Count |
|---|---|---|
| R | Residential | 214,548 |
| C | Commercial | 19,635 |
| E | Exempt | 13,941 |
| A | Agricultural | 3,739 |
| I | Industrial | 2,656 |
| U | Utilities | 174 |

**Distress:** 13,577 parcels with `NETDELQ` > 0 · 1,072 parcels carry a `FRCLSR` date.

## Full column list (as delivered)

`TXYR` · `PARCELID` · `HLF1CHG` · `HLF2CHG` · `HLF1RED` · `HLF2RED` · `HLF1ADJ` ·
`HLF2ADJ` · `HLF1RLBK` · `HLF2RLBK` · `HLF1HMSD` · `HLF2HMSD` · `HLF1HMRB` · `HLF2HMRB` ·
`HLF1PEN` · `HLF2PEN` · `HLF1SPASMTS` · `HLF2SPASMTS` · `FULLYRAMTDUE` · `NETDELQ` ·
`HLF1AMTDUE` · `HLF2AMTDUE` · `HLF1DAYCRDT` · `HLF2DAYCRDT` · `PARCELLOCATION` · `LEGAL1` ·
`LEGAL2` · `LEGAL3` · `ACRES` · `TXDST` · `CLS` · `LUC` · `AGLAND` · `ASMTLAND` ·
`ASMTBLDG` · `ASMTTOTAL` · `TAXABLELAND` · `TAXABLEBLDG` · `PUBLICUTILITY` · `ROLLTYPE` ·
`TAXABLETOTAL` · `OWNERNAME1` · `OWNERNAME2` · `MAILINGNAME1` · `MAILINGNAME2` · `PADDR1` ·
`PADDR2` · `PADDR3` · `CITYNAME` · `MORTCO` · `NBHD` · `ASMTWEN` · `AC` · `HMSDLAND` ·
`HMSDBLDG` · `FRCLSR` · `SALESDTE` · `PRICE` · `YRBL` · `GROSSRATE` · `EFFRATE` · `REDRATE` ·
`DUEDATE` · `B` · `HLF1DELQ` · `RENTALREG` · `AETASMTLAND` · `AETASMTBLDG` · `AETASMTTOTAL` ·
`AETTAXABLELAND` · `AETTAXABLEBLDG` · `AETTAXABLETOTAL` · `CASMTLAND` · `CTAXABLELAND` ·
`HMSDFLAG` · `SQ. FT.` · `DYTNCRDT` · `OWNOCC` · `CITY/TOWNSHIP` · `SCHOOL DISTRICT` ·
`PARCEL LOCATION ZIP` · `CENSUS TRACT`

Selected definitions from the official layout PDF:

| Field | Meaning |
|---|---|
| `NETDELQ` | Net delinquent amount |
| `RENTALREG` | Registered with the Rental Registration Program |
| `HMSDFLAG` | Indicator whether parcel is flagged for Homestead Exemption |
| `MORTCO` | Mortgage code (usually mortgage company, or **multiple-parcel owner**) |
| `DYTNCRDT` | Parcel flagged for Dayton Credit ($25.00 max) |
| `NBHD` | Neighborhood number (decode via the Neighborhood Codes file) |
| `REDRATE` | Reduction factor |
| `ASMTWEN` | Last date value/class record was updated |

## Gotchas

- **Headers are space-padded.** `hdr.index("OWNOCC")` fails unless you `.strip()` every
  header first. This silently makes fields look absent.
- **`FRCLSR` is a date, not a boolean** — values like `10-JUN-26`. Blank means no
  foreclosure. Dates are `DD-MON-YY` Oracle style.
- **`OWNOCC` (135,858) and `HMSDFLAG` (33,065) are not the same thing.** Owner-occupancy
  credit is broad; the homestead exemption is age/disability/income-restricted. Don't
  treat homestead as a general owner-occupancy proxy — use `OWNOCC`.
- **`RENTALREG = Y` is registration, not rental status.** 17,454 registered against
  ~118,834 non-owner-occupied parcels countywide, so **registration is far from complete
  coverage of the rental stock.** It measures compliance as much as tenure.
- **This is countywide (254,693 parcels), not Dayton-only.** Filter via `CITY/TOWNSHIP`
  or join to city parcels.
- Layout-PDF names don't always match delivered headers (`SALEDTE` vs `SALESDTE`).
- The CSV is **656 MB uncompressed** — stream it, don't load it into memory whole.
