# Divergent copies of the parcel base layer

**Eleven different record counts are published for a layer named "parcel" across the
City's GIS servers.** A consumer asking "how many parcels are in Dayton" gets a different
answer depending on which service they happen to open.

Edit dates identify a current layer — `DaytonParcels`, edited June 2026 — but only on
ArcGIS Online. **Every one of the divergent copies lives on the on-premise server, which
publishes no edit dates at all**, so nothing distinguishes them from the outside.

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

## Update dates resolve about half of it

Two freshness signals exist, and they are not evenly distributed.

**The on-premise server publishes nothing.** Of the **56** parcel-named layers carrying
records there — which is where all eleven divergent counts live — **zero** expose
`editingInfo.lastEditDate`. For the layers that actually disagree, there is no update
signal at all.

**ArcGIS Online does publish it**, and it is decisive where available:

| `dataLastEditDate` | Records | Service |
|---|---:|---|
| **2026-06-16** | **88,668** | **`DaytonParcels`** |
| 2024-09-13 | — | `Parcels_HCS_Nuisance_WaterZero` |
| 2017-02-06 | 88,512 | `SLSA_2014_Parcels` |

**`DaytonParcels` is demonstrably the most recently maintained parcel layer** — data
edited 16 June 2026, with an item date that matches, so the metadata is not merely being
touched. That is independent corroboration for the layer this inventory already uses as
its spine.

It also identifies one of the eleven: **88,512 is `SLSA_2014_Parcels`, last edited
February 2017** — a nine-year-old project extract still being served, and a likely
contributor to the ~87,000 cluster.

**What remains undatable:** 86,799 and 86,939 exist only on the on-premise server, and
88,898 sits in `PublicWorks` with no signal. Update dates confirm which layer is current;
they cannot tell you what the older copies are or whether anything still depends on them.

---

## What this does and does not show

**It does show** that the same conceptual layer is served at materially different vintages
from different departmental folders. On the on-premise server — where the divergence lives
— nothing indicates which is authoritative, because no layer there publishes an edit date.

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

Sharpened by the edit-date evidence above, this is narrower than "pick a canonical layer":

**1. Confirm `DaytonParcels` is canonical.** Its edit date already says so; a line in the
service description would make that explicit rather than inferred.

**2. Label or retire the on-premise copies.** They publish no edit dates, so a consumer
has no way to tell they are older — which is the actual trap. `SLSA_2014_Parcels`
(February 2017) is the clearest case.

**3. Enable editor tracking on the on-premise server.** Zero of 56 parcel layers there
expose `lastEditDate`. This is the same ask as in `docs/FRESHNESS.md`, and this section is
the concrete argument for it: with edit dates, most of this document would have been
answerable in one query instead of requiring a full crawl.

None of these moves data or changes a service.

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
