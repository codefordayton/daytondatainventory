# Water/WaterDataTest

> Water Utitlites App

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Water/WaterDataTest/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Water_WaterDataTest
- **Created:** None  ·  **Item modified:** None
- **Tags:** Water

## Publisher description

Water Utitlites App

## Layer 0: Areas of Interest

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 1: Used Address

- **Records:** 163,184
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ADDRESSALPHNUM` | String |  | len 15 |
| `SUBUNIT` | String |  | len 16 |
| `USEDADDRESS` | String |  | len 50 |
| `ATLAS` | String |  | **Values:** `A` = Active or Assigned; `X` = Wrecked Address; `D` = Deleted or Expired · len 2 |
| `ADDRS_NOTE` | String |  | len 50 |
| `X_COORD` | Integer |  |  |
| `Y_COORD` | Integer |  |  |
| `ADDRKEY` | Double |  |  |
| `STNO` | String |  | len 10 |
| `PREDIR` | String |  | **Values:** `N` = North; `S` = South; `E` = East; `W` = West; `NW` = Northwest; `NE` = Northeast; `SE` = Southeast; `SW` = Southwest; `NB` = Northbound; `SB` = Southbound; `EB` = Eastbound; `WB` = Westbound · len 3 |
| `STNAME` | String |  | len 28 |
| `SUFFIX` | String |  | **Values:** `Ave` = Avenue; `Blvd` = Boulevard; `Cir` = Circle; `Ct` = Court; `Dr` = Drive; `Hwy` = Highway; `Ln` = Lane; `Loop` = Loop; `Park` = Park; `Pike` = Pike; `Pkwy` = Parkway; `Pl` = Place; …(+8 more) · len 4 |
| `POSTDIR` | String |  | **Values:** `N` = North; `S` = South; `E` = East; `W` = West; `NE` = Northeast; `NW` = Northwest; `SE` = Southeast; `SW` = Southwest · len 3 |
| `STSUB` | String |  | len 16 |
| `CITY` | String |  | len 28 |
| `STATE` | String |  | len 2 |
| `ZIP` | String |  | len 10 |
| `ST2NAME` | String |  | len 28 |
| `TAXPINNO` | String |  | len 20 |
| `K_PID` | String |  | len 20 |
| `ALTERNATEADDRESS` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `YCOORD` | Double |  |  |
| `XCOORD` | Double |  |  |
| `AddressType` | String |  | len 255 |
| `AddressUpdateHansen` | SmallInteger | Push Update to Hansen |  |
| `UsedAddressID` | Integer | Used Address ID |  |
| `BaseAddressID` | Integer | Base Address ID |  |
| `FullAddress` | String | Full Address | len 254 |
| `FullSuffix` | String |  | **Values:** `Avenue` = Avenue; `Boulevard` = Boulevard; `Circle` = Circle; `Court` = Court; `Drive` = Drive; `Highway` = Highway; `Lane` = Lane; `Loop` = Loop; `Park` = Park; `Pike` = Pike; `Parkway` = Parkway; `Place` = Place; …(+8 more) · len 50 |
| `AREAS` | String | Area | len 100 |
| `PRIMARYADDR` | String | Primary Address | len 5 |
| `LUC_Int` | Integer |  |  |
| `LUC_Description` | String |  | len 100 |
| `ZONING_CODE` | String |  | len 255 |
| `PRI_BOARDSORT` | String |  | len 255 |
| `PRI_BOARD` | String |  | len 255 |
| `HIST_DIST_CODE` | String |  | len 255 |
| `PD_District` | String |  | **Values:** `East District` = East District; `West District` = West District; `Central District` = Central District; `Dayton International Airport` = Dayton International Airport · len 50 |
| `PD_Beat` | String |  | len 50 |
| `PD_Sector` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 2: Points of Interest

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 3: Landmark Buildings

- **Records:** 71
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `ADDRESS` | String |  | len 25 |
| `LOT__` | String |  | len 10 |
| `BOOK_PAGE_` | String |  | len 25 |
| `DESCRIPTIO` | String |  | len 35 |
| `LABL` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 4: Mile Markers

- **Records:** 790
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `INTNUM` | Integer |  |  |
| `ST_NAME` | String |  | len 40 |
| `MILEMARKER` | String |  | len 20 |
| `ST_NAME2` | String |  | len 10 |
| `ADDRESS` | String |  | len 40 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 5: Bike Routes

- **Records:** 2,962
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ROADNAME` | String |  | len 254 |
| `PREFIX` | String |  | len 254 |
| `NAME` | String |  | len 254 |
| `TYPE` | String |  | len 254 |
| `SUFFIX` | String |  | len 254 |
| `FUNCCLS` | String |  | len 254 |
| `REGIONALNE` | String |  | len 254 |
| `County` | String |  | len 3 |
| `MPO` | String |  | len 1 |
| `BIKE_ROUTE` | String |  | len 1 |
| `ROUTE_TYPE` | String |  | len 10 |
| `ROUTE_DIFF` | String |  | len 10 |
| `HILL` | String |  | len 1 |
| `HILL_GRADE` | String |  | len 3 |
| `HILL_DIR` | String |  | len 10 |
| `BIKE_FACIL` | String |  | len 1 |
| `FACIL_TYPE` | String |  | len 20 |
| `ST_LABEL` | String |  | len 1 |
| `DAYTON` | String |  | len 1 |
| `MILES` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 6: Truck Routes

- **Records:** 354
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `sde_base_GISADMIN_pwTruckRoutes` | String | sde_base.GISADMIN.pwTruckRoutes.Entity | len 16 |
| `Layer` | String |  | len 255 |
| `Level_` | Integer |  |  |
| `Color` | Integer |  |  |
| `Linetype` | String |  | len 255 |
| `Text_` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 8: Parcel Dimensions - Annotation Labels

- **Records:** 865,084
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FeatureID` | Integer |  |  |
| `ZOrder` | Integer |  |  |
| `AnnotationClassID` | Integer |  |  |
| `SymbolID` | Integer |  |  |
| `Status` | SmallInteger |  | **Values:** `0` = Placed; `1` = Unplaced |
| `TextString` | String |  | len 255 |
| `FontName` | String |  | len 255 |
| `FontSize` | Double |  |  |
| `Bold` | SmallInteger |  | **Values:** `1` = Yes; `0` = No |
| `Italic` | SmallInteger |  | **Values:** `1` = Yes; `0` = No |
| `Underline` | SmallInteger |  | **Values:** `1` = Yes; `0` = No |
| `VerticalAlignment` | SmallInteger |  | **Values:** `0` = Top; `1` = Center; `2` = Baseline; `3` = Bottom |
| `HorizontalAlignment` | SmallInteger |  | **Values:** `0` = Left; `1` = Center; `2` = Right; `3` = Full |
| `XOffset` | Double |  |  |
| `YOffset` | Double |  |  |
| `Angle` | Double |  |  |
| `FontLeading` | Double |  |  |
| `WordSpacing` | Double |  |  |
| `CharacterWidth` | Double |  |  |
| `CharacterSpacing` | Double |  |  |
| `FlipAngle` | Double |  |  |
| `Override` | Integer |  |  |
| `PARDIM_` | Integer |  |  |
| `PARDIM_ID` | Integer |  |  |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `OFFSETX` | Double |  |  |
| `OFFSETY` | Double |  |  |
| `HEIGHT` | Double |  |  |
| `SYMBOL` | Integer |  |  |
| `LEVEL_` | Integer |  |  |
| `TEXT` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 171: Dim

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 172: Utilities

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 173: Fiber Optics

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 174: Traffic Signals

- **Records:** 426
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ts_num` | SmallInteger |  |  |
| `text_` | String |  | len 6 |
| `TStype` | String |  | **Values:** `F` = F; `I` = I; `S` = S; `T` = T; `T-P` = T-P; `T-S` = T-S; `T-P-S` = T-P-S; `R-F` = R-F; `R-I` = R-I; `R-RA` = R-RA; `R-S` = R-S; `R-T` = R-T; …(+1 more) · len 5 |
| `Street1` | String |  | len 20 |
| `Street2` | String |  | len 20 |
| `Street3` | String |  | len 20 |
| `Street4` | String |  | len 20 |
| `controller` | String |  | len 10 |
| `ip` | String |  | len 15 |
| `ring` | Integer |  |  |
| `luminaires` | SmallInteger |  |  |
| `LED_lumins` | String |  | len 5 |
| `cntdn_peds` | String |  | len 5 |
| `UPS` | String |  | **Values:** `Y` = Y; `N` = N · len 1 |
| `UPS_date` | Date |  |  |
| `batt_date` | Date |  |  |
| `rbattmangr` | String |  | **Values:** `Y` = Y; `N` = N · len 1 |
| `invrtr_ip` | String |  | len 15 |
| `rbms_ip` | String |  | len 15 |
| `admitdelta` | SmallInteger |  |  |
| `admit_date` | Date |  |  |
| `Status` | String |  | **Values:** `ACTIVE` = ACTIVE; `INACTIVE` = INACTIVE · len 255 |
| `POINT_X` | Double |  |  |
| `POINT_Y` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `Comments` | String |  | len 255 |
| `admit1` | Integer |  |  |
| `admit2` | Integer |  |  |
| `admit3` | Integer |  |  |
| `admit4` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 175: Fiber End-Points

