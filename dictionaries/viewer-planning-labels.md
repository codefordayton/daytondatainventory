# Viewer/Planning_Labels

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Viewer/Planning_Labels/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Viewer_Planning_Labels
- **Created:** None  ·  **Item modified:** None
- **Tags:** Viewer

## Layer 0: Address Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 1: Used Address Labels

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

## Layer 2: Base Address Labels

- **Records:** 1,047,380
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `BASELINEID` | Integer |  |  |
| `EVENODD` | String |  | len 1 |
| `GEONAMEID` | Integer |  |  |
| `GEONAME` | String |  | len 45 |
| `ADDRESS` | String |  | len 100 |
| `STATEFIPS` | String |  | len 3 |
| `STATE` | String |  | len 2 |
| `COUNTYFIPS` | String |  | len 3 |
| `COUNTY` | String |  | len 25 |
| `SUBCOUNTY` | String |  | len 25 |
| `PLACEFIPS` | String |  | len 5 |
| `PLACE` | String |  | len 25 |
| `USPS_CITY` | String |  | len 25 |
| `GOV_BLG_FG` | String |  | len 1 |
| `MUNCSKEY` | String |  | len 6 |
| `USPSID` | Integer |  |  |
| `URBCSKEY` | String |  | len 6 |
| `LASTLINE` | String |  | len 6 |
| `FINANCENUM` | String |  | len 6 |
| `RECTYPCODE` | String |  | len 1 |
| `FLOODPLAIN` | String |  | len 10 |
| `LANDUSE` | String |  | len 10 |
| `DGN_PANEL` | String |  | len 10 |
| `ORTHOQUAD` | String |  | len 10 |
| `GRID1000ID` | Integer |  |  |
| `GRID2000ID` | Integer |  |  |
| `X_COORD` | Integer |  |  |
| `Y_COORD` | Integer |  |  |
| `METALROUTE` | Integer |  |  |
| `TIREROUTE` | Integer |  |  |
| `DPD_BEAT` | String |  | len 10 |
| `CODEADDR` | String |  | len 102 |
| `MATCH1` | String |  | len 3 |
| `TEMP_CK` | String |  | len 10 |
| `PO_NAME` | String |  | len 28 |
| `STATE2` | String |  | len 2 |
| `SUMBLKPOP` | Double |  |  |
| `POP2001` | Double |  |  |
| `ZIP_PROB` | String |  | len 4 |
| `LEAFZONE` | String |  | len 5 |
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
| `BASEADDRES` | Integer |  |  |
| `BASEADDR_1` | String |  | len 1 |
| `BASEADDR_2` | Integer |  |  |
| `BASELINESI` | String |  | len 1 |
| `ADDRESSNUM` | Integer |  |  |
| `SUBCOUNTYF` | String |  | len 5 |
| `USPS_ZIPCO` | String |  | len 5 |
| `USPS_ZIPPL` | String |  | len 4 |
| `USPS_CARRI` | String |  | len 4 |
| `USPS_BUSIN` | String |  | len 40 |
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
| `PROTECTEDW` | String |  | len 10 |
| `HOUSINGDIS` | String |  | len 10 |
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
| `DPD_DFD_SE` | String |  | len 3 |
| `DFD_DISTRI` | String |  | len 10 |
| `DPD_DIST_2` | String |  | len 5 |
| `SDE_DBO_BA` | Double |  |  |
| `WCCOLLEC_2` | String |  | len 10 |
| `ST_MAINTNC` | String |  | len 5 |
| `SNOW_ICE_R` | Integer |  |  |
| `SNOW_ICE_1` | Integer |  |  |
| `INTERSECT_` | String |  | len 10 |
| `MAP_SECTIO` | String |  | len 2 |
| `METAL_TIRE` | String |  | len 2 |
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

## Layer 3: Street Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 4: Street Name Labels

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

## Layer 5: Alley Name Labels

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

## Layer 6: Misc Street Name Labels

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

## Layer 7: Mile Marker Labels

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

## Layer 8: Areas of Interest Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 9: Landmark Building Labels

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

## Layer 10: Bike Route Labels

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

## Layer 11: Parcel Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 12: Key Parcel and Parcel Labels

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
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 13: Parcel and Lot Number Labels

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
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 14: Lot Number Labels

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
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 15: Parcel Dimensions - Annotation Labels

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

