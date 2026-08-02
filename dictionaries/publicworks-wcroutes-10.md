# PublicWorks/WCRoutes_10

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/WCRoutes_10/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_WCRoutes_10
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 0: Recycle

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

## Layer 1: Bulk

- **Records:** 235
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `BULK_RT` | String |  | len 10 |
| `DAY_` | String |  | len 1 |
| `ZONE_` | String |  | len 1 |
| `SECTION_` | SmallInteger |  |  |
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
| `OBJECTID` | OID |  |  |
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 2: Container

- **Records:** 202
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CONT_RT` | String |  | len 10 |
| `DAY_` | String |  | len 1 |
| `ZONE_` | String |  | len 10 |
| `SECTION_` | String |  | len 10 |
| `WC_RT_CONT` | String |  | len 10 |
| `RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `COLL_DAY` | String |  | len 12 |
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

## Layer 3: MetalTireLtLoader

- **Records:** 195
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COLL_DAY` | String |  | len 12 |
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

## Layer 4: Trash

- **Records:** 432
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TRASH_RT` | String |  | len 10 |
| `DAY_` | String |  | len 1 |
| `SECTION_` | SmallInteger |  |  |
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

## Layer 6: Neighborhood

- **Records:** 97
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LEVEL_` | Double |  |  |
| `MSLINK_ORA` | Double |  |  |
| `ACRES` | Double |  |  |
| `PERIMETER` | Double |  |  |
| `GISADMIN_N` | String |  | len 14 |
| `LAYER` | String |  | len 32 |
| `COLOR` | Integer |  |  |
| `PRI_BOARD` | String |  | len 5 |
| `HOOD` | String |  | len 50 |
| `ABR` | String |  | len 35 |
| `PLC_BEAT` | Integer |  |  |
| `PLC_DISTR` | Integer |  |  |
| `GISADMIN_1` | Double |  |  |
| `OLD_ABR` | String |  | len 15 |
| `OLD_HOOD` | String |  | len 50 |
| `Done` | String |  | len 254 |
| `PRIBD` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GLOBALID` | String |  | len 38 |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `GlobalID_1` | GlobalID |  |  |

</details>

