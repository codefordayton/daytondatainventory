# Dayton / Montgomery County Data Inventory

An inventory of datasets published by the **City of Dayton** and **Montgomery County, Ohio**,
built for the City of Dayton housing policy **data subcommittee**.

This covers the **non-Building-Blocks** portion of the subcommittee's "Inventory & assess
current datasets" deliverable. Primary scope is official City of Dayton and Montgomery
County publishers; MVRPC has been swept as well since it holds the regional
affordability/tenure data. State/federal sources (Ohio SOS, HUD, Census) are noted where
authoritative but not yet systematically swept.

> ### Scope
> Everything catalogued here was obtained from the agencies' own public endpoints —
> ArcGIS REST services, bulk file downloads, and public search portals. No licensed or
> third-party platform data is included, and every figure was pulled from the source
> rather than read off a landing page.

**Harvest date: 2026-08-02.**

---

## What's here

| Path | Contents |
|---|---|
| `catalog/master_catalog.csv` | Master inventory — 1,775 datasets, 294 housing-relevant, with `queryable` status |
| `dictionaries/` | 42 dictionaries, incl. the address→parcel bridge |
| `data/raw/ohfa/` | OHFA affordability-exit export (manual browser download) |
| `docs/HOUSING_PRIORITY.md` | The shortlist: which datasets actually matter for housing policy |
| `docs/SOURCES.md` | Source register — every portal, how to access it, what's blocked |
| `docs/CAVEATS.md` | Data gotchas found while harvesting. **Read before analyzing.** |
| `docs/FRESHNESS.md` | Measured refresh cadence and staleness. Which sources are actually current. |
| `docs/PERMIT_LINKING.md` | How the City's live permit system and the County's copy relate, and how far they join. |
| `docs/PERMIT_LAYER.md` | Parcel-keyed permit layer for ingestion into parcel platforms. |
| `docs/CITY_OWNED_PROPERTY.md` | Reconciling City and County records of City-owned property. |
| `data/derived/` | Consumable outputs — parcel-keyed CSVs and GeoJSON. |
| `docs/mc_file_layouts/` | Official record-layout PDFs from the County (7 files) |
| `data/raw/` | Raw harvest output (JSON). Regenerate the rest from these. |
| `scripts/` | Harvesters + generators. All re-runnable. |

## Source systems found

1. **City of Dayton ArcGIS Online** (`DaytonOhio`, org `3dDB2Kk6kuA2gIGw`)
   — 1,271 public items, of which **374 are data services**. Fully open REST API.
2. **City of Dayton on-premise ArcGIS Server** (`maps.daytonohio.gov`)
   — **352 services across 35 folders**. A separate, larger catalog than the AGOL org,
   not surfaced by any Hub site. This is where code enforcement and operational data live.
3. **Montgomery County Auditor/Treasurer bulk downloads**
   — 9 datasets, **3,856 archived files**, some back to 2001. Plain HTTP, no auth.
4. **Montgomery County Auditor ArcGIS Server** (`gis.mcohio.org`)
   — 12 map/feature services incl. parcels, voter geography, and a geocoder.
5. **Montgomery County Board of Elections** — precinct shapefiles + interactive extracts.
6. **MVRPC** (`3TIUdMHOqnLBrZEH`) — 3,422 items / 1,011 data services, 106 housing-relevant.
   Regional, not city-published, but holds the affordability and cost-burden data.

The catalog uses the subcommittee's per-dataset schema (name · source/owner · theme ·
geography · granularity · access · cadence · formats · key fields · priority ·
current/desired use state · notes). **`priority`, `current_use_state`, and
`desired_use_state` are deliberately left blank** — those are the team's judgment calls,
not something to infer.

## Findings worth flagging up front

- **The County Taxroll answers the tenure question.** 254,693 parcels with `OWNOCC`
  owner-occupancy (Y 135,858 / N 118,834), `RENTALREG` rental registration (Y 17,454),
  `FRCLSR` foreclosure dates (1,072), delinquency (13,577), and a **census tract on every
  row**. Downloaded and verified in full. This was previously assumed to need a records
  request — it doesn't.
- **Every major housing dataset is now joinable at parcel level.** City and County parcel
  IDs already match (96.3% direct join), and code enforcement — which carries no parcel ID —
  now bridges through `ADDRKEY` at **99.97%** (12,875 of 12,879 incidents). Validated: the
  code-complaint rate climbs monotonically with condition grade, 2.5% on vacant lots to
  53% on dilapidated. See
  [`dictionaries/address-parcel-bridge.md`](dictionaries/address-parcel-bridge.md).
- **Subsidized-housing roll-off is federal, not local.** Neither the City nor County
  publishes an income-restricted inventory. HUD does: **120 LIHTC properties (8,412 LI
  units)** and **83 project-based Section 8 properties (5,586 assisted units)**, both open
  REST layers. **23 Section 8 contracts covering 812 units expire by 2030.** LIHTC has no
  expiration field — those dates must be derived. See
  [`dictionaries/subsidized-housing-rolloff.md`](dictionaries/subsidized-housing-rolloff.md).
- **CAMA closes the permits gap.** The County's monthly CAMA extract is a 35-table,
  2.3 GB relational dump — not just "property characteristics." It contains **251,570
  parcel-linked building permits (1960–2026)**, dwelling **condition ratings** on 189,389
  homes, **living-unit counts**, and **44,771 apartment units with rents**. Building
  permits were a priority theme listed as having no source; they've been public all along.
- **Housing Condition Survey 2025** grades **88,922 parcels** on a 0–5 condition scale
  and carries the 2023 grade in the same row — parcel-level condition *change* is
  already computable today.
- **Code enforcement is available** at `maps.daytonohio.gov` — 12,879 housing
  complaints for 2026 YTD, with status and outcome. It isn't advertised anywhere public.
