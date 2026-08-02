# PublicWorks/PWservices

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/PWservices/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_PWservices
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 0: Trash Service Area

- **Records:** 432
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TRASH_RT` | String |  | len 10 |
| `SECTION_` | SmallInteger |  |  |
| `DAY_` | String |  | len 1 |
| `WC_RT_TRASH` | String |  | len 10 |
| `RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `Day` | String |  | len 50 |
| `Cal_Link` | String |  | len 150 |
| `SUPERVISOR` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 1: Recycle Service Area

- **Records:** 364
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `RECY_RT` | String |  | len 10 |
| `DAY_` | String |  | len 1 |
| `ZONE_` | String |  | len 1 |
| `SECTION_` | String |  | len 25 |
| `WC_RT_RECY` | Integer |  |  |
| `RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `Day` | String |  | len 50 |
| `Cal_Link` | String |  | len 150 |
| `SUPERVISOR` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 2: Bulk Service Area

- **Records:** 235
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `BULK_RT` | String |  | len 10 |
| `ZONE_` | String |  | len 1 |
| `SECTION_` | SmallInteger |  |  |
| `DAY_` | String |  | len 1 |
| `WC_RT_BULK` | String |  | len 10 |
| `RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `SUPERVISOR` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |

</details>

## Layer 3: Biweekly Bulk Service Area

- **Records:** 223
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `BWBULK_RT` | String |  | len 10 |
| `BWDAY_` | String |  | len 1 |
| `BWWEEK_` | String |  | len 1 |
| `BWDAY_LBL` | String |  | len 10 |
| `BWWEEK_LBL` | String |  | len 10 |
| `BWBULK_RT_FULL` | String |  | len 12 |
| `TRASH_RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `SUPERVISOR` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 4: Container Service Area

- **Records:** 202
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COLL_DAY` | String | TRASH_DAY | len 12 |
| `CONT_RT` | String |  | len 10 |
| `DAY_` | String |  | len 1 |
| `SECTION_` | String |  | len 10 |
| `WC_RT_CONT` | String |  | len 10 |
| `RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `SUPERVISOR` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 5: MetalTireLtLoader Service Area

- **Records:** 195
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COLL_DAY` | String | TRASH_DAY | len 12 |
| `DAY_` | String |  | len 1 |
| `ZONE_` | String |  | len 1 |
| `SECTION_` | SmallInteger |  |  |
| `METAL_RT` | String |  | len 10 |
| `MTRT` | String |  | len 10 |
| `WC_RT_METL` | Integer |  |  |
| `MTHANEMPID` | String |  | len 10 |
| `TIRE_RT` | String |  | len 10 |
| `TRRT` | String |  | len 10 |
| `WC_RT_TIRE` | Integer |  |  |
| `TRHANEMPID` | String |  | len 10 |
| `LT_LDR_RT` | String |  | len 10 |
| `LLRT` | String |  | len 10 |
| `WC_RT_LLDR` | Integer |  |  |
| `LLHANEMPID` | String |  | len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 6: Leaf Service Area

- **Records:** 0
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NEIGHBORHOOD` | String |  | len 50 |
| `ST_DISTRIC` | String |  | len 15 |
| `LEAF_ZONE` | String |  | len 5 |
| `STMNTDST` | String |  | len 2 |
| `WC_Day` | String |  | len 10 |
| `WC_Zone` | SmallInteger |  |  |
| `WC_DayZone` | String | WC_Dayzone | len 50 |
| `PickupDate1` | Date |  |  |
| `PickupDate2` | Date |  |  |
| `PickupDate3` | Date |  |  |
| `PickupDate4` | Date |  |  |
| `CalendarURL` | String |  | len 255 |
| `DAY_` | String |  | len 1 |
| `Day` | String |  | **Values:** `Mon` = Monday; `Tue` = Tuesday; `Wed` = Wednesday; `Thu` = Thursday; `Fri` = Friday; `Sat` = Saturday; `Sun` = Sunday · len 50 |
| `OLD_NEIGHBORHOOD` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

