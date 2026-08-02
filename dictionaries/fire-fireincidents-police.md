# Fire/FireIncidents_Police

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Fire/FireIncidents_Police/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Fire_FireIncidents_Police
- **Created:** None  ·  **Item modified:** None
- **Tags:** Fire

## Layer 0: Police Stations

- **Records:** 5
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `Precinct` | String |  | len 50 |
| `Descript` | String |  | len 254 |
| `Address` | String |  | len 254 |
| `City` | String |  | len 10 |
| `State` | String |  | len 2 |
| `Zip` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 1: Fire Incidents - Greater 2019

- **Records:** 219,699
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Join_Count` | Integer |  |  |
| `TARGET_FID` | Integer |  |  |
| `RowNumber` | Integer |  |  |
| `DaysSince` | Integer |  |  |
| `CAD_NO` | String |  | len 22 |
| `Address` | String |  | len 80 |
| `MapNo` | String |  | len 22 |
| `Incident` | String |  | len 24 |
| `IncType` | String |  | len 26 |
| `IncCat` | String |  | len 27 |
| `Apparatus` | String |  | len 10 |
| `ApparatusDescription` | String |  | len 255 |
| `ApparatusType` | String |  | len 255 |
| `Platoon` | String |  | len 4 |
| `DayName` | String |  | len 13 |
| `DisTime` | Double |  |  |
| `TEnroute` | Double |  |  |
| `TStaged` | Double |  |  |
| `TOnSite` | Double |  |  |
| `Ttransp` | Double |  |  |
| `TAtHosp` | Double |  |  |
| `TInServ` | Double |  |  |
| `TInQuart` | Double |  |  |
| `DisDate` | Date |  |  |
| `Month` | Integer |  |  |
| `Day` | Integer |  |  |
| `Year` | Integer |  |  |
| `Latitude` | String |  | len 32 |
| `Longitude` | String |  | len 32 |
| `PERIMETER` | Double |  |  |
| `BIGBNDY_` | Integer |  |  |
| `BIGBNDY_ID` | Integer |  |  |
| `NAME` | String |  | len 50 |
| `NAME_CODE` | Integer |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAM` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | Integer | OBJECTID |  |
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry |  |  |
| `GLOBALID` | String |  | len 38 |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `GlobalID_1` | String |  | len 38 |

</details>

## Layer 2: Company In Districts

- **Records:** 12
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Square_Mil` | Double |  |  |
| `Id` | Integer |  |  |
| `Company` | String |  | len 12 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

