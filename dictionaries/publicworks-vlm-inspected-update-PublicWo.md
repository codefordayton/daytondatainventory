# PublicWorks/VLM_Inspected_UPDATE

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/VLM_Inspected_UPDATE/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_VLM_Inspected_UPDATE
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 0: VLM Inspected Parcels

- **Records:** 12,531
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.VLM_Parcels.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.VLM_Parcels.TAXPINNO` | String | TAXPINNO | len 20 |
| `GISADMIN.VLM_Parcels.TAXAREA` | String | TAXAREA | len 10 |
| `GISADMIN.VLM_Parcels.LOTNUMBER` | String | LOTNUMBER | len 20 |
| `GISADMIN.VLM_Parcels.ACREAGE` | String | ACREAGE | len 12 |
| `GISADMIN.VLM_Parcels.LOC_NBR` | Double | LOC_NBR |  |
| `GISADMIN.VLM_Parcels.LOC_DIR` | String | LOC_DIR | len 4 |
| `GISADMIN.VLM_Parcels.LOC_STREET` | String | LOC_STREET | len 50 |
| `GISADMIN.VLM_Parcels.LOC_SUFFIX` | String | LOC_SUFFIX | len 10 |
| `GISADMIN.VLM_Parcels.K_PID` | String | K_PID | len 18 |
| `GISADMIN.VLM_Parcels.GLOBALID` | GlobalID | GLOBALID |  |
| `GISADMIN.VLM_Parcels.OWNER1` | String | OWNER1 | len 100 |
| `GISADMIN.VLM_Parcels.OWNER2` | String | OWNER2 | len 100 |
| `GISADMIN.VLM_Parcels.PAR_LOC` | String | PAR_LOC | len 50 |
| `GISADMIN.VLM_Parcels.MOW_ORDER` | Double | MOW_ORDER |  |
| `GISADMIN.VLM_Parcels.VLM_PHOTO` | String | VLM_PHOTO | len 150 |
| `GISADMIN.VLM_Parcels.Shape` | Geometry | Shape |  |
| `GISADMIN.VLM_Parcels.created_user` | String | created_user | len 255 |
| `GISADMIN.VLM_Parcels.created_date` | Date | created_date |  |
| `GISADMIN.VLM_Parcels.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.VLM_Parcels.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.VLM_Inspection_UPDATE.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.VLM_Inspection_UPDATE.PARCEL_ID` | String | Parcel ID | len 20 |
| `GISADMIN.VLM_Inspection_UPDATE.NEIGHBORHOOD` | String | Neighborhood | **Values:** `AIRPORT` = AIRPORT; `ARLINGTON HEIGHTS` = ARLINGTON HEIGHTS; `BELMONT` = BELMONT; `BURKHARDT` = BURKHARDT; `CARILLON` = CARILLON; `COLLEGE HILL` = COLLEGE HILL; `CORNELL HEIGHTS` = CORNELL HEIGHTS; `DAYTON VIEW TRIANGLE` = DAYTON VIEW TRIANGLE; `DEWEESE` = DEWEESE; `DOWNTOWN` = DOWNTOWN; `EASTERN HILLS` = EASTERN HILLS; `EASTMONT` = EASTMONT; …(+53 more) · len 50 |
| `GISADMIN.VLM_Inspection_UPDATE.STREET_TYPE` | String | Street Type | **Values:** `Residential` = Residential; `Thoroughfare` = Thoroughfare · len 50 |
| `GISADMIN.VLM_Inspection_UPDATE.LOT_TYPE` | String | Lot Type | **Values:** `VL` = Vacant Lot; `S` = Structure; `TL` = Tractor Lot; `SB` = Structure - Boarded; `VS` = Structure - Unsecure; `OCC` = Structure - Occupied; `LEAF` = Leaf Removal · len 50 |
| `GISADMIN.VLM_Inspection_UPDATE.TREE_REMOVAL` | String | Tree Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `GISADMIN.VLM_Inspection_UPDATE.BRUSH_REMOVAL` | String | Brush Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `GISADMIN.VLM_Inspection_UPDATE.BULK_REMOVAL` | String | Bulk Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `GISADMIN.VLM_Inspection_UPDATE.TRASHBIN_REMOVAL` | String | Trash Bin Removal | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `GISADMIN.VLM_Inspection_UPDATE.OWNER_MOWED` | String | Owner Mowed | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `GISADMIN.VLM_Inspection_UPDATE.OCCUPIED` | String | Occupied | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `GISADMIN.VLM_Inspection_UPDATE.ACCESSIBLE` | String | Accessible | **Values:** `NO` = NO; `YES` = YES · len 3 |
| `GISADMIN.VLM_Inspection_UPDATE.COMMENT` | String | Field Comment | len 255 |
| `GISADMIN.VLM_Inspection_UPDATE.created_user` | String | Added By | len 255 |
| `GISADMIN.VLM_Inspection_UPDATE.created_date` | Date | Added Date |  |
| `GISADMIN.VLM_Inspection_UPDATE.last_edited_user` | String | Edited By | len 255 |
| `GISADMIN.VLM_Inspection_UPDATE.last_edited_date` | Date | Edited Date |  |
| `GISADMIN.VLM_Inspection_UPDATE.LOCATION` | String | LOCATION | len 255 |
| `GISADMIN.VLM_Inspection_UPDATE.GlobalID_1` | GUID | GlobalID |  |
| `GISADMIN.VLM_Inspection_UPDATE.REINSPECTED` | String | REINSPECTED | **Values:** `NO` = NO; `YES` = YES · len 50 |
| `GISADMIN.VLM_Inspection_UPDATE.Old_Neighborhood` | String | Old_Neighborhood | len 50 |
| `GISADMIN.VLM_Inspection_UPDATE.GlobalID` | String | GlobalID | len 38 |

## Layer 1: VLM Inspections

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

