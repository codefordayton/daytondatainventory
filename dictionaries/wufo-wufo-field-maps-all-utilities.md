# WUFO/WUFO_Field_Maps_All_Utilities

> WUFO Field Maps All Utilities Map Layers

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/WUFO/WUFO_Field_Maps_All_Utilities/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=WUFO_WUFO_Field_Maps_All_Utilities
- **Created:** None  ·  **Item modified:** None
- **Tags:** WUFO

## Publisher description

WUFO Field Maps All Utilities Map Layers

## Layer 0: Map Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 1: Address Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 2: Used Address Labels

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
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 3: Base Address Labels

- **Records:** 1,047,380
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `BASEADDRES` | Integer |  |  |
| `BASEADDR_1` | String |  | len 1 |
| `BASEADDR_2` | Integer |  |  |
| `BASELINEID` | Integer |  |  |
| `BASELINESI` | String |  | len 1 |
| `EVENODD` | String |  | len 1 |
| `ADDRESSNUM` | Integer |  |  |
| `GEONAMEID` | Integer |  |  |
| `GEONAME` | String |  | len 45 |
| `ADDRESS` | String |  | len 100 |
| `STATEFIPS` | String |  | len 3 |
| `STATE` | String |  | len 2 |
| `COUNTYFIPS` | String |  | len 3 |
| `COUNTY` | String |  | len 25 |
| `SUBCOUNTYF` | String |  | len 5 |
| `SUBCOUNTY` | String |  | len 25 |
| `PLACEFIPS` | String |  | len 5 |
| `PLACE` | String |  | len 25 |
| `USPS_CITY` | String |  | len 25 |
| `USPS_ZIPCO` | String |  | len 5 |
| `USPS_ZIPPL` | String |  | len 4 |
| `USPS_CARRI` | String |  | len 4 |
| `USPS_BUSIN` | String |  | len 40 |
| `GOV_BLG_FG` | String |  | len 1 |
| `MUNCSKEY` | String |  | len 6 |
| `USPSID` | Integer |  |  |
| `URBCSKEY` | String |  | len 6 |
| `LASTLINE` | String |  | len 6 |
| `FINANCENUM` | String |  | len 6 |
| `RECTYPCODE` | String |  | len 1 |
| `CENSUS1980` | String |  | len 16 |
| `CENSUS1990` | String |  | len 16 |
| `CENSUS2000` | String |  | len 16 |
| `CENSUS2010` | String |  | len 16 |
| `PRIORITYBO` | String |  | len 2 |
| `PRIORITY_1` | String |  | len 10 |
| `PLANNINGDI` | String |  | len 8 |
| `PLANNING_1` | String |  | len 30 |
| `HISTORICDI` | String |  | len 3 |
| `HISTORIC_1` | String |  | len 25 |
| `ZONINGDIST` | String |  | len 5 |
| `ZONINGDI_1` | String |  | len 20 |
| `FLOODPLAIN` | String |  | len 10 |
| `PROTECTEDW` | String |  | len 10 |
| `LANDUSE` | String |  | len 10 |
| `HOUSINGDIS` | String |  | len 10 |
| `DGN_PANEL` | String |  | len 10 |
| `ORTHOQUAD` | String |  | len 10 |
| `GRID1000ID` | Integer |  |  |
| `GRID2000ID` | Integer |  |  |
| `X_COORD` | Integer |  |  |
| `Y_COORD` | Integer |  |  |
| `WCCOLLECTI` | String |  | len 10 |
| `WASTECOLLE` | Integer |  |  |
| `WCROUTENAM` | String |  | len 16 |
| `WCROUTERAD` | String |  | len 3 |
| `WCCOLLEC_1` | String |  | len 1 |
| `BULKWASTER` | Integer |  |  |
| `BULKROUTEN` | String |  | len 10 |
| `BULKROUTER` | String |  | len 3 |
| `BULKCOLLEC` | String |  | len 10 |
| `BULKZONENU` | String |  | len 1 |
| `BULKDAYNUM` | String |  | len 1 |
| `METALTIREL` | Integer |  |  |
| `METALROUTE` | Integer |  |  |
| `TIREROUTE` | Integer |  |  |
| `LTLOADERRO` | Integer |  |  |
| `METALTIR_1` | String |  | len 10 |
| `METALTIR_2` | Integer |  |  |
| `METALTIR_3` | Integer |  |  |
| `RECYCLEROU` | Integer |  |  |
| `RECYCLER_1` | String |  | len 10 |
| `RECYCLECOL` | String |  | len 10 |
| `RECYCLER_2` | Integer |  |  |
| `RECYCLEDAY` | Integer |  |  |
| `RECYCLEZON` | Integer |  |  |
| `CONTAINERR` | String |  | len 6 |
| `CONTAINE_1` | Integer |  |  |
| `CONTAINERD` | String |  | len 3 |
| `CONTAINE_2` | Integer |  |  |
| `CAD_ADDRES` | String |  | len 45 |
| `DPD_DISTRI` | String |  | len 25 |
| `DPD_DIST_1` | String |  | len 10 |
| `DPD_BEAT` | String |  | len 10 |
| `DPD_DFD_SE` | String |  | len 3 |
| `DFD_DISTRI` | String |  | len 10 |
| `DPD_DIST_2` | String |  | len 5 |
| `CODEADDR` | String |  | len 102 |
| `MATCH1` | String |  | len 3 |
| `TEMP_CK` | String |  | len 10 |
| `PO_NAME` | String |  | len 28 |
| `STATE2` | String |  | len 2 |
| `SDE_DBO_BA` | Double |  |  |
| `SUMBLKPOP` | Double |  |  |
| `POP2001` | Double |  |  |
| `ZIP_PROB` | String |  | len 4 |
| `WCCOLLEC_2` | String |  | len 10 |
| `LEAFZONE` | String |  | len 5 |
| `ST_MAINTNC` | String |  | len 5 |
| `SNOW_ICE_R` | Integer |  |  |
| `SNOW_ICE_1` | Integer |  |  |
| `INTERSECT_` | String |  | len 10 |
| `DIF_CADSEC` | Integer |  |  |
| `CAD_FDSP` | String |  | len 6 |
| `CAD_PDSP` | String |  | len 6 |
| `FHZHR` | String |  | len 7 |
| `FSPOR` | String |  | len 7 |
| `FEHSD` | String |  | len 7 |
| `STREET_ID` | Integer |  |  |
| `FIRE_EH1` | String |  | len 3 |
| `FIRE_EH2` | String |  | len 3 |
| `FIRE_ORGNL` | String |  | len 2 |
| `MAP_SECTIO` | String |  | len 2 |
| `METAL_TIRE` | String |  | len 2 |
| `ADDRKEY` | Double |  |  |
| `STNO` | String |  | len 10 |
| `PREDIR` | String |  | len 3 |
| `STNAME` | String |  | len 28 |
| `SUFFIX` | String |  | len 4 |
| `POSTDIR` | String |  | len 3 |
| `STSUB` | String |  | len 16 |
| `CITY` | String |  | len 28 |
| `ZIP` | String |  | len 10 |
| `ST2NAME` | String |  | len 28 |
| `ST2POSTDIR` | String |  | len 3 |
| `ST2PREDIR` | String |  | len 3 |
| `ST2SUFFIX` | String |  | len 4 |
| `ST3NAME` | String |  | len 28 |
| `ST3POSTDIR` | String |  | len 3 |
| `ST3PREDIR` | String |  | len 3 |
| `ST3SUFFIX` | String |  | len 4 |
| `GEONAME_ID` | Integer |  |  |
| `AlternateA` | String |  | len 200 |
| `FullAddres` | String |  | len 254 |
| `FullSuffix` | String |  | len 50 |
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
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 4: Street Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 5: Street Name Labels

- **Records:** 76,466
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

## Layer 6: Alley Name Labels

- **Records:** 3,716
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

## Layer 7: Misc Street Name Labels

- **Records:** 864
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

## Layer 8: Mile Marker Labels

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

## Layer 9: Parcel Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 10: Key Parcel and Parcel Labels

