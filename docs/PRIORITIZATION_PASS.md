# Prioritization Pass — 261 Housing-Relevant Datasets
*Combines the Tier framework from `HOUSING_PRIORITY.md` with data-quality signals
(records, field count, last-updated) pulled from the per-dataset dictionaries.
Run 2026-08-10.*

## Method
- Records/fields/last-updated pulled from `dictionaries/*.md` where one exists
  (matched by name — 116 of 261 have real data this way); the 12 already-verified
  Tier-1 backbone datasets use the hard numbers from `HOUSING_PRIORITY.md` directly.
- Quality score = recent update (≥2024) + has records + has ≥5 fields + queryable.
- Priority bucket = theme (from the original crawl) × quality score, with the
  known backbone datasets pinned to Tier 1/2 regardless.

## Bucket counts
| Bucket | Count |
|---|---:|
| Tier 1/2 backbone (already known-good) | 12 |
| High-value theme, good data — promotion candidates | 101 |
| High-value theme, weak/missing data — flagged | 52 |
| High-value theme, **unprofiled** (no data pulled yet) | 20 |
| Medium-value / supporting themes | 36 |
| Lower-value / context | 40 |

## ⚠️ Finding #1 — before this goes anywhere near the subcommittee: prune noise first
The "promotion candidates" and "weak data" buckets are inflated by two effects
that need a human pass, not more automation:

**(a) Genuine near-duplicate publishing.** At least **19 parcel-flavored layers**
across City departments carry >50k records each, in at least 4 different
"generations" (273,627 / 88,668 / 88,512 / 86,939 / 86,799), spread across Fire,
PublicWorks (2 copies), Water, Environmental (2 copies), Basemaps, Base,
COD_Webpage, Engineering, and a project-specific SLSA extract. None is flagged
as canonical. **This is a real, reportable finding** — it's not that the data is
missing, it's that ~8 departments are each maintaining their own stale copy of
the same base layer. Worth naming to the City directly (dovetails with the ERP
conversation) rather than trying to rank "which duplicate is best."

