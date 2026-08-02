# Police/PoliceAreas

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Police/PoliceAreas/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Police_PoliceAreas
- **Created:** None  ·  **Item modified:** None
- **Tags:** Police

## Layer 0: District

- **Records:** 4
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `District` | String |  | len 254 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |
| `Shape_Area` | Double |  |  |

</details>

## Layer 1: Beat

- **Records:** 15
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Beat` | String |  | len 50 |
| `Beat_NUm` | String |  | len 254 |
| `District` | String |  | len 254 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |
| `Shape_Area` | Double |  |  |

</details>

## Layer 2: Sector

- **Records:** 178
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `POD` | String |  | len 50 |
| `Beat` | String |  | len 50 |
| `Sector` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |
| `Shape_Area` | Double |  |  |

</details>

