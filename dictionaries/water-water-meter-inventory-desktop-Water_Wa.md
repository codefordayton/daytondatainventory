# Water/Water_Meter_Inventory_Desktop

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Water/Water_Meter_Inventory_Desktop/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Water_Water_Meter_Inventory_Desktop
- **Created:** None  ·  **Item modified:** None
- **Tags:** Water

## Layer 0: wFacilityMeters

- **Records:** 78
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Name` | String |  | len 50 |
| `Address` | String |  | len 100 |
| `WaterDivision` | String | Water Division | **Values:** `WD` = Water Distribution; `WST` = Water Supply & Treatment; `WE` = Water Engineering; `WA` = Water Administration; `WEM` = Water Environmental Management; `WUFO` = Water Utility Field Operations; `WR` = Water Reclamation · len 50 |
| `ContactPerson` | String | Contact Person | len 50 |
| `ContactNumber` | String | Contact Number | len 50 |
| `XCoord` | Double | X Coordinate |  |
| `YCoord` | Double | Y Coordinate |  |
| `FacilityType` | String | Facility Type | len 50 |
| `Comments` | String |  | len 200 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: sde.GISADMIN.wFacilityMeterInventory

- **Records:** 114

| Field | Type | Alias | Notes |
|---|---|---|---|
| `MeterNumber` | String | Meter Number | len 50 |
| `DRNumber` | String | DR Number | len 50 |
| `MeterCompany` | String | Meter Company | **Values:** `Vect` = Vectren; `DPL` = DP&L; `Pro` = Proliance; `Oth` = Other · len 50 |
| `AccountNumber` | String | Account Number | len 50 |
| `Name` | String |  | len 50 |
| `MeterInformation` | String |  | len 150 |
| `MeterMake` | String |  | len 30 |
| `MeterType` | String |  | **Values:** `Gas` = Gas; `Electric` = Electric · len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

