# Planning/MapLayers_Planning_LotLinks2

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Planning/MapLayers_Planning_LotLinks2/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Planning_MapLayers_Planning_LotLinks2
- **Created:** None  ·  **Item modified:** None
- **Tags:** Planning

## Layer 0: Used Address

- **Records:** 163,184
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `YCOORD` | Double |  |  |
| `XCOORD` | Double |  |  |
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
| `AddressType` | String |  | len 255 |
| `AddressUpdateHansen` | SmallInteger | Push Update to Hansen |  |
| `UsedAddressID` | Integer | Used Address ID |  |
| `BaseAddressID` | Integer | Base Address ID |  |
| `FullAddress` | String | Full Address | len 254 |
| `FullSuffix` | String |  | **Values:** `Avenue` = Avenue; `Boulevard` = Boulevard; `Circle` = Circle; `Court` = Court; `Drive` = Drive; `Highway` = Highway; `Lane` = Lane; `Loop` = Loop; `Park` = Park; `Pike` = Pike; `Parkway` = Parkway; `Place` = Place; …(+8 more) · len 50 |
| `AREAS` | String | Area | len 100 |
| `PRIMARYADDR` | String | Primary Address | len 5 |
| `ZONING_CODE` | String |  | len 255 |
| `PRI_BOARDSORT` | String |  | len 255 |
| `PRI_BOARD` | String |  | len 255 |
| `HIST_DIST_CODE` | String |  | len 255 |
| `LUC_Int` | Integer |  |  |
| `LUC_Description` | String |  | len 100 |
| `PD_District` | String |  | **Values:** `East District` = East District; `West District` = West District; `Central District` = Central District; `Dayton International Airport` = Dayton International Airport · len 50 |
| `PD_Beat` | String |  | len 50 |
| `PD_Sector` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GLOBALID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 2: Zoning

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 3: Historic District

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
| `Shape` | Geometry |  |  |
| `OBJECTID_1` | OID |  |  |
| `GlobalID_1` | Double | Shape.STArea() |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 4: Zoning District

- **Records:** 970
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NEW_ZONE` | String | New Zoning District | len 25 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 5: Administrative Boundaries

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 6: Building Footprint

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
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 7: Plan_POD_District

- **Records:** 5
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `GISADMIN.Plan_POD_District.Area` | Integer |  |  |
| `Name` | SmallInteger |  |  |
| `Name_2` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 8: Dayton Corporation Boundary

- **Records:** 2
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NAME` | String | Name | len 50 |
| `VERSIONNAM` | String |  | len 50 |
| `Done` | String |  | len 254 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID_1` | OID |  |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |

</details>

## Layer 9: Neighborhood

- **Records:** 97
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `HOOD` | String | Neighborhood | len 50 |
| `PRI_BOARD` | String | Priority Board | len 5 |
| `ABR` | String | Neighborhood Abbreviation | len 35 |
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
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 11: Centerline

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
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `VERSIONNAM` | String |  | len 50 |
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
| `OBJECTID` | Integer |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID_1` | OID |  |  |
| `Shape_Leng` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 12: addressParcelCamaSL_VW

- **Records:** 273,310

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TAXPINNO` | String |  | len 20 |
| `PARLOC` | String |  | len 103 |
| `USEDADDRESS` | String |  | len 50 |
| `LOTNUMBER` | String |  | len 20 |
| `K_PID` | String |  | len 18 |
| `LOC_AREA` | String |  | len 30 |
| `TAXAREA` | String |  | len 10 |
| `TAXDISTRIC` | String |  | len 5 |
| `NBHD` | String |  | len 8 |
| `CLASS` | String |  | len 4 |
| `ACRES` | String |  | len 15 |
| `SALE_DATE` | String |  | len 10 |
| `SALE_PRICE` | String |  | len 15 |
| `SOURCEDOC` | String |  | len 20 |
| `HOT_LINK` | String |  | len 75 |
| `NumOcc` | String |  | len 8000 |
| `WEB_BKPG_LINK` | String |  | len 100 |
| `CREATEDATE` | Date |  |  |
| `Field4` | String |  | len 2147483647 |
| `PHOTO_LINK` | String |  | len 100 |
| `OWNER_NAME` | String |  | len 205 |
| `OWNER_NA_1` | String |  | len 205 |
| `OWNER_ADDR` | String |  | len 134 |
| `OWNER_AD_1` | String |  | len 80 |
| `MAILING_NA` | String |  | len 205 |
| `MAILING__1` | String |  | len 205 |
| `MAILING_AD` | String |  | len 132 |
| `MAILING__2` | String |  | len 80 |
| `MAILING__3` | String |  | len 123 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | Integer |  |  |

</details>

## Layer 13: addressSL_VW

- **Records:** 143,861

| Field | Type | Alias | Notes |
|---|---|---|---|
| `USEDADDRESS` | String |  | len 50 |
| `TAXPINNO` | String |  | len 20 |
| `K_PID` | String |  | len 20 |
| `STNO` | String |  | len 10 |

## Layer 14: CAMA

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

## Layer 15: CAMA_LandUseCodes

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