- **Records:** 91
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `fac_type` | String |  | len 50 |
| `fac_name` | String |  | len 50 |
| `IT_rings` | String |  | len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 176: Fiber Lines

- **Records:** 247
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Layer` | String |  | len 255 |
| `Level_` | Integer |  |  |
| `Color` | Integer |  |  |
| `Linetype` | String |  | len 255 |
| `Text_` | String |  | len 255 |
| `Broadband_Status` | String |  | len 50 |
| `fibercount` | SmallInteger |  |  |
| `aerial` | String |  | len 10 |
| `IT_rings` | String |  | len 10 |
| `SDE_Publish_GISADMIN_pwOptics_E` | String | SDE_Publish.GISADMIN.pwOptics.Entity | len 16 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 177: Fiber Poles

- **Records:** 14
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 178: Union Rd Wellfield

- **Records:** 2
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PIN` | String |  | len 30 |
| `X` | Double | X Coordinate |  |
| `Y` | Double | Y Coordinate |  |
| `ACRES` | Double | Acres |  |
| `TAXID` | String | TAX ID | len 5 |
| `BLOCKNUM` | String | Block Number | len 5 |
| `TransCard` | String | Transaction Card | len 30 |
| `TaxMail1` | String | Tax Mail 1 | len 50 |
| `TaxMail3` | String | Tax Mail 3 | len 50 |
| `Address1` | String | Address 1 | len 50 |
| `Address3` | String | Address 3 | len 50 |
| `OWNER1` | String | Owner | len 40 |
| `ADDRESSUNI` | String | Address Unit | len 40 |
| `DWELPICS` | String | Images | len 30 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 179: Well Fields

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 180: Well Head Operation Areas

- **Records:** 12
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `AREAID` | String | Area Identifier | len 50 |
| `AREANAME` | String | Area Name | len 100 |
| `AREATYPE` | String | Area Type | **Values:** `Administrative Area` = Administrative Area; `Engineering District` = Engineering District; `Inspection Area` = Inspection Area; `Maintenance Area` = Maintenance Area; `Wellfield Operation Area` = Wellfield Operation Area; `Water Operations Area` = Water Operations Area; `Water Resource Area` = Water Resource Area; `Water Protection District` = Water Protection District · len 50 |
| `PERSON` | String | Contact Person | len 100 |
| `DESCRIP` | String | Description | len 255 |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 181: Water Protection District

- **Records:** 12
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `AREAID` | String | Area ID | len 50 |
| `AREANAME` | String | Area Name | len 100 |
| `AREATYPE` | String | Area Type | **Values:** `Administrative Area` = Administrative Area; `Engineering District` = Engineering District; `Inspection Area` = Inspection Area; `Maintenance Area` = Maintenance Area; `Wellfield Operation Area` = Wellfield Operation Area; `Water Operations Area` = Water Operations Area; `Water Resource Area` = Water Resource Area; `Water Protection District` = Water Protection District · len 50 |
| `DESCRIP` | String | Description | len 255 |
| `LASTUPDATE` | Date | Last Update Date |  |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GlobalID` | GlobalID |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 182: Water Resources

- **Records:** 1
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `AREAID` | String | Area ID | len 50 |
| `AREANAME` | String | Area Name | len 100 |
| `AREATYPE` | String | Area Type | **Values:** `Administrative Area` = Administrative Area; `Engineering District` = Engineering District; `Inspection Area` = Inspection Area; `Maintenance Area` = Maintenance Area; `Wellfield Operation Area` = Wellfield Operation Area; `Water Operations Area` = Water Operations Area; `Water Resource Area` = Water Resource Area; `Water Protection District` = Water Protection District · len 50 |
| `DESCRIP` | String | Description | len 255 |
| `LASTUPDATE` | Date | Last Update Date |  |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GlobalID` | GlobalID |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 183: Impervious Areas

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 184: Centroid

- **Records:** 88,071
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COLOR` | Integer | Color |  |
| `MSFEATURE` | Double | MS Feature |  |
| `MSFENTITY` | Double | MS Entity 1 |  |
| `MSLINK` | Double | MS Link |  |
| `MSENTITY` | Double | MS Entity 2 |  |
| `DISTRICT` | String | Tax District | len 4 |
| `BOOK` | Integer | Tax Book |  |
| `PAGE_NUM` | SmallInteger | Tax Page |  |
| `P_SUFFIX` | String | Tax Suffix | len 1 |
| `P_INDEX` | Integer | Tax Index |  |
| `TOTAL_AREA` | Double | Total Area |  |
| `RES_SAMPLE` | SmallInteger |  |  |
| `CLASS_CODE` | String | Class Code | len 1 |
| `USE_CODE` | String | Use Code | len 3 |
| `MAPID` | String | Map ID | len 3 |
| `X_COORD` | Double | X Coordinate |  |
| `Y_COORD` | Double | Y Coordinate |  |
| `KEY_PARCEL` | String | Key Parcel | len 20 |
| `SPECIAL` | Integer | Special |  |
| `ORPHAN_REC` | Integer | Orphan Record |  |
| `OWNER` | String | Owner | len 56 |
| `LO_ADDR` | String | Low Address | len 30 |
| `HI_ADDR` | String | High Address | len 6 |
| `ST_DIR` | String | Street Direction | len 1 |
| `ST_NAME` | String | Street Name | len 22 |
| `ST_TYPE` | String | Street Type | len 2 |
| `ACCT_NUMBE` | String | Account Number | len 10 |
| `CNTY_ACCT_` | String | County Account | len 10 |
| `ACCT_TYPE` | String | Account Type | len 2 |
| `BOOK_ROUTE` | String | Book Route | len 6 |
| `ST_SEQUENC` | String | Street Sequence | len 4 |
| `SERVICE_CI` | String | Service CI | len 2 |
| `ORIGIN_FLA` | String | Origin FLA | len 1 |
| `LOT_NUM` | String | Lot Number | len 26 |
| `B_NAME1` | String | B Name 1 | len 32 |
| `B_NAME2` | String | B Name 2 | len 32 |
| `B_P_I` | String | BPI | len 11 |
| `TOTAL_BILL` | Double | Total Bill |  |
| `IMG` | String | Image | len 15 |
| `EXT` | String |  | len 3 |
| `FULLPATH` | String | Full Path | len 30 |
| `PARCEL_ID` | String | Parcel ID | len 16 |
| `RAZED` | String | Razed | len 2 |
| `COMMENTS` | String | Comments | len 56 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 185: Centroid Hooks

- **Records:** 18,155
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LAYER` | String | Layer | len 32 |
| `COLOR` | Integer | Color |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 186: Impervious Area

