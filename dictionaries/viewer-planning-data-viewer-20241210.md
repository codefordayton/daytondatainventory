# Viewer/Planning_Data_Viewer_20241210

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Viewer/Planning_Data_Viewer_20241210/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Viewer_Planning_Data_Viewer_20241210
- **Created:** None  ·  **Item modified:** None
- **Tags:** Viewer

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

## Layer 7: Parcels

- **Records:** 273,627
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.mc_parcel_polygon_e.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.mc_parcel_polygon_e.TAXPINNO` | String | Parcel ID | len 20 |
| `GISADMIN.mc_parcel_polygon_e.TAXDISTRIC` | String | Tax District | len 5 |
| `GISADMIN.mc_parcel_polygon_e.TAXBOOK` | String | Tax Book | len 4 |
| `GISADMIN.mc_parcel_polygon_e.TAXPAGE` | String | Tax Page | len 2 |
| `GISADMIN.mc_parcel_polygon_e.TAXSUF` | String | Tax Suffix | len 1 |
| `GISADMIN.mc_parcel_polygon_e.TAXINDEX` | String | Tax Index | len 4 |
| `GISADMIN.mc_parcel_polygon_e.TAXAREA` | String | Tax Area | len 10 |
| `GISADMIN.mc_parcel_polygon_e.LOTNUMBER` | String | Lot Number | len 20 |
| `GISADMIN.mc_parcel_polygon_e.ACREAGE` | String | Acreage | len 12 |
| `GISADMIN.mc_parcel_polygon_e.LOC_NBR` | Double | Street Number |  |
| `GISADMIN.mc_parcel_polygon_e.LOC_DIR` | String | Street Direction | len 4 |
| `GISADMIN.mc_parcel_polygon_e.LOC_STREET` | String | Street Name | len 50 |
| `GISADMIN.mc_parcel_polygon_e.LOC_SUFFIX` | String | Street Suffix | len 10 |
| `GISADMIN.mc_parcel_polygon_e.LOC_AREA` | String | Jurisdiction | len 30 |
| `GISADMIN.mc_parcel_polygon_e.NBHD_1` | String | Neighborhood Code | len 10 |
| `GISADMIN.mc_parcel_polygon_e.K_PID` | String | Key Parcel ID | len 18 |
| `GISADMIN.mc_parcel_polygon_e.HOT_LINK` | String | Link | len 75 |
| `GISADMIN.mc_parcel_polygon_e.PHOTO_LINK` | String | Parcel ID - Photo Link | len 100 |
| `GISADMIN.mc_parcel_polygon_e.WEB_BKPG_LINK` | String | Tax Map Link | len 100 |
| `GISADMIN.mc_parcel_polygon_e.C_BLOCK` | String | Census Block | len 20 |
| `GISADMIN.mc_parcel_polygon_e.C_TRACK` | String | Census Tract | len 20 |
| `GISADMIN.mc_parcel_polygon_e.SHAPE` | Geometry | SHAPE |  |
| `GISADMIN.mc_parcel_polygon_e.GlobalID` | GlobalID | GlobalID |  |
| `GISADMIN.WEB_CAMA.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.WEB_CAMA.PARID` | String | PARID | len 30 |
| `GISADMIN.WEB_CAMA.NBHD` | String | NBHD | len 8 |
| `GISADMIN.WEB_CAMA.PARLOC` | String | PARLOC | len 103 |
| `GISADMIN.WEB_CAMA.LEGAL1` | String | LEGAL1 | len 60 |
| `GISADMIN.WEB_CAMA.LEGAL2` | String | LEGAL2 | len 60 |
| `GISADMIN.WEB_CAMA.LEGAL3` | String | LEGAL3 | len 60 |
| `GISADMIN.WEB_CAMA.CLASS` | String | CLASS | len 4 |
| `GISADMIN.WEB_CAMA.LUC` | String | LUC | len 4 |
| `GISADMIN.WEB_CAMA.ACRES` | String | ACRES | len 15 |
| `GISADMIN.WEB_CAMA.ASSDCAUV` | String | ASSDCAUV | len 20 |
| `GISADMIN.WEB_CAMA.ASSDLAND` | String | ASSDLAND | len 20 |
| `GISADMIN.WEB_CAMA.ASSDBLDG` | String | ASSDBLDG | len 20 |
| `GISADMIN.WEB_CAMA.ASSDTOTAL` | String | ASSDTOTAL | len 20 |
| `GISADMIN.WEB_CAMA.APPRCAUV` | String | APPRCAUV | len 20 |
| `GISADMIN.WEB_CAMA.APPRLAND` | String | APPRLAND | len 20 |
| `GISADMIN.WEB_CAMA.APPRBLDG` | String | APPRBLDG | len 20 |
| `GISADMIN.WEB_CAMA.APPRTOTAL` | String | APPRTOTAL | len 20 |
| `GISADMIN.WEB_CAMA.DWEL_STYLE` | String | DWEL_STYLE | len 40 |
| `GISADMIN.WEB_CAMA.DWEL_YRBLT` | Double | DWEL_YRBLT |  |
| `GISADMIN.WEB_CAMA.DWEL_RMTOT` | Double | DWEL_RMTOT |  |
| `GISADMIN.WEB_CAMA.DWEL_RMBED` | Double | DWEL_RMBED |  |
| `GISADMIN.WEB_CAMA.DWEL_SFLA` | Double | DWEL_SFLA |  |
| `GISADMIN.WEB_CAMA.DWEL_BSMT` | String | DWEL_BSMT | len 40 |
| `GISADMIN.WEB_CAMA.DWEL_HEAT` | String | DWEL_HEAT | len 40 |
| `GISADMIN.WEB_CAMA.DWEL_FUEL` | String | DWEL_FUEL | len 40 |
| `GISADMIN.WEB_CAMA.COMM_YRBLT` | Double | COMM_YRBLT |  |
| `GISADMIN.WEB_CAMA.COMM_UNITS` | Double | COMM_UNITS |  |
| `GISADMIN.WEB_CAMA.COMM_SF` | Double | COMM_SF |  |
| `GISADMIN.WEB_CAMA.COMM_BED` | Double | COMM_BED |  |
| `GISADMIN.WEB_CAMA.OBY_UNITS` | Double | OBY_UNITS |  |
| `GISADMIN.WEB_CAMA.OBY_AREA` | Double | OBY_AREA |  |
| `GISADMIN.WEB_CAMA.OBY_YRBLT` | Double | OBY_YRBLT |  |
| `GISADMIN.WEB_CAMA.OBY_GRADE` | String | OBY_GRADE | len 40 |
| `GISADMIN.WEB_CAMA.OBY_VALUE` | Double | OBY_VALUE |  |
| `GISADMIN.WEB_CAMA.SALE_DATE` | String | SALE_DATE | len 10 |
| `GISADMIN.WEB_CAMA.SALE_PRICE` | String | SALE_PRICE | len 15 |
| `GISADMIN.WEB_CAMA.SPECASMTS` | String | SPECASMTS | len 1 |
| `GISADMIN.WEB_CAMA.CREATEDATE` | Date | CREATEDATE |  |
| `GISADMIN.WEB_CAMA.HMSDFLAG` | String | HMSDFLAG | len 1 |
| `GISADMIN.WEB_CAMA.OWNER_NAME` | String | OWNER_NAME | len 205 |
| `GISADMIN.WEB_CAMA.OWNER_NA_1` | String | OWNER_NA_1 | len 205 |
| `GISADMIN.WEB_CAMA.OWNER_ADDR` | String | OWNER_ADDR | len 134 |
| `GISADMIN.WEB_CAMA.OWNER_AD_1` | String | OWNER_AD_1 | len 80 |
| `GISADMIN.WEB_CAMA.OWNER_AD_2` | String | OWNER_AD_2 | len 123 |
| `GISADMIN.WEB_CAMA.MAILING_NA` | String | MAILING_NA | len 205 |
| `GISADMIN.WEB_CAMA.MAILING__1` | String | MAILING__1 | len 205 |
| `GISADMIN.WEB_CAMA.MAILING_AD` | String | MAILING_AD | len 132 |
| `GISADMIN.WEB_CAMA.MAILING__2` | String | MAILING__2 | len 80 |
| `GISADMIN.WEB_CAMA.MAILING__3` | String | MAILING__3 | len 123 |
| `GISADMIN.WEB_CAMA.DWEL_EXTWA` | String | DWEL_EXTWA | len 40 |
| `GISADMIN.WEB_CAMA.DWEL_STORI` | Double | DWEL_STORI |  |
| `GISADMIN.WEB_CAMA.DWEL_FIXBA` | Double | DWEL_FIXBA |  |
| `GISADMIN.WEB_CAMA.DWEL_FIXHA` | Double | DWEL_FIXHA |  |
| `GISADMIN.WEB_CAMA.DWEL_HEATS` | String | DWEL_HEATS | len 40 |
| `GISADMIN.WEB_CAMA.DWEL_WBFP_` | Double | DWEL_WBFP_ |  |
| `GISADMIN.WEB_CAMA.DWEL_WBFP1` | Double | DWEL_WBFP1 |  |
| `GISADMIN.WEB_CAMA.COMM_STRUC` | String | COMM_STRUC | len 30 |
| `GISADMIN.WEB_CAMA.COMM_STORI` | Double | COMM_STORI |  |
| `GISADMIN.WEB_CAMA.OBY_IMPROV` | String | OBY_IMPROV | len 30 |
| `GISADMIN.WEB_CAMA.OBY_CONDIT` | String | OBY_CONDIT | len 40 |
| `GISADMIN.WEB_CAMA.SALE_CONVN` | String | SALE_CONVN | len 15 |
| `GISADMIN.WEB_CAMA.SALE_OLDOW` | String | SALE_OLDOW | len 205 |
| `GISADMIN.WEB_CAMA.MCITYNAME` | String | MCITYNAME | len 40 |
| `GISADMIN.WEB_CAMA.MSTATECODE` | String | MSTATECODE | len 2 |
| `GISADMIN.WEB_CAMA.MZIP1` | String | MZIP1 | len 5 |
| `GISADMIN.WEB_CAMA.GlobalID` | GUID | GlobalID |  |
| `GISADMIN.CAMA_LANDUSECODES.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.CAMA_LANDUSECODES.Field1` | Integer | Field1 |  |
| `GISADMIN.CAMA_LANDUSECODES.Field2` | Integer | Field2 |  |
| `GISADMIN.CAMA_LANDUSECODES.Field3` | String | Field3 | len 1073741822 |
| `GISADMIN.CAMA_LANDUSECODES.Field4` | String | Field4 | len 1073741822 |
| `GISADMIN.CAMA_LANDUSECODES.GlobalID` | String | GlobalID | len 38 |

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

## Layer 197: Dim

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 198: Zoning

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 199: Flood Plain

- **Records:** 29
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LEVEL_` | SmallInteger | Level |  |
| `COLOR` | SmallInteger | Color |  |
| `TEXT` | String | Feature Type | len 50 |
| `LABEL` | String | Feature Label | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 200: Wellfield District

