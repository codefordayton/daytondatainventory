# Accela Citizen Access — Dayton permits & planning cases

> The City's live permitting system, queryable through its public portal. This is the
> source I initially, wrongly, recorded as "not published" — the GIS layers expose only
> code enforcement, but the permit records are reachable through Accela Citizen Access.
>
> Route established by Code for Dayton's
> [demolition_checker](https://github.com/codefordayton/demolition_checker), built for
> Preservation Dayton to watch wrecking permits.

Verified live 2026-08-02. Type catalog: `data/raw/accela_aca_permit_types.json`.

---

## Endpoint

```
https://aca-prod.accela.com/DAYTON/Cap/CapHome.aspx?module=Building&TabName=Building
```

Not an API — an **ASP.NET WebForms search page**. A query is a `POST` carrying
`__VIEWSTATE`, `__EVENTTARGET`, and the search fields, with results paginated by further
postbacks. `demolition_checker` implements this in Scrapy; the postback-following helpers
there are the reusable part.

Key form fields:

| Field | Purpose |
|---|---|
| `ctl00$PlaceHolderMain$generalSearchForm$ddlGSPermitType` | record type (see below) |
| `ctl00$PlaceHolderMain$generalSearchForm$txtGSStartDate` | start date, `MM/DD/YYYY` |
| `ctl00$PlaceHolderMain$btnNewSearch` | the `__EVENTTARGET` that runs the search |

## Modules

| Module | Searchable record types |
|---|---|
| **Building** | **49** — permits, licences, appeals |
| **Planning** | 1 — `Planning/Planning Case/NA/NA` |
| Enforcement · Licenses · Fire · Public Works | page loads, no record-type dropdown |

Enforcement returning no dropdown is consistent with code enforcement being exposed
through the GIS layer instead (`AccelaIncidents`), not through this portal.

## The 49 Building record types

Values are hierarchical: `module/type/subtype/category`.

**Residential permits** — `Building/{Building, Electrical, Plumbing, Mechanical, Gas,
Sewer, Water, Fire Alarm, Fire Sprinkler, Footer Foundation Slab, Flood Plain, RVO,
Zoning Only, Wrecking}/Residential/NA`

**Commercial permits** — the same list plus `Tent Permit`, all under `/Commercial/NA`

**Waivers** — `Building/Waivers/{Residential,Commercial}/TRP`

**Non-typed** — `Building/Sign/NA/NA`, `Building/Miscellaneous/NA/NA`,
`Building/REV/NA/NA` (permit revision), `Building/BBA/NA/NA` (Board of Appeal),
`Building/Site Plan Development/NA/NA`, `Building/Special Service Inspection/NA/NA`

**Trade licences & registrations** — `Building/Licenses/{Plumbing, Journeyman Plumbers,
Apprentice Plumbers, Electrical Contractor, Pipe-Laying, HVAC}/{License, Application}`

The two the demolition checker uses:
`Building/Wrecking/Residential/NA` and `Building/Wrecking/Commercial/NA`.

## Fields returned

Per `src/schema.py` in demolition_checker:

| Field | Example / note |
|---|---|
| `record_number` | `WRK2024R-00138` — type prefix + year + R/C + sequence |
| `record_details_link` | URL to the `CapDetail` page (more fields available there) |
| `record_type` | the searched type |
| `project_name` | often blank |
| `address` | work location |
| `expiration_date` | present in the grid; no populated example found yet |
| `short_notes` | free text |

A single-result search **redirects to `CapDetail` instead of the results grid**, so a
scraper must handle both page shapes. demolition_checker does this in
`determine_search_results_page`.

## Why this matters for housing policy

**Demolitions.** Wrecking permits are the city's own record of demolition, filed as they
happen. Compare with County CAMA `PERMIT.DAT` (9,548 demolition permits, 1960–2026) —
that is the assessor's downstream copy, so ACA should be more current.

**Reinvestment.** Residential building, electrical, plumbing, mechanical, and RVO permits
per parcel are the clearest available signal of private investment in the housing stock —
the counterpart to the condition survey's decline signal.

**Trade capacity.** The licence registrations are a rough proxy for contractor supply,
which bears on whether rehab demand can actually be met locally.

## Caveats

**Scraping a WebForms UI is brittle by nature.** `__VIEWSTATE` is session-bound and the
control IDs are generated. demolition_checker guards this well — it asserts that the page
either shows records or shows the no-results message, and raises if neither holds, so a
layout change fails loudly instead of silently returning nothing. Keep that assertion in
anything derived from it.

**Be a considerate client.** This is a live permitting system serving contractors and
residents. Query by date window, cache aggressively, and don't parallelise.

**Not a bulk endpoint.** There is no "download all permits" — records come back paginated
per type and date range. A full backfill means iterating 49 types across a date range.

**ACA vs CAMA are different views.** ACA is the city's live system of record. CAMA
`PERMIT.DAT` is the county's parcel-linked copy with a `WHY` category and declared
valuation. CAMA has valuation and parcel IDs; ACA has currency and the city's own type
taxonomy. Neither supersedes the other, and they should not be summed.

**No parcel ID.** ACA returns an address, so joining to parcels needs the same address
bridge used for code enforcement — see
[`address-parcel-bridge.md`](address-parcel-bridge.md).