- **Records:** 8,032
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COLOR` | Integer | Color |  |
| `COMMENTS` | String | Comments | len 56 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 188: Water

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 189: Water Hydrants

- **Records:** 6,099
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Hydrant ID | len 16 |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `LASTSERVICE` | Date | Last Service Date |  |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `FLOW` | Double | Flow Rate (GPM) |  |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `AUXVALVE` | String | Aux Valve | len 1 |
| `BARRELSIZE` | Double | Barrel Size |  |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FEEDERDIAM` | Double | Feeder Diameter |  |
| `FEEDERLEN` | Double | Feeder Length |  |
| `FEEDERTYPE` | String | Feeder Type | **Values:** `0` = No Code · len 6 |
| `HT` | Double | Height |  |
| `INTKEY` | Integer | Intersection |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OUTLSZ1` | Double | Size of Outlet1 |  |
| `OUTLSZ2` | Double | Size of Outlet2 |  |
| `OUTLSZ3` | Double | Size of Outlet3 |  |
| `OUTLSZ4` | Double | Size of Outlet4 |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PACKING` | String | Packing | **Values:** `0` = No Code · len 4 |
| `PAINTTYPE` | String | Paint Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 8 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `WVKEY` | Integer | Valve |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `COLOR` | String | Paint Color | **Values:** `BLUE` = BLUE - LOW; `GREEN` = GREEN - HIGH; `ORANGE` = ORANGE - MEDIUM · len 8 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `INSPECTIONGROUP` | String |  | len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `ADDRESS` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 190: Water Meters

- **Records:** 69,020
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ACCOUNT_NU` | Double |  |  |
| `TAXPINNO` | String |  | len 254 |
| `ACCOUNT__1` | Integer |  |  |
| `STREET_NUM` | Integer |  |  |
| `DIRECTION` | String |  | len 254 |
| `STREET_NAM` | String |  | len 254 |
| `USEDADDRES` | String |  | len 254 |
| `ACCOUNT_ST` | String |  | len 254 |
| `CITY_ID` | Integer |  |  |
| `CATEGORY_C` | String |  | len 254 |
| `LOT_NUMBER` | String |  | len 254 |
| `CLASS_CODE` | String |  | len 254 |
| `USE_CODE` | String |  | len 254 |
| `BANKRUPTCY` | String |  | len 254 |
| `BILLING_TY` | String |  | len 254 |
| `CASH_ONLY_` | String |  | len 254 |
| `PAYMENT_PL` | String |  | len 254 |
| `CASUAL_ACC` | String |  | len 254 |
| `Y` | Double |  |  |
| `X` | Double |  |  |
| `LATITUDE` | Double |  |  |
| `LONGITUDE` | Double |  |  |
| `DATE_CREAT` | String |  | len 254 |
| `TOTAL_IMPE` | String |  | len 254 |
| `IMPERVIOUS` | String |  | len 254 |
| `CERTIFIABL` | String |  | len 254 |
| `FIXED_INCO` | String |  | len 254 |
| `SPECIAL_AC` | String |  | len 254 |
| `BOD_SS_FLA` | String |  | len 254 |
| `FLAT_ACCOU` | String |  | len 254 |
| `BILLING_PE` | String |  | len 254 |
| `BPI_DISTRI` | String |  | len 254 |
| `BPI_BOOK` | String |  | len 254 |
| `BPI_PAGE` | String |  | len 254 |
| `BPI_SUFFIX` | String |  | len 254 |
| `BPI_INDEX` | String |  | len 254 |
| `WAT_ENG_DI` | String |  | len 254 |
| `BILL_AMOUN` | Double |  |  |
| `PPLAN_PERM` | String |  | len 254 |
| `METER_NO` | Integer |  |  |
| `METER_MAKE` | String |  | len 254 |
| `USAGE_INDI` | String |  | len 254 |
| `NO_OF_HYDR` | String |  | len 254 |
| `FIRE_LINE_` | String |  | len 254 |
| `NO_OF_PRIV` | String |  | len 254 |
| `SENIOR_CIT` | String |  | len 254 |
| `DISABLD` | String |  | len 254 |
| `RESIDENT_O` | String |  | len 254 |
| `NO_OF_CONS` | Integer |  |  |
| `INCLUDE_IN` | String |  | len 254 |
| `SHUT_OFF_D` | String |  | len 254 |
| `LEGAL_ACTI` | String |  | len 254 |
| `BOARD_OF_R` | String |  | len 254 |
| `NET_BALANC` | Double |  |  |
| `FORD_OR_LA` | String |  | len 254 |
| `READ_SEQUE` | String |  | len 254 |
| `HI_LIMIT` | String |  | len 254 |
| `LO_LIMIT` | String |  | len 254 |
| `BILLING_DI` | String |  | len 254 |
| `ACTION_TAK` | Integer |  |  |
| `ROUTE_NUMB` | Integer |  |  |
| `COL_AGENCY` | String |  | len 254 |
| `DEPOSIT_BA` | String |  | len 254 |
| `NET_ONLY_F` | String |  | len 254 |
| `NO_READ_ID` | String |  | len 254 |
| `ACTUAL_SHU` | String |  | len 254 |
| `ALLOCATION` | String |  | len 254 |
| `SHUT_OFF_R` | String |  | len 254 |
| `DEPOSIT_PA` | String |  | len 254 |
| `RESI_NON_R` | String |  | len 254 |
| `OPEN_WORK_` | String |  | len 254 |
| `FPU_CODE` | String |  | len 254 |
| `COUNTY_ACC` | String |  | len 254 |
| `NO_OF_BAD_` | String |  | len 254 |
| `BACK_FLOW_` | String |  | len 254 |
| `TOUCH_PAD_` | String |  | len 254 |
| `OLD_REMOTE` | String |  | len 254 |
| `LARGE_METE` | String |  | len 254 |
| `BAD_CHECK_` | String |  | len 254 |
| `DELQ_BALAN` | Double |  |  |
| `MASTER_MET` | String |  | len 254 |
| `PREVIOUS_M` | String |  | len 254 |
| `PREVIOUS_1` | String |  | len 254 |
| `BILLDATE_C` | Integer |  |  |
| `STORM_LEVE` | Integer |  |  |
| `EPAYMENT_I` | String |  | len 254 |
| `EPAYMENT_1` | String |  | len 254 |
| `BYPASS_FLA` | String |  | len 254 |
| `PRINT_SURP` | String |  | len 254 |
| `NO_OF_BROK` | Integer |  |  |
| `SPECIAL_MO` | Integer |  |  |
| `PROPERTY_S` | Integer |  |  |
| `PROPERTY_1` | String |  | len 254 |
| `Geometry` | String |  | len 254 |
| `COMMENTS` | String |  | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `Test` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 191: Water Pumps

- **Records:** 213
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Pump ID | len 20 |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `PUMPTYPE` | String | Pump Type | **Values:** `Axial Flow` = Axial Flow; `Centrifugal` = Centrifugal; `Jet` = Jet; `Reciprocating` = Reciprocating; `Rotary` = Rotary; `Turbine` = Turbine; `Other` = Other; `Unknown` = Unknown · len 50 |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `ELEVATION` | Double | Elevation |  |
| `INLETDIAM` | Double | Inlet Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `DISCHDIAM` | Double | Discharge Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `RATEDFLOW` | String | Rated Flow | len 20 |
| `RATEDPRESS` | String | Rated Pressure | len 20 |
| `DYNHEAD` | String | Total Dynamic Head | len 20 |
| `SHUTHEAD` | Double | Shutoff Head |  |
| `DESHEAD` | Double | Design Head |  |
| `MAXOPHEAD` | Double | Max Operating Head |  |
| `NAME` | String | Name | len 50 |
| `DESIGNGPM` | Double | Design GPM |  |
| `MAXOPDISC` | Double | Max Operating Discharge |  |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `AVGMONUSG` | Double | Average Monthly Usage |  |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FLOW` | Double | Flow |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `MOSERNO` | String | Motor Serial # | len 20 |
| `PMRPM` | String | RPM's | len 7 |
| `PRCLKEY` | Integer | Parcel |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `PUMPTRIM` | String | Trim | len 6 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SITEKEY` | Integer | Site |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `USGDATE` | Date |  |  |
| `USGTOT` | Double | Usage Total |  |
| `WSRCKEY` | Integer |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 192: Curb Stop Valves

- **Records:** 4,825
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DIR` | String | Direction To Open | len 1 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `ELEV` | Double | Elevation |  |
| `HIGHPRES` | Double | High Pressure |  |
| `INTKEY` | Integer | Intersection |  |
| `LOWPRES` | Double | Low Pressure |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Mufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 244: Hydrant Valves

