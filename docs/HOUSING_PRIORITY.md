# Housing Policy Priority Datasets

The shortlist. Out of 1,767 catalogued datasets, these are the ones that carry
real weight for housing policy work. Ordered by how central they are.

All record counts and dates were pulled live on **2026-08-01**.

---

## Tier 1 — The backbone

### 1. Dayton Housing Condition Survey Parcels 2025
**88,922 parcels · 66 fields · last edited 2026-07-10**
`https://services2.arcgis.com/3dDB2Kk6kuA2gIGw/arcgis/rest/services/Dayton_Housing_Condition_Survey_Parcels_2025/FeatureServer`

Parcel-level exterior condition grades for the whole city, with **2023 grades carried
in the same table** (`GRADE_2023`) plus a precomputed change field (`HCS_DIFF`). This is
the single most valuable housing dataset the city publishes — it supports
condition change over time at parcel, street, and neighborhood level.

Grade scale (from `GRADE` / `GRADE_DESC`):

| Grade | Meaning | Count (2025) |
|---|---|---|
| 0 | Vacant lot | 19,144 |
| 1 | Sound | 32,045 |
| 2 | Minor repair | 13,524 |
| 3 | Major repair | 9,517 |
| 4 | Rehabilitation | 959 |
| 5 | Dilapidated | 189 |
| *(null)* | Not surveyed | 13,544 |

Occupancy status (`STATUS`): `OCC` occupied 50,774 · `VS` vacant & secure 2,557 ·
`VB` vacant & boarded 1,588 · `DEMO` 1,103 · `VTO` vacant/too damaged to board 123 ·
`NA` 18,184 · null 14,593.

Per-defect flags (YES/NO): roof, foundation, porch, siding, soffit, fascia, gutter,
chimney, paint, window — so you can profile *what kind* of deterioration, not just how much.

There is a **2023 edition** (66,033 parcels, 29 fields) as a separate service, and a
public Hub site at `https://dayton-housing-condition-survey-DaytonOhio.hub.arcgis.com`.

### 2. Accela Housing Code Enforcement Incidents
**12,879 records · 2026-01-02 → 2026-06-30**
`https://maps.daytonohio.gov/gisservices/rest/services/Accela_UPDATES/AccelaIncidents_UPDATE/MapServer/0`

Live code enforcement complaints, all `COMPLAINT_TYPE = HOUSING`. Point geometry,
complaint number, address, neighborhood, record date, status, action taken, assigned staff.

Status distribution: CLOSED 5,072 · OPEN 4,955 · ACTIVE 1,520 · ABATED 965 ·
PAID 196 · ABATED/PAID 61 · plus review/appeal/extension states.

⚠️ **Two services exist and neither is the full history.** The non-`_UPDATE` sibling
(`/Accela/AccelaIncidents/MapServer/0`) is readable — the earlier 503 was transient load —
but holds **8,805 records covering only 2022-07-24 → 2023-01-19**, a stale snapshot with a
48-field schema against the newer service's 90. Between January 2023 and January 2026
nothing is published.

⭐ **Permits are a separate route.** Code enforcement is the only thing in the GIS layers,
but the City's permit records — 49 record types including demolition — are queryable
through **Accela Citizen Access**. See
[`dictionaries/accela-permits-aca.md`](../dictionaries/accela-permits-aca.md).

### 3. Montgomery County CAMA Characteristics — ⭐ downloaded and parsed
**76 monthly files · Jan 2011 → Jun 2026 · 2.3 GB unzipped · 35 relational tables**
`https://go.mcohio.org/applications/treasurer/search/filedownloads.cfm` (type `CC`)
Full dictionary: [`dictionaries/mc-cama.md`](../dictionaries/mc-cama.md) ·
parser: [`scripts/cama.py`](../scripts/cama.py)

Far more than "property characteristics." Verified contents:

- **`PARDAT`** 259,815 parcels with **`LIVUNIT` living-unit counts** — the stock-by-units
  denominator that was missing. 1 unit 186,734 · 2 units 5,167 · 3–4 2,756 · 5–19 1,007 · 20+ 651.
