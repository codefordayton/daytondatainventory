# PublicWorks/Waste_Collection_Pickup_Map_Public

> This map is used to author a map service for the Government Services Locator.

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/Waste_Collection_Pickup_Map_Public/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_Waste_Collection_Pickup_Map_Public
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Publisher description

This map is used to author a map service for the Government Services Locator.

## Layer 0: Trash Pickup

- **Records:** 220
- **Geometry:** Polygon

These districts are used to identify service area schedules for curbside trash pickup.

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `NHBHD_CODE` | String |  | len 8 |
| `PRIORTY_BD` | String |  | len 10 |
| `NHBHD_NAME` | String |  | len 50 |
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
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 7: Recycling Pickup

- **Records:** 184
- **Geometry:** Polygon

These districts are used to identify service area schedules for curbside recycling pickup.

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `NHBHD_CODE` | String |  | len 8 |
| `PRIORTY_BD` | String |  | len 10 |
| `NHBHD_NAME` | String |  | len 50 |
| `ROUTENAME` | String |  | len 10 |
| `DAY_` | String |  | len 1 |
| `ZONE_` | String |  | len 1 |
| `WC_RT_RECY` | Integer |  |  |
| `RECY_RT` | String |  | len 10 |
| `RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `RECYCLRTID` | String |  | len 10 |
| `SECTION_` | String |  | len 25 |
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
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 8: Leaf Pickup

- **Records:** 66
- **Geometry:** Polygon

These districts are used to identify service area schedules for curbside leaf pickup.

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `DayZone` | String |  | len 50 |
| `NEIGHBORHOOD` | String |  | len 50 |
| `ST_DISTRIC` | String |  | len 15 |
| `LEAF_ZONE` | String |  | len 5 |
| `STMNTDST` | String |  | len 2 |
| `LEAFZONE` | String |  | len 3 |
| `ZONE_` | String |  | len 255 |
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
| `Cal_Link` | String |  | len 150 |
| `OLD_NEIGHBORHOOD` | String |  | len 50 |
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

## Layer 10: Collection Neighborhoods

- **Records:** 66
- **Geometry:** Polygon

The location of neighborhoods.

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LAYER` | String |  | len 32 |
| `LEVEL_` | Double |  |  |
| `COLOR` | Integer |  |  |
| `MSLINK_ORA` | Double |  |  |
| `PRI_BOARD` | String |  | len 5 |
| `HOOD` | String |  | len 50 |
| `ABR` | String |  | len 35 |
| `PLC_BEAT` | Integer |  |  |
| `PLC_DISTR` | Integer |  |  |
| `ACRES` | Double |  |  |
| `PERIMETER` | Double |  |  |
| `GISADMIN_N` | String |  | len 14 |
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
| `OBJECTID` | OID |  |  |
| `GLOBALID` | String |  | len 38 |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `GlobalID_1` | GlobalID |  |  |

</details>

