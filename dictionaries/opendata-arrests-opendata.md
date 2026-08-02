# OpenData/Arrests_OpenData

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/OpenData/Arrests_OpenData/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=OpenData_Arrests_OpenData
- **Created:** None  ·  **Item modified:** None
- **Tags:** OpenData

## Layer 0: --

- **Records:** 1
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `STATECODE` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 1: GeoMax.gisadmin.PoliceArrest_OpenData

- **Records:** 48,778

| Field | Type | Alias | Notes |
|---|---|---|---|
| `RowNumber` | Integer |  |  |
| `BookingNumber` | String |  | len 200 |
| `Sex` | String |  | len 13 |
| `Age` | Integer |  |  |
| `Adult_Juvenile` | String |  | len 10 |
| `Race` | String |  | len 30 |
| `Ethnicity` | String |  | len 22 |
| `Arrest_Date` | Date |  |  |
| `Year` | Integer |  |  |
| `Arrest_Time` | String |  | len 8 |
| `Category` | String |  | len 23 |
| `Charge` | String |  | len 20 |
| `Charge_Description` | String |  | len 100 |
| `Jurisdiction` | String |  | len 27 |
| `Warrant_Number` | String |  | len 24 |
| `Warrant_Originating_Agency` | String |  | len 30 |
| `Armed_With1_Desc` | String |  | len 30 |
| `Armed_With2_Desc` | String |  | len 30 |
| `Armed_With3_Desc` | String |  | len 30 |
| `USER_Status` | String |  | len 8 |
| `Crime_Description` | String |  | len 82 |
| `NIBRS_Code` | String |  | len 6 |
| `Neighborhood` | String |  | len 100 |
| `Priority_Board` | String |  | len 100 |
| `ORC_Part` | String |  | len 24 |
| `Primary_Charge` | String |  | len 100 |
| `Primary_Charge_Disposition` | String |  | len 80 |

