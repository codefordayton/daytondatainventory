# ContoursSpotElevation

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/ContoursSpotElevation/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=ContoursSpotElevation
- **Created:** None  ·  **Item modified:** None

## Layer 0: sde_publish.GISADMIN.SpotElevation

- **Records:** 145,053
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ELEVATION` | Double |  |  |
| `TYPE` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `SHAPE` | Geometry | Shape |  |
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: sde_publish.GISADMIN.Contour

- **Records:** 197,339
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TYPE` | String |  | len 80 |
| `ELEVATION` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `SHAPE.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