- **Records:** 272,751
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
| `SHAPE` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 11: Parcel and Lot Number Labels

- **Records:** 272,751
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
| `SHAPE` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 12: Lot Number Labels

- **Records:** 272,751
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
| `SHAPE` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |

</details>

## Layer 13: Parcel Dimensions - Annotation Labels

- **Records:** 865,084
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FeatureID` | Integer | FEATUREID |  |
| `ZOrder` | Integer | ZORDER |  |
| `AnnotationClassID` | Integer | ANNOTATIONCLASSID |  |
| `SymbolID` | Integer | SYMBOLID |  |
| `Status` | SmallInteger | STATUS | **Values:** `0` = Placed; `1` = Unplaced |
| `TextString` | String | TEXTSTRING | len 255 |
| `FontName` | String | FONTNAME | len 255 |
| `FontSize` | Double | FONTSIZE |  |
| `Bold` | SmallInteger | BOLD | **Values:** `1` = Yes; `0` = No |
| `Italic` | SmallInteger | ITALIC | **Values:** `1` = Yes; `0` = No |
| `Underline` | SmallInteger | UNDERLINE | **Values:** `1` = Yes; `0` = No |
| `VerticalAlignment` | SmallInteger | VERTICALALIGNMENT | **Values:** `0` = Top; `1` = Center; `2` = Baseline; `3` = Bottom |
| `HorizontalAlignment` | SmallInteger | HORIZONTALALIGNMENT | **Values:** `0` = Left; `1` = Center; `2` = Right; `3` = Full |
| `XOffset` | Double | XOFFSET |  |
| `YOffset` | Double | YOFFSET |  |
| `Angle` | Double | ANGLE |  |
| `FontLeading` | Double | FONTLEADING |  |
| `WordSpacing` | Double | WORDSPACING |  |
| `CharacterWidth` | Double | CHARACTERWIDTH |  |
| `CharacterSpacing` | Double | CHARACTERSPACING |  |
| `FlipAngle` | Double | FLIPANGLE |  |
| `Override` | Integer | OVERRIDE |  |
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
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 159: Dim

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 160: Utility Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 161: Union Rd Wellfield Labels

- **Records:** 2
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PIN` | String |  | len 30 |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `ACRES` | Double |  |  |
| `TAXID` | String |  | len 5 |
| `BLOCKNUM` | String |  | len 5 |
| `TransCard` | String |  | len 30 |
| `TaxMail1` | String |  | len 50 |
| `TaxMail2` | String |  | len 40 |
| `TaxMail3` | String |  | len 50 |
| `Address1` | String |  | len 50 |
| `Address2` | String |  | len 40 |
| `Address3` | String |  | len 50 |
| `AnnexNotes` | String |  | len 50 |
| `ParlNote` | String |  | len 50 |
| `ParTrackpd` | String |  | len 25 |
| `LandImage` | String |  | len 25 |
| `OWNER1` | String |  | len 40 |
| `ADDRESSUNI` | String |  | len 40 |
| `DWELPICS` | String |  | len 30 |
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
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 162: Sanitary Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 163: Sanitary Manhole Label

- **Records:** 20,207
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERT` | Double | Invert |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `WALLMAT` | String | Wall Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 25 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String |  | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date |  |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String |  | len 16 |
| `MODELOWNER` | String |  | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String |  | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `BARLDIAM` | Double |  |  |
| `BASETYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer |  |  |
| `CONETYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double |  |  |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String |  | len 1 |
| `FRAMETYPE` | String |  | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double |  |  |
| `INTKEY` | Integer |  |  |
| `LOC` | String |  | len 4 |
| `MAPNO` | String |  | len 14 |
| `METERED` | String |  | len 1 |
| `PRCLKEY` | Integer |  |  |
| `RINGSTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer |  |  |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String |  | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String |  | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 6 |
| `ZCOORD` | String |  | len 15 |
| `CHNGDT` | Date |  |  |
| `EXPBY` | String |  | len 12 |
| `EXPDATE` | Date |  |  |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String |  | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
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

## Layer 164: Sanitary Forced Main Size Label

- **Records:** 38
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 20 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `EDITORNAME` | String | EditorName | len 50 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `INSTDATE` | Date | Installed |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLP` | Double | Slope |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 165: Sanitary Main Size Label

- **Records:** 20,998
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `root_treated` | String |  | len 10 |
| `date_treated` | Date |  |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 166: Storm Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 167: Outfall Labels

- **Records:** 542
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `AVGDISCH` | String | Average Discharge | len 10 |
| `DISCHID` | String | Discharge Identifier | len 20 |
| `DISCHRGTYP` | String | Discharge Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `OVERFLOW` = OVERFLOW · len 50 |
| `PEAKDISCH` | String | Peak Discharge | len 10 |
| `PERMIT` | String | Permitted | len 30 |
| `PERMITID` | String | Permit Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Outfall ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION_1` | Integer | ROTATION |  |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BARLDIAM` | Double | Barrel Diameter |  |
| `BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double | Cover Diameter |  |
| `CVRTYPE` | String | Cover Type | **Values:** `DUC` = DUCTILE; `BOL` = BOLTED; `PRE` = PRESSURE; `MLT` = MULTI-HOLE; `FOR` = FOUR-HOLE; `TWO` = TWO-HOLE; `SID` = SIDE SLOTS-SOLID; `PIC` = CONCEALED PICKHOLES; `OTH` = OTHER · len 4 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double | Dist To Hydrant |  |
| `INTKEY` | Integer | Intersection |  |
| `METERED` | String | Metered | len 1 |
| `MHDPTH` | Double | Manhole Depth |  |
| `PRCLKEY` | Integer | Parcel |  |
| `RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer | Street Segemt Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `WALLTYPE` | String | Wall Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `IMAGE01` | String | Image01 | len 100 |
| `IMAGE02` | String | Image02 | len 100 |
| `IMAGE03` | String | Image03 | len 100 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `BACKFLOW` | String | Backflow | len 5 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `DEST` | String |  | **Values:** `Primary` = Primary; `Secondary` = Secondary; `Not in Dayton` = Not in Dayton; `Does Not Exist` = Does Not Exist; `Other` = Other; `N/A` = N/A · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 168: Storm Manhole Label

- **Records:** 14,939
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `INVERT` | Double | Invert |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 50 |
| `WALLMAT` | String | Wall Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 25 |
| `MHTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `INSIDE DROP` = INSIDE DROP; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFALL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 15 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `LOCDESC` | String | Location Description | len 200 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String |  | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date |  |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Integer |  |  |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `BARLDIAM` | Double |  |  |
| `BASETYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer |  |  |
| `CONETYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double |  |  |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String |  | len 1 |
| `FRAMETYPE` | String |  | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double |  |  |
| `INTKEY` | Integer |  |  |
| `METERED` | String |  | len 1 |
| `MHDPTH` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `RINGSTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer |  |  |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String |  | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String |  | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger |  |  |
| `LININGTYPE` | String |  | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
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

## Layer 169: Storm Inlet Label

- **Records:** 22,550
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `INLETTYPE` | String | Inlet Type | **Values:** `OTM` = OPEN TOP MANHOLE; `DAD` = DOUBLE ALLEY DRIP (TYPE E); `GINLET` = GRATE INLET; `EEAD` = END TO END ALLEY DRIP (TYPE C); `CCB` = CURB CATCH BASIN; `CINLET` = CURB INLET; `SAD` = SINGLE ALLEY DRIP; `CATBSN` = CATCH BASIN; `HEDWAL` = HEAD WALL; `DWNSP` = DOWNSPOUT; `DWTRWL` = DEWATERING WELL; `CULVERT` = CULVERT · len 50 |
| `ACCESSDIAM` | Double | Access Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `INVERTELEV` | Double | Invert Elevation |  |
| `ACCESSMAT` | String | Access Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `ACCESSTYPE` | String | Access Type | **Values:** `Door` = Door; `Grate` = Grate; `Cover` = Cover; `Hand` = Hand; `Lid` = Lid; `Unknown` = Unknown · len 20 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Inlet ID | len 16 |
| `COMPTYPE` | Double |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Integer |  |  |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONNLEN` | Double | Connection Length |  |
| `CONNPIPETY` | String | Connection Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 6 |
| `CONNSZ` | Double | Connection Pipe Size |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DWNCONN` | String | Connection Type | len 4 |
| `DWNDIR` | String | Inlet Direction | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DWNDIS` | Double | Inlet Distance |  |
| `DWNFR` | String | Inlet Distance From | len 2 |
| `DWNINV` | Double | Downstream Invert |  |
| `DWNSTINKEY` | Integer | Connections Inlet ID |  |
| `GRATETYPE` | String | Grate Type | len 6 |
| `INLDPTH` | Double | Inlet Depth |  |
| `INLLEN` | Double | Length |  |
| `INLWID` | Double | Width |  |
| `INTKEY` | Integer | Intersection |  |
| `LOC` | String | Location Information | len 4 |
| `MAINKEY` | Integer | Main |  |
| `MATL` | String | Material | len 6 |
| `OUTLDPTH` | Double | Outlet Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UPSINV` | Double | Upstream Invert |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
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

## Layer 170: Storm Main Size Label

- **Records:** 40,862
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `PARLINENO` | String |  | len 1 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `COMPTYPE` | Double |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `HANSENID` | String | Hansen ID | len 50 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Dwn | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MAPNO` | String | Map # | len 14 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `DWNELEV_NAVD88` | Double | Down MH Invert Elevation NAVD88 |  |
| `UPSELEV_NAVD88` | Double | Up MH Invert Elevation NAVD88 |  |
| `FROMMH_LONGER` | String |  | len 50 |
| `TOMH_LONGER` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `DirFlowUpdate` | String | Direction of Flow Updated | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 171: Water Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 172: Water Network Structure Labels