- **Records:** 6,639
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `Ball` = Ball; `Butterfly` = Butterfly; `Cone` = Cone; `Gate` = Gate; `Plug` = Plug; `Roundway` = Roundway; `Other` = Other; `Unknown` = Unknown · len 30 |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `HYDRFLAG` | SmallInteger | Hydrant Valve | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `LASTUPDATE` | Date | LastUpdate |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `ELEV` | Double | Elevation |  |
| `HIGHPRES` | Double | High Pressure |  |
| `INTKEY` | Integer | Intersection |  |
| `LOWPRES` | Double | Low Pressure |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Mufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `OLD_AREAS` | String |  | len 50 |
| `ValveCriticallity` | String |  | **Values:** `1` = Critical (Transmission Main Valves 16” and Larger) Exercise annually; `2` = Critical (Hospitals, nursing homes, schools etc.) Exercise annually; `3` = Non-Critical (12” through 4” normal system valves) Exercise on 5 year cycle · len 50 |
| `UtilNetFlag` | String |  | len 255 |
| `Recommendation` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 193: Water Control Valves

- **Records:** 203
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DIR` | String | Direction To Open | len 1 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `ELEV` | Double | Elevation |  |
| `HIGHPRES` | Double | High Pressure |  |
| `INTKEY` | Integer | Intersection |  |
| `LOWPRES` | Double | Low Pressure |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Mufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `UNITTYPE` | String |  | len 6 |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `OLD_AREAS` | String |  | len 50 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 194: Water System Valves

- **Records:** 16,291
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `Ball` = Ball; `Butterfly` = Butterfly; `Cone` = Cone; `Gate` = Gate; `Plug` = Plug; `Roundway` = Roundway; `Other` = Other; `Unknown` = Unknown · len 30 |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `HYDRFLAG` | SmallInteger | Hydrant Valve | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `LASTUPDATE` | Date | LastUpdate |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `ELEV` | Double | Elevation |  |
| `HIGHPRES` | Double | High Pressure |  |
| `INTKEY` | Integer | Intersection |  |
| `LOWPRES` | Double | Low Pressure |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Mufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `OLD_AREAS` | String |  | len 50 |
| `ValveCriticallity` | String |  | **Values:** `1` = Critical (Transmission Main Valves 16” and Larger) Exercise annually; `2` = Critical (Hospitals, nursing homes, schools etc.) Exercise annually; `3` = Non-Critical (12” through 4” normal system valves) Exercise on 5 year cycle · len 50 |
| `UtilNetFlag` | String |  | len 255 |
| `Recommendation` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 195: Production Wells

- **Records:** 114
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NAME` | String | Name | len 20 |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Well ID | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STANDWAT` | Double | Std Water Level |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `WELLDPTH` | Double | Well Depth |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `CAPUM` | String | Capacity Units | len 4 |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `HT` | Double | Height |  |
| `MODELNO` | String | Model # | len 20 |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SITEKEY` | Integer | Site |  |
| `SUDESC` | String | Storage Unit Description | len 30 |
| `THICKNESS_1` | Double | Thickness |  |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `WATLEV` | Double | Water Level |  |
| `WLEVUM` | String | Water Level Units | len 4 |
| `TWC_EL` | Double |  |  |
| `SURF_EL` | Double |  |  |
| `SCREEN` | String |  | len 254 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 196: Flow Meters

- **Records:** 75
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NAME` | String | Name | len 20 |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Well ID | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STANDWAT` | Double | Std Water Level |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `WELLDPTH` | Double | Well Depth |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `CAPUM` | String | Capacity Units | len 4 |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `HT` | Double | Height |  |
| `MODELNO` | String | Model # | len 20 |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SITEKEY` | Integer | Site |  |
| `SUDESC` | String | Storage Unit Description | len 30 |
| `THICKNESS_1` | Double | Thickness |  |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `WATLEV` | Double | Water Level |  |
| `WLEVUM` | String | Water Level Units | len 4 |
| `TWC_EL` | Double |  |  |
| `SURF_EL` | Double |  |  |
| `SCREEN` | String |  | len 254 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 197: Enclosed Storage Facilities

- **Records:** 14
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NAME` | String | Name | len 20 |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Well ID | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STANDWAT` | Double | Std Water Level |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `WELLDPTH` | Double | Well Depth |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `CAPUM` | String | Capacity Units | len 4 |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `HT` | Double | Height |  |
| `MODELNO` | String | Model # | len 20 |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SITEKEY` | Integer | Site |  |
| `SUDESC` | String | Storage Unit Description | len 30 |
| `THICKNESS_1` | Double | Thickness |  |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `WATLEV` | Double | Water Level |  |
| `WLEVUM` | String | Water Level Units | len 4 |
| `TWC_EL` | Double |  |  |
| `SURF_EL` | Double |  |  |
| `SCREEN` | String |  | len 254 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 198: Investigation Wells

- **Records:** 458
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NAME` | String | Name | len 20 |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Well ID | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STANDWAT` | Double | Std Water Level |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `WELLDPTH` | Double | Well Depth |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `CAPUM` | String | Capacity Units | len 4 |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `HT` | Double | Height |  |
| `MODELNO` | String | Model # | len 20 |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SITEKEY` | Integer | Site |  |
| `SUDESC` | String | Storage Unit Description | len 30 |
| `THICKNESS_1` | Double | Thickness |  |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `WATLEV` | Double | Water Level |  |
| `WLEVUM` | String | Water Level Units | len 4 |
| `TWC_EL` | Double |  |  |
| `SURF_EL` | Double |  |  |
| `SCREEN` | String |  | len 254 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 199: Early Warning Wells

- **Records:** 173
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NAME` | String | Name | len 20 |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Well ID | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STANDWAT` | Double | Std Water Level |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `WELLDPTH` | Double | Well Depth |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `CAPUM` | String | Capacity Units | len 4 |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `HT` | Double | Height |  |
| `MODELNO` | String | Model # | len 20 |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SITEKEY` | Integer | Site |  |
| `SUDESC` | String | Storage Unit Description | len 30 |
| `THICKNESS_1` | Double | Thickness |  |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `WATLEV` | Double | Water Level |  |
| `WLEVUM` | String | Water Level Units | len 4 |
| `TWC_EL` | Double |  |  |
| `SURF_EL` | Double |  |  |
| `SCREEN` | String |  | len 254 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 200: Water Fittings