- **`DWELL`** 189,389 dwellings with **condition (`CDU`)** — Average 148,976, Fair 17,073,
  Good 15,789, Very Good 3,518, **Poor 3,069, Unsound 801** — plus construction grade,
  rooms, baths, heat, living area, and year built. **48% of the stock predates 1960**
  (pre-1940 20%, 1940–59 28%).
- **`PERMIT`** 251,570 **building permits**, 1960→2026, parcel-linked, ~10,000/year, with
  type, valuation ($20.0 B total), and status. **9,548 demolition permits.** The 2019
  spike (12,671 permits, 442 demos) is the tornado outbreak.
- **`COMAPT`** **44,771 apartment units** across 3,640 parcels, by bedroom count, with
  assessor-recorded rents. ⚠️ Valuation rents, *not* market rents — see the dictionary.
- Embedded **code lookup tables** (`GRADE`, `CDU`, `HEAT`, `BSMT`, `EXTWALL`, `NBHD`) that
  decode every categorical column.

**This closes the permits gap.** Building permits were listed as a priority theme with no
identified source; they've been in the public CAMA download all along.

⚠️ Two parsing traps that silently corrupt results — `DWELL.DAT` records span three lines
(naive reading gives a 3x overcount), and the layout PDF is off by one byte from `GRADE`
onward. Both are handled in `scripts/cama.py` and documented in the dictionary.

### 4. Montgomery County Sales files
**Weekly (301 files, from 2011) · Monthly (110, from 2009) · Yearly (18, from 2001)**

Every recorded transfer: parcel ID, conveyance number, sale date, price, old and new
owner, mailing address, class, acreage, taxable and assessed values, sale type,
sale validity. 23 fields; layout in `docs/mc_file_layouts/sales_file_layout.pdf`.

The **mailing address vs. parcel location** split is what lets you identify
absentee/out-of-state ownership — see `CAVEATS.md` before using price fields.

### 4b. Montgomery County Taxroll — ⭐ the single most useful file
**254,693 parcels · 82 columns · 1,572 archived files back to 2019-03**
`https://go.mcohio.org/applications/treasurer/search/filedownloads.cfm` (type `TR`)
Full dictionary: [`dictionaries/mc-taxroll.md`](../dictionaries/mc-taxroll.md)

Downloaded and parsed in full on 2026-08-01. This one file carries **tenure, ownership,
delinquency, foreclosure, year built, and a census tract** on every parcel row:

| Field | Verified values |
|---|---|
| `OWNOCC` — owner occupancy | **Y 135,858 / N 118,834** |
| `RENTALREG` — rental registration | **Y 17,454** |
| `HMSDFLAG` — homestead exemption | Y 33,065 |
| `NETDELQ` > 0 | **13,577 parcels delinquent** |
| `FRCLSR` (a date, not a flag) | **1,072 parcels in foreclosure** |
| `CENSUS TRACT` | 419 distinct — **direct ACS join, no geocoding** |
| `CLS` | R 214,548 · C 19,635 · E 13,941 · A 3,739 · I 2,656 · U 174 |

Plus `OWNERNAME`/`MAILINGNAME`/`PADDR`/`CITYNAME` for absentee and LLC ownership analysis,
and `MORTCO` which flags **multiple-parcel owners** — the institutional-investor signal.

⚠️ `RENTALREG = Y` counts **registrations**, not rentals: 17,454 registered against
~118,834 non-owner-occupied parcels. That gap is itself a policy finding, but don't read
it as the rental stock.

### 4c. Subsidized housing & affordability roll-off — ⭐ federal, not local
**LIHTC: 120 properties / 8,412 LI units · Section 8: 83 properties / 5,586 assisted units**
Full dictionary: [`dictionaries/subsidized-housing-rolloff.md`](../dictionaries/subsidized-housing-rolloff.md)

Neither the City nor the County publishes an income-restricted inventory. It has to be
assembled from federal sources — both of which are open ArcGIS REST layers:

