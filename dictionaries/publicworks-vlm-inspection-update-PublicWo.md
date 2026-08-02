# PublicWorks/VLM_Inspection_UPDATE

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/VLM_Inspection_UPDATE/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_VLM_Inspection_UPDATE
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 0: Dayton Parcels for VLM

- **Records:** 88,898
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TAXPINNO` | String |  | len 20 |
| `TAXAREA` | String |  | len 10 |
| `LOTNUMBER` | String |  | len 20 |
| `ACREAGE` | String |  | len 12 |
| `LOC_NBR` | Double |  |  |
| `LOC_DIR` | String |  | len 4 |
| `LOC_STREET` | String |  | len 50 |
| `LOC_SUFFIX` | String |  | len 10 |
| `K_PID` | String |  | len 18 |
| `OWNER1` | String |  | len 100 |
| `OWNER2` | String |  | len 100 |
| `PAR_LOC` | String |  | len 50 |
| `MOW_ORDER` | Double |  |  |
| `VLM_PHOTO` | String |  | len 150 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 1: GISADMIN.VLM_Inspections

- **Records:** 12,536

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PARCEL_ID` | String | Parcel ID | len 20 |
| `NEIGHBORHOOD` | String | Neighborhood | **Values:** `AIRPORT` = AIRPORT; `ARLINGTON HEIGHTS` = ARLINGTON HEIGHTS; `BELMONT` = BELMONT; `BURKHARDT` = BURKHARDT; `CARILLON` = CARILLON; `COLLEGE HILL` = COLLEGE HILL; `CORNELL HEIGHTS` = CORNELL HEIGHTS; `DAYTON VIEW TRIANGLE` = DAYTON VIEW TRIANGLE; `DEWEESE` = DEWEESE; `DOWNTOWN` = DOWNTOWN; `EASTERN HILLS` = EASTERN HILLS; `EASTMONT` = EASTMONT; …(+53 more) · len 50 |
| `STREET_TYPE` | String | Street Type | **Values:** `Residential` = Residential; `Thoroughfare` = Thoroughfare · len 50 |
| `LOT_TYPE` | String | Lot Type | **Values:** `VL` = Vacant Lot; `S` = Structure; `TL` = Tractor Lot; `SB` = Structure - Boarded; `VS` = Structure - Unsecure; `OCC` = Structure - Occupied; `LEAF` = Leaf Removal · len 50 |
| `TREE_REMOVAL` | String | Tree Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `BRUSH_REMOVAL` | String | Brush Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `BULK_REMOVAL` | String | Bulk Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `TRASHBIN_REMOVAL` | String | Trash Bin Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `OWNER_MOWED` | String | Owner Mowed | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `OCCUPIED` | String | Occupied | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `ACCESSIBLE` | String | Accessible | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `COMMENT` | String | Field Comment | len 255 |
| `created_user` | String | Added By | len 255 |
| `created_date` | Date | Added Date |  |
| `last_edited_user` | String | Edited By | len 255 |
| `last_edited_date` | Date | Edited Date |  |
| `LOCATION` | String |  | len 255 |
| `REINSPECTED` | String |  | **Values:** `NO` = NO; `YES` = YES · len 50 |
| `Old_Neighborhood` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 2: GISADMIN.VLM_Inspections__ATTACH

- **Records:** 10,965

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ATTACHMENTID` | OID |  |  |
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |

</details>

