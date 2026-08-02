# Fire/FireAreas

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Fire/FireAreas/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Fire_FireAreas
- **Created:** None  ·  **Item modified:** None
- **Tags:** Fire

## Layer 0: Company In Districts

- **Records:** 13
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `Company` | String |  | len 12 |
| `Square_Mil` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `District` | SmallInteger |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |
| `Shape_Area` | Double |  |  |

</details>

## Layer 1: Medic Sectors

- **Records:** 202
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Company` | String |  | len 255 |
| `Sector` | String |  | len 255 |
| `primary_` | String | primary | len 255 |
| `secondary` | String |  | len 255 |
| `tertiary` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `Sector_ID` | SmallInteger | Sector ID |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |
| `Shape_Area` | Double |  |  |

</details>

## Layer 2: Fire Sectors

- **Records:** 202
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Company` | String |  | len 255 |
| `Sector` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `SectorID` | SmallInteger |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape_Length` | Double |  |  |
| `Shape_Area` | Double |  |  |

</details>