- **Records:** 6
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `Acreage` | Integer |  |  |

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

## Layer 201: Planned Development

- **Records:** 136
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FEATURE` | String | Feature Type | len 16 |
| `DISTRICT` | String | District | len 16 |
| `YEAR` | Date | Year |  |
| `ORDINANCE` | String | Ordinance | len 16 |
| `CPB` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 202: Urban Preservation

- **Records:** 4
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `URBAN_RENE` | String | Urban Renewal Area | len 16 |
| `AREA_` | Double | Area |  |
| `PERIMETER` | Double | Perimeter |  |
| `ACRES` | Double | Acres |  |
| `HECTARES` | Double | Hectares |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 203: Historic District

- **Records:** 20
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FEATURE` | String | Feature Type | len 16 |
| `NAME` | String | Name | len 16 |
| `DISTRICT` | String | District | len 16 |
| `YEAR` | Date | Year |  |
| `ORDINANCE` | String | Ordinance | len 16 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 204: POD

- **Records:** 5
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Name_2` | String | District Name | len 10 |
| `GISADMIN.Plan_POD_District.Area` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 205: Graphics Overlay

- **Records:** 3
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LABEL` | String | Area Label | len 30 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 206: Zoning District

- **Records:** 970
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PERIMETER` | Double | Perimeter |  |
| `NEWZONING2` | Integer | New Zoning 2 |  |
| `AREA_1` | Double | Area |  |
| `NEWZONING1` | Integer | New Zoning 1 |  |
| `FEATURE` | String | Feature Type | len 25 |
| `NAME` | String | Name | len 50 |
| `DISTRICT` | String | Zoning District | len 5 |
| `LAYER` | String | Layer | len 32 |
| `NEW_ZONE` | String | New Zoning District | len 25 |
| `POLYGONID` | Integer | Polygon ID |  |
| `GISADMIN_Plan_Zoning_AREA` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 207: Vacant Land Management

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 209: Administrative Boundaries

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 210: Building Footprint

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

## Layer 211: CDBG Eligible

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

## Layer 212: Dayton Corporation Boundary

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

## Layer 213: Neighborhood

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

## Layer 214: County-City_Twp Boundaries

- **Records:** 71
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PERIMETER` | Double |  |  |
| `BIGBNDY_` | Integer |  |  |
| `BIGBNDY_ID` | Integer |  |  |
| `NAME` | String |  | len 50 |
| `NAME_CODE` | SmallInteger |  |  |
| `WEB_ARCHIVE_INDEX` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 215: Centerline

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