- **Records:** 962
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
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
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

## Layer 173: Water Control Valve Label

- **Records:** 203
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double |  |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date |  |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `COMPLEXKEY` | Integer |  |  |
| `DIR` | String |  | len 1 |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `ELEV` | Double |  |  |
| `HIGHPRES` | Double |  |  |
| `INTKEY` | Integer |  |  |
| `LOWPRES` | Double |  |  |
| `MAINKEY` | Integer |  |  |
| `MFGKEY` | Integer |  |  |
| `MODELNO` | String |  | len 20 |
| `NOTURNS` | String |  | len 6 |
| `OBST` | String |  | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `PRESZONE` | String |  | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer |  |  |
| `SERNO` | String |  | len 20 |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer |  |  |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String |  | len 6 |
| `VALVESTAT` | String |  | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 174: Water Curb Stop Valve Label

- **Records:** 4,825
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double |  |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date |  |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `COMPLEXKEY` | Integer |  |  |
| `DIR` | String |  | len 1 |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `ELEV` | Double |  |  |
| `HIGHPRES` | Double |  |  |
| `INTKEY` | Integer |  |  |
| `LOWPRES` | Double |  |  |
| `MAINKEY` | Integer |  |  |
| `MFGKEY` | Integer |  |  |
| `MODELNO` | String |  | len 20 |
| `NOTURNS` | String |  | len 6 |
| `OBST` | String |  | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `PRESZONE` | String |  | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer |  |  |
| `SERNO` | String |  | len 20 |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer |  |  |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String |  | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
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

## Layer 175: Water Valve Label

- **Records:** 22,930
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double |  |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `Ball` = Ball; `Butterfly` = Butterfly; `Cone` = Cone; `Gate` = Gate; `Plug` = Plug; `Roundway` = Roundway; `Other` = Other; `Unknown` = Unknown · len 30 |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `HYDRFLAG` | SmallInteger | Hydrant Valve | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `COMPLEXKEY` | Integer |  |  |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `ELEV` | Double |  |  |
| `HIGHPRES` | Double |  |  |
| `INTKEY` | Integer |  |  |
| `LOWPRES` | Double |  |  |
| `MAINKEY` | Integer |  |  |
| `MFGKEY` | Integer |  |  |
| `MODELNO` | String |  | len 20 |
| `OBST` | String |  | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `PRESZONE` | String |  | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer |  |  |
| `SERNO` | String |  | len 20 |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer |  |  |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String |  | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
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

## Layer 176: Water Hydrant Label

- **Records:** 6,099
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double |  |  |
| `MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `LASTSERVICE` | Date | Last Service Date |  |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date |  |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `FLOW` | Double | Flow Rate (GPM) |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `AUXVALVE` | String |  | len 1 |
| `BARRELSIZE` | Double |  |  |
| `COMPLEXKEY` | Integer |  |  |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FEEDERDIAM` | Double |  |  |
| `FEEDERLEN` | Double |  |  |
| `FEEDERTYPE` | String |  | **Values:** `0` = No Code · len 6 |
| `HT` | Double |  |  |
| `INTKEY` | Integer |  |  |
| `MAINKEY` | Integer |  |  |
| `MFGKEY` | Integer |  |  |
| `MODELNO` | String |  | len 20 |
| `OBST` | String |  | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OUTLSZ1` | Double |  |  |
| `OUTLSZ2` | Double |  |  |
| `OUTLSZ3` | Double |  |  |
| `OUTLSZ4` | Double |  |  |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PACKING` | String |  | **Values:** `0` = No Code · len 4 |
| `PAINTTYPE` | String |  | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 8 |
| `PRCLKEY` | Integer |  |  |
| `PRESZONE` | String |  | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SEGKEY` | Integer |  |  |
| `SERNO` | String |  | len 20 |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer |  |  |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `WVKEY` | Integer |  |  |
| `ZCOORD` | String |  | len 15 |
| `COLOR` | String |  | **Values:** `BLUE` = BLUE - LOW; `GREEN` = GREEN - HIGH; `ORANGE` = ORANGE - MEDIUM · len 8 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `INSPECTIONGROUP` | String |  | len 50 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `ADDRESS` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 177: Water Main Size Label

- **Records:** 57,556
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `UNITID` | String | Main ID 1 | len 20 |
| `UNITID2` | String | Main ID 2 | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
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
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CLASS` | String | Pipe Class | **Values:** `51` = CLASS 51; `53` = CLASS 53 · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 179: Flood Plain Labels

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
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 180: Intersection Labels

- **Records:** 4,729
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INTERSECTION_ENTITY` | String | ENTITY | len 16 |
| `STREET1` | String |  | len 30 |
| `STREET2` | String |  | len 30 |
| `STREET3` | String |  | len 20 |
| `STREET4` | String |  | len 20 |
| `STREET5` | String |  | len 20 |
| `DWG` | String |  | len 8 |
| `REVISION` | Date |  |  |
| `COMMENTS` | String |  | len 50 |
| `FULLPATH` | String |  | len 64 |
| `EXT` | String |  | len 3 |
| `ATLAS` | String |  | len 3 |
| `PLANIMET` | String |  | len 10 |
| `MSLINK` | Integer |  |  |
| `XCOORDINAT` | String |  | len 40 |
| `YCOORDINAT` | String |  | len 40 |
| `WEBPATH` | String |  | len 150 |
| `GISADMIN_Intersection_LEN` | Double | LEN |  |
| `DISTANCE` | Double |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `MOBILEPATH` | String |  | len 150 |
| `DMSLINK` | String |  | len 150 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PortalLink` | String | Portal Link | len 400 |
| `TempWebLink` | String |  | len 150 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_12` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `OBJECTID_1` | Integer |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 181: Survey Data Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 182: Survey Control - '88 Labels

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
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 183: Survey Control - All Labels

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
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 185: Survey Project Labels

- **Records:** 342
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `JOBNUMBER` | String |  | len 50 |
| `SURVEYYEAR` | SmallInteger |  |  |
| `COMMENTS` | String |  | len 255 |
| `PWJOB` | SmallInteger | PWJob |  |
| `FILEPATH` | String |  | len 1073741822 |
| `PDFPATH` | String |  | len 255 |
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

## Layer 186: Completed Level Circuit Labels

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
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 187: Proposed Level Circuit Labels

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
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 188: Recorded Plat - Annotation Labels

- **Records:** 22,764
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FeatureID` | Integer | FEATUREID |  |
| `ZOrder` | Integer | ZORDER |  |
| `AnnotationClassID` | Integer | ANNOTATIONCLASSID |  |
| `SymbolID` | Integer | SYMBOLID |  |
| `Status` | SmallInteger | STATUS | **Values:** `0` = Placed; `1` = Unplaced |
| `RECPLAT_` | Integer |  |  |
| `RECPLAT_ID` | Integer |  |  |
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

