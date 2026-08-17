# City of Dayton owned property — reconciling two records

**There is no single dataset that encompasses City-owned property.** Two exist, they
disagree on 1,317 parcels, and neither alone answers the question a developer-facing
inventory needs.

This documents what each holds, how far they diverge, why the obvious owner-name filter
misclassifies, and how to separate development sites from operational holdings.

Built by [`scripts/build_city_owned_inventory.py`](../scripts/build_city_owned_inventory.py).
Outputs in `data/derived/`. Measured 2026-08-17.

---

## Why this exists

A request came through the Housing Data Subcommittee for an inventory of City-owned
property to share with developers interested in building new homes. Three problems
surfaced immediately, all of them real:

1. Filtering on owner name is over-inclusive.
2. The City's record and the County's record disagree.
3. There is no obvious way to separate parcels the City holds *for a function* (parks,
   rights-of-way, facilities) from parcels that could be *development sites*.

Each is addressed below with numbers rather than impressions.

---

## The two sources

| | **City GIS layer** | **County tax roll** |
|---|---|---|
| Service / file | `City_of_Dayton_Owned_Parcel` | `TAXROLL_*.csv` |
| Parcels | 1,912 | 2,781 |
| Freshness | **last edited 2021-07-30** | **published daily** |
| Ownership authority | secondary | **authoritative** |
| Carries intent | ✅ `DEPARTMENT`, `INTENDEDUSE`, `LEASE`, `SALE` | ✗ |
| Carries land use | partial | ✅ `LUC`, `CLS`, assessed values |

**Agreement is partial:**

| | Parcels |
|---|---|
| In both records | 1,688 |
| County only — not in the City's layer | **1,093** |
| City layer only — not in the County's | **224** |
| **Reconciled total** | **3,005** |

The City layer's five-year staleness is the likely explanation for most of the 1,093:
acquisitions since July 2021 would not appear in it. The 224 in the other direction are
more interesting and worth a look — they are parcels the City records as its own that the
County does not attribute to it.

⚠️ Neither number should be quoted as "the City owns N properties" without saying which
record it came from.

---

## Owner-name matching: the school district problem

A naive match on owner names containing both *city* and *dayton* returns **2,904** parcels.
**123 of those are not the municipal corporation:**

| Entity type | Parcels |
|---|---|
| **Dayton City School District** (Board of Education) | **107** |
| Private companies (LLC / Inc) | 6 |
| Churches and religious organisations | 5 |
| County | 2 |
| Other | 3 |

The school district is a separate legal body. Including its 107 parcels in a City
inventory is a material error, not a rounding one.

**But tightening the match naively also fails.** The tax roll writes the City several ways:

```
CITY OF DAYTON
THE CITY OF DAYTON
THE CITY OF DAYTON OHIO
DAYTON OH CITY OF
DAYTON CITY OH OF
```

A filter anchored on `CITY OF DAYTON` alone drops real parcels. The matcher in
`build_city_owned_inventory.py` uses an inclusion pattern covering these spellings plus an
exclusion list for other entities. Both are visible at the top of the script and should be
reviewed when the roll changes.

Result: **2,781 parcels** genuinely owned by the City per the County.

---

## Separating function from development potential

Stripping parcels with building value is the right instinct but does not go far enough —
only **263 of 2,781** carry a building. That removes City Hall, fire and police stations
and Ottawa Yards, and leaves 2,518 parcels including every park, median and street
remnant.

The County's **land use code** does the rest of the work, and it is classification the
Auditor already maintains:

| LUC | Meaning | Parcels |
|---|---|---|
| 640 | Exempt, owned by municipals | 2,108 |
| **400** | **Commercial vacant land** | **225** |
| **500** | **Residential vacant land, lot** | **182** |
| 620 | Exempt, owned by counties | 73 |
| **300** | **Industrial, vacant land** | **32** |
| 613 | Exempt land only | 18 |
| 600 | Exempt, owned by USA | 18 |

LUC 640 is the operational bucket — parks, rights-of-way, facilities. LUC 300/400/500 are
vacant land, and they are where development candidates live.

The City layer's `INTENDEDUSE` adds a second, independent signal where it is populated:
**302 Surplus · 34 Development · 22 Operations · 712 Other · 856 blank**.

### The candidate rule

A parcel is flagged `development_candidate = Y` when it has **no building value** AND
either the County classes it as vacant land **or** the City flagged it Surplus/Development.

**748 candidates**, of which 322 are explicitly flagged by the City.

⚠️ This is a **screening filter, not a disposition list.** It has not been checked for
easements, deed restrictions, environmental status, or whether a "vacant" parcel is
actually a drainage swale. Confirm parcel by parcel before anything goes to a developer.

---

## Outputs

| File | Rows | Contents |
|---|---|---|
| `city_owned_properties.csv` | 3,005 | Every parcel from either record, with `source` |
| `city_owned_development_candidates.csv` | 748 | The screened subset |
| `city_owned_properties.geojson` | 2,347 | Point geometry, WGS84 |

Columns: `parcel`, `source`, `owner_name`, `address`, `jurisdiction`, `luc`, `luc_desc`,
`parcel_class`, `acres`, `assessed_land`, `assessed_bldg`, `has_building`,
`city_department`, `city_intended_use`, `development_candidate`, `census_tract`,
`lat`, `lon`.

**`source` is the important column.** It records whether a parcel appears in both records,
the County's only, or the City's only — so disagreement travels with the data instead of
being silently resolved.

### Geometry

2,347 of 3,005 parcels are mapped. Coordinates come from the City address layer where a
parcel has an address, and from **parcel centroids** otherwise — necessary because many
City holdings are vacant lots and rights-of-way with no address point.

The remaining 658 have neither, mostly `city_layer_only` parcels absent from the current
parcel layer.

---

## Rebuilding

```bash
# taxroll is published daily; grab the current one
curl -O https://go.mcohio.org/applications/treasurer/search/data/Taxroll/TAXROLL_YYYYMMDD.zip

python3 scripts/build_city_owned_inventory.py \
        TAXROLL_YYYYMMDD.csv \
        data/raw/city_owned_parcels.json \
        data/raw/address_bridge.json \
        data/derived
```

`city_owned_parcels.json` is a pull of the City layer; `parcel_centroids.json` alongside
the bridge supplies geometry for unaddressed parcels.

---

## Caveats for anyone sharing this

**The City layer is five years old.** Any parcel acquired or disposed of since July 2021
is represented only by the County record, if at all.

**The two records disagree on 1,317 parcels.** That is 44% of the reconciled total. A
clean-looking list that hides this overstates confidence.

**`development_candidate` is a screen, not a recommendation.** 748 parcels warrant a look;
they have not been vetted.

**The school district is excluded deliberately.** If someone's prior list looked bigger,
this is likely why.

**Ownership itself is occasionally contested.** Cases exist where City and County records
disagree on who owns a parcel. `source = city_layer_only` (224 parcels) is where to look.

---

## What would fix this

**Refresh the City's property layer.** It carries the fields that matter —
`DEPARTMENT`, `INTENDEDUSE`, `LEASE`, `SALE` — and none of them are in the County record.
A current version of this layer would make the reconciliation largely unnecessary.

**Populate `INTENDEDUSE`.** It is blank on 856 of 1,926 parcels. It is the only field in
either source that directly answers "is this a development site," and filling it is a data
entry task, not a systems project.