## Layer 16: Dim

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 17: Zoning Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 18: Flood Plain Labels

- **Records:** 29
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LEVEL_` | SmallInteger |  |  |
| `COLOR` | SmallInteger |  |  |
| `TEXT` | String |  | len 50 |
| `MSLINK_DBA` | Integer |  |  |
| `MSCTLG_DBA` | Integer |  |  |
| `LABEL` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 19: Planned Development Labels

- **Records:** 136
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `FEATURE` | String |  | len 16 |
| `DISTRICT` | String |  | len 16 |
| `YEAR` | Date |  |  |
| `ORDINANCE` | String |  | len 16 |
| `CPB` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 20: Urban Preservation Labels

- **Records:** 4
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `URBAN_RENE` | String |  | len 16 |
| `AREA_` | Double |  |  |
| `PERIMETER` | Double |  |  |
| `ACRES` | Double |  |  |
| `HECTARES` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 21: Historic District Labels

- **Records:** 20
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `FEATURE` | String |  | len 16 |
| `NAME` | String |  | len 16 |
| `DISTRICT` | String |  | len 16 |
| `YEAR` | Date |  |  |
| `ORDINANCE` | String |  | len 16 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 22: POD Labels

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
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 23: Graphics Overlay Labels

- **Records:** 3
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `LABEL` | String |  | len 30 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 24: Zoning District Labels

- **Records:** 970
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN_Plan_Zoning_AREA` | Double |  |  |
| `PERIMETER` | Double |  |  |
| `NEWZONING2` | Integer |  |  |
| `NEWZONIN_1` | Integer |  |  |
| `AREA_1` | Double |  |  |
| `PERIMETE_1` | Double |  |  |
| `NEWZONING_` | Integer |  |  |
| `NEWZONING1` | Integer |  |  |
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `DISTRICT` | String |  | len 5 |
| `MATCH_` | String |  | len 10 |
| `LAYER` | String |  | len 32 |
| `NEW_ZONE` | String |  | len 25 |
| `REZONED` | String |  | len 16 |
| `POLYGONID` | Integer |  |  |
| `SCALE` | Double |  |  |
| `ANGLE` | Integer |  |  |
| `DISTANCE` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE_LENG` | Double |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 25: Vacant Land Mowing Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 26: Vacant Land Inspections/Mowing Labels

- **Records:** 273,627
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
| `ACAD_COLOR` | Double |  |  |
| `TAXDISTRIC` | String |  | len 5 |
| `TAXBOOK` | String |  | len 4 |
| `TAXPAGE` | String |  | len 2 |
| `TAXSUF` | String |  | len 1 |
| `TAXINDEX` | String |  | len 4 |
| `SOURCEDOC` | String |  | len 20 |
| `SURVEY` | String |  | len 12 |
| `PID_FLG01` | String |  | len 10 |
| `LOC_AREA` | String |  | len 30 |
| `PID_VERIFY` | String |  | len 1 |
| `PID_STATUS` | Double |  |  |
| `CAMA_MATCH` | String |  | len 1 |
| `NBHD_1` | String |  | len 10 |
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
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 27: 2016 Abated Properties Labels

- **Records:** 273,627
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
| `ACAD_COLOR` | Double |  |  |
| `TAXDISTRIC` | String |  | len 5 |
| `TAXBOOK` | String |  | len 4 |
| `TAXPAGE` | String |  | len 2 |
| `TAXSUF` | String |  | len 1 |
| `TAXINDEX` | String |  | len 4 |
| `SOURCEDOC` | String |  | len 20 |
| `SURVEY` | String |  | len 12 |
| `PID_FLG01` | String |  | len 10 |
| `LOC_AREA` | String |  | len 30 |
| `PID_VERIFY` | String |  | len 1 |
| `PID_STATUS` | Double |  |  |
| `CAMA_MATCH` | String |  | len 1 |
| `NBHD_1` | String |  | len 10 |
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
| `SHAPE` | Geometry | Shape |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 28: Administrative Boundaries

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 29: CDBG Eligible Labels

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

## Layer 30: Neighborhood Low Labels

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

## Layer 31: Neighborhood High Labels

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

## Layer 32: County-City-Twp Boundary Labels

- **Records:** 33
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

## Layer 33: VLM_Inspection

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

## Layer 34: vlm_MowingVerification

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

## Layer 35: VLM_Inspection_UP__AT

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