## Layer 189: Default

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 190: Default_1

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 191: Default_2

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 192: Recorded Survey - Annotation Labels

- **Records:** 22,764
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FeatureID` | Integer |  |  |
| `ZOrder` | Integer |  |  |
| `AnnotationClassID` | Integer |  |  |
| `SymbolID` | Integer |  |  |
| `Status` | SmallInteger |  | **Values:** `0` = Placed; `1` = Unplaced |
| `RECPLAT_` | Integer |  |  |
| `RECPLAT_ID` | Integer |  |  |
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

## Layer 193: Default

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 194: Default_1

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 195: Default_2

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 196: Recorded Plat Labels

- **Records:** 10,688
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ACAD_COLOR` | SmallInteger |  |  |
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
| `SUBNAME` | String |  | len 75 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 197: Edge of Pavement

- **Records:** 5,109
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `TYPE` | SmallInteger |  | **Values:** `0` = PAVED; `1` = UNPAVED; `2` = NO DATA |
| `SOURCE` | SmallInteger |  | **Values:** `0` = HISTORICAL DOCUMENTS; `1` = AERIAL PHOTOGRAPHY; `3` = LIDAR; `2` = COUNTY FC |
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
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 198: Utilities

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 199: Water

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 200: Water Hydrants

- **Records:** 6,099
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `UNITID` | String | Hydrant ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `BARRELSIZE` | Double | Barrel Size |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FEEDERDIAM` | Double | Feeder Diameter |  |
| `FEEDERLEN` | Double | Feeder Length |  |
| `HT` | Double | Height |  |
| `MODELNO` | String | Model # | len 20 |
| `OUTLSZ1` | Double | Size of Outlet1 |  |
| `OUTLSZ2` | Double | Size of Outlet2 |  |
| `OUTLSZ3` | Double | Size of Outlet3 |  |
| `OUTLSZ4` | Double | Size of Outlet4 |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `ZCOORD` | String | Z Coord | len 15 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `INSPECTIONGROUP` | String |  | len 50 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `ADDRESS` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 201: Water Meters

- **Records:** 438
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `ACCOUNTID` | String | Account Number | len 30 |
| `METSERVICE` | String | Metered Service | len 5 |
| `SERVICETYPE` | String | Service Type | **Values:** `Domestic` = Domestic; `Commercial` = Commercial; `Industrial` = Industrial; `Fire` = Fire; `Other` = Other; `Unknown` = Unknown · len 50 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `LOCATIONID` | String | Location Identifier | len 20 |
| `CRITICAL` | SmallInteger | CriticalCustomer | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Meter ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `AVGMONUSG` | Double | Average Monthly Usage |  |
| `BYPASS` | String | Bypass | len 1 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `INTKEY` | Integer | Intersection |  |
| `MAINKEY` | Integer | Main |  |
| `METERSZ` | Double | Meter Size |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NODIALS` | Integer | Number of Dials |  |
| `PRCLKEY` | Integer | Parcel |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `REMMFGKEY` | Integer | Remote Manufacturer |  |
| `REMSERNO` | String | Remote Serial # | len 20 |
| `SEALNO` | String | Seal # | len 20 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Meter Type | **Values:** `DISC` = DISC; `PISTN` = PISTON; `MLJET` = MULTIJET; `TURHR` = TURBINE HORIZONTAL; `TURVR` = TURBINE VERTICAL; `COMPS` = COMPOUND SINGLE DIAL; `COMPD` = COMPOUND TWO DIAL; `COMPT` = COMPOUND THREE DIAL; `ELECT` = ELECTRONIC TRANSDUCER; `MAGNT` = MAGNETIC; `VENT` = VENTURIE; `FIRE` = FIRE; …(+4 more) · len 6 |
| `USGDATE` | Date |  |  |
| `USGTOT` | Double | Total Usage |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `ACCTNO` | String | Account # | len 24 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `ERTNO` | String | ERT # | len 16 |
| `ERTTYPE` | String | ERT Type | **Values:** `0` = No Code · len 8 |
| `OUTFORREAD` | String | Out for Reading | len 1 |
| `METERCOMP` | String | Component | len 4 |
| `POSITION` | Integer | Position |  |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
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

## Layer 202: Water Pumps

- **Records:** 213
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `PUMPTYPE` | String | Pump Type | **Values:** `Axial Flow` = Axial Flow; `Centrifugal` = Centrifugal; `Jet` = Jet; `Reciprocating` = Reciprocating; `Rotary` = Rotary; `Turbine` = Turbine; `Other` = Other; `Unknown` = Unknown · len 50 |
| `LOCDESC` | String | Location Description | len 200 |
| `RATEDFLOW` | String | Rated Flow | len 20 |
| `DYNHEAD` | String | Total Dynamic Head | len 20 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `UNITID` | String | Pump ID | len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `FLOW` | Double | Flow |  |
| `MODELNO` | String | Model # | len 20 |
| `MOSERNO` | String | Motor Serial # | len 20 |
| `PMRPM` | String | RPM's | len 7 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SERNO` | String | Serial # | len 20 |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `USGDATE` | Date |  |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 203: Curb Stop Valves

- **Records:** 4,825
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `UNITID` | String | Valve ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 204: Water Control Valves

- **Records:** 203
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `UNITID` | String | Valve ID | len 16 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DIR` | String | Direction To Open | len 1 |
| `MODELNO` | String | Model # | len 20 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String |  | len 6 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 205: Water System Valves

- **Records:** 22,930
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `Ball` = Ball; `Butterfly` = Butterfly; `Cone` = Cone; `Gate` = Gate; `Plug` = Plug; `Roundway` = Roundway; `Other` = Other; `Unknown` = Unknown · len 30 |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `HYDRFLAG` | SmallInteger | Hydrant Valve | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `UNITID` | String | Valve ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `ValveCriticallity` | String |  | **Values:** `1` = Critical (Transmission Main Valves 16” and Larger) Exercise annually; `2` = Critical (Hospitals, nursing homes, schools etc.) Exercise annually; `3` = Non-Critical (12” through 4” normal system valves) Exercise on 5 year cycle · len 50 |
| `UtilNetFlag` | String |  | len 255 |
| `Recommendation` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 206: Production Wells

- **Records:** 114
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `NAME` | String | Name | len 20 |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `UNITID` | String | Well ID | len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STANDWAT` | Double | Std Water Level |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 207: Flow Meters

- **Records:** 75
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `NAME` | String | Name | len 20 |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `UNITID` | String | Well ID | len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STANDWAT` | Double | Std Water Level |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 208: Enclosed Storage Facilities

- **Records:** 14
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `NAME` | String | Name | len 20 |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `UNITID` | String | Well ID | len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STANDWAT` | Double | Std Water Level |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 209: Investigation Wells