- **Records:** 39,221
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Fitting ID | len 16 |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `FITTINGTYPE` | String | Fitting Type | **Values:** `ANGLE` = < 45 DEGREE BEND; `ENDPT` = END POINT/PLUG; `JNT-T` = T-JOINT; `JNT-X` = CROSS JOINT; `VLV` = VALVE; `RED` = REDUCER; `45` = 45 DEGREE BEND; `90` = 90 DEGREE BEND; `SRV` = LARGE SERVICE LINE NODE; `JUNC` = JUNCTION CHAMBER; `PLUG` = MAIN LINE PLUG; `COUPLING` = COUPLING; …(+9 more) · len 50 |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Fitting ID | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTFRND` | Double | Node Location |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FRND` | String | From Node | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `INTKEY` | Integer | Intersection |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `PRCLKEY` | Integer | Parcel |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 201: Water Hydrant Laterals

- **Records:** 6,645
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `LINETYPE` | String | Line Type | **Values:** `Hydrant` = Hydrant; `Irrigation` = Irrigation; `Other` = Other; `Unknown` = Unknown; `Domestic` = Domestic; `Fire` = Fire; `Industrial` = Industrial; `Commercial` = Commercial · len 30 |
| `LOCDESC` | String | Location Description | len 50 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Service Line ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `BLDGKEY` | Integer | Building |  |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRITSRV` | String | Critical Service | **Values:** `ADULT` = ANY AGES ADULT DAY CARE; `ALTA` = ALTA NURSING HOME; `CATMAN` = CATALPA MANOR NURSING CENTER; `DHEALT` = DAYTON HEALTH CARE CENTER; `EASTMAN` = EASTVIEW MANOR RESIDENTIAL CTR; `FORVIEW` = FOREST VIEW NURSING CENTER; `GOODSM` = GOOD SAMARITAN HOSP. & TRAUMA; `GRAFT` = GRAFTON OAKS NURSING CENTER; `GRNDVW` = GRANDVIEW HOSPITAL; `GRNHLT` = GRANDVIEW HEALTH CARE CENTER; `LOVCAR` = LOVING CARE NURSING CENTER; `MAPLE` = MAPLEVIEW MANOR; …(+7 more) · len 9 |
| `CURBSTOP` | String | Curb Stop Location | len 254 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `EPAID` | String | EPA ID # | len 12 |
| `FIRELINE` | String | Fire Line | len 1 |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `NPDESID` | String | NPDES # | len 12 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SIC` | String |  | len 4 |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `TAPLOC` | String | Water Tap Location | len 254 |
| `UICID` | String | UIC ID # | len 14 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `PITCHERGIVEN` | String | Pitcher Given | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |
| `LEN_1` | Double | sde.GISADMIN.wLateralLine.LEN |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `PRVT_MATERIAL` | String | Private Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 255 |
| `GISADMIN.wLateralLine.LEN` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 202: Water Services

- **Records:** 59,203
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `LINETYPE` | String | Line Type | **Values:** `Hydrant` = Hydrant; `Irrigation` = Irrigation; `Other` = Other; `Unknown` = Unknown; `Domestic` = Domestic; `Fire` = Fire; `Industrial` = Industrial; `Commercial` = Commercial · len 30 |
| `LOCDESC` | String | Location Description | len 50 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Service Line ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `BLDGKEY` | Integer | Building |  |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRITSRV` | String | Critical Service | **Values:** `ADULT` = ANY AGES ADULT DAY CARE; `ALTA` = ALTA NURSING HOME; `CATMAN` = CATALPA MANOR NURSING CENTER; `DHEALT` = DAYTON HEALTH CARE CENTER; `EASTMAN` = EASTVIEW MANOR RESIDENTIAL CTR; `FORVIEW` = FOREST VIEW NURSING CENTER; `GOODSM` = GOOD SAMARITAN HOSP. & TRAUMA; `GRAFT` = GRAFTON OAKS NURSING CENTER; `GRNDVW` = GRANDVIEW HOSPITAL; `GRNHLT` = GRANDVIEW HEALTH CARE CENTER; `LOVCAR` = LOVING CARE NURSING CENTER; `MAPLE` = MAPLEVIEW MANOR; …(+7 more) · len 9 |
| `CURBSTOP` | String | Curb Stop Location | len 254 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `EPAID` | String | EPA ID # | len 12 |
| `FIRELINE` | String | Fire Line | len 1 |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `NPDESID` | String | NPDES # | len 12 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SIC` | String |  | len 4 |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `TAPLOC` | String | Water Tap Location | len 254 |
| `UICID` | String | UIC ID # | len 14 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `PITCHERGIVEN` | String | Pitcher Given | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |
| `LEN_1` | Double | sde.GISADMIN.wLateralLine.LEN |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `PRVT_MATERIAL` | String | Private Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 255 |
| `GISADMIN.wLateralLine.LEN` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 203: Distribution Water Main

- **Records:** 51,265
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `UNITID` | String | Main ID 1 | len 20 |
| `UNITID2` | String | Main ID 2 | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CORRFACTOR` | Double | Corrosion Factor |  |
| `DIRFRNODE1` | String | Dir From Endpoint1 | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRNODE2` | String | Dir From Endpoint2 | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DPTH` | Double | Depth |  |
| `FFACTOR` | Double | Friction Factor |  |
| `FROSTDPTH` | Double | Frost Depth |  |
| `GAUGE` | String | Gauge | len 2 |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `LOCATOR` | String | Locator Wire | len 1 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SCHED` | String | Pipe Schedule | len 3 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SOILTYPE` | String | Soil Type | **Values:** `CLAY` = CLAY; `HDPN` = HARD PAN; `RKCL` = ROCK AND CLAY; `ROCK` = ROCKS; `SAND` = SAND; `SGRA` = SAND/GRAVEL; `SHAL` = SHALE; `COR` = CORROSIVE; `CRST` = CRUSHED STONE; `PIT` = PIT RUN; `PITC` = PIT RUN AND CLAY · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CLASS` | String | Pipe Class | **Values:** `51` = CLASS 51; `53` = CLASS 53 · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 243: Transmission Water Main

- **Records:** 5,980
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `UNITID` | String | Main ID 1 | len 20 |
| `UNITID2` | String | Main ID 2 | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CORRFACTOR` | Double | Corrosion Factor |  |
| `DIRFRNODE1` | String | Dir From Endpoint1 | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRNODE2` | String | Dir From Endpoint2 | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DPTH` | Double | Depth |  |
| `FFACTOR` | Double | Friction Factor |  |
| `FROSTDPTH` | Double | Frost Depth |  |
| `GAUGE` | String | Gauge | len 2 |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `LOCATOR` | String | Locator Wire | len 1 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SCHED` | String | Pipe Schedule | len 3 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SOILTYPE` | String | Soil Type | **Values:** `CLAY` = CLAY; `HDPN` = HARD PAN; `RKCL` = ROCK AND CLAY; `ROCK` = ROCKS; `SAND` = SAND; `SGRA` = SAND/GRAVEL; `SHAL` = SHALE; `COR` = CORROSIVE; `CRST` = CRUSHED STONE; `PIT` = PIT RUN; `PITC` = PIT RUN AND CLAY · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CLASS` | String | Pipe Class | **Values:** `51` = CLASS 51; `53` = CLASS 53 · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 204: Intersection Bubble

- **Records:** 4,729
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `STREET1` | String | Street 1 | len 30 |
| `STREET2` | String | Street 2 | len 30 |
| `STREET3` | String | Street 3 | len 20 |
| `STREET4` | String | Street 4 | len 20 |
| `STREET5` | String | Street 5 | len 20 |
| `DWG` | String | Drawing ID | len 8 |
| `FULLPATH` | String | Link Path | len 64 |
| `EXT` | String | File Type | len 3 |
| `ATLAS` | String | Atlas | len 3 |
| `PLANIMET` | String | Planimetric | len 10 |
| `MSLINK` | Integer | MS Link |  |
| `XCOORDINAT` | String | X Coordinate | len 40 |
| `YCOORDINAT` | String | Y Coordinate | len 40 |
| `WEBPATH` | String | Web Path | len 150 |
| `LASTUPDATE` | Date | Last Update |  |
| `MOBILEPATH` | String | Mobile Path | len 150 |
| `DMSLINK` | String | DMS Link | len 150 |
| `PortalLink` | String | Portal Link | len 400 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `TempWebLink` | String |  | len 150 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_12` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 205: Water Pressure Zones

- **Records:** 14
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ZONEID` | String | Pressure Zone Identifier | len 3 |
| `ZONENAME` | String | Pressure Zone Name | len 3 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `GlobalID` | GlobalID |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 208: Atlas Grid