- **HUD LIHTC Database** — 120 Montgomery County properties (88 in Dayton, 5,762 LI units).
  ⚠️ **No expiration field exists**; roll-off must be derived as placed-in-service + 30
  years (the same assumption NHPD publishes). Estimated exits: **12 properties / 1,586 LI
  units in 2027–2030**, 21 / 1,654 in 2031–2035. 42 properties are already past their
  statutory minimum and need individual status checks.
- **HUD Multifamily Assisted** — 83 properties with **real published contract expiration
  dates**, refreshed monthly. **23 contracts / 812 units expire on or before 2030**,
  including Chevy Chase Park (232 units, 2029-09-22).

⚠️ **Do not add the two together** — 15 properties appear in both under matching names.

The authoritative state source is **OHFA's "Projects Exiting LIHTC Affordability Period"**
Tableau dashboard, and the canonical national one is **NHPD** (free registration). Neither
is scriptable; both are documented in the dictionary as next steps.

### 5. Montgomery County Delinquent Files
**81 monthly files · Jan 2005 → Jul 2026**

Tax-delinquent parcels. The standard leading indicator for distress, abandonment,
and forfeiture pipeline. Layout: `docs/mc_file_layouts/delq_file_layout.pdf`.

---

### 6. MVRPC Regional Housing Study — Block Groups (`HS_BlockGroups`)
**793 block groups · 744 fields** (≈422 block groups in Montgomery County)
`https://services.arcgis.com/3TIUdMHOqnLBrZEH/arcgis/rest/services/HS_BlockGroups/FeatureServer/1`
⚠️ **Layer index 1, not 0.**

ACS/Census-derived: tenure, owner/renter cost burden split, rent bands, home values,
mortgage costs, vacancy, year built, income, demographics. Verified live: 793 features,
744 fields. This is the affordability/tenure layer the city's own data doesn't provide.

Regional rather than city-published, so it sits outside the strict "official City/County"
scope — but it's the authoritative regional rollup and is maintained.
MVRPC's full org holds **3,422 items / 1,011 data services**, of which 106 are
housing-relevant — considerably more than the ~176 previously estimated, and worth its
own dedicated pass.

### 7. City of Dayton Housing Projects (`HousingRequest_ExportFeature1`)
**376 projects · 3,929 units · 56 fields**
`https://services2.arcgis.com/3dDB2Kk6kuA2gIGw/arcgis/rest/services/HousingRequest_ExportFeature1/FeatureServer/0`

Backs the public Housing Dashboard StoryMap. Verified live distributions:

| UnitType (affordability) | Projects | | UnitTenure | Projects |
|---|---|---|---|---|
| Affordable | 245 | | Owner | 301 |
| Subsidized 0–80% AMI | 84 | | Rental | 58 |
| Market-Rate | 36 | | Homelessness Assistance | 8 |
| Homelessness Assistance | 8 | | Demolition | 4 |
| Demolition | 3 | | *(blank)* | 5 |

⚠️ **One-time geocoded export, not a live-maintained layer** — treat the counts as a
snapshot and confirm cadence/ownership with the publisher.
⚠️ **Field names are mangled by the export**: `USER_Unit_` = UnitType,
`USER_Unit1` = UnitTenure, `USER__Unit` = NumberOfUnits, `USER_Fundi` = FundingSources.
Read the **aliases**, not the names.
⚠️ This service **rejects `groupByFieldsForStatistics`** (returns empty). Pull records
with `outFields` and aggregate client-side.

`HousingProjects_ProgramType` in the same org also has 376 rows / 56 fields — almost
certainly the same underlying export under a second name. Confirm before treating as
independent.

---

## Tier 2 — Strong supporting data

