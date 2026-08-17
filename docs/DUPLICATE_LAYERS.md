# Divergent copies of the parcel base layer

**Eleven different record counts are published for a layer named "parcel" across the
City's GIS server.** A consumer asking "how many parcels are in Dayton" gets a different
answer depending on which service they happen to open, and none is marked canonical.

This is a finding about how the data is organised, not a criticism of any department. It
is also the kind of thing only a full sweep surfaces — each service looks fine on its own.

Measured 2026-08-17 from the on-premise server crawl (`data/raw/fields_dayton_server.json`).

---

## What was found

Layers whose own name contains "parcel", grouped by record count:

| Records | Services | Folders |
|---:|---:|---|
| 865,084 | 10 | Planning, Viewer, WUFO, Water |
| **273,627** | 11 | (root), FieldMaps, Fire, PublicWorks, Viewer, WPA, WUFO, Water |
| **273,310** | 8 | (root), FieldMaps, Planning, Viewer, WUFO, Water |
| **273,113** | 1 | EmergencyManagement |
| **272,810** | 1 | Hansen |
| **272,751** | 5 | Planning, Viewer, WUFO |
| **88,898** | 1 | PublicWorks |
| **88,512** | 1 | PublicWorks |
| **86,939** | 2 | Base, Environmental |
| **86,799** | 3 | COD_Webpage, Engineering, Police |
| 12,531 | 1 | PublicWorks |

Two clusters matter:

**County-scale (~273,000).** Five counts within 876 records of each other, spread across
eight folders including Emergency Management and Hansen, each holding its own.

**City-scale (~87,000).** Four counts spanning **2,099 records** — 86,799 · 86,939 ·
88,512 · 88,898. This is the range that matters for housing work, because it is the
Dayton parcel universe.

The 865,084 and 12,531 layers are almost certainly a different thing entirely (parcel
lines, or a project subset) rather than another copy.

---

## What this does and does not show

**It does show** that the same conceptual layer is served at materially different vintages
from different departmental folders, with nothing indicating which is authoritative.

**It does not show** that eight departments each maintain a separate copy. Much of the
apparent duplication is composite map services — `Viewer/MapLayers_Citywide`,
`FieldMaps/MapLayers_AllUtilities`, `WUFO/WUFO_Field_Maps_All_Utilities` — that legitimately
*include* a shared reference layer. Sharing a reference layer is normal practice and not a
problem.

The problem is narrower and more specific: **within the City-scale cluster, four different
answers exist for the same question.** Whether that is stale copies, or intentionally
different extracts (one excluding condominium sub-parcels, another including
rights-of-way), cannot be determined from record counts alone. Both explanations are
consistent with the evidence, and both are worth resolving — because a consumer cannot
tell them apart either.

---

## Why it matters here

This inventory selected `DaytonParcels` (88,668 records) as the parcel spine, and the
City↔County join was measured at 96.3% against it. Had a different copy been picked, that
figure would differ — and nothing in the published metadata would have flagged the choice
as significant.

More broadly, any analysis joining to "the parcel layer" inherits whichever vintage its
author happened to open. Two analyses can disagree for no reason either author can see.

---

## The ask

**Designate a canonical parcel layer and say so in its description.** One line of metadata
on the authoritative service — and ideally a note on the others pointing at it — would
resolve this without moving any data or changing any service.

This is cheap relative to the confusion it prevents, and it sits naturally alongside the
other two GIS asks in `docs/FRESHNESS.md`: publishing `lastEditDate`, and labelling
historical layers as historical.

---

## Reproducing

```python
import json, collections, re
d = json.load(open('data/raw/fields_dayton_server.json'))['datasets']
par = collections.defaultdict(set)
for ds in d:
    for L in ds.get('layers', []):
        if re.search(r'parcel', L.get('name') or '', re.I) and L.get('recordCount'):
            par[L['recordCount']].add(ds['title'])
for n, svcs in sorted(par.items(), reverse=True):
    print(f"{n:>10,}  {len(svcs):>3} services")
```

Regenerate the input with:

```bash
python3 scripts/extract_fields.py data/raw/arcgis_dayton_server.json \
        data/raw/fields_dayton_server.json
```