- **Records:** 458
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `NAME` | String | Name | len 20 |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `UNITID` | String | Well ID | len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STANDWAT` | Double | Std Water Level |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 210: Early Warning Wells

- **Records:** 173
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `NAME` | String | Name | len 20 |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+5 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `UNITID` | String | Well ID | len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNFR` | String | Screen From | len 3 |
| `SCRNTO` | String | Screen To | len 3 |
| `SCRNTYPE` | String | Screen Type | **Values:** `SHUTT` = LAYNE STEEL SHUTTER SCREEN; `SSWW` = JOHNSON STAINLESS ST WIRE WND; `STRAIN` = COOK BRASS STRAINER SCREEN; `SHUTSS` = LAYNE SHUTTER STAINLESS STEEL; `WWSTL` = JOHNSON STEEL WIRE WOUND · len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STANDWAT` | Double | Std Water Level |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH · len 6 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `CAP` | Double | Capacity |  |
| `DPTH` | Double | Depth |  |
| `GROUNDELEV` | Double | Ground Elev |  |
| `OVERELEV` | Double | Overflow Elev |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field; `RRR` = Rip Rap Road Well Field · len 50 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 211: Water Hydrant Laterals

- **Records:** 6,645
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CRITSRV` | String | Critical Service | **Values:** `ADULT` = ANY AGES ADULT DAY CARE; `ALTA` = ALTA NURSING HOME; `CATMAN` = CATALPA MANOR NURSING CENTER; `DHEALT` = DAYTON HEALTH CARE CENTER; `EASTMAN` = EASTVIEW MANOR RESIDENTIAL CTR; `FORVIEW` = FOREST VIEW NURSING CENTER; `GOODSM` = GOOD SAMARITAN HOSP. & TRAUMA; `GRAFT` = GRAFTON OAKS NURSING CENTER; `GRNDVW` = GRANDVIEW HOSPITAL; `GRNHLT` = GRANDVIEW HEALTH CARE CENTER; `LOVCAR` = LOVING CARE NURSING CENTER; `MAPLE` = MAPLEVIEW MANOR; …(+7 more) · len 9 |
| `CURBSTOP` | String | Curb Stop Location | len 254 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `TAPLOC` | String | Water Tap Location | len 254 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `GISADMIN.wLateralLine.LEN` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `PRVT_MATERIAL` | String | Private Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 212: Water Services

- **Records:** 59,203
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `LINETYPE` | String | Line Type | **Values:** `Hydrant` = Hydrant; `Irrigation` = Irrigation; `Other` = Other; `Unknown` = Unknown; `Domestic` = Domestic; `Fire` = Fire; `Industrial` = Industrial; `Commercial` = Commercial · len 30 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CRITSRV` | String | Critical Service | **Values:** `ADULT` = ANY AGES ADULT DAY CARE; `ALTA` = ALTA NURSING HOME; `CATMAN` = CATALPA MANOR NURSING CENTER; `DHEALT` = DAYTON HEALTH CARE CENTER; `EASTMAN` = EASTVIEW MANOR RESIDENTIAL CTR; `FORVIEW` = FOREST VIEW NURSING CENTER; `GOODSM` = GOOD SAMARITAN HOSP. & TRAUMA; `GRAFT` = GRAFTON OAKS NURSING CENTER; `GRNDVW` = GRANDVIEW HOSPITAL; `GRNHLT` = GRANDVIEW HEALTH CARE CENTER; `LOVCAR` = LOVING CARE NURSING CENTER; `MAPLE` = MAPLEVIEW MANOR; …(+7 more) · len 9 |
| `CURBSTOP` | String | Curb Stop Location | len 254 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `TAPLOC` | String | Water Tap Location | len 254 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `GISADMIN.wLateralLine.LEN` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `PRVT_MATERIAL` | String | Private Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 213: Water Mains

- **Records:** 57,556
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `UNITID` | String | Main ID 1 | len 20 |
| `UNITID2` | String | Main ID 2 | len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DPTH` | Double | Depth |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 214: Intersection Bubble

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
| `ATLAS` | String | Atlas | len 3 |
| `XCOORDINAT` | String | X Coordinate | len 40 |
| `YCOORDINAT` | String | Y Coordinate | len 40 |
| `WEBPATH` | String | Web Path | len 150 |
| `LASTUPDATE` | Date | Last Update |  |
| `MOBILEPATH` | String | Mobile Path | len 150 |
| `DMSLINK` | String | DMS Link | len 150 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PortalLink` | String | Portal Link | len 400 |
| `TempWebLink` | String |  | len 150 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_12` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 215: Water Pressure Zones

- **Records:** 14
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ZONENAME` | String | Pressure Zone Name | len 3 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 216: City View - Water

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 217: Water Mains

- **Records:** 9,974
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 218: Storm

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 219: Storm Inlets

- **Records:** 22,550
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `INLETTYPE` | String | Inlet Type | **Values:** `OTM` = OPEN TOP MANHOLE; `DAD` = DOUBLE ALLEY DRIP (TYPE E); `GINLET` = GRATE INLET; `EEAD` = END TO END ALLEY DRIP (TYPE C); `CCB` = CURB CATCH BASIN; `CINLET` = CURB INLET; `SAD` = SINGLE ALLEY DRIP; `CATBSN` = CATCH BASIN; `HEDWAL` = HEAD WALL; `DWNSP` = DOWNSPOUT; `DWTRWL` = DEWATERING WELL; `CULVERT` = CULVERT · len 50 |
| `ACCESSDIAM` | Double | Access Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `INVERTELEV` | Double | Invert Elevation |  |
| `ACCESSMAT` | String | Access Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `ACCESSTYPE` | String | Access Type | **Values:** `Door` = Door; `Grate` = Grate; `Cover` = Cover; `Hand` = Hand; `Lid` = Lid; `Unknown` = Unknown · len 20 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Inlet ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONNLEN` | Double | Connection Length |  |
| `CONNPIPETY` | String | Connection Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 6 |
| `CONNSZ` | Double | Connection Pipe Size |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DWNCONN` | String | Connection Type | len 4 |
| `DWNDIR` | String | Inlet Direction | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DWNDIS` | Double | Inlet Distance |  |
| `DWNFR` | String | Inlet Distance From | len 2 |
| `DWNINV` | Double | Downstream Invert |  |
| `DWNSTINKEY` | Integer | Connections Inlet ID |  |
| `GRATETYPE` | String | Grate Type | len 6 |
| `INLDPTH` | Double | Inlet Depth |  |
| `INLLEN` | Double | Length |  |
| `INLWID` | Double | Width |  |
| `INTKEY` | Integer | Intersection |  |
| `LOC` | String | Location Information | len 4 |
| `MAINKEY` | Integer | Main |  |
| `MATL` | String | Material | len 6 |
| `OUTLDPTH` | Double | Outlet Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UPSINV` | Double | Upstream Invert |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 220: Storm Manholes

- **Records:** 14,939
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `INVERT` | Double | Invert |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 50 |
| `WALLMAT` | String | Wall Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 25 |
| `MHTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `INSIDE DROP` = INSIDE DROP; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFALL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 15 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `LOCDESC` | String | Location Description | len 200 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String | Lined | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Manhole ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BARLDIAM` | Double | Barrel Diameter |  |
| `BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double | Cover Diameter |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double | Dist To Hydrant |  |
| `INTKEY` | Integer | Intersection |  |
| `METERED` | String | Metered | len 1 |
| `MHDPTH` | Double | Manhole Depth |  |
| `PRCLKEY` | Integer | Parcel |  |
| `RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer | Street Segemt Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 221: Outfalls

- **Records:** 542
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `AVGDISCH` | String | Average Discharge | len 10 |
| `DISCHID` | String | Discharge Identifier | len 20 |
| `DISCHRGTYP` | String | Discharge Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `OVERFLOW` = OVERFLOW · len 50 |
| `PEAKDISCH` | String | Peak Discharge | len 10 |
| `PERMIT` | String | Permitted | len 30 |
| `PERMITID` | String | Permit Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Outfall ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION_1` | Integer | ROTATION |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BARLDIAM` | Double | Barrel Diameter |  |
| `BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double | Cover Diameter |  |
| `CVRTYPE` | String | Cover Type | **Values:** `DUC` = DUCTILE; `BOL` = BOLTED; `PRE` = PRESSURE; `MLT` = MULTI-HOLE; `FOR` = FOUR-HOLE; `TWO` = TWO-HOLE; `SID` = SIDE SLOTS-SOLID; `PIC` = CONCEALED PICKHOLES; `OTH` = OTHER · len 4 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double | Dist To Hydrant |  |
| `INTKEY` | Integer | Intersection |  |
| `METERED` | String | Metered | len 1 |
| `MHDPTH` | Double | Manhole Depth |  |
| `PRCLKEY` | Integer | Parcel |  |
| `RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer | Street Segemt Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `WALLTYPE` | String | Wall Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `IMAGE01` | String | Image01 | len 100 |
| `IMAGE02` | String | Image02 | len 100 |
| `IMAGE03` | String | Image03 | len 100 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `BACKFLOW` | String | Backflow | len 5 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `DEST` | String |  | **Values:** `Primary` = Primary; `Secondary` = Secondary; `Not in Dayton` = Not in Dayton; `Does Not Exist` = Does Not Exist; `Other` = Other; `N/A` = N/A · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 222: Storm Network Structures

- **Records:** 32
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Diversion Chamber` = Diversion Chamber; `Diversion Point` = Diversion Point; `Junction Chamber` = Junction Chamber; `Pump Station` = Pump Station; `Split Manhole` = Split Manhole; `Storage Basin` = Storage Basin; `Tide Chamber` = Tide Chamber; `Lift Station` = Lift Station; `Discharge Structure` = Discharge Structure; `Unknown` = Unknown; `Other` = Other; `Virtual Junction` = Virtual Junction · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Lift Station ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `LSDESC` | String | Lift Station Description | len 30 |
| `MAINKEY` | Integer | Main Type |  |
| `MODELNO` | String | Model # | len 20 |
| `NOPUMPS` | Integer | # of Pumps |  |
| `OVFLELEV` | Double | Overflow Elevation |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUDISSIZE` | Double | Pump Discharge Size |  |
| `PUMPCAP` | Double | Pump Capacity |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Lift Station Type | **Values:** `B` = STORM - DRAINAGE; `A` = STORM - FLOOD CONTROL; `SANI` = SANITARY; `STORM` = STORM; `FLOOD` = STORM - FLOOD CONTROL; `DRAIN` = STORM - DRAINAGE · len 6 |
| `WETWLELEV` | Double | Wet Well Elevation |  |
| `WETWLVOL` | Double | Wet Well Volume |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `NAME` | String | Name | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
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

## Layer 223: Storm System Valves

- **Records:** 68
- **Geometry:** Point

Storm System Valves

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
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `INVERTELEV` | Double | Invert Elevation |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String | Z Coord | len 15 |
| `INTKEY` | Integer | Intersection |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `ANCILLARYROLE` | SmallInteger | AncillaryRole | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 224: Storm Control Valves

- **Records:** 2
- **Geometry:** Point

Storm Control Valves

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `BFLY` = BUTTERFLY VALVE; `BLOFF` = BLOWOFF VALVE; `CHECK` = CHECK VALVE; `DCHCK` = DISCHARGE CHECK VALVE; `DISOL` = DISCHARGE ISOLATION VALVE; `GATE` = GATE VALVE; `GLOBE` = GLOBE VALVE; `BALL` = BALL VALVE; `RSWED` = RESILIENT WEDGE VALVE; `LAYDW` = LAY-DOWN VALVE; `BYPAS` = BYPASS GATE VALVE; `PIEDO` = PIEDOMETER VALVE; …(+16 more) · len 30 |
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
| `DIR` | String | Direction to Open | len 1 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `INVERTELEV` | Double | Invert Elevation |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NOTURNS` | String | # of Turns | len 6 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String | Z Coord | len 15 |
| `INTKEY` | Integer | Intersection |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `ANCILLARYROLE` | SmallInteger | AncillaryRole | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 225: Storm Fittings