- **The County has a 15-year monthly archive** of sales, tax roll, delinquency, and full
  CAMA property characteristics, with official record layouts. This is the deepest
  longitudinal housing data available to the committee, and it's just sitting there.

## Reproducing the harvest

```bash
python3 scripts/harvest_arcgis_org.py 3dDB2Kk6kuA2gIGw data/raw/arcgis_cityofdayton.json
python3 scripts/harvest_arcgis_server.py https://gis.mcohio.org/server/rest/services data/raw/arcgis_mcohio_server.json
python3 scripts/extract_fields.py data/raw/arcgis_cityofdayton.json data/raw/fields_dayton_housing.json --filter "housing|nuisance|vacant|parcel|..."
python3 scripts/parse_mc_treasurer.py data/raw/mc_fdpopup data/raw/mc_treasurer_manifest.json
python3 scripts/build_dictionaries.py data/raw/fields_dayton_housing.json dictionaries
python3 scripts/build_catalog.py

# County CAMA extract (fixed-width, 35 tables)
pdftotext -layout docs/mc_file_layouts/Cama_Data_Layout.pdf layout.txt
python3 scripts/cama.py spec layout.txt cama_spec.json
python3 scripts/cama.py freq cama_spec.json PERMIT PERMIT.DAT WHY FLAG

# Federal subsidized-housing layers
python3 scripts/harvest_lihtc.py data/raw/lihtc_montgomery_oh.json Montgomery OH
python3 scripts/harvest_hud_assisted.py data/raw/hud_assisted_montgomery_oh.json Montgomery 39

# Address -> parcel bridge for code enforcement
python3 scripts/build_address_bridge.py data/raw/address_bridge.json
python3 scripts/harvest_accela.py       data/raw/accela_incidents.json
python3 scripts/match_accela_parcels.py data/raw/accela_incidents.json \
        data/raw/address_bridge.json    data/raw/accela_parcel_matched.json
```

Everything is stdlib Python 3 — no dependencies to install.

## Status / next steps

- [x] Sweep City of Dayton ArcGIS Online org
- [x] Sweep City of Dayton on-premise ArcGIS Server
- [x] Sweep Montgomery County Auditor/Treasurer bulk files
- [x] Sweep Montgomery County Auditor GIS server
- [x] Locate Board of Elections data products
- [x] Data dictionaries for housing-relevant Dayton AGOL layers (35)
- [x] Verify MVRPC Montgomery County rollup against the live layer (reproduces exactly)
- [x] Full download + profile of the County Taxroll (254,693 rows)
- [x] Full download + parse of the County CAMA extract (35 tables; parser in `scripts/cama.py`)
- [ ] Data dictionaries for the on-prem server layers (352 services, not yet field-extracted)
- [ ] Transcribe remaining County layout PDFs (Taxroll and CAMA done; sales, delinquent, streetlights, refunds, neighborhood codes outstanding)
- [x] Parcel ID joins — measured, not assumed. City↔County joins directly at 96.3%; no
      crosswalk needed. Code enforcement bridged via `ADDRKEY` at 99.97%.
- [x] Probe every city service for real Query capability — 256 of 374 readable; 118 are
      form endpoints, empty, dead, or token-gated. Catalog now carries `queryable`.
- [ ] Ask City GIS why `2026_Spring_Ortho` and `J_McGee` are listed publicly but require a
      token — likely a sharing misconfiguration
- [x] Accela permits located via Accela Citizen Access (49 record types) — route from
      Code for Dayton's demolition_checker
- [ ] Build a general ACA harvester across all 49 record types (demolition_checker covers
      the 2 wrecking types; the postback mechanics generalise)
- [ ] Ask City GIS about code enforcement 2023–2025 — the two public services leave a
      three-year hole
- [ ] Ask City GIS about full-history code enforcement (public endpoint is 2026 YTD only)
- [x] Sweep MVRPC org; verify `HS_BlockGroups` and the Housing Dashboard layer
- [ ] Dedicated pass on MVRPC's 106 housing-relevant services (only 2 profiled so far)
- [x] LIHTC/HUD subsidized inventory + affordability roll-off — harvested from HUD;
      OHFA and NHPD identified as the authoritative follow-ups
- [x] **OHFA** "Projects Exiting LIHTC Affordability" — obtained via manual browser
      download. 104 Montgomery projects; validates the derived dates at 91% within ±1 year
      and catches re-syndications the derivation misses entirely.
- [ ] OHFA "Map of Multifamily Rental Properties" dashboard — not yet pulled
- [ ] **NHPD** (free registration) — for cross-program deduplication, Section 8 renewal
      status, and Section 202/811/USDA 515/HOME/HTF units. Note its LIHTC end dates use
      the same PIS+30 derivation already computed here, so it will not validate those.
- [ ] Greater Dayton Premier Management (public housing authority) — biggest known gap
- [ ] USPS vacancy data; Land Bank public program data
- [ ] Dayton Metro Library, DataOhio, Census/ACS as secondary sources
- [ ] Decide refresh cadence and whether to snapshot County monthly files locally

## A note on scope

This sweep covers what these agencies *publish*. Some things a housing committee wants
are **not** in any open portal — evictions (Municipal Court), subsidized/LIHTC inventory
with roll-off dates, and utility shutoffs. Those need direct requests.

**Rental registration is *not* one of them.** It's a field (`RENTALREG`) in the County's
public Taxroll bulk file — 17,454 registered parcels as of 2026-07-31 — alongside
`OWNOCC` owner-occupancy and `FRCLSR` foreclosure dates. See
[`dictionaries/mc-taxroll.md`](dictionaries/mc-taxroll.md). `docs/SOURCES.md` tracks
what's ruled in and out.
