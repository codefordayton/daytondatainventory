# Police/CrimeVictimDashboard

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Police/CrimeVictimDashboard/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Police_CrimeVictimDashboard
- **Created:** None  ·  **Item modified:** None
- **Tags:** Police

## Layer 0: --

- **Records:** 35
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PERIMETER` | Double |  |  |
| `BIGBNDY_` | Integer |  |  |
| `BIGBNDY_ID` | Integer |  |  |
| `NAME` | String |  | len 50 |
| `NAME_CODE` | Integer |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAM` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `Done` | String |  | len 254 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 1: dbo.vu_CrimeVictimDashboard

- **Records:** 4

| Field | Type | Alias | Notes |
|---|---|---|---|
| `nibrs_code` | String |  | len 160 |
| `subgroup` | String |  | len 50 |
| `crime_desc` | String |  | len 160 |
| `v_type` | String |  | len 160 |
| `sex` | String |  | len 16 |
| `race` | String |  | len 16 |
| `eth` | String |  | len 16 |
| `age` | String |  | len 16 |
| `yr` | Integer |  |  |
| `crimes` | Integer |  |  |
| `ROWNUMBER` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ESRI_OID` | OID |  |  |

</details>

