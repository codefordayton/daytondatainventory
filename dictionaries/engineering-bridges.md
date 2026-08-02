# Engineering/Bridges

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Engineering/Bridges/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Engineering_Bridges
- **Created:** None  ·  **Item modified:** None
- **Tags:** Engineering

## Layer 0: Bridges

- **Records:** 189
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `TYPE` | SmallInteger |  | **Values:** `0` = ROAD BRIDGE; `1` = ROAD OVERPASS; `2` = RAILROAD BRIDGE; `3` = TRAIL OR BIKE PATH BRIDGE; `4` = NO DATA |
| `SOURCE` | SmallInteger |  | **Values:** `0` = HISTORICAL DOCUMENTS; `1` = AERIAL PHOTOGRAPHY; `3` = LIDAR; `2` = COUNTY FC |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry |  |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

