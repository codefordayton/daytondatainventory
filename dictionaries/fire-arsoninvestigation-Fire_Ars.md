# Fire/ArsonInvestigation

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Fire/ArsonInvestigation/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Fire_ArsonInvestigation
- **Created:** None  ·  **Item modified:** None
- **Tags:** Fire

## Layer 0: Fire Locations

- **Records:** 5
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FireLocation` | String | Fire Location | len 50 |
| `IncidentType` | String | Incident Type | **Values:** `Arson - Arrest` = Arson - Arrest; `Arson - No Arrest` = Arson - No Arrest; `Other` = Other · len 50 |
| `LocationType` | String | Location Type | **Values:** `Residential` = Residential; `Commercial` = Commercial; `Other` = Other · len 50 |
| `FireInvestigator` | String | Fire Investigator | len 50 |
| `FireStatus` | String | Fire Status | **Values:** `Active - Under Investigation` = Active - Under Investigation; `Active - Arrest Pending` = Active - Arrest Pending; `Inactive - Suspended` = Inactive - Suspended; `Closed` = Closed; `Other` = Other · len 50 |
| `FireCompany` | SmallInteger | Fire Company | **Values:** `2` = 02; `4` = 04; `8` = 08; `10` = 10; `11` = 11; `12` = 12; `13` = 13; `14` = 14; `15` = 15; `16` = 16; `17` = 17; `18` = 18 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `Comments` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 1: Camera Locations

- **Records:** 17
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CameraLocation` | String | Camera Location | len 50 |
| `CameraType` | String | Camera Type | **Values:** `Police` = Police; `Fire` = Fire; `Private - Friendly` = Private - Friendly · len 50 |
| `CameraDirection` | String | Camera Direction | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `Comments` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 2: Field Interviews

- **Records:** 5
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FILocation` | String | FI Location | len 50 |
| `FIName` | String | FI Name | len 50 |
| `FIAddress` | String | FI Address | len 50 |
| `FIPhone` | String | FI Phone | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `Comments` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `FIDate` | Date |  |  |
| `Shape` | Geometry |  |  |

</details>