- **Records:** 511
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TEXT_1` | String | Atlas Number | len 254 |
| `WEBPATH` | String | Web Path | len 100 |
| `FULLPATH` | String | Full Path | len 75 |
| `EXT` | String | File Type | len 4 |
| `SANAPATH` | String | Sanitary Path | len 200 |
| `DOCPATH` | String | Doc Path | len 254 |
| `VERSIONNAM` | String |  | len 50 |
| `WTRPATH` | String | Water Path | len 200 |
| `MBLSANPATH` | String | Mobile Sanitary Path | len 100 |
| `MBLSTMPATH` | String | Mobile Storm Path | len 70 |
| `MBLWTRPATH` | String | Mobile Water Path | len 70 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 209: Survey Data

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 210: Survey Control High

- **Records:** 1,180
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PID` | String |  | len 50 |
| `CODBMID` | Double |  |  |
| `DISPLAYNAM` | String |  | len 254 |
| `STAMPEDNAM` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `OBJECTID` | OID |  |  |

</details>

## Layer 211: Survey Control Low

- **Records:** 1,180
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PID` | String |  | len 50 |
| `CODBMID` | Double |  |  |
| `DISPLAYNAM` | String |  | len 254 |
| `STAMPEDNAM` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `OBJECTID` | OID |  |  |

</details>

## Layer 212: Survey Control - '88 Elevations

- **Records:** 1,180
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PID` | String |  | len 50 |
| `CODBMID` | Double |  |  |
| `DISPLAYNAM` | String |  | len 254 |
| `STAMPEDNAM` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `OBJECTID` | OID |  |  |

</details>

## Layer 213: Survey Project

- **Records:** 342
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `JOBNUMBER` | String | Job Number | len 50 |
| `SURVEYYEAR` | SmallInteger | Survey Year |  |
| `COMMENTS` | String | Comments | len 255 |
| `PWJOB` | SmallInteger | Public Works Job |  |
| `FILEPATH` | String | File Path | len 1073741822 |
| `PDFPATH` | String | PDF Path | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 214: Completed Level Circuits

- **Records:** 203
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COLOR` | Integer |  |  |
| `LINETYPE` | String |  | len 254 |
| `COMPLETED` | String |  | len 2 |
| `LINEDESC` | String | Line Description | len 100 |
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

## Layer 215: Proposed Level Circuits

- **Records:** 56
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COLOR` | Integer |  |  |
| `LINETYPE` | String |  | len 254 |
| `COMPLETED` | String |  | len 2 |
| `LINEDESC` | String | Line Description | len 100 |
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

## Layer 219: Recorded Plat

- **Records:** 10,688
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ACAD_COLOR` | SmallInteger |  |  |
| `SUBNAME` | String |  | len 75 |
| `REC_BOOK` | String |  | len 20 |
| `PLAT_BK` | String |  | len 20 |
| `DIRECTORY` | String |  | len 15 |
| `REC_PLATBK` | String |  | len 20 |
| `HOT_LINK` | String |  | len 100 |
| `WEB_RECPLAT_LINK` | String |  | len 100 |
| `S_DATE` | String |  | len 8 |
| `L_DATE` | String |  | len 10 |
| `GIS_RP_NBR` | Double |  |  |
| `JA_JOIN` | Double |  |  |
| `J_AREA` | String |  | len 50 |
| `CREATE_FLG` | String |  | len 1 |
| `CREATE_OPER` | String |  | len 3 |
| `CREATE_DATE` | String |  | len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 220: Administrative Boundaries

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 221: Building Footprint

- **Records:** 338,321
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NUMSTORIES` | Integer |  |  |
| `BLDGHEIGHT` | Integer |  |  |
| `TYPE` | Integer |  |  |
| `CTYSTRUCT` | String |  | len 20 |
| `SOURCE` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `Shape_Leng` | Double |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 222: CDBG Eligible

