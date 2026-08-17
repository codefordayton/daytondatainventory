# Data Caveats

Things that will bite you. Found while harvesting on 2026-08-01.

---

## County sales files

**`PRICE` is frequently `000000000.00`.** In the July 2026 monthly file, many records
carry a zero price with `SALEVALIDITY = "NOT VALIDATED"`. These are real transfers
(quitclaims, family transfers, trust transfers, sheriff's deeds) but they are *not*
arm's-length sales. **Filter on `SALEVALIDITY` before computing any price statistic**,
or your median sale price will be badly wrong.

**The layout PDF field names don't match the actual CSV headers.** The official
`sales file layout.pdf` documents `TAXABLELAND`, `TAXABLEBLDG`, `TAXABLETOTAL`; the
delivered CSV uses `TAXLAND`, `TAXBLDG`, `TAXTOTAL`. Same for `SALEDTE` (PDF: `SALEDT`).
Trust the CSV header, use the PDF for meaning.

**`TAXABLE*` vs `ASMT*` is counterintuitive.** In Ohio, assessed value is normally 35%
of market. Here it's inverted from what the names suggest: `TAXLAND` ≈ 35% of `ASMTLAND`.
Verified on a sample row: `TAXLAND` 24,370 / `ASMTLAND` 69,620 = 0.35. So **`ASMT*` is
effectively the 100% market value** and `TAX*` is the 35% taxable figure.

**Dates are `DD-MON-YY`** (`22-JUL-26`) — Oracle-style, not ISO. Parse explicitly.

---

## Housing Condition Survey

**13,544 parcels have a null `GRADE`** in the 2025 survey and 14,593 have null `STATUS`.
These are not "sound" — they're **not surveyed**. Treating null as zero or as a category
will distort every neighborhood rollup. Always report a surveyed-denominator.

**`GRADE` = 0 means vacant lot, not "worst condition."** The scale is not monotonic in
severity: 0 = vacant lot, then 1 (sound) → 5 (dilapidated). Sorting by grade puts
vacant lots at the "good" end.

**Row counts differ between 2023 (66,033) and 2025 (88,922).** The 2025 edition covers
more parcels, so year-over-year comparison must be done on the **intersection**, not on
aggregate totals. `HCS_DIFF` / `HCS_DIFF_AVG` are precomputed for exactly this reason —
prefer them over recomputing, but confirm how nulls were handled.

**Duplicated/renamed columns.** The 2025 table carries `GlobalID`, `GlobalID_1`,
`GlobalID_1_1`, `GlobalID_12`, `GlobalID_12_13`, `OBJECTID_1`, `OBJECTID_1_1`,
`TAXPINNO_1` — artifacts of repeated spatial joins. Also both `NEIGHBORHOOD` and `NHOOD`.
Confirm which neighborhood field is authoritative before grouping.

**`ACRES`, `APPRLAND`, `APPRBLDG` are stored as String**, not numeric. Cast before math.

---

## Accela code enforcement

**The `_UPDATE` service works; the base service does not.** `/Accela_UPDATES/
AccelaIncidents_UPDATE/` queries fine. `/Accela/AccelaIncidents/` returns **HTTP 503
"Wait timeout for the request exceeded"** on query, though its metadata reads fine.

**Coverage is 2026 YTD only** (2026-01-02 → 2026-06-30) in the working service. If you
need multi-year enforcement history you'll have to ask the city — don't assume the
public endpoint is the whole record.

**All 12,879 records are `COMPLAINT_TYPE = HOUSING`.** Either the service is
pre-filtered to housing, or other complaint types live elsewhere. Worth confirming;
it changes whether you can compare housing to other nuisance categories.

**No parcel ID.** Joins must go through address (`ADDRESS`, `ADDRKEY`, or the
`STR_NO`/`STR_DIR`/`STR_NAME`/`STR_SUFFIX` components). Address matching in Dayton is
non-trivial — use `Dayton Used Address` (163,184 records) as the reference set.

---

## Access and infrastructure

**Some hosts 403 scripted requests.** The BOE shapefile and Ohio SOS voter portal both
reject default `curl`. The BOE download works with a normal browser `User-Agent`; the
**Ohio SOS voter portal blocks it regardless** and needs a real browser session.

**A dead link on the BOE site:** `http://www.mcauditor.org/downloads/gis_download_geodb.cfm`
(linked from Forms and Information) redirects to mcohio.org and **404s**. The live
county GIS is `https://gis.mcohio.org/server/rest/services`.

**Search engines will send you to the wrong Montgomery County.** Queries for
"Montgomery County GIS open data" surface `montcopa` (Pennsylvania) and `mcgov`
(Maryland) portals above the Ohio one. Ohio is **`mcohio.org`**. Related: sites like
`montgomerycountyauditors.org`, `ohioauditors.org`, and `countyauditors.org` are **SEO
scrapers, not government sites** — don't cite them.

**One dataset in the Dayton org is not Dayton data:**
`EnvironmentalEquityInAlleghenyCounty_BDA_WFL1` (Allegheny County, PA) — presumably a
copied template item. A reminder that org membership alone doesn't make something local.

**County listing pages are legacy ColdFusion** with unquoted, backslash-separated
`href` attributes and `target` before `href`. Naive HTML parsing silently drops rows —
including the newest file in every dataset. `scripts/parse_mc_treasurer.py` handles this;
if you write your own parser, verify against the on-screen row count.

---

## MVRPC / regional layers

**`HS_BlockGroups` is at layer index 1, not 0.** Hitting `/FeatureServer/0` will not give
you the housing indicators. Verified: layer 1 = 793 features, 744 fields.

**744 fields is not a usable table as-is.** Expect to build a curated field subset before
handing this to anyone. The ACS derivation also means margins of error exist upstream but
are not necessarily carried in the layer — check before publishing block-group estimates.

**MVRPC 2025 Regional Housing Study ≠ the Bowen Study.** These are two separate,
duplicative efforts (Bowen was commissioned by the Market Analysis subcommittee). Don't
conflate them in the inventory.

## Housing Dashboard export

**`HousingRequest_ExportFeature1` field names are mangled.** The geocoding export
truncated them into `USER_Unit_` (UnitType), `USER_Unit1` (UnitTenure), `USER__Unit`
(NumberOfUnits), `USER_Fundi` (FundingSources). Three near-identical names differing only
by underscores — easy to mix up. **Use the field aliases.**

**It rejects `groupByFieldsForStatistics`** — statistics queries return an empty feature
set with no error. Pull rows with `outFields` and aggregate client-side. (This is why the
tallies in `HOUSING_PRIORITY.md` were computed from a full 376-row pull.)

**It's a one-time export, not a live layer.** Counts are a snapshot of unknown vintage.

## Scope boundary

**Public sources only.** Everything here comes from the agencies' own public endpoints.
Where a dataset is only available through a licensed third-party platform, record it as
out of scope with a note on who to approach, rather than extracting it.

**Coordinate outreach before contacting data holders.** Several agencies appear
repeatedly across these sources; uncoordinated requests from different people are worse
than one considered ask.

---

## County Taxroll (added after full download, 2026-08-01)

**Headers are space-padded.** The delivered CSV pads header names with trailing spaces, so
`hdr.index("OWNOCC")` raises and a naive `"CLS" in hdr` check returns False. Fields look
absent when they aren't. **`.strip()` every header before indexing.**

**`FRCLSR` is a date, not a boolean.** Values look like `10-JUN-26`; blank means no
foreclosure. 1,072 of 254,693 parcels carry one.

**`OWNOCC` ≠ `HMSDFLAG`.** Owner-occupancy credit (`OWNOCC` Y = 135,858) is broad; the
homestead exemption (`HMSDFLAG` Y = 33,065) is age/disability/income-restricted. Using
homestead as a general owner-occupancy proxy understates owner-occupancy by ~4x.

**`RENTALREG` measures registration, not rental status.** 17,454 registered parcels
against ~118,834 non-owner-occupied. The gap is a compliance finding, not a count of
rentals — don't present it as rental stock.

**Countywide, not Dayton.** 254,693 parcels covers all of Montgomery County. Filter on
`CITY/TOWNSHIP` before reporting anything as a Dayton figure.

**656 MB uncompressed.** Stream it; don't read it into memory whole.

**`CENSUS TRACT` is already on every row** (419 distinct) — join to ACS directly rather
than geocoding. This is the cheapest bridge between County parcel data and Census
demographics, and it means the parcel-ID crosswalk isn't a prerequisite for
tract-level work.

## Verification note

The Montgomery County rollup carried in `PRIOR_RESEARCH_CONTEXT.md` (252,061 units;
owner-occ 142,075 / renter-occ 85,987 / vacant 23,999; owner cost-burdened 18%, renter
42%) was **re-derived independently from `HS_BlockGroups` layer 1 filtered to
`County LIKE '%Montgomery%'` — 422 block groups — and reproduces exactly.** Those figures
are safe to cite.

Note these are **ACS-derived housing units (252,061)** and will not agree with the
**Taxroll parcel count (254,693)** — different universes (housing units vs. parcels,
survey estimate vs. administrative record). Don't reconcile them; cite the right one for
the question.

---

## County CAMA extract (added after full parse, 2026-08-01)

Three traps here are the kind that produce confident wrong answers rather than errors.

**1. `DWELL.DAT` records span three physical lines.** A 643-char data line, a wrapped
9-char date line, then a blank line. Line-by-line reading returns **568,167 rows when
there are 189,389 dwellings** — a 3x overcount — and manufactures 378,778 rows that look
like real records with every field blank. Nothing errors. `scripts/cama.py` stitches
records; if you roll your own, check that your row count is 189,389.

**2. The layout PDF is off by one byte from `GRADE` onward.** In `DWELDAT`, columns
starting at ≤ 92 (`HEAT`) align with the delivered file; from start 95 (`GRADE`) on,
everything sits one byte later than documented. Symptom: `CDU` reads as `0A`/`0F`/`0G`
instead of `AV`/`FR`/`GD`, and `GRADE` as `2C+` instead of `C+`. With the +1 shift, `CDU`
matches the documented code set for **99.9%** of records; without it, **0.0%**. Encoded as
`OFFSET_FIXES` in `scripts/cama.py`. Assume other tables may have similar drift — validate
against the lookup files before trusting a column.

**3. `COMAPT` rents are valuation rents, not market rents.** Median ≈ $500/month for a
2-bedroom, far below Dayton market. These are scheduled/economic rents used in the income
approach to assessment and may be stale. Useful for identifying multifamily inventory and
for relative comparison; **not** a basis for any affordability claim. Use ACS or HUD Fair
Market Rents for rent levels.

**Lesser gotchas:**
- Multiple `CARD` values per parcel in `DWELL` (1 for 188,367; 2–6 for the rest).
  Aggregate by `PARID`.
- `PERMIT` layout descriptions are wrong: `NUM` is labeled "Tax Year" and `PERMDT`
  "User ID of last maintenance". They are the permit number and permit date.
- One `PERMIT` record is dated 2027 — filter implausible dates.
- The small `.DAT` files (`GRADE`, `EXTWALL`, `HEAT`, `BSMT`, `ATTIC`, `SHFACT`, `CICDU`,
  `NBHD`) are **code lookup tables shipped with the data**. Decode from these rather than
  inferring; that is how the `CDU` offset above was caught.

---

## Subsidized housing / affordability roll-off (added 2026-08-01)

**HUD's LIHTC database has no expiration field.** It carries `YR_PIS` and `YR_ALLOC` only.
Every LIHTC roll-off year in this repo is **derived** (placed-in-service + 15 compliance +
15 extended use = 30). That matches NHPD's published assumption, but actual extended-use
terms are set by the recorded agreement, are often longer, and can be shortened via the
Qualified Contract process. **Never cite a derived date for a named property** without
confirming against OHFA or NHPD.

**Do not add LIHTC units to Section 8 units.** 15 Montgomery County properties appear in
both HUD datasets under matching names, and the real overlap is probably higher since that
was a name match. Summing the two produces a materially inflated subsidized-unit count —
the single likeliest error with these sources.

**Contract expiration is not unit loss.** Most project-based Section 8 contracts are
renewed, frequently on short terms, so the same property reappears every few years. The
expiration list is an engagement calendar, not a loss forecast. NHPD's
`S8_1_RenewalStatus` carries actual renewal status.

**"Already past" ≠ no longer affordable.** 42 LIHTC properties (2,175 LI units) are past
their derived 30-year minimum. Many are re-syndicated or still restricted. The figure means
"needs checking," not "lost."

**`YR_PIS = '8888'`** is a placeholder in the HUD LIHTC data (one Montgomery County
record). Validate year fields before arithmetic.

**OHFA's Tableau dashboards are not scriptable.** Appending `.csv` to a Tableau view URL
returns only the first sheet — for these dashboards a filter control (21 bytes,
`Appalachia / Yes / No`), which looks like a successful export. The `.pdf` export renders
charts, not tables. Use the dashboard's own download control in a browser.

**`CURCNTY='39113'` returns zero** on the HUD layers even though it looks like the right
county FIPS. Filter on `STATE2KX='39' AND CURCNTY_NM LIKE '%Montgomery%'` instead.

**`OCCUPANCY_RATE` does not exist** on the HUD Multifamily layer despite being a natural
guess; the field is `PCT_OCCUPIED`. An invalid field name fails the whole query with
`'outFields' parameter is invalid` rather than skipping the bad field.

**NHPD does not improve on the derived LIHTC dates.** Its documentation states LIHTC
subsidies "are automatically assumed to have a subsidy end date 30 years past the year the
tax credit was placed in service" — the same derivation used in this repo. Pulling NHPD
reproduces those numbers rather than checking them. **OHFA holds the recorded extended-use
agreements and is the only source that can confirm an actual date.** NHPD's distinct value
is cross-program deduplication, `S8_1_RenewalStatus`, and the programs HUD's two layers
omit (Section 202/811, USDA 515, HOME, HTF).

## OHFA export (obtained 2026-08-02)

**The file is UTF-16, TAB-delimited, despite the `.csv` extension.** Opening it as UTF-8
comma-separated gives garbage or a single mangled column. Use
`open(path, encoding='utf-16')` with `delimiter='\t'`.

**OHFA's column is "Est. Program Exit."** The allocating agency is publishing an estimate
too. It is the best available source — it reflects re-syndications that HUD's
placed-in-service year cannot — but it is still not the recorded legal term. For a binding
date on a specific property, the restrictive covenant is the only authority.

**OHFA lists only currently-active projects.** 39 of the 42 properties flagged "already
past" from HUD data simply do not appear. Absence from OHFA is *evidence of* exit, not
proof — a property could be out of OHFA's scope for other reasons.

**Do not strip phase numerals when matching project names.** "Dayton View Commons II" is a
different project from "Dayton View Commons," with different dates. An earlier match that
stripped `II`/`III` produced false pairings and a misleading disagreement rate; with
numerals preserved, agreement rose to 91% within ±1 year.

**Universe mismatch with HUD.** OHFA Montgomery County = 104 projects / 8,861 units;
HUD LIHTC = 120 properties / 8,412 LI units. Different scopes (active OHFA-funded vs. all
LIHTC ever placed in service) and different unit definitions (total vs. low-income). Do
not treat either count as a correction of the other.

**Derived dates fail on re-syndication.** PIS + 30 is 91% accurate in aggregate but can be
half a century wrong on individual properties that received a new allocation (Mad River
Manor +52 years, Jaycee Towers +47). This is the concrete reason not to name properties
off derived dates.

## Parcel ID joins (measured 2026-08-02)

**City and County parcel IDs are already compatible.** City HCS `PARCELID`
(`R72 08702 0039`) matches County `PARID`/`PARCELID` format exactly. Measured join rate
against the County taxroll: **96.3%** (15,525 of 16,116 distinct IDs from a 20,000-row
HCS sample). No translation layer is required.

**The real loss is blank IDs, not mismatched ones.** ~17% of sampled HCS rows carry no
`PARCELID`. `KEY_PARCELID` and `K_PID` — which look like alternates — were blank in every
row inspected. Check completeness before assuming a field is populated.

**HCS has multiple rows per parcel** (one per structure; see `STRUCTURE`/`STRUCTURES`).
Aggregate by `PARCELID` before joining County attributes or you will duplicate them.

**Accela code enforcement is the only genuine crosswalk problem** — it carries no parcel
ID, only address components. That is address matching, not ID translation, and needs
`Dayton Used Address` or the County `MC_ProLocator` geocoder.

## Address → parcel bridge (built 2026-08-02)

**ArcGIS `resultRecordCount` is silently capped by the server.** The Dayton address service
caps at 1,000 per page. Asking for 2,000 returns 1,000, and the common termination test
`len(features) < requested_page_size` then reads a *full* page as the last one. This
produced a bridge containing 1,000 of 163,184 records that reported success and looked
plausible. **Terminate on `exceededTransferLimit`**, never on page length. Every harvester
in `scripts/` now does this — check any older code you reuse.

**`KEY_PARCELID` / `K_PID` are decoys.** They look like parcel identifiers and are blank in
every HCS row inspected. `TAXPINNO` is the populated parcel id in the address layer;
`PARCELID` in the HCS.

**Don't force-match the residue.** 4 of 12,879 incidents have `ADDRKEY` values absent from
the address layer (new addresses). They are left null. A wrong parcel silently corrupts
downstream joins in a way a null does not.

**6% of matched parcels are absent from the County taxroll** (409 of 6,866) — plausibly
exempt, demolished, or recently split. Expect a small drop when chaining
code enforcement → parcel → taxroll.

**Complaint rates from this data are six-month rates**, since the Accela service is 2026
YTD only. Do not annualize without confirming coverage.

**Multi-unit buildings share one parcel**, so per-parcel complaint counts aggregate across
units — right for owner-level analysis, wrong for per-unit rates.

## Not every published service holds data (probed 2026-08-02)

Of the 374 Feature/Map services in the City of Dayton ArcGIS Online org,
**256 are readable and 118 are not.** Being listed publicly does not mean being queryable.
`scripts/probe_capabilities.py` records declared capabilities and whether a count query
actually succeeds; the catalog carries `queryable` and `capabilities` columns.

| Reason | Count |
|---|---|
| Survey123 `_form` submission endpoint (`Create,Editing`, no Query) | 59 |
| Query declared but zero layers/tables | 40 |
| Dead or erroring (404, unreachable, "Error invoking service") | 13 |
| Tile/image only, no features | 4 |
| **Token required despite public listing** | **2** |

**`_form` vs `_results`.** Survey123 publishes a pair: `_form` is the write-only
submission endpoint, `_results` is the readable data. Opening a `_form` service in a map
viewer fails with *"layer view requires a layer with query capability"* — working as
designed, not a broken link. Catalogue the `_results` half.

**Token-required services are listed as public.** All 374 items report
`access: public` at the *item* level — the search API only returns public items. The token
requirement lives on the underlying *service*, so it only surfaces when the endpoint is
called. Two services are affected:

- `2026_Spring_Ortho` — `https://maps.daytonohio.gov/image/rest/services/Ortho/2026_Spring_Ortho/MapServer`
- `J_McGee` — `https://maps.daytonohio.gov/server/rest/services/PublicWorks/J_McGee/MapServer`

Neither is housing-relevant, but the mismatch is worth reporting to City GIS: a publicly
listed, publicly linkable item whose data requires authentication is more likely a sharing
misconfiguration than an intentional state.

**Housing-relevant count corrected 303 → 294** once write-only endpoints stopped being
counted as datasets.

## Accela — three separate surfaces, easily confused

Dayton runs Accela for both permitting and code enforcement, but they surface differently
and only one is in the GIS catalogue.

| Surface | What it holds | Access |
|---|---|---|
| `Accela_UPDATES/AccelaIncidents_UPDATE` | 12,879 housing complaints, **2026-01-02 → 2026-06-30**, 90 fields | GIS REST |
| `Accela/AccelaIncidents` | 8,805 housing complaints, **2022-07-24 → 2023-01-19**, 48 fields | GIS REST |
| **Accela Citizen Access** | **49 permit/licence record types incl. demolition** | web portal, no API |

**The older GIS service is not a superset — it is a different window.** An earlier note
here speculated it held the full history; it does not. The two windows are disjoint and
there is **no public code enforcement data for 2023–2025**. Their schemas also differ (48
vs 90 fields), so the two cannot be naively stacked.

**Its 503 was transient.** `Accela/AccelaIncidents` refused a count query under load and
answered normally later. Retry before recording a service as blocked.

**"The city publishes no permit data" was wrong.** Permits are absent from the GIS layers
but live in Accela Citizen Access at
`https://aca-prod.accela.com/DAYTON/Cap/CapHome.aspx?module=Building&TabName=Building`,
searchable by record type and date. Route established by Code for Dayton's
[demolition_checker](https://github.com/codefordayton/demolition_checker).

**ACA is a WebForms UI, not an API.** Queries are `__VIEWSTATE` postbacks, results are
paginated by further postbacks, and a single result redirects to a detail page instead of
the results grid. Any scraper must handle both shapes and should assert that the page
matches an expected form so a layout change fails loudly rather than silently returning
zero records.

**ACA and CAMA `PERMIT.DAT` are different views of permits** — city system of record vs
county parcel-linked copy with valuation. Do not sum them.

## Freshness is mostly unknowable on ArcGIS

**98% of published layers report no last-edit date.** Of 1,671 layers carrying records,
only 37 expose `editingInfo.lastEditDate`. For the rest there is no machine-readable way
to tell whether the data is current — a consumer cannot distinguish a live layer from an
abandoned copy without asking someone.

**Item `modified` is not a data-freshness signal.** It moves when the item record changes,
not when the data does. `Dayton Used Address` has an item date of 2018 yet matched 99.97%
of 2026 code enforcement addresses — the data is maintained, the metadata is not. Do not
treat a stale item date as evidence the data is stale, or a fresh one as evidence it isn't.

**Some served layers are years old.** `SLSA_2014_Parcels` (88,512 rows) last changed in
2017; `City_of_Dayton_Owned_Parcel` in 2021. They are still discoverable and still
returned by queries. Check age before using anything as current.

Full detail, including measured County cadence, is in `docs/FRESHNESS.md`.

## A 403 on maps.daytonohio.gov is not a lockout

Opening `https://maps.daytonohio.gov/gisservices/rest/services` in a browser returns
**403 — "The administrator has disabled the Services Directory."** That is Esri's
human-browsable HTML view being switched off as a hardening setting. It is long-standing
configuration, not a block, and not a reaction to anyone's traffic.

**The JSON API underneath is fully open.** Append `?f=json` to any URL on that host:

```
/rest/services            -> 403   (HTML directory, disabled)
/rest/services?f=json     -> 200   (35 folders, 18 root services)
/…/MapServer/0/query?where=1=1&returnCountOnly=true&f=json   -> works
```

Every harvester here appends `f=json`, which is why none of them ever saw the 403.

The side effect is worth naming: with the directory disabled and no portal linking to it,
this server is effectively undiscoverable by browsing — 352 services and ~59.5 million
records that are entirely public and that a person clicking around would conclude are not
there. `docs/SOURCES.md` lists the folder structure and `dictionaries/` covers the layers
that carry data.

## City-owned property: two records that disagree

**No single source encompasses City-owned property.** The City's GIS layer holds 1,912
parcels and was last edited 2021-07-30; the County tax roll attributes 2,781 to the City
and is published daily. **They agree on 1,688** — 1,093 appear only in the County record,
224 only in the City's. Any count of "City-owned properties" must say which record it came
from.

**Owner-name matching pulls in the school district.** A naive match on owner names
containing *city* and *dayton* returns 2,904 parcels, of which **107 belong to the Dayton
City School District** — a separate legal body — plus churches, LLCs and County parcels.
Tightening the match naively also fails: the roll writes the City as `CITY OF DAYTON`,
`THE CITY OF DAYTON`, `DAYTON OH CITY OF` and `DAYTON CITY OH OF`, so an anchored filter
drops real parcels. See `scripts/build_city_owned_inventory.py` for the curated matcher.

**Building value alone does not separate function from development potential.** Only 263
of 2,781 City parcels carry a building, so filtering on it removes City Hall and the fire
stations but leaves every park, median and street remnant. The County's land use code is
the usable discriminator: LUC 640 is operational municipal property (2,108 parcels), while
LUC 300/400/500 is vacant land (439).

Full analysis in `docs/CITY_OWNED_PROPERTY.md`.