**(b) Tagging false positives.** The original crawl's theme-tagging swept in
clearly non-housing items under `affordability/tenure` and `ownership/transfers`
via loose keyword matching — e.g. *GMR Bike Rental*, *Regional Bikeway in Miami
Valley*, *PLAN4Health Highway Shields*. These inflate the "weak data" bucket with
noise, not real gaps. **Recommend a manual prune pass before circulating a
"prioritized list" externally** — sharing an obviously-noisy list undercuts
credibility with partners (same instinct as Nicole's "what does this data really
mean" caution from the 8/5 meeting, applied to the catalog itself).

## Finding #2 — the real "point the city here" shortlist
Once the noise above is set aside, the genuinely **high-value + unprofiled**
items are a clean, small list that matches (and slightly extends) what
`README.md`'s own next-steps already flagged — reassuring, not a contradiction:

- Building permits & trade licenses (49 Accela record types — Dave's crawler already covers 2 of them)
- BuildingServicesHousingInspectionAreas
- Vacant Property Registration
- Public housing & HCV inventory (Greater Dayton Premier Management — biggest known gap)
- Local Homelessness Data (CoC)
- Residential Rental Property Registration roster
- Deeds, mortgages, liens / Conveyance form search
- Map of Multifamily Rental Properties (OHFA)
- Projects Exiting LIHTC Program Affordability Period (OHFA dashboard)
- National Housing Preservation Database (NHPD — needs free registration)

**Recommendation:** this list — not the raw 261 — is what's worth walking the
subcommittee through. It's small, concrete, and each item maps to a specific
next action (an outreach ask, a portal to profile, or a registration to complete).

## Backbone (Tier 1/2) — unchanged, already solid
No changes recommended to the 8 backbone + ~13 supporting datasets already named
in `HOUSING_PRIORITY.md` — this pass confirms rather than revises that list.

## Pruning pass results (8/10)
Full row-level output: **`catalog/pruned_dataset_list.csv`** (all 261, with a
`prune_status` + `prune_reason` column so every call is auditable/reversible).

| Status | Count | Meaning |
|---|---:|---|
| **Kept** | 157 | Confirmed relevant, no change |
| **Deduped** | 20 | Consolidated into a canonical entry (see below) |
| **Review** | 21 | Ambiguous — needs a human call, not auto-decided |
| **Removed** | 63 | High-confidence noise (see reasons below) |

**Deduplication:** ~16 near-identical department copies of the parcel base
layer were consolidated under the existing **`DaytonParcels`** (Tier 2)
entry — Fire, PublicWorks (×2), Water, Environmental (×2), Base, Basemaps,
COD_Webpage, Engineering, and an SLSA project extract all point at the same
underlying data. Separately, **9 township-level "Zoning" layers** (Bethel,
Concord, Monroe, Newberry, Newton, Springcreek, Staunton, Union, Washington
Twp) share an identical 970-record/29-field footprint with **"Regional Zoning,
2025"** — almost certainly the same regional dataset re-published per
township — consolidated under the regional entry.

**Removed (63) — three patterns, all high-confidence:**
1. **Wrong geography entirely** — e.g. `EnvironmentalEquityInAlleghenyCounty…`
   (that's Pittsburgh, PA, not Dayton).
2. **Mistagged infrastructure** — water/storm/lift-station "condition"
   assessments swept in on the keyword "condition," but they're about pipes,
   not housing.
3. **An orphaned bookmark set** — ~25 items suffixed `(Properties Saved)`
   from what looks like a Piqua-area "Built Environment Assessment" project
   (Piqua is a different city, in Miami Co., not Montgomery Co./Dayton) —
   these read like exported map bookmarks, not curated datasets.

**Review (21) — genuinely ambiguous, left for a human call, not deleted:**
Fire inspection/hydrant datasets (fire-safety-adjacent, unclear if in scope),
`County_Boundaries` (likely just a reference layer, mistagged), adjacent-county
property tables (Greene/Miami Co.), a few oddly-named layers (`MOTNAP`,
`MCDMerge`, `BMVSurveyMap2022`), property-recovery time series (could be
foreclosure-adjacent), and a handful of topically-relevant-but-orphaned
affordability layers (`CostBurdenedByTract`, `Low Income Low Access`,
`pesMedianIncome2`) where the *topic* matters but this particular instance
looks like a dead bookmark, not a live source.

**Known gap in this pass:** exact-name matching missed at least one variant
(`…StormOutfallSamplingVisualInspectionReferenceLayers`, a longer name than
guessed) — treat this pass as a strong first cut, not a final audit. Expect
another round. *(Fixed in the geo-check pass below, once the full name turned up.)*

## Geographic sanity check (8/10) — mostly clean
Triggered by the Allegheny County, PA find: that dataset was real, owned by an
actual City of Dayton GIS staff account (`barnold_Dayton_OH`), just off-topic
content someone published into the org's shared space — not a crawl error.
Checked all 178 kept/review items against their cached ArcGIS extent
(offline, from the original crawl JSON — no re-crawl needed):

- **1 new outlier found** — and it's a false positive: `…AccelaIncidents_UPDATE.aprx`
  had extent values in a projected coordinate system (State Plane, not lon/lat
  degrees), which tripped the naive check. It's a real, already-known Accela
  dataset — no action needed.
- **69 of 178 items have no cached extent** (mostly on-premise ArcGIS Server /
  County bulk-file sources, which don't carry item-level extent metadata the
  way ArcGIS Online items do) — not checked, would need a live per-service query.
- **Net: no second Allegheny-County-style item found** among what could be checked.

## Freshness + record-count pass (8/10) — "is this someone's scratchpad?"
First pass flagged 21 items as small (<100 records) and stale/undated. On
inspection, **most were false positives from one pattern**: Dayton has ~65-97
neighborhoods, so any *per-neighborhood* reference layer (boundaries, profiles,
population density) legitimately has ~65-97 rows — that's the correct size for
what it is, not a sign of neglect. Reclassified 14 of the 21 on that basis
(listed in the CSV as `false-positive (small-by-design or pipeline gap)`),
including `ARPA Focus Neighborhoods` (already documented elsewhere as "(6)" by
design) and the HUD Section-8 backbone dataset (small by nature — 83 real
properties — just missing a field-count in my own extraction, not a data problem).

**5 genuine candidates remain** — small, stale/undated, and not explained by a
known-small universe:

| Dataset | Records | Updated | Why it looks like scratch work |
|---|---:|---|---|
| `COD_Webpage/Zoning` | 4 | none | The real zoning layer elsewhere has ~970 records — 4 is suspiciously thin for the same claimed content |
| `COVID19/AddressSearch` | 7 | none | Reads like a leftover pandemic-era tool, not a maintained source |
| `Fire/2018_Completed_Inspections` | 6 | none | Name suggests a one-off pull, not an ongoing dataset |
| `Police/CrimeVictimDashboard` | 35 | none | Also questionable whether this belongs in "housing-relevant" at all |
| `Seibert Riverview Curtis Neighborhood Survey` | 66 | 2023-10-16 | Ambiguous — could be 66 real community-survey responses (legitimately small) rather than a broken extract; not confident either way |

**Recommendation:** these 5 are worth a quick human look before the list goes
out, but they're low-stakes either way — none were candidates for the
"point the city here" shortlist to begin with.