- **Records:** 139
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TRAC_BLKG` | String |  | len 254 |
| `CNT_TRAC_B` | Integer |  |  |
| `OID_` | Integer |  |  |
| `CDBGUOGID` | String |  | len 12 |
| `CDBGNAME` | String |  | len 11 |
| `CDBGTYPE` | String |  | len 11 |
| `STUSAB` | String |  | len 8 |
| `LOGRECNO` | String |  | len 11 |
| `STATE` | String |  | len 7 |
| `COUNTY` | String |  | len 8 |
| `COUNTYNAME` | String |  | len 14 |
| `COUSUB` | String |  | len 9 |
| `COUSUBNAME` | String |  | len 14 |
| `PLACE` | String |  | len 7 |
| `PLACENAME` | String |  | len 12 |
| `TRACT` | String |  | len 7 |
| `BLKGRP` | String |  | len 8 |
| `POP100` | Integer |  |  |
| `HU100` | Integer |  |  |
| `FAMMOD` | Integer |  |  |
| `FAMLOW` | Integer |  |  |
| `FAMVLOW` | Double |  |  |
| `NFAMMOD` | Double |  |  |
| `NFAMLOW` | Double |  |  |
| `NFAMVLOW` | Double |  |  |
| `HHMOD` | Integer |  |  |
| `HHLOW` | Integer |  |  |
| `HHVLOW` | Integer |  |  |
| `FAMPMOD` | Double |  |  |
| `FAMPLOW` | Double |  |  |
| `FAMPVLOW` | Double |  |  |
| `NFAMPMOD` | Double |  |  |
| `NFAMPLOW` | Double |  |  |
| `NFAMPVLOW` | Double |  |  |
| `PMOD` | Integer |  |  |
| `PLOW` | Integer |  |  |
| `PVLOW` | Integer |  |  |
| `LOWMOD` | Integer |  |  |
| `LOWMODUNIV` | Double |  |  |
| `LOWMODPCT` | Double |  |  |
| `TRANDBG` | String |  | len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 223: Dayton Corporation Boundary

- **Records:** 2
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PERIMETER` | Double |  |  |
| `BIGBNDY_` | Integer |  |  |
| `BIGBNDY_ID` | Integer |  |  |
| `NAME` | String |  | len 50 |
| `NAME_CODE` | Integer |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAM` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `Done` | String |  | len 254 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 224: Neighborhood

- **Records:** 97
- **Geometry:** Polygon

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
| `OLD_ABR` | String |  | len 15 |
| `OLD_HOOD` | String |  | len 50 |
| `GISADMIN_N` | String |  | len 14 |
| `GISADMIN_1` | Double |  |  |
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

## Layer 226: Centerline

- **Records:** 81,061
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FNODE_` | Double |  |  |
| `TNODE_` | Double |  |  |
| `LPOLY_` | Double |  |  |
| `RPOLY_` | Double |  |  |
| `LENGTH` | Double |  |  |
| `B40_` | Double |  |  |
| `B40_ID` | Double |  |  |
| `LINE_ID` | Double |  |  |
| `LEFT_FROM` | Integer |  |  |
| `LEFT_TO` | Integer |  |  |
| `RIGHT_FROM` | Integer |  |  |
| `RIGHT_TO` | Integer |  |  |
| `GEONAME` | String |  | len 60 |
| `GEONAME_ID` | Double |  |  |
| `ADDRCODE_L` | String |  | len 1 |
| `ADDRCODE_R` | String |  | len 1 |
| `ZIPL` | String |  | len 5 |
| `ZIPR` | String |  | len 5 |
| `ROW_PLACEL` | String |  | len 5 |
| `ROW_PLACER` | String |  | len 5 |
| `ROW_CSUBL` | String |  | len 5 |
| `ROW_CSUBR` | String |  | len 5 |
| `CTL` | String |  | len 6 |
| `CTR` | String |  | len 6 |
| `BLK90L` | String |  | len 4 |
| `BLK90R` | String |  | len 4 |
| `TRACTL` | Double |  |  |
| `TRACTR` | Double |  |  |
| `BLOCKR` | Double |  |  |
| `BLOCKL` | Double |  |  |
| `PROBLEM` | String |  | len 10 |
| `CFCC` | String |  | len 3 |
| `ONE_WAY` | String |  | len 2 |
| `CODE` | String |  | len 10 |
| `ORDINANCE` | String |  | len 16 |
| `ORD_DATE` | String |  | len 8 |
| `ROAD_TYPE` | String |  | len 50 |
| `CLASSWORK` | String |  | len 16 |
| `FCC` | String |  | len 4 |
| `DOMAIN_` | String |  | len 10 |
| `STATUS` | String |  | len 10 |
| `RE_CK_STAT` | String |  | len 3 |
| `TYPE_` | String |  | len 10 |
| `ARCHIV_TYP` | String |  | len 10 |
| `GNDIRPREFX` | String |  | len 2 |
| `GNBASENAME` | String |  | len 45 |
| `GNSUFTYPE` | String |  | len 4 |
| `GNDIRSUFX` | String |  | len 2 |
| `ORD_TYPE` | String |  | len 3 |
| `ORD_NUMBER` | Integer |  |  |
| `TEMPHOLD` | String |  | len 16 |
| `ORDNCE_DAT` | String |  | len 10 |
| `GALTNAME2` | String |  | len 50 |
| `BIKEROUTE` | String |  | len 3 |
| `TR_REG` | Integer |  |  |
| `ROUTE_ID1` | String |  | len 10 |
| `ROUTE_ID2` | String |  | len 10 |
| `GALTNAME1` | String |  | len 50 |
| `GEN_ADDR` | String |  | len 3 |
| `BNDRY_TYPE` | String |  | len 10 |
| `EXTLINKID` | Double |  |  |
| `BULK_RT` | String |  | len 50 |
| `CNT_BULK_R` | Double |  |  |
| `COLL_DAY_L` | String |  | len 10 |
| `RT_WC_L` | Double |  |  |
| `RT_BULK_L` | Double |  |  |
| `RT_METL_L` | Double |  |  |
| `RT_TIRE_L` | Double |  |  |
| `RT_LLDR_L` | Double |  |  |
| `RT_RECY_L` | Double |  |  |
| `RT_CONTN_L` | Double |  |  |
| `COLL_DAY_R` | String |  | len 10 |
| `RT_WC_R` | Double |  |  |
| `RT_BULK_R` | Double |  |  |
| `RT_METL_R` | Double |  |  |
| `RT_TIRE_R` | Double |  |  |
| `RT_LLDR_R` | Double |  |  |
| `RT_RECY_R` | Double |  |  |
| `RT_CONTN_R` | Double |  |  |
| `NBHDCODE_L` | String |  | len 8 |
| `PB_L` | String |  | len 10 |
| `NHBHD_L` | String |  | len 50 |
| `NBHDCODE_R` | String |  | len 8 |
| `PB_R` | String |  | len 10 |
| `NHBHD_R` | String |  | len 50 |
| `BOUNDARY` | String |  | len 50 |
| `ST_MAINT_L` | String |  | len 10 |
| `ST_MAINT_R` | String |  | len 10 |
| `ST_CLASS` | String |  | len 10 |
| `FUNCT_CLAS` | String |  | len 3 |
| `FC_ID` | Double |  |  |
| `CLASS` | Double |  |  |
| `SUBCLASS` | Double |  |  |
| `WATERTYPE` | String |  | len 20 |
| `WATER_FEAT` | String |  | len 16 |
| `WATER_PATH` | String |  | len 16 |
| `GNIS_ID` | String |  | len 10 |
| `GNIS_NAME` | String |  | len 65 |
| `REACHCODE` | String |  | len 14 |
| `FTYPE` | String |  | len 35 |
| `FCODE` | String |  | len 50 |
| `CORP` | String |  | len 1 |
| `TOWNSHIP` | String |  | len 1 |
| `COUNTY` | String |  | len 3 |
| `COUNTYLINE` | String |  | len 20 |
| `FUNCSTAT` | String |  | len 1 |
| `TEMPTYPE` | String |  | len 16 |
| `TEMPGEONAM` | String |  | len 50 |
| `BLOCK_L` | String |  | len 60 |
| `BLOCK_R` | String |  | len 60 |
| `DPD_SECT_L` | Double |  |  |
| `DPD_SECT_R` | Double |  |  |
| `BD_SECTOR` | Double |  |  |
| `PLANDST_L` | String |  | len 5 |
| `PLANDST_R` | String |  | len 5 |
| `BD_PLANDST` | Double |  |  |
| `CTY_FIPS_L` | String |  | len 3 |
| `CTY_FIPS_R` | String |  | len 3 |
| `CSB_FIPS_L` | String |  | len 5 |
| `CSB_FIPS_R` | String |  | len 5 |
| `PL_FIPS_L` | String |  | len 5 |
| `PL_FIPS_R` | String |  | len 5 |
| `BD_COUNTY` | Integer |  |  |
| `BD_COUSUB` | Integer |  |  |
| `BD_PLACE` | Integer |  |  |
| `CS_COUSUBL` | String |  | len 5 |
| `CS_COUSUBR` | String |  | len 5 |
| `CS_PLACEL` | String |  | len 5 |
| `CS_PLACER` | String |  | len 5 |
| `OS_COUSUBL` | String |  | len 5 |
| `OS_COUSUBR` | String |  | len 5 |
| `OS_PLACEL` | String |  | len 5 |
| `OS_PLACER` | String |  | len 5 |
| `T_COSUBL` | String |  | len 5 |
| `T_COSUBR` | String |  | len 5 |
| `T_PLACEL` | String |  | len 5 |
| `T_PLACER` | String |  | len 5 |
| `T_CSUBL_X` | String |  | len 3 |
| `T_CSUBR_X` | String |  | len 3 |
| `T_PLACEL_X` | String |  | len 3 |
| `T_PLACER_X` | String |  | len 3 |
| `GIS_DOMAIN` | String |  | len 5 |
| `LABLPDMASK` | Double |  |  |
| `LABLNORMAL` | Double |  |  |
| `X_LINE` | String |  | len 2 |
| `DE_ICE_L` | Double |  |  |
| `DE_ICE_R` | Double |  |  |
| `RT_TYPE` | Double |  |  |
| `DE_ICE_2` | Double |  |  |
| `CK` | String |  | len 3 |
| `X_SCTN_NM` | String |  | len 50 |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAM` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `L_CITY` | String |  | len 30 |
| `R_CITY` | String |  | len 30 |
| `L_STATE` | String |  | len 2 |
| `R_STATE` | String |  | len 2 |
| `L_TWP` | String |  | len 18 |
| `R_TWP` | String |  | len 18 |
| `L_ZIP` | String |  | len 5 |
| `R_ZIP` | String |  | len 5 |
| `L_COUNTY` | String |  | len 3 |
| `R_COUNTY` | String |  | len 3 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `Shape_Leng` | Double |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 227: Topographic

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 228: Spot Elevations

- **Records:** 19,181
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN_ContourPoint_AREA` | Double | AREA |  |
| `PERIMETER` | Double |  |  |
| `CONTOUR_` | Integer |  |  |
| `CONTOUR_ID` | Integer |  |  |
| `FCODE` | Integer |  |  |
| `ELEV` | Double |  |  |
| `FEATURE` | String |  | len 34 |
| `POLYGONID` | Integer |  |  |
| `SCALE` | Double |  |  |
| `ANGLE` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 229: Index Contours

