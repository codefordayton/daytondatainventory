# EmergencyManagement/StructureConditions_EOC

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/EmergencyManagement/StructureConditions_EOC/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=EmergencyManagement_StructureConditions_EOC
- **Created:** None  ·  **Item modified:** None
- **Tags:** EmergencyManagement

## Layer 2: Structure Conditions

- **Records:** 0
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DATE` | Date | Inspection Date |  |
| `INSPNAME` | String | Inspector Name | len 100 |
| `NOTES` | String | Notes | len 350 |
| `PARCELID` | String | Parcel ID | len 50 |
| `ADDRNUM` | Integer | ADDR NUM |  |
| `ADDRST` | String | ADDR ST | len 100 |
| `ADDRSUF` | String | ADDR SUF | len 10 |
| `FULLADDR` | String | Address | len 150 |
| `OWNER` | String | Property Owner | len 100 |
| `ZIP` | String |  | len 5 |
| `ZONECD` | String | Zone Code | len 10 |
| `GUID` | GUID |  |  |
| `STRUC_TYPE` | String | Structure Type | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `ResidentialStrucType` | String | REsidential Structure Type | **Values:** `HOUSE` = HOUSE; `APARTMENT` = APARTMENT; `GARAGE` = GARAGE; `OTHER` = OTHER · len 255 |
| `OccupancyStatus` | String | Occupancy Status | **Values:** `VACANT` = VACANT; `OCCUPIED` = OCCUPIED · len 255 |
| `Occupy_OK` | String | Okay to Occupy | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 255 |
| `PartialOccup_Displaced` | String | Partial Occupancy Displaced Persons | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 255 |
| `NoOccup_Displaced` | String | No Occupancy Displaced Persons | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 255 |
| `UtilitiesDamage` | String | Damaged Utilities | **Values:** `ELECTRICAL PERMIT` = ELECTRICAL PERMIT; `MECHANICAL` = MECHANICAL · len 255 |
| `CONDTRATING` | String | Condition Rating | **Values:** `NO DAMAGE` = NO DAMAGE; `COSMETIC, NO BLG PERMIT REQ` = COSMETIC, NO BLG PERMIT REQ; `REPAIR PERMIT, NO STRUCTURE REQ` = REPAIR PERMIT, NO STRUCTURE REQ; `REPAIR PERMIT, REQUIRES ARCH/STRUCTURAL` = REPAIR PERMIT, REQUIRES ARCH/STRUCTURAL; `WRECKING PERMIT` = WRECKING PERMIT · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: Parcel Polygons

- **Records:** 273,113
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TAXPINNO` | String |  | len 20 |
| `ACAD_COLOR` | Double |  |  |
| `TAXDISTRIC` | String |  | len 5 |
| `TAXBOOK` | String |  | len 4 |
| `TAXPAGE` | String |  | len 2 |
| `TAXSUF` | String |  | len 1 |
| `TAXINDEX` | String |  | len 4 |
| `SOURCEDOC` | String |  | len 20 |
| `TAXAREA` | String |  | len 10 |
| `LOTNUMBER` | String |  | len 20 |
| `ACREAGE` | String |  | len 12 |
| `SURVEY` | String |  | len 12 |
| `LOC_NBR` | Double |  |  |
| `LOC_DIR` | String |  | len 4 |
| `LOC_STREET` | String |  | len 50 |
| `LOC_SUFFIX` | String |  | len 10 |
| `PID_FLG01` | String |  | len 10 |
| `LOC_AREA` | String |  | len 30 |
| `PID_VERIFY` | String |  | len 1 |
| `PID_STATUS` | Double |  |  |
| `CAMA_MATCH` | String |  | len 1 |
| `NBHD_1` | String |  | len 10 |
| `K_PID` | String |  | len 18 |
| `SURVEY_REQUIRED` | String |  | len 1 |
| `STR_ID` | Integer |  |  |
| `MCSTR_ID` | Integer |  |  |
| `BLDG_CNT` | SmallInteger |  |  |
| `ADDR_CNT` | SmallInteger |  |  |
| `HOT_LINK` | String |  | len 75 |
| `PHOTO_LINK` | String |  | len 100 |
| `WEB_BKPG_LINK` | String |  | len 100 |
| `WEB_ARCHIVE_LINK` | String |  | len 100 |
| `C_BLOCK` | String |  | len 20 |
| `C_TRACK` | String |  | len 20 |
| `X_GIS_REF` | Double |  |  |
| `OWNER1` | String |  | len 100 |
| `OWNER2` | String |  | len 100 |
| `LOC_CITY` | String |  | len 30 |
| `LOC_STATE` | String |  | len 4 |
| `LOC_ZIP` | String |  | len 5 |
| `LOC_ZIP4` | String |  | len 5 |
| `LOC_FADDRESS` | String |  | len 100 |
| `LOC_ZIP_FLG` | String |  | len 1 |
| `PARCEL_USE` | String |  | len 15 |
| `PARCEL_USE_DOC` | String |  | len 100 |
| `PARCEL_USE_WEB` | String |  | len 120 |
| `DISCLAIMER1` | String |  | len 100 |
| `DISCLAIMER2` | String |  | len 100 |
| `WEB_ARCHIVE_P` | String |  | len 50 |
| `WEB_ARCHIVE_S` | String |  | len 50 |
| `CREATE_FLG` | String |  | len 1 |
| `CREATE_OPER` | String |  | len 3 |
| `CREATE_DATE` | String |  | len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

