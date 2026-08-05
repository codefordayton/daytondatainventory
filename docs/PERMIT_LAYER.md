# Permit layer — parcel-linkable output

A parcel-keyed permit dataset built for ingestion into parcel-based analytics platforms,
alongside condition, tenure, census and the other layers in this inventory.

Built by [`scripts/build_permit_layer.py`](../scripts/build_permit_layer.py).
Outputs live in `data/derived/`. Open formats only — no GIS software required to produce
or consume them.

Current build: **4,852 permits, 2026 H1**.

---

## The three outputs

| File | Rows | What it is |
|---|---|---|
| `permits_parcel.csv` | 4,852 | One row per permit, carrying a parcel id |
| `parcel_permit_summary.csv` | 2,838 | One row per parcel — the join-ready rollup |
| `permits.geojson` | 3,926 | Point geometry, WGS84 |

**`parcel_permit_summary.csv` is the one to hand to a parcel platform.** One row per
parcel means it joins directly against condition grades, tenure, delinquency and census
without any spatial operation:

```
parcel, permit_count, distinct_types, top_type, total_valuation,
first_permit, last_permit, address, lat, lon
```

`permits_parcel.csv` keeps permit-level detail for anyone who needs it. The GeoJSON is a
convenience for desktop GIS and web maps, not the primary artifact.

---

## Parcel resolution: 84%

Two independent routes, best first, with the method recorded on every row so consumers
can filter by confidence.

| Method | Permits | Basis |
|---|---|---|
| `permit_number` | 1,763 | Exact link to County CAMA — see [PERMIT_LINKING.md](PERMIT_LINKING.md) |
| `address` | 2,332 | Address match through the City address layer |
| `unmatched` | 757 | No parcel resolved |
| **Total resolved** | **4,095 (84%)** | across **2,838 distinct parcels** |

The two routes are complementary rather than redundant: the permit-number link is exact
but only reaches types the County records, while address matching covers the trades CAMA
omits entirely. Neither alone gets past ~43%.

255 of the 757 unmatched have **no address at all** in the results grid — mostly trade
licences and registrations, which are not property-related and legitimately have nowhere
to land.

---

## What's in it

**Current rollup:** 2,838 parcels · 559 with more than one permit · **$49.2M** total
declared valuation.

Busiest parcels are institutional — a hospital campus, downtown blocks — which is a
useful sanity check that the join is landing where activity actually is.

⚠️ `valuation` comes from CAMA and is populated on only 265 records. Treat total valuation
as a floor, not a measure. Accela's own fee data would need the record detail pages.

---

## Geometry

Coordinates come from the City address layer, requested in **WGS84 (EPSG:4326)** so the
server reprojects from State Plane — no local reprojection and no dependency.

Validated: **99.7% of points fall inside Dayton's bounding box** (lon −84.344 … −84.094,
lat 39.717 … 39.920). The handful outside are parcels in adjoining jurisdictions where
work was permitted by the City.

---

## Rebuilding

```bash
# 1. harvest permits for a window
python3 scripts/harvest_accela_permits.py data/raw/accela_permits_2026h1.json \
        --start 01/01/2026 --end 06/30/2026 --delay 2

# 2. optional: recover exact parcel ids from CAMA
python3 scripts/link_permits.py data/raw/accela_permits_2026h1.json PERMIT.DAT \
        data/raw/cama_spec.json data/raw/accela_permits_linked.json 2026

# 3. build the layer
python3 scripts/build_permit_layer.py data/raw/accela_permits_2026h1.json \
        data/raw/address_bridge.json data/derived \
        --linked data/raw/accela_permits_linked.json
```

Step 2 is optional — without it the layer still resolves parcels by address, just at a
lower rate and without valuation.

The address bridge must carry coordinates; rebuild it with
`scripts/build_address_bridge.py` if `lat`/`lon` are missing.

---

## Caveats

**This is a six-month window.** 2026 H1 only. The harvester takes any date range; a
multi-year backfill is a parameter change, run in yearly chunks.

**The upstream source is a scraped WebForms portal.** It works and it fails loudly, but it
can break on any portal update. This layer demonstrates the data's value; it is not a
substitute for a supported export from the permitting system, and anyone depending on it
should know that.

**Parcel ≠ address.** Multi-unit buildings put several permits on one parcel, which is
correct for parcel-level analysis but wrong for per-unit rates.

**Match method matters.** `permit_number` is an exact identifier match. `address` is a
normalized string match and will occasionally attach a permit to a neighbouring parcel
where addressing is ambiguous. Filter on `match_method` if precision matters more than
coverage.

**Valuation is sparse and comes from the County**, not the City. See above.