- **Records:** 45,737
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FNODE_` | Integer |  |  |
| `TNODE_` | Integer |  |  |
| `LPOLY_` | Integer |  |  |
| `RPOLY_` | Integer |  |  |
| `LENGTH` | Double |  |  |
| `CONTOUR_` | Integer |  |  |
| `CONTOUR_ID` | Integer |  |  |
| `FCODE` | Integer |  |  |
| `ELEV` | Double |  |  |
| `FEATURE` | String |  | len 34 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 230: Intermediate Contours

- **Records:** 184,381
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FNODE_` | Integer |  |  |
| `TNODE_` | Integer |  |  |
| `LPOLY_` | Integer |  |  |
| `RPOLY_` | Integer |  |  |
| `LENGTH` | Double |  |  |
| `CONTOUR_` | Integer |  |  |
| `CONTOUR_ID` | Integer |  |  |
| `FCODE` | Integer |  |  |
| `ELEV` | Double |  |  |
| `FEATURE` | String |  | len 34 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 231: WEB_CAMA

- **Records:** 254,227

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PARID` | String |  | len 30 |
| `NBHD` | String |  | len 8 |
| `PARLOC` | String |  | len 103 |
| `OWNER_NAME` | String |  | len 205 |
| `OWNER_NA_1` | String |  | len 205 |
| `OWNER_ADDR` | String |  | len 134 |
| `OWNER_AD_1` | String |  | len 80 |
| `OWNER_AD_2` | String |  | len 123 |
| `MAILING_NA` | String |  | len 205 |
| `MAILING__1` | String |  | len 205 |
| `MAILING_AD` | String |  | len 132 |
| `MAILING__2` | String |  | len 80 |
| `MAILING__3` | String |  | len 123 |
| `LEGAL1` | String |  | len 60 |
| `LEGAL2` | String |  | len 60 |
| `LEGAL3` | String |  | len 60 |
| `CLASS` | String |  | len 4 |
| `LUC` | String |  | len 4 |
| `ACRES` | String |  | len 15 |
| `ASSDCAUV` | String |  | len 20 |
| `ASSDLAND` | String |  | len 20 |
| `ASSDBLDG` | String |  | len 20 |
| `ASSDTOTAL` | String |  | len 20 |
| `APPRCAUV` | String |  | len 20 |
| `APPRLAND` | String |  | len 20 |
| `APPRBLDG` | String |  | len 20 |
| `APPRTOTAL` | String |  | len 20 |
| `DWEL_STYLE` | String |  | len 40 |
| `DWEL_EXTWA` | String |  | len 40 |
| `DWEL_STORI` | Double |  |  |
| `DWEL_YRBLT` | Double |  |  |
| `DWEL_RMTOT` | Double |  |  |
| `DWEL_RMBED` | Double |  |  |
| `DWEL_FIXBA` | Double |  |  |
| `DWEL_FIXHA` | Double |  |  |
| `DWEL_SFLA` | Double |  |  |
| `DWEL_BSMT` | String |  | len 40 |
| `DWEL_HEAT` | String |  | len 40 |
| `DWEL_HEATS` | String |  | len 40 |
| `DWEL_FUEL` | String |  | len 40 |
| `DWEL_WBFP_` | Double |  |  |
| `DWEL_WBFP1` | Double |  |  |
| `COMM_STRUC` | String |  | len 30 |
| `COMM_YRBLT` | Double |  |  |
| `COMM_STORI` | Double |  |  |
| `COMM_UNITS` | Double |  |  |
| `COMM_SF` | Double |  |  |
| `COMM_BED` | Double |  |  |
| `OBY_IMPROV` | String |  | len 30 |
| `OBY_UNITS` | Double |  |  |
| `OBY_AREA` | Double |  |  |
| `OBY_YRBLT` | Double |  |  |
| `OBY_GRADE` | String |  | len 40 |
| `OBY_CONDIT` | String |  | len 40 |
| `OBY_VALUE` | Double |  |  |
| `SALE_DATE` | String |  | len 10 |
| `SALE_PRICE` | String |  | len 15 |
| `SALE_CONVN` | String |  | len 15 |
| `SALE_OLDOW` | String |  | len 205 |
| `SPECASMTS` | String |  | len 1 |
| `CREATEDATE` | Date |  |  |
| `HMSDFLAG` | String |  | len 1 |
| `MCITYNAME` | String |  | len 40 |
| `MSTATECODE` | String |  | len 2 |
| `MZIP1` | String |  | len 5 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 234: vlm_MowingVerification

- **Records:** 31,903

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Parcel_ID` | String |  | len 50 |
| `Service1` | Date |  |  |
| `Service2` | Date |  |  |
| `Service3` | Date |  |  |
| `Service4` | Date |  |  |
| `Service6` | Date |  |  |
| `Service5` | Date |  |  |
| `OCCUPIED1` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OWNER_MOWED1` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `MISSED1` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OCCUPIED2` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OWNER_MOWED2` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `MISSED2` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OCCUPIED3` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OWNER_MOWED3` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `MISSED3` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OCCUPIED4` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OWNER_MOWED4` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `MISSED4` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OCCUPIED5` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OWNER_MOWED5` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `MISSED5` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OCCUPIED6` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `OWNER_MOWED6` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `MISSED6` | String | OCCUPIED6 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `ServiceYear` | String | Service Year | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 235: addressParcelCamaSL_VW

- **Records:** 273,310

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TAXPINNO` | String |  | len 20 |
| `OWNER_NAME` | String |  | len 40 |
| `OWNER_NA_1` | String |  | len 40 |
| `OWNER_ADDR` | String |  | len 134 |
| `OWNER_AD_1` | String |  | len 80 |
| `PARLOC` | String |  | len 103 |
| `MAILING_NA` | String |  | len 40 |
| `MAILING__1` | String |  | len 40 |
| `MAILING_AD` | String |  | len 132 |
| `MAILING__2` | String |  | len 80 |
| `MAILING__3` | String |  | len 123 |
| `USEDADDRESS` | String |  | len 50 |
| `LOTNUMBER` | String |  | len 20 |
| `K_PID` | String |  | len 18 |
| `LOC_AREA` | String |  | len 30 |
| `TAXAREA` | String |  | len 10 |
| `TAXDISTRIC` | String |  | len 5 |
| `NBHD` | String |  | len 8 |
| `CLASS` | String |  | len 4 |
| `Field4` | String |  | len 2147483647 |
| `ACRES` | String |  | len 15 |
| `SALE_DATE` | String |  | len 10 |
| `SALE_PRICE` | String |  | len 15 |
| `SOURCEDOC` | String |  | len 20 |
| `HOT_LINK` | String |  | len 75 |
| `NumOcc` | String |  | len 8000 |
| `WEB_BKPG_LINK` | String |  | len 100 |
| `PHOTO_LINK` | String |  | len 100 |
| `CREATEDATE` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | Integer |  |  |
| `ESRI_OID` | OID |  |  |

</details>

## Layer 236: addressSL_VW

- **Records:** 143,861

| Field | Type | Alias | Notes |
|---|---|---|---|
| `STNO` | String |  | len 10 |
| `USEDADDRESS` | String |  | len 50 |
| `TAXPINNO` | String |  | len 20 |
| `K_PID` | String |  | len 20 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ESRI_OID` | OID |  |  |

</details>

## Layer 237: CAMA_LANDUSECODES

- **Records:** 145

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Field1` | Integer |  |  |
| `Field2` | Integer |  |  |
| `Field3` | String |  | len 1073741822 |
| `Field4` | String |  | len 1073741822 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |

</details>

