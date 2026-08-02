# EmergencyManagement/PoliceActiveCalls_EOC__

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/EmergencyManagement/PoliceActiveCalls_EOC__/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=EmergencyManagement_PoliceActiveCalls_EOC__
- **Created:** None  ·  **Item modified:** None
- **Tags:** EmergencyManagement

## Layer 0: Active Calls

- **Records:** 15
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Call_Time` | Date |  |  |
| `callsign` | String |  | len 100 |
| `incidentnumber` | String |  | len 200 |
| `dispatchtime` | Date |  |  |
| `onscenetime` | Date |  |  |
| `latitude` | Double |  |  |
| `longitude` | Double |  |  |
| `PRTY` | String |  | len 20 |
| `incidenttypecode` | String |  | len 20 |
| `incidentTypeDescription` | String |  | len 512 |
| `routestatusname` | String |  | len 20 |
| `RowNumber` | OID |  |  |
| `Geometry` | Geometry |  |  |

## Layer 8: Active Units

- **Records:** 662,132

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Unit_ID` | String |  | len 8 |
| `Agency` | String |  | len 2 |
| `Home_DArea` | String |  | len 20 |
| `Current_DArea` | String |  | len 20 |
| `Vehicle_ID` | String |  | len 20 |
| `Dept_ID_S` | String |  | len 20 |
| `Dept_ID_2` | String |  | len 20 |
| `Login_Date` | Date |  |  |
| `Logoff_Date` | Date |  |  |
| `Cadid` | Integer |  |  |
| `TransactionType` | String |  | len 20 |
| `RowNumber` | OID |  |  |

## Layer 9: Off Duty Vehicles

- **Records:** 13,544

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | OID |  |  |
| `ListID` | Integer |  |  |
| `ApplyDate` | Date |  |  |
| `Officer_Email` | String |  | len 100 |
| `OfficerName` | String |  | len 100 |
| `Start_Time` | String |  | len 10 |
| `End_Time` | String |  | len 10 |
| `Reason` | String |  | len 50 |
| `Comments` | String |  | len 1073741822 |
| `Created` | Date |  |  |
| `RowNumber` | Integer |  |  |