- **Records:** 3,434
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `FITTINGTYPE` | String | Fitting Type | **Values:** `ANGLE` = < 45 DEGREE BEND; `ENDPT` = END POINT/PLUG; `JNT-T` = T-JOINT; `JNT-X` = CROSS JOINT; `VLV` = VALVE; `RED` = REDUCER; `45` = 45 DEGREE BEND; `90` = 90 DEGREE BEND; `SRV` = LARGE SERVICE LINE NODE; `JUNC` = JUNCTION CHAMBER; `PLUG` = MAIN LINE PLUG; `COUPLING` = COUPLING; …(+9 more) · len 50 |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer | Fitting ID |  |
| `UNITID` | String | Fitting ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTFRND` | Double | Node Location |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FRND` | String | From Node | len 1 |
| `INTKEY` | Integer | Intersection |  |
| `MAINKEY` | Integer | Main |  |
| `MAPNO` | String | Map # | len 14 |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `PRCLKEY` | Integer | Parcel |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 226: Storm Mains

- **Records:** 40,862
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `PARLINENO` | String |  | len 1 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `HANSENID` | String | Hansen ID | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Dwn | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MAPNO` | String | Map # | len 14 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `DWNELEV_NAVD88` | Double | Down MH Invert Elevation NAVD88 |  |
| `UPSELEV_NAVD88` | Double | Up MH Invert Elevation NAVD88 |  |
| `FROMMH_LONGER` | String |  | len 50 |
| `TOMH_LONGER` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `DirFlowUpdate` | String | Direction of Flow Updated | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 227: Outfall Areas

- **Records:** 556
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NOTES` | String | Notes | len 64 |
| `UNIT_ID` | String | Outfall ID | len 60 |
| `CODNOTES` | String | Comments | len 80 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 228: City View - Storm

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 229: Storm Network Structures

- **Records:** 32
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Diversion Chamber` = Diversion Chamber; `Diversion Point` = Diversion Point; `Junction Chamber` = Junction Chamber; `Pump Station` = Pump Station; `Split Manhole` = Split Manhole; `Storage Basin` = Storage Basin; `Tide Chamber` = Tide Chamber; `Lift Station` = Lift Station; `Discharge Structure` = Discharge Structure; `Unknown` = Unknown; `Other` = Other; `Virtual Junction` = Virtual Junction · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Lift Station ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `LSDESC` | String | Lift Station Description | len 30 |
| `MAINKEY` | Integer | Main Type |  |
| `MODELNO` | String | Model # | len 20 |
| `NOPUMPS` | Integer | # of Pumps |  |
| `OVFLELEV` | Double | Overflow Elevation |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUDISSIZE` | Double | Pump Discharge Size |  |
| `PUMPCAP` | Double | Pump Capacity |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Lift Station Type | **Values:** `B` = STORM - DRAINAGE; `A` = STORM - FLOOD CONTROL; `SANI` = SANITARY; `STORM` = STORM; `FLOOD` = STORM - FLOOD CONTROL; `DRAIN` = STORM - DRAINAGE · len 6 |
| `WETWLELEV` | Double | Wet Well Elevation |  |
| `WETWLVOL` | Double | Wet Well Volume |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `NAME` | String | Name | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 230: Storm Mains

- **Records:** 39,525
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `PARLINENO` | String |  | len 1 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `COMPTYPE` | Double |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `HANSENID` | String | Hansen ID | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Dwn | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MAPNO` | String | Map # | len 14 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `DWNELEV_NAVD88` | Double | Down MH Invert Elevation NAVD88 |  |
| `UPSELEV_NAVD88` | Double | Up MH Invert Elevation NAVD88 |  |
| `FROMMH_LONGER` | String |  | len 50 |
| `TOMH_LONGER` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `DirFlowUpdate` | String | Direction of Flow Updated | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 231: Outfall Areas

- **Records:** 556
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NOTES` | String | Notes | len 64 |
| `UNIT_ID` | String | Outfall ID | len 60 |
| `CODNOTES` | String | Comments | len 80 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 232: Sanitary

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 233: Sanitary Flow Meters