| Dataset | Size | Why it matters |
|---|---|---|
| **DaytonParcels** | 88,668 · 57 fields | City parcel base layer; the join spine |
| **City_of_Dayton_Owned_Parcel** | 1,926 | Publicly held inventory — disposition/land bank questions |
| **ARPA Nuisance Parcel Points** | 1,259 · 27 fields | Nuisance abatement targets funded by ARPA |
| **Nuisance Map 10.24** | 1,752 | More recent nuisance snapshot |
| **Issue 9 Vacant Mowing** (2018–2021 + current) | 5,182–7,640/yr | Vacant-lot maintenance; a *proxy time series for vacancy* |
| **Dayton Used Address** | 163,184 · 47 fields | Master address list — essential for address matching |
| **HOUSING_INSPECTION_AREAS_2025** | 107 | Inspector geography; explains coverage patterns |
| **HousingProjects_ProgramType** | 376 · 56 fields | Funded housing projects by program |
| **Zoning** | 970 | Regulatory capacity, what can be built where |
| **Dayton Neighborhood Boundary** | 66 | The standard reporting geography |
| **DaytonNeighborhoods_Population** | 65 · 33 fields | Population denominators per neighborhood |
| **Taxroll** | 1,572 files, from 2019 | Full tax roll; ownership + valuation + exemptions |
| **Parcels_HCS_Nuisance_WaterZero** | 5 layers · 159,656 rows | Pre-joined HCS + nuisance + **zero-water-usage** — a strong vacancy signal |

`Parcels_HCS_Nuisance_WaterZero` deserves a look: someone at the city has already
joined condition survey, nuisance, and zero water consumption. Zero-water is one of the
better empirical vacancy indicators, and it appears the city already computes it.

---

## Tier 3 — Context

- **Qualified Opportunity Zones (Montgomery County OH)** — investment incentive geography
- **ARPA Focus Neighborhoods** (6) — where recovery dollars were targeted
- **Neighborhood_Profile** / **Population_Density_per_Neighborhood** — denominators
- **TornadoAssessment_Housing** (1,015) — 2019 tornado damage; still shapes some stock
- **Street Light Districts** (93 monthly files) — assessment districts, parcel-linked
- **BOE precinct shapefiles** — for tying housing conditions to civic participation

---

## The joins that make this work — measured, not assumed

**City ↔ County needs no crosswalk.** Tested 2026-08-02: City HCS `PARCELID` uses the same
format as County `PARID` (`R72 08702 0039` / `A01 00202 0061`), and **96.3% of distinct
City parcel IDs join directly to the County taxroll** (15,525 of 16,116 in a 20,000-row
sample). These systems already speak the same language.

The real obstacles are different, and smaller:

1. **Blank parcel IDs in the HCS** — ~17% of sampled rows (3,386 of 20,000) have no
   `PARCELID` at all. `KEY_PARCELID` and `K_PID` are also blank in the rows checked. This
   is the largest single join loss, and it is a data-completeness problem, not a
   format-translation problem.
2. **~3.7% genuinely unmatched** (591 IDs) — patterns like `R72 00305 78E1` suggest
   split/merged or special parcels. Worth a look but not a blocker.
3. **Multiple HCS rows per parcel** — one row per structure, so aggregate by `PARCELID`
   before joining or you will multiply county attributes.
4. ~~**Accela code enforcement has no parcel ID**~~ — ✅ **SOLVED 2026-08-02.**
   `Dayton Used Address` carries both `ADDRKEY` (Accela's key) and `TAXPINNO` (the parcel
   id), so this is an exact integer join, not fuzzy matching. **12,875 of 12,879 incidents
   matched (99.97%)** to 6,866 parcels. See
   [`dictionaries/address-parcel-bridge.md`](../dictionaries/address-parcel-bridge.md).

**With the bridge built, every major housing dataset is now joinable at parcel level.**
Validation: code-complaint rate rises monotonically with HCS condition grade — 2.5% on
vacant lots, 6.0% sound, 12.0% minor repair, 22.4% major repair, 47.7% rehabilitation,
53.0% dilapidated. A dilapidated parcel is **21× more likely** to carry a complaint than a
vacant lot.

**And for anything tract-level, no join is needed at all** — the County taxroll carries
`CENSUS TRACT` on every row (419 distinct), so ACS work can start immediately.
