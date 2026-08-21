# Developable sites layer

Undeveloped land and underutilized structures in Dayton, assembled against the 2026 Bowen
recommendation to *"create a detailed list of undeveloped land and underutilized structures
(e.g. vacant schools, churches, warehouses) that could support residential development or
adaptive reuse."*

Built by [`scripts/build_developable_sites.py`](../scripts/build_developable_sites.py).
Outputs in `data/derived/`. Built 2026-08-21.

**Audience: developers.** The question is *where could something be built* — not what is
already being built. The City's Housing Dashboard answers the latter and is a different
product for a different reader.

⚠️ **This is the universe to filter from, not a filtered list.** 11,907 parcels is a long
way from "a detailed list of developable sites." Nothing here has been checked for
easements, deed restrictions, environmental status, or whether a parcel recorded as vacant
is actually a drainage swale. Filtering criteria are a policy decision and have
deliberately not been applied.

---

## What's included

| Site type | Count | Basis |
|---|---:|---|
| `vacant_land` | 11,816 | County land use codes 300 / 400 / 500, any owner |
| `vacant_structure` | 91 | Church, school or warehouse **with a building**, recorded vacant by the Housing Condition Survey |
| **Total** | **11,907** | 5,986 with coordinates |

Vacant land by type: residential lots 9,827 · commercial 1,715 · industrial 274.

**The 91 vacant structures are the more actionable half.** They come from cross-referencing
the land uses Bowen names against HCS occupancy status, so they are confirmed vacant rather
than assumed: 60 vacant & secure, 19 vacant & boarded, 12 demolition. 595 parcels in those
same land uses were *excluded* because the survey records them occupied. Examples include
former Board of Education buildings on S Ludlow and a Land Bank warehouse on N Jefferson.

---

## Size — and why the first attempt was wrong

Most sites are small. Above a quarter acre the universe collapses:

| Size | Sites |
|---|---:|
| under ¼ acre | 10,975 |
| ¼ – ½ acre | 333 |
| ½ – 1 acre | 181 |
| 1 – 2 acres | 110 |
| 2 – 5 acres | 107 |
| **5+ acres** | **76** |
| size unknown | 125 |

**A ¼-acre floor gives 807 sites. A 1-acre floor gives 293.**

⚠️ **The tax roll's `ACRES` field is unusable on its own.** It is blank or zero on **89%**
of Dayton parcels — meaning *not recorded*, not *small*. A first pass using it produced a
plausible-looking distribution built almost entirely on missing data.

Acreage here is derived from **parcel geometry** (`DaytonParcels.Shape__Area`), calibrated
against the 271 parcels that do carry a recorded acreage. Derived values match the recorded
ones to three decimal places. Conversion factor: `acres = Shape__Area × 0.000146`.

Three fields ship so the provenance stays visible:

- `acres` — the tax roll value, mostly zero
- `acres_geometry` — derived from parcel geometry
- `acres_best` — geometry where available, tax roll otherwise

---

## Fields

| Group | Fields |
|---|---|
| Site | `parcel`, `site_type`, `use_desc`, `luc`, `parcel_class`, `address` |
| Size | `acres`, `acres_geometry`, `acres_best` |
| Owner | `owner_name`, `owner_type`, `owner_mailing` |
| Assemblage | `owner_site_count`, `owner_site_acres` |
| Value | `assessed_land`, `assessed_bldg`, `assessed_total`, `year_built` |
| Condition | `hcs_grade`, `hcs_status` |
| Geography | `census_tract`, `neighborhood_code`, `lat`, `lon` |

### Ownership

| Owner type | Sites |
|---|---:|
| Individual | 8,950 |
| Company / trust | 2,294 |
| City of Dayton | 433 |
| Other public | 154 |
| Land bank | 76 |

`owner_mailing` is included because a developer's first question about a privately held
parcel is who to contact — and because a mailing address in another state is itself a
signal about how the parcel is being held.

### Assemblage

`owner_site_count` and `owner_site_acres` give the number of vacant parcels each owner
holds and their combined acreage. Contiguous lots under a single owner are the practical
route to a site larger than one lot, and they do not look like sites when read parcel by
parcel. This is the cheapest available proxy for assembly potential; true adjacency would
need a geometry pass.

---

## Rebuilding

```bash
python3 scripts/build_developable_sites.py \
        TAXROLL_YYYYMMDD.csv \
        data/raw/hcs_grades.json \
        data/raw/address_bridge.json \
        data/derived
```

Requires `parcel_areas.json` and `parcel_centroids.json` alongside the bridge — both are
pulled from `DaytonParcels` by parcel-id batch via POST (a GET URL exceeds length limits at
this batch size).

The tax roll is published daily, so this refreshes as often as needed.

---

## Known limits

**Not a vetted list.** No check for easements, deed restrictions, environmental status,
utility access, or zoning suitability. A developer would need all of those.

**Half the sites lack coordinates.** 5,986 of 11,907 are mapped. Vacant lots frequently
have no address point, and 341 parcels were not found in the current parcel layer at all —
consistent with the parcel-vintage divergence documented in
[`DUPLICATE_LAYERS.md`](DUPLICATE_LAYERS.md).

**Vacancy for structures depends on the condition survey.** A church or warehouse the
survey did not visit will not appear, regardless of its actual state. 43 candidate parcels
had no HCS record at all.

**Land use codes describe assessment, not potential.** LUC 500 means the Auditor classes a
parcel as residential vacant land. It says nothing about whether anything can be built
there.

**Approved plans and proposed sites are not included.** Compiling those remains manual
work, and it is precisely the gap that prompted this request.

Note that `HousingProjects_ProgramType` / the City's Housing Dashboard StoryMap is **not**
the same thing and should not be offered as a substitute. That layer shows 376 projects
already **in execution** — funded, underway, or complete — which answers a resident's or a
civic-health question ("what is happening in Dayton?"). This layer answers a developer's
("where could something be built?"). Opportunity and activity are different questions, and
a site that already has a funded project on it is arguably the *last* place a developer
needs to look.