- **Records:** 67
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERT` | Double | Invert |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `WALLMAT` | String | Wall Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 25 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String | Lined | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Flow Meter ID | len 16 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `EDITORNAME` | String | EditorName | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BARLDIAM` | Double | Barrel Diameter |  |
| `BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double | Cover Diameter |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double | Dist to Hydrant |  |
| `INTKEY` | Integer | Intersection |  |
| `LOC` | String | Location Information | len 4 |
| `MAPNO` | String | Map # | len 14 |
| `METERED` | String | Metered | len 1 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 6 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `EXPBY` | String | Expired By | len 12 |
| `EXPDATE` | Date | Expired |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 234: Sanitary Network Structures

- **Records:** 115
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NAME` | String | Name | len 20 |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Diversion Chamber` = Diversion Chamber; `Diversion Point` = Diversion Point; `Junction Chamber` = Junction Chamber; `Production Well` = Production Well; `Pump Station` = Pump Station; `Split Manhole` = Split Manhole; `Storage Basin` = Storage Basin; `Tide Chamber` = Tide Chamber; `Treatment Plant` = Treatment Plant; `Lift Station` = Lift Station; `Discharge Structure` = Discharge Structure; `Unknown` = Unknown; …(+10 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Structure ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `LSDESC` | String | Lift Station Description | len 30 |
| `MAINKEY` | Integer | Main |  |
| `MODELNO` | String | Model # | len 20 |
| `NOPUMPS` | Integer | # of Pumps |  |
| `OVFLELEV` | Double | Overflow Elevation |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUDISSIZE` | Double | Pump Discharge Size |  |
| `PUMPCAP` | Double | Pump Capacity |  |
| `SEGKEY` | Integer | Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Lift Station Type | **Values:** `B` = STORM - DRAINAGE; `A` = STORM - FLOOD CONTROL; `SANI` = SANITARY; `STORM` = STORM; `FLOOD` = STORM - FLOOD CONTROL; `DRAIN` = STORM - DRAINAGE · len 6 |
| `WETWLELEV` | Double | Wet Well Elevation |  |
| `WETWLVOL` | Double | Wet Well Volume |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 235: Sanitary Meters

- **Records:** 34
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `FACILITYNAME` | String | Facility Name | len 100 |
| `LARGEMETER` | SmallInteger | Large Meter Flag | **Values:** `0` = False; `1` = True |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `ACCOUNTID` | String | Account Identifier | len 20 |
| `LOCATIONID` | String | Location Identifier | len 20 |
| `CRITICAL` | SmallInteger | Critical Customer | **Values:** `0` = False; `1` = True |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Sum Flow |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `ID` | Integer | Meter ID |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 236: Sanitary Manholes

- **Records:** 20,207
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERT` | Double | Invert |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `WALLMAT` | String | Wall Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 25 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String | Lined | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Manhole ID | len 16 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `EDITORNAME` | String | EditorName | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BARLDIAM` | Double | Barrel Diameter |  |
| `BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double | Cover Diameter |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double | Dist to Hydrant |  |
| `INTKEY` | Integer | Intersection |  |
| `LOC` | String | Location Information | len 4 |
| `MAPNO` | String | Map # | len 14 |
| `METERED` | String | Metered | len 1 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 6 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `EXPBY` | String | Expired By | len 12 |
| `EXPDATE` | Date | Expired |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 237: Sanitary Fittings

- **Records:** 514
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `FITTINGTYPE` | String | Fitting Type | **Values:** `ANGLE` = < 45 DEGREE BEND; `ENDPT` = END POINT/PLUG; `JNT-T` = T-JOINT; `JNT-X` = CROSS JOINT; `VLV` = VALVE; `RED` = REDUCER; `45` = 45 DEGREE BEND; `90` = 90 DEGREE BEND; `SRV` = LARGE SERVICE LINE NODE; `JUNC` = JUNCTION CHAMBER; `PLUG` = MAIN LINE PLUG; `COUPLING` = COUPLING; …(+9 more) · len 50 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Fitting ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `CADTYPE` | String |  | len 32 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTFRND` | Double | Node Location |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FRND` | String | From Node | len 1 |
| `INTKEY` | Integer | Intersection |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `PRCLKEY` | Integer | Parcel |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 238: Sanitary Clean Outs

- **Records:** 7
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DIR` | String | Direction to Open | len 1 |
| `DISTRICT` | String | District | len 4 |
| `INTKEY` | Integer | Intersection |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `LOC` | String | Location Information | len 4 |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NOTURNS` | String | # of Turns | len 6 |
| `OBST` | String | Obstruction | len 6 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESIZE` | Double | Valve Size |  |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `ACCESSMAT` | String | Access Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `ACESSTYPE` | String | Access Type | **Values:** `Door` = Door; `Grate` = Grate; `Cover` = Cover; `Hand` = Hand; `Lid` = Lid; `Unknown` = Unknown · len 20 |
| `INTDEPTH` | Double | Interior Depth |  |
| `DEVICETYPE` | String | Clean Out Type | **Values:** `Flushing Structure` = Flushing Structure; `Lamp Hole` = Lamp Hole; `Other` = Other; `Unknown` = Unknown; `CLNOUT` = Cleanout; `PLUG` = Plug; `SS` = Sampling Station; `BMSO` = Bridge Maint Service Outlet; `DRNWEL` = DRNWEL; `AS` = AS; `NONWRK` = NON WORK ORDER RELATED ISSUE; `SW` = SW; …(+1 more) · len 30 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 239: Sanitary System Valves

- **Records:** 134
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
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | len 4 |
| `INTKEY` | Integer | Intersection |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OBST` | String | Obstruction | len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
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

## Layer 240: Sanitary Control Valves

- **Records:** 154
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `BFLY` = BUTTERFLY VALVE; `BLOFF` = BLOWOFF VALVE; `CHECK` = CHECK VALVE; `DCHCK` = DISCHARGE CHECK VALVE; `DISOL` = DISCHARGE ISOLATION VALVE; `GATE` = GATE VALVE; `GLOBE` = GLOBE VALVE; `BALL` = BALL VALVE; `RSWED` = RESILIENT WEDGE VALVE; `LAYDW` = LAY-DOWN VALVE; `BYPAS` = BYPASS GATE VALVE; `PIEDO` = PIEDOMETER VALVE; …(+16 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DIR` | String | Direction to Open | len 1 |
| `DISTRICT` | String | District | len 4 |
| `INTKEY` | Integer | Intersection |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NOTURNS` | String | # of Turns | len 6 |
| `OBST` | String | Obstruction | len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 241: Sanitary Gravity Mains - Lining

- **Records:** 20,998
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `VERSIONNAME` | String | Version | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `root_treated` | String |  | len 10 |
| `date_treated` | Date |  |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 242: Sanitary Services

- **Records:** 50,230
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `LINETYPE` | String | Line Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 30 |
| `LOCDESC` | String | Location Description | len 50 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `DISTANCE` | Integer | Distance |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Service ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BLDGKEY` | Integer | Building |  |
| `CLNOUT` | String | CleanOut Loc | len 20 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `EPAID` | String | EPA ID # | len 12 |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MUNICOND` | String | Municipal Cond | **Values:** `DEAD` = DEAD/NOT WORKING; `DETR` = DETERIORATED; `FAIR` = FAIR; `GOOD` = GOOD; `NEW` = NEW; `POOR` = POOR; `SCHR` = SCHEDULE FOR REPLACEMENT · len 4 |
| `NOTAPS` | Integer | # of Taps |  |
| `NPDESID` | String | NPDES # | len 12 |
| `OWNCOND` | String | Owner Cond | **Values:** `DEAD` = DEAD/NOT WORKING; `DETR` = DETERIORATED; `FAIR` = FAIR; `GOOD` = GOOD; `NEW` = NEW; `POOR` = POOR; `SCHR` = SCHEDULE FOR REPLACEMENT · len 4 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PROPLNDPTH` | Double | Property Ln Depth |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SIC` | String |  | len 4 |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `TAPADDRKEY` | Integer | Tap Address |  |
| `TAPDIST` | Double | Tap Location |  |
| `TAPFROM` | String | From Node | len 1 |
| `UICID` | String | UIC ID # | len 14 |
| `UNITTYPE` | String | Service Line Type | **Values:** `COPPER` = COPPER; `DOMEST` = DOMESTIC; `FIRE` = FIRE; `IRRIGA` = IRRIGATION · len 6 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 243: Sanitary Force Mains

