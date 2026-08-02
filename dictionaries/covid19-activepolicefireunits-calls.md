# COVID19/ActivePoliceFireUnits_Calls

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/COVID19/ActivePoliceFireUnits_Calls/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=COVID19_ActivePoliceFireUnits_Calls
- **Created:** None  ·  **Item modified:** None
- **Tags:** COVID19

## Layer 0: Active Fire Units

- **Records:** 0
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Latitude2` | Double |  |  |
| `Longitude2` | Double |  |  |
| `Unit_ID` | String |  | len 8 |
| `Division` | String |  | len 20 |
| `Login_Date` | Date |  |  |
| `Crew` | String |  | len 100 |
| `IncNum` | String |  | len 200 |
| `Time` | String |  | len 5 |
| `Date` | String |  | len 10 |
| `Incident` | String |  | len 254 |
| `Priority` | String |  | len 20 |
| `Status` | String |  | len 20 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 3: Police - Active Calls

- **Records:** 15
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `RowNumber` | OID |  |  |
| `CallTime` | Date |  |  |
| `CallSign` | String |  | len 100 |
| `IncNum` | String |  | len 200 |
| `DispTime` | Date |  |  |
| `OnSceneTime` | Date |  |  |
| `Priority` | String |  | len 20 |
| `IncidentType` | String |  | len 512 |
| `Status` | String |  | len 20 |
| `Geometry` | Geometry |  |  |

