# Engineering/Trails

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Engineering/Trails/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Engineering_Trails
- **Created:** None  ·  **Item modified:** None
- **Tags:** Engineering

## Layer 0: Trails

- **Records:** 1,115
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `TYPE` | SmallInteger |  | **Values:** `0` = FOOT TRAIL; `1` = BIKE PATH |
| `TrailLength` | Integer |  |  |
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
| `SHAPE.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