- **Records:** 38
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 20 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `INSTDATE` | Date | Installed |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLP` | Double | Slope |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 244: Sanitary Gravity Mains

- **Records:** 20,998
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `root_treated` | String |  | len 10 |
| `date_treated` | Date |  |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 245: Root Control Main

- **Records:** 2,147
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `root_treated` | String |  | len 10 |
| `date_treated` | Date |  |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 246: City View - Sanitary

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 247: Sanitary Flow Meters

- **Records:** 20,207
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERT` | Double | Invert |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `WALLMAT` | String | Wall Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 25 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String | Lined | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `COMPKEY` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Flow Meter ID | len 16 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BARLDIAM` | Double | Barrel Diameter |  |
| `BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `CVRDIAM` | Double | Cover Diameter |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double | Dist to Hydrant |  |
| `INTKEY` | Integer | Intersection |  |
| `LOC` | String | Location Information | len 4 |
| `MAPNO` | String | Map # | len 14 |
| `METERED` | String | Metered | len 1 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 6 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `EXPBY` | String | Expired By | len 12 |
| `EXPDATE` | Date | Expired |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 248: Sanitary Network Structures

- **Records:** 115
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NAME` | String | Name | len 20 |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Diversion Chamber` = Diversion Chamber; `Diversion Point` = Diversion Point; `Junction Chamber` = Junction Chamber; `Production Well` = Production Well; `Pump Station` = Pump Station; `Split Manhole` = Split Manhole; `Storage Basin` = Storage Basin; `Tide Chamber` = Tide Chamber; `Treatment Plant` = Treatment Plant; `Lift Station` = Lift Station; `Discharge Structure` = Discharge Structure; `Unknown` = Unknown; …(+10 more) · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Structure ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `LSDESC` | String | Lift Station Description | len 30 |
| `MAINKEY` | Integer | Main |  |
| `MODELNO` | String | Model # | len 20 |
| `NOPUMPS` | Integer | # of Pumps |  |
| `OVFLELEV` | Double | Overflow Elevation |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PUDISSIZE` | Double | Pump Discharge Size |  |
| `PUMPCAP` | Double | Pump Capacity |  |
| `SEGKEY` | Integer | Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UNITTYPE` | String | Lift Station Type | **Values:** `B` = STORM - DRAINAGE; `A` = STORM - FLOOD CONTROL; `SANI` = SANITARY; `STORM` = STORM; `FLOOD` = STORM - FLOOD CONTROL; `DRAIN` = STORM - DRAINAGE · len 6 |
| `WETWLELEV` | Double | Wet Well Elevation |  |
| `WETWLVOL` | Double | Wet Well Volume |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 249: Sanitary Force Mains

- **Records:** 32
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 20 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `INSTDATE` | Date | Installed |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLP` | Double | Slope |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 250: Sanitary Gravity Mains

- **Records:** 4,133
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Priority Board | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Neighborhood | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `root_treated` | String |  | len 10 |
| `date_treated` | Date |  |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 251: Areas of Interest

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 252: Used Address

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
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 253: Mile Markers

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

## Layer 254: Bike Routes

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

## Layer 255: Truck Routes

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
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 256: Atlas Grid

- **Records:** 511
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TEXT_1` | String | Atlas Number | len 254 |
| `WEBPATH` | String | Web Path | len 100 |
| `FULLPATH` | String | Full Path | len 75 |
| `EXT` | String | File Type | len 4 |
| `SANAPATH` | String | Sanitary Path | len 200 |
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

</details>

## Layer 257: Impervious Areas

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 258: Centroid

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

## Layer 259: Centroid Hooks

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

## Layer 260: Impervious Area

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

## Layer 261: Union Rd Wellfield

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
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 262: Well Fields

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 263: Well Head Operation Areas

- **Records:** 12
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `AREANAME` | String | Area Name | len 100 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 264: Water Protection District

- **Records:** 12
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `AREANAME` | String | Area Name | len 100 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 265: Water Resources

- **Records:** 1
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `AREANAME` | String | Area Name | len 100 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 266: Parcel Dimensions - Annotation Labels

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

## Layer 82: Dim

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 267: Parcels

- **Records:** 273,627
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
| `SHAPE` | Geometry |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |

</details>

## Layer 268: Survey Data

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 269: Survey Control High

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
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 270: Survey Control Low

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
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 271: Survey Control - '88 Elevations

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
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 272: Survey Project

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

## Layer 273: Completed Level Circuits

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
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 274: Proposed Level Circuits

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
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 276: Recorded Plat - Annotation Labels

- **Records:** 22,764
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FeatureID` | Integer |  |  |
| `ZOrder` | Integer |  |  |
| `AnnotationClassID` | Integer |  |  |
| `SymbolID` | Integer |  |  |
| `Status` | SmallInteger |  | **Values:** `0` = Placed; `1` = Unplaced |
| `RECPLAT_` | Integer |  |  |
| `RECPLAT_ID` | Integer |  |  |
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

## Layer 118: Default

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 119: Default_1

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 120: Default_2

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 277: Recorded Survey - Annotation Labels

- **Records:** 22,764
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FeatureID` | Integer |  |  |
| `ZOrder` | Integer |  |  |
| `AnnotationClassID` | Integer |  |  |
| `SymbolID` | Integer |  |  |
| `Status` | SmallInteger |  | **Values:** `0` = Placed; `1` = Unplaced |
| `RECPLAT_` | Integer |  |  |
| `RECPLAT_ID` | Integer |  |  |
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

## Layer 122: Default

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 123: Default_1

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 124: Default_2

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 278: Recorded Plat

- **Records:** 10,688
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ACAD_COLOR` | SmallInteger |  |  |
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
| `SUBNAME` | String |  | len 75 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 279: County Utilities

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 280: County Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 281: County Water System Valve Labels

- **Records:** 22,930
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
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
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
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
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

## Layer 282: County Water Hydrant Labels

- **Records:** 6,099
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `LASTSERVICE` | Date | Last Service Date |  |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `FLOW` | Double | Flow Rate (GPM) |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Hydrant ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
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
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `WVKEY` | Integer | Valve |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `COLOR` | String | Paint Color | **Values:** `BLUE` = BLUE - LOW; `GREEN` = GREEN - HIGH; `ORANGE` = ORANGE - MEDIUM · len 8 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `INSPECTIONGROUP` | String |  | len 50 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `ADDRESS` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 283: County Water Main Labels

- **Records:** 57,556
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `UNITID` | String | Main ID 1 | len 20 |
| `UNITID2` | String | Main ID 2 | len 20 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
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
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CLASS` | String | Pipe Class | **Values:** `51` = CLASS 51; `53` = CLASS 53 · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 284: County Sanitary Force Main Labels

- **Records:** 199
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LEGACYID` | String |  | len 20 |
| `ASSETMAINT` | String |  | len 90 |
| `JURISDICTI` | String |  | len 90 |
| `NOTES` | String |  | len 254 |
| `FACILITYID` | String |  | len 20 |
| `INSTALLDAT` | Date |  |  |
| `MATERIAL` | String |  | len 5 |
| `DIAMETER` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE_STLe` | Double |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 285: County Sanitary Gravity Main Labels

- **Records:** 33,026
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LEGACYID` | String |  | len 20 |
| `ASSETMAINT` | String |  | len 90 |
| `JURISDICTI` | String |  | len 90 |
| `NOTES` | String |  | len 254 |
| `SUBTYPECD` | Integer |  |  |
| `FACILITYID` | String |  | len 20 |
| `INSTALLDAT` | Date |  |  |
| `MATERIAL` | String |  | len 5 |
| `PERCENTSLO` | Double |  |  |
| `DIAMETER` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE_STLe` | Double |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 305: Administrative Boundaries

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 306: Building Footprint

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

## Layer 307: Dayton Corporation Boundary

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
| `OBJECTID_1` | OID |  |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 308: Neighborhood

- **Records:** 97
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN_N` | String |  | len 14 |
| `PRI_BOARD` | String | Priority Board | len 5 |
| `HOOD` | String | Neighborhood | len 50 |
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
| `Shape` | Geometry |  |  |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 309: County-City_Twp Boundaries

- **Records:** 33
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
| `OBJECTID_1` | OID |  |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 310: Centerline

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

## Layer 311: addressParcelCamaSL_VW

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

## Layer 312: addressSL_VW

- **Records:** 143,861

| Field | Type | Alias | Notes |
|---|---|---|---|
| `USEDADDRESS` | String |  | len 50 |
| `TAXPINNO` | String |  | len 20 |
| `K_PID` | String |  | len 20 |
| `STNO` | String |  | len 10 |

## Layer 313: CAMA

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

