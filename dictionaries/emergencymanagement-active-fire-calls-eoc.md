# EmergencyManagement/Active_Fire_Calls_eoc

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/EmergencyManagement/Active_Fire_Calls_eoc/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=EmergencyManagement_Active_Fire_Calls_eoc
- **Created:** None  ·  **Item modified:** None
- **Tags:** EmergencyManagement

## Layer 0: Fire Active Calls

- **Records:** 12
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `RowNumber` | OID |  |  |
| `CallSign` | String |  | len 100 |
| `IncidentNumber` | String |  | len 200 |
| `Time` | String |  | len 5 |
| `Date` | String |  | len 10 |
| `DispTime` | Date |  |  |
| `latitude` | Double |  |  |
| `longitude` | Double |  |  |
| `IncidentTypeDescription` | String |  | len 512 |
| `UnitType` | String |  | len 17 |
| `Geometry` | Geometry |  |  |

## Layer 1: Fire Active Units

- **Records:** 7,379

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Unit_ID` | String |  | len 20 |
| `Agency` | String |  | len 2 |
| `Current_DArea` | String |  | len 20 |
| `Dept_ID_S` | String |  | len 20 |
| `Login_Date` | Date |  |  |
| `Logoff_Date` | Date |  |  |
| `Cadid` | OID |  |  |

