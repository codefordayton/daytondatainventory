# Data Freshness

How current each source actually is — measured on 2026-08-02, not taken from
documentation. The short version: **the County's bulk files are the only sources with a
reliable, verifiable refresh cadence.** For most of the City's GIS layers there is no way
to tell how fresh the data is.

---

## County bulk files — measured cadence

Refresh interval computed from the gaps between published files, so this is observed
behaviour rather than a stated policy.

| Dataset | Files | Interval | Newest | Age |
|---|---|---|---|---|
| **Taxroll** | 1,572 | **daily** | 2026-07-31 | 2 days |
| **Available Tax Refunds** | 1,589 | **daily** | 2026-07-31 | 2 days |
| Weekly Sales | 301 | weekly | 2026-07-25 | 8 days |
| Monthly Sales | 110 | monthly | 2026-07-31 | 2 days |
| Delinquent Files | 81 | monthly | 2026-07-31 | 2 days |
| Street Light Districts | 93 | monthly | 2026-07-31 | 2 days |
| Neighborhood Codes | 16 | monthly | 2026-08-01 | 1 day |
| CAMA Characteristics | 76 | monthly | 2026-06-30 | 33 days |
| Yearly Sales | 18 | annual | 2026-08-01 | 1 day |

**Taxroll is published daily**, not monthly — 1,572 files since March 2019. Anything
needing current ownership, owner-occupancy, rental registration or foreclosure status can
be at most a day behind. This is the freshest substantial dataset in the whole inventory.

CAMA is the laggard at ~33 days, which is expected for a 2.3 GB monthly extract.

**Rental registrations** are dated 2026-07-01 across all 67 district files, consistent
with a monthly rebuild, but only one snapshot has been observed — cadence unconfirmed.

---

## ArcGIS layers — mostly unknowable

ArcGIS exposes two freshness signals. They are not equivalent:

- **`editingInfo.lastEditDate`** — when the *data* last changed. The signal that matters.
- **item `modified`** — when the *item record* last changed. A metadata edit bumps it; a
  data load may not. Weak evidence at best.

Of **1,671 layers carrying records**:

| | Layers | Share |
|---|---|---|
| Report a last-edit date | **37** | **2%** |
| Report nothing | 1,634 | 98% |

**For 98% of the City's published layers there is no machine-readable way to tell whether
the data is current.** That is the single largest governance gap in this inventory — a
bigger practical problem than any missing dataset, because it means a consumer cannot
distinguish live data from an abandoned copy without asking a person.

Among the 37 that do report, most are stale:

| Freshness | Layers | Records |
|---|---|---|
| Updated this month | 2 | 177,844 |
| Last 3 months | 1 | 88,668 |
| Within a year | 10 | 4,513 |
| **1–3 years stale** | **9** | **291,853** |
| **3+ years stale** | **15** | **127,958** |

Oldest layers still serving data include `SLSA_2014_Parcels` (88,512 rows, last edited
February 2017) and the `Issue_9_Vacant_Mowing` series (2017–2020).

### Item-modified dates, for what they are worth

All 374 AGOL services carry one. The distribution is not encouraging: **270 of 374 are
over a year old**, 163 of them over three years.

| Age of item record | Services |
|---|---|
| This month | 35 |
| Within 3 months | 10 |
| Within a year | 59 |
| 1–3 years | 107 |
| 3+ years | 163 |

---

## The datasets that matter, individually

| Dataset | Item modified | Age | Read |
|---|---|---|---|
| Dayton Housing Condition Survey 2025 | 2026-06-15 | 48d | **Current.** Layer also reports edits to 2026-07-10. |
| DaytonParcels | 2026-06-16 | 47d | **Current.** |
| Nuisance Map 10.24 | 2026-06-01 | 62d | Recent. |
| Zoning | 2026-01-14 | 200d | Plausible — zoning changes slowly. |
| Dayton Neighborhood Boundary | 2025-11-17 | 258d | Fine — boundaries are stable. |
| HousingProjects_ProgramType | 2025-11-13 | 262d | ⚠️ A one-time export; treat as a snapshot. |
| ARPA Nuisance Parcel Points | 2022-09-27 | **1,405d** | ⚠️ Nearly 4 years old. |
| City_of_Dayton_Owned_Parcel | 2021-07-30 | **1,829d** | ⚠️ 5 years old. Publicly-held inventory changes constantly — do not treat as current. |
| **Dayton Used Address** | 2018-11-09 | **2,823d** | ⚠️ See below. |

**`Dayton Used Address` needs care.** Its item record is nearly eight years old, yet it
serves 163,184 addresses and the address→parcel bridge matched 99.97% of 2026 code
enforcement incidents against it — including addresses for complaints filed this year. The
data is evidently being maintained even though the item metadata is not. This is precisely
why item-modified is a weak signal, and why the four unmatched incidents (all high
`ADDRKEY` values, i.e. new addresses) are worth watching as a lag indicator.

---

## Live sources

| Source | Freshness |
|---|---|
| **Accela Citizen Access** (permits) | Live — queries hit the working permitting system |
| **Accela code enforcement** (`_UPDATE`) | Current year, refreshed |
| Accela code enforcement (base service) | **Frozen** — 2022-07 → 2023-01 only |
| HUD Multifamily Assisted | Monthly per HUD |
| HUD LIHTC / Public Housing | Annual-ish |
| OHFA exiting-affordability | Unknown; dashboard gives no date |

---

## How to re-check

```bash
python3 scripts/build_catalog.py      # recomputes observed county cadence
python3 scripts/probe_capabilities.py data/raw/arcgis_cityofdayton.json out.json
python3 scripts/extract_fields.py     # refreshes lastEditDate where published
```

The `cadence` column in `catalog/master_catalog.csv` now carries measured intervals for
County files and the item-modified date for ArcGIS services. It is deliberately explicit
about which is which, because they mean different things.

---

## What to ask for

**Populate `lastEditDate`.** 98% of layers publish no data-freshness signal. Enabling
editor tracking is a configuration change, not a project, and it would let every consumer
tell live data from an abandoned copy without contacting anyone.

**Retire or label the stale layers.** `SLSA_2014_Parcels`, the `Issue_9_Vacant_Mowing`
series and similar are still served and still discoverable. If they are historical, saying
so in the description costs nothing and prevents someone analysing 2017 data as current.

**Confirm `City_of_Dayton_Owned_Parcel`.** Five years without an update on the city's own
property inventory is either a metadata problem or a real one, and it matters for
disposition and land bank work.
