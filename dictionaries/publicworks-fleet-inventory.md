# PublicWorks/Fleet_Inventory

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/Fleet_Inventory/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_Fleet_Inventory
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 0: Fleet Master List

- **Records:** 1,348
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `VEHICLE_ID` | Double |  |  |
| `MAKE_MODEL` | String |  | len 255 |
| `SERIAL_NO` | String |  | len 255 |
| `LICENSE` | String |  | len 255 |
| `DEPT` | Double |  | **Values:** `1200` = CLERK OF COMMISION; `2101` = PUBLIC INFORMATION; `2320` = CODE ENFORCEMENT; `2321` = HOUSING INSPECTION; `2322` = HOUSING INSPECTION; `2380` = PLANNING-CD DIRECTOR; `2390` = PLANNING & COMMUNITY DEVELOPMENT; `2410` = ZONING ADMINISTRATION; `2430` = BUILDING INSPECTION; `2509` = MUNICIPAL COURTS-EHDP-HOME DETENTION; `2510` = MUNICIPAL COURTS; `3400` = S&T-ADMINISTRATION; …(+46 more) |
| `CLASS` | Double |  | **Values:** `200` = ATV; `201` = MOTORCYCLE; `202` = BOAT; `300` = COMPACT SEDAN; `301` = MID-SIZED SEDAN; `302` = FULL SIZE SEDAN; `303` = PATROL SEDAN; `400` = COMPACT SUV; `401` = MID-SIZED SUV; `402` = FULL SIZE SUV; `403` = PATROL SUV; `500` = COMPACT PICKUP; …(+48 more) |
| `MILEAGE` | Double |  |  |
| `DATE_ACQUIRED` | Date |  |  |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `FIELD_NOTE` | String |  | len 255 |
| `VEHICLE_NAME` | String |  | len 20 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: sde.GISADMIN.Fleet_Master_List__ATTACH

- **Records:** 1,226

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `VEHICLE_ID` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