## Layer 217: WEB_CAMA

- **Records:** 254,227

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PARID` | String |  | len 30 |
| `NBHD` | String |  | len 8 |
| `PARLOC` | String |  | len 103 |
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
| `DWEL_YRBLT` | Double |  |  |
| `DWEL_RMTOT` | Double |  |  |
| `DWEL_RMBED` | Double |  |  |
| `DWEL_SFLA` | Double |  |  |
| `DWEL_BSMT` | String |  | len 40 |
| `DWEL_HEAT` | String |  | len 40 |
| `DWEL_FUEL` | String |  | len 40 |
| `COMM_YRBLT` | Double |  |  |
| `COMM_UNITS` | Double |  |  |
| `COMM_SF` | Double |  |  |
| `COMM_BED` | Double |  |  |
| `OBY_UNITS` | Double |  |  |
| `OBY_AREA` | Double |  |  |
| `OBY_YRBLT` | Double |  |  |
| `OBY_GRADE` | String |  | len 40 |
| `OBY_VALUE` | Double |  |  |
| `SALE_DATE` | String |  | len 10 |
| `SALE_PRICE` | String |  | len 15 |
| `SPECASMTS` | String |  | len 1 |
| `CREATEDATE` | Date |  |  |
| `HMSDFLAG` | String |  | len 1 |
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
| `DWEL_EXTWA` | String |  | len 40 |
| `DWEL_STORI` | Double |  |  |
| `DWEL_FIXBA` | Double |  |  |
| `DWEL_FIXHA` | Double |  |  |
| `DWEL_HEATS` | String |  | len 40 |
| `DWEL_WBFP_` | Double |  |  |
| `DWEL_WBFP1` | Double |  |  |
| `COMM_STRUC` | String |  | len 30 |
| `COMM_STORI` | Double |  |  |
| `OBY_IMPROV` | String |  | len 30 |
| `OBY_CONDIT` | String |  | len 40 |
| `SALE_CONVN` | String |  | len 15 |
| `SALE_OLDOW` | String |  | len 205 |
| `MCITYNAME` | String |  | len 40 |
| `MSTATECODE` | String |  | len 2 |
| `MZIP1` | String |  | len 5 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 218: VLM_Inspection

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
| `GlobalID_1` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |

</details>

## Layer 219: VLM_Inspection__ATTACH

- **Records:** 10,965

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `ATTACHMENTID` | OID |  |  |
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 220: vlm_MowingVerification

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

## Layer 221: T2016_VLM_DB_ABATED_2017

- **Records:** 6,721

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PARCEL_ID` | String | Parcel ID | len 255 |
| `LOT_TYPE` | String | Lot Type | len 255 |
| `ADDRESS_NO` | String | Address Number | len 255 |
| `ST_DIR` | String | Street Direction | len 255 |
| `STREET` | String | Street | len 255 |
| `ST_SUFFIX` | String | Street Suffix | len 255 |
| `NEIGHBORHOOD` | String | Neighborhood | len 255 |
| `LOCATION` | String | Location | len 255 |
| `ABATEMENT_ID` | String | Abatement ID | len 255 |
| `SERVICE_1` | String | Service | len 255 |
| `BILLING` | String | Billing | len 255 |
| `LOT_NUMBER` | Double | Lot Number |  |
| `CUSTOMER_NO` | String | Customer Number | len 255 |
| `SEQUENCE` | String | Sequence | len 255 |
| `OWNER` | String | Owner | len 255 |
| `OWNER_ADDRESS` | String | Owner Address | len 255 |
| `ABATE` | SmallInteger | Abate |  |
| `OWNER_ADDRESS_3` | String | Owner Address cont | len 255 |
| `SERVICE_COMMENTS` | String | Service Comments | len 255 |
| `CUSTOMER_NO_AR` | String | Customer Number AR | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 222: addressParcelCamaSL_VW

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

## Layer 223: addressSL_VW

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

## Layer 224: CAMA_LANDUSECODES

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

