# Viewer/MapLabels_Citywide

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Viewer/MapLabels_Citywide/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Viewer_MapLabels_Citywide
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
| `AlternateA` | String |  | len 200 |
| `FullAddres` | String |  | len 254 |
| `FullSuffix` | String |  | len 50 |
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

## Layer 16: Dim

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 17: Easement Labels

- **Records:** 213,840
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REFERENCE` | String |  | len 31 |
| `ACAD_COLOR` | SmallInteger |  |  |
| `ACAD_TEXT` | String |  | len 20 |
| `DISTANCE` | Double |  |  |
| `WIDTH` | Double |  |  |
| `TYPE` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 18: Zoning Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 19: Flood Plain Labels

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

## Layer 20: Planned Development Labels

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

## Layer 21: Urban Preservation Labels

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

## Layer 22: Historic District Labels

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

## Layer 23: POD Labels

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

## Layer 24: Graphics Overlay Labels

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

## Layer 25: Zoning District Labels

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

## Layer 26: Utility Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 27: Street Light Labels

- **Records:** 20,691
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `NearestAddress` | String |  | len 100 |
| `Owner` | String |  | **Values:** `COD` = City of Dayton; `MVL` = Miami Valley Lighting; `Unknown` = Unknown; `Unknown-Tagged` = Unknown - Tag Added During Survey; `CODO` = City of Dayton-Other; `ODOT` = ODOT · len 30 |
| `PoleNumber` | String |  | len 15 |
| `Suffix` | String |  | **Values:** `A` = A; `B` = B; `C` = C; `D` = D; `E` = E; `F` = F · len 1 |
| `ExistingTagNumber` | String |  | len 15 |
| `PoleType` | String |  | **Values:** `Wood` = Wood; `Aluminum` = Aluminum; `Steel` = Steel; `Decorative` = Decorative; `Building Mount` = Building Mount; `Underpass Mount` = Underpass Mount; `Decorative Other` = Decorative Other · len 30 |
| `LuminaireHeight` | String |  | **Values:** `5` = 5; `10` = 10; `15` = 15; `20` = 20; `25` = 25; `30` = 30; `35` = 35; `40` = 40; `45` = 45; `50` = 50; `55` = 55; `60` = 60; …(+9 more) · len 50 |
| `LuminaireWattage` | String |  | **Values:** `5` = 5; `7` = 7; `10` = 10; `15` = 15; `17` = 17; `20` = 20; `25` = 25; `31` = 31; `40` = 40; `54` = 54; `73` = 73; `110` = 110; …(+16 more) · len 15 |
| `LuminaireArmLength` | String |  | **Values:** `2` = 2; `4` = 4; `6` = 6; `8` = 8; `10` = 10; `12` = 12; `14` = 14; `16` = 16; `18` = 18; `20` = 20; `22` = 22; `24` = 24; …(+6 more) · len 5 |
| `LuminaireBulbType` | String |  | **Values:** `Blue` = Blue; `Red` = Red; `Yellow` = Yellow; `White` = White; `Unknown` = Unknown; `Unreadable` = Unreadable; `LED No Sticker` = LED No Sticker; `N/A` = N/A · len 30 |
| `LensType` | String |  | **Values:** `Drop Globe` = Drop Globe; `Flat` = Flat; `Globe` = Globe; `N/A` = N/A · len 20 |
| `SurveyDate` | Date |  |  |
| `InstallationDate` | Date |  |  |
| `RepairDate` | Date | RepaireDate |  |
| `Comments` | String |  | len 100 |
| `StreetView` | String |  | len 254 |
| `Comments_QAQC` | String |  | len 100 |
| `OID_num` | SmallInteger |  |  |
| `OID_txt` | String |  | len 50 |
| `ENG_CHECK` | String |  | **Values:** `Y` = Yes; `N` = No · len 255 |
| `LED_PHASE` | String |  | len 10 |
| `Key_PoleNumber` | String |  | len 15 |
| `ArchiveYear` | SmallInteger |  |  |
| `ExpireDate` | Date |  |  |
| `NoPinsReceptacle` | SmallInteger | Number Pins Receptacle | **Values:** `0` = 0; `1` = 1; `3` = 3; `5` = 5; `7` = 7 |
| `Dimmable` | String |  | **Values:** `Y` = Yes; `N` = No · len 255 |
| `PoleStatus` | String | Pole Status | **Values:** `In Service` = In Service; `Down` = Down; `Missing` = Missing; `Tilting` = Tilting · len 25 |
| `PoleStatusDate` | Date |  |  |
| `SL_DIST` | String |  | len 50 |
| `SL_INT` | String |  | **Values:** `Y` = Yes; `N` = No · len 5 |
| `SL_HWAY` | String |  | **Values:** `Y` = Yes; `N` = No · len 5 |
| `LED` | String |  | **Values:** `Y` = Yes; `N` = No · len 5 |
| `Neighborhood` | String |  | **Values:** `Arlington Heights` = Arlington Heights; `Belmont` = Belmont; `Burkhardt` = Burkhardt; `Carillon` = Carillon; `College Hill` = College Hill; `Cornell Heights` = Cornell Heights; `Dayton View Triangle` = Dayton View Triangle; `DeWeese` = DeWeese; `Downtown` = Downtown; `Eastern Hills` = Eastern Hills; `Eastmont` = Eastmont; `Edgemont` = Edgemont; …(+54 more) · len 50 |
| `LightStatus` | String | Light Status | **Values:** `In Service` = In Service; `Out` = Out; `Cycling` = Cycling; `Flickering` = Flickering; `Other` = Other · len 25 |
| `LightStatusDate` | Date | Light Status Date |  |
| `PoleCondition` | String | Pole Condition | **Values:** `Needs Painted` = Needs Painted; `Needs Replaced` = Needs Replaced · len 25 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 28: Fiber Optic Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 29: Traffic Signals Labels

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

## Layer 30: Fiber End-Points Labels

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

## Layer 31: Fiber Lines Labels

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

## Layer 32: Union Rd Wellfield Labels

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
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 33: Sanitary Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 34: Sanitary Manhole Label

- **Records:** 20,207
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
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
| `LASTUPDATE` | Date |  |  |
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
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | String |  | len 15 |
| `CHNGDT` | Date |  |  |
| `EXPBY` | String |  | len 12 |
| `EXPDATE` | Date |  |  |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String |  | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String |  | len 3 |
| `DATELINED` | Date |  |  |
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
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 35: Sanitary Forced Main Size Label

- **Records:** 38
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPESHP` | String |  | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 20 |
| `PIPETYPE` | String |  | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String |  | len 16 |
| `UNITID2` | String |  | len 16 |
| `UNITTYPE` | String |  | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 18 |
| `MODELOWNER` | String |  | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String |  | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String |  | len 50 |
| `COMPKEY` | Integer |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `COMPLEXKEY` | Integer |  |  |
| `CRIT` | String |  | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String |  | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String |  | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double |  |  |
| `DWNDPTH` | Double |  |  |
| `DWNELEV` | Double |  |  |
| `FFACTOR` | Double |  |  |
| `GROUNDWAT` | Double |  |  |
| `INSTDATE` | Date |  |  |
| `JTLEN` | Double |  |  |
| `JTTYPE` | String |  | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String |  | len 4 |
| `MFGKEY` | Integer |  |  |
| `PIPEDIAM` | Double |  |  |
| `PIPEHT` | Double |  |  |
| `PIPELEN` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `SEGKEY` | Integer |  |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLP` | Double |  |  |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String |  | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double |  |  |
| `UPSELEV` | Double |  |  |
| `XCOORD` | String |  | len 15 |
| `YCOORD` | String |  | len 15 |
| `ZCOORD` | String |  | len 15 |
| `CHNGDT` | Date |  |  |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String |  | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String |  | len 2 |
| `DATELINED` | Date |  |  |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 36: Sanitary Gravity Main Size Label

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
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 37: Storm Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 38: Outfall Labels

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
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date |  |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Outfall ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION_1` | Integer | ROTATION |  |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
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
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `OLD_AREAS` | String |  | len 50 |
| `BACKFLOW` | String | Backflow | len 5 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `DEST` | String |  | **Values:** `Primary` = Primary; `Secondary` = Secondary; `Not in Dayton` = Not in Dayton; `Does Not Exist` = Does Not Exist; `Other` = Other; `N/A` = N/A · len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 39: Storm Manhole Label

- **Records:** 14,939
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Integer |  |  |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
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
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger |  |  |
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `LININGTYPE` | String |  | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String |  | len 3 |
| `DATELINED` | Date |  |  |
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
| `GPSDATE` | Date | GPS Date |  |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 40: Storm Inlet Label

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
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date |  |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Double |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Integer |  |  |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `COMPLEXKEY` | Integer |  |  |
| `CONNLEN` | Double |  |  |
| `CONNPIPETY` | String |  | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 6 |
| `CONNSZ` | Double |  |  |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DWNCONN` | String |  | len 4 |
| `DWNDIR` | String |  | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DWNDIS` | Double |  |  |
| `DWNFR` | String |  | len 2 |
| `DWNINV` | Double |  |  |
| `DWNSTINKEY` | Integer |  |  |
| `GRATETYPE` | String |  | len 6 |
| `INLDPTH` | Double |  |  |
| `INLLEN` | Double |  |  |
| `INLWID` | Double |  |  |
| `INTKEY` | Integer |  |  |
| `LOC` | String |  | len 4 |
| `MAINKEY` | Integer |  |  |
| `MATL` | String |  | len 6 |
| `OUTLDPTH` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `SEGKEY` | Integer |  |  |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UPSINV` | Double |  |  |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger |  |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 41: Storm Main Size Label

- **Records:** 40,862
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `PARLINENO` | String |  | len 1 |
| `UNITID` | String |  | len 16 |
| `UNITID2` | String |  | len 16 |
| `COMPTYPE` | Double |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `HANSENID` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `ADDRKEY` | Integer |  |  |
| `ADDRQUAL` | String |  | len 254 |
| `ASBLT` | String |  | len 10 |
| `COMPLEXKEY` | Integer |  |  |
| `CRIT` | String |  | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String |  | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String |  | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double |  |  |
| `DWNDPTH` | Double |  |  |
| `FFACTOR` | Double |  |  |
| `GROUNDWAT` | Double |  |  |
| `JTLEN` | Double |  |  |
| `JTTYPE` | String |  | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String |  | len 4 |
| `MAPNO` | String |  | len 14 |
| `MFGKEY` | Integer |  |  |
| `PIPEDIAM` | Double |  |  |
| `PIPEHT` | Double |  |  |
| `PIPELEN` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `SEGKEY` | Integer |  |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String |  | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String |  | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `UPSDPTH` | Double |  |  |
| `XCOORD` | String |  | len 15 |
| `YCOORD` | String |  | len 15 |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPESHP` | String |  | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger |  |  |
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `LINED` | String |  | len 2 |
| `DATELINED` | Date |  |  |
| `DWNELEV_NAVD88` | Double |  |  |
| `UPSELEV_NAVD88` | Double |  |  |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `FROMMH_LONGER` | String |  | len 50 |
| `TOMH_LONGER` | String |  | len 50 |
| `OLD_AREAS` | String |  | len 50 |
| `DirFlowUpdate` | String | Direction of Flow Updated | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 42: Water Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 43: Water Network Structure Labels

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
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 44: Water Control Valve Label

- **Records:** 203
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Double |  |  |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
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
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTEDITOR` | String | Last Editor | len 50 |
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

## Layer 45: Water Curb Stop Valve Label

- **Records:** 4,825
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Double |  |  |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
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
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTEDITOR` | String | Last Editor | len 50 |
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

## Layer 46: Water Valve Label

- **Records:** 22,930
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Double |  |  |
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
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | String |  | len 15 |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
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
| `Shape` | Geometry | SHAPE |  |
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 47: Water Hydrant Label

- **Records:** 6,099
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPKEY` | Integer |  |  |
| `UNITID` | String |  | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String |  | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Double |  |  |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
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
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | String |  | len 15 |
| `COLOR` | String |  | **Values:** `BLUE` = BLUE - LOW; `GREEN` = GREEN - HIGH; `ORANGE` = ORANGE - MEDIUM · len 8 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `LASTSERVICE` | Date | Last Service Date |  |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `FLOW` | Double | Flow Rate (GPM) |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
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

## Layer 48: Water Main Size Label

- **Records:** 57,556
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `COMPKEY` | Integer |  |  |
| `MAINCOMP1` | Integer |  |  |
| `MAINCOMP2` | Integer |  |  |
| `UNITID` | String |  | len 20 |
| `UNITID2` | String |  | len 20 |
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
| `CORRFACTOR` | Double |  |  |
| `DIRFRNODE1` | String |  | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRNODE2` | String |  | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String |  | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DPTH` | Double |  |  |
| `FFACTOR` | Double |  |  |
| `FROSTDPTH` | Double |  |  |
| `GAUGE` | String |  | len 2 |
| `JTLEN` | Double |  |  |
| `JTTYPE` | String |  | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String |  | len 4 |
| `LOCATOR` | String |  | len 1 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `MFGKEY` | Integer |  |  |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPELEN` | Double |  |  |
| `PRCLKEY` | Integer |  |  |
| `PRESZONE` | String |  | **Values:** `High` = High; `Low` = Low; `SH` = Super High · len 4 |
| `SCHED` | String |  | len 3 |
| `SEGKEY` | Integer |  |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String |  | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SOILTYPE` | String |  | **Values:** `CLAY` = CLAY; `HDPN` = HARD PAN; `RKCL` = ROCK AND CLAY; `ROCK` = ROCKS; `SAND` = SAND; `SGRA` = SAND/GRAVEL; `SHAL` = SHALE; `COR` = CORROSIVE; `CRST` = CRUSHED STONE; `PIT` = PIT RUN; `PITC` = PIT RUN AND CLAY · len 4 |
| `SPECINST` | Blob |  |  |
| `STKEY` | Integer |  |  |
| `SUBAREA` | String |  | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String |  | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String |  | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+6 more) · len 6 |
| `XCOORD` | String |  | len 15 |
| `YCOORD` | String |  | len 15 |
| `ZCOORD` | String |  | len 15 |
| `CLASS` | String |  | **Values:** `51` = CLASS 51; `53` = CLASS 53 · len 4 |
| `AREAS` | String |  | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String |  | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String |  | len 2 |
| `DATELINED` | Date |  |  |
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+14 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+36 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTEDITOR` | String | Last Editor | len 50 |
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
| `GLOBALID` | GlobalID |  |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 49: TMDI Year Label

- **Records:** 414
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `StreetNumb` | Double |  |  |
| `StreetName` | String |  | len 254 |
| `SourceName` | String |  | len 254 |
| `Owner_Name` | String |  | len 254 |
| `Owner_Mail` | String |  | len 254 |
| `Parcel_Num` | String |  | len 254 |
| `LotNumber` | String |  | len 254 |
| `Outfall_ID` | String |  | len 254 |
| `General_Co` | String |  | len 254 |
| `COCs` | String |  | len 254 |
| `BUSTR` | String |  | len 254 |
| `CERCLA` | String |  | len 254 |
| `FRS` | String |  | len 254 |
| `NPDES` | String |  | len 254 |
| `RCRA` | String |  | len 254 |
| `Air` | String |  | len 254 |
| `SDWA` | String |  | len 254 |
| `OH_CORE` | String |  | len 254 |
| `TRI` | String |  | len 254 |
| `Database_C` | String |  | len 254 |
| `NAICS_Code` | String |  | len 254 |
| `NAICS_Desc` | String |  | len 254 |
| `SIC_Code` | String |  | len 254 |
| `CatchBasin` | String |  | len 254 |
| `NumCatchBa` | String |  | len 254 |
| `Ponds` | String |  | len 254 |
| `UST` | String |  | len 254 |
| `AST` | String |  | len 254 |
| `DrumEquivalent` | String |  | len 254 |
| `RainShelte` | String |  | len 254 |
| `SecondaryC` | String |  | len 254 |
| `TruckDocks` | String |  | len 254 |
| `SaltSoilPi` | String |  | len 254 |
| `Comments` | String |  | len 254 |
| `AddressCom` | String |  | len 254 |
| `TMDI` | Double |  |  |
| `FHPR` | Double |  |  |
| `Installati` | String |  | len 254 |
| `Source_Typ` | String |  | len 254 |
| `Contaminan` | String |  | len 254 |
| `x` | Double |  |  |
| `y` | Double |  |  |
| `Protection` | String |  | len 254 |
| `CumulativeNumber` | Integer |  |  |
| `BMP_Score` | Double |  |  |
| `RSV` | Double |  |  |
| `BusStartYear` | Integer |  |  |
| `SourceType` | String |  | len 150 |
| `Address` | String |  | len 150 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID | OBJECTID_1 |  |
| `Shape` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 50: Intersection Labels

- **Records:** 4,729
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INTERSECTION_ENTITY` | String |  | len 16 |
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
| `DISTANCE` | Double |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `MOBILEPATH` | String |  | len 150 |
| `DMSLINK` | String |  | len 150 |
| `GISADMIN_Intersection_LEN` | Double | LEN |  |
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
| `OBJECTID` | Integer |  |  |
| `OBJECTID_1` | Integer |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 51: Survey Data Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 52: Survey Control - '88 Labels

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

## Layer 53: Survey Control - All Labels

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

## Layer 54: County GPS Point Labels

- **Records:** 156
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `SDE_MC_GPSPTS_POINT_E_AREA` | Double | AREA |  |
| `PERIMETER` | Double |  |  |
| `GPSPTS_` | Integer |  |  |
| `GPSPTS_ID` | Integer |  |  |
| `PID` | String |  | len 9 |
| `DESIGNATION` | String |  | len 19 |
| `Y_COORDINATE` | Double |  |  |
| `X_COORDINATE` | Double |  |  |
| `ELEVATION` | Double |  |  |
| `DESCRIPTION` | String |  | len 40 |
| `POLYGONID` | Integer |  |  |
| `SCALE` | Double |  |  |
| `ANGLE` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 55: Survey Project Labels

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

## Layer 56: Completed Level Circuit Labels

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

## Layer 57: Proposed Level Circuit Labels

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

## Layer 58: Recorded Plat - Annotation Labels

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

## Layer 59: Default

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 60: Default_1

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 61: Default_2

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 62: Recorded Plat Labels

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

## Layer 63: Services-Service Areas

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 64: Housing Inspection Area Labels

- **Records:** 107
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PRI_BOARD` | String | Priority Board | len 5 |
| `HOOD` | String | Neighborhood | len 50 |
| `ABR` | String | Abbreviation | len 35 |
| `EMPID` | String | Employee ID | len 12 |
| `COMMENT_` | String | Comment | len 50 |
| `Map_Label` | String | Map Label | len 15 |
| `Insp_Name` | String | Inspector Name | len 40 |
| `Insp_ID` | SmallInteger | Inspector ID |  |
| `Supv_ID` | SmallInteger | Supervisor ID |  |
| `Job_Code` | String | Job Code | len 4 |
| `Phone` | String |  | len 15 |
| `Dist_ID` | Double | District ID |  |
| `OLD_HOOD` | String |  | len 50 |
| `OLD_ABR` | String |  | len 15 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 65: Resurfacing Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 66: Labels - All Years (Street-Year)

- **Records:** 17,038
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GEONAME` | String |  | len 60 |
| `XSTREETA` | String |  | len 80 |
| `XSTREETB` | String |  | len 80 |
| `CLID` | Integer |  |  |
| `YEARPAVED` | Integer |  |  |
| `COMMENTS` | String |  | len 255 |
| `ARCHYEAR` | Integer |  |  |
| `SINUOUSITY` | Double |  |  |
| `LINESEGS` | Integer |  |  |
| `FRACDIM` | Double |  |  |
| `YEARPROPOSED` | Integer |  |  |
| `FCC` | String |  | len 4 |
| `FUNC_CLASS` | String |  | len 3 |
| `PAVECLASS` | String |  | **Values:** `Class 1` = Concrete Pavement; `Class 2` = Brick Wearing Course on Concrete Base; `Class 3` = Asphalt on Concrete Base; `Class 4` = Asphalt on Brick Base; `Class 5` = Asphalt Pavement on Stone or Gravel Base; `Class 6` = Gravel Roadway (plain or oiled); `Class 7` = Concrete Sidewalks and Driveways; `Class 8` = Sodded Areas; `Class 9` = Unimproved Areas · len 10 |
| `VECTRENCIPYR` | String |  | len 4 |
| `FIELD_NOTE` | String |  | len 255 |
| `WC_SERVICE` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `NEED_PAVED` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `CDBG` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 255 |
| `ENG_CHECK` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `A_PAVE_COND` | String |  | **Values:** `Good` = Good; `Fair` = Fair; `Poor` = Poor; `None` = None; `Vacated` = Vacated · len 10 |
| `A_PHOLE_PATCH` | String |  | **Values:** `No` = No; `Yes` = Yes · len 10 |
| `A_VEGETATION` | String |  | **Values:** `No` = No; `Yes` = Yes · len 10 |
| `A_BULK_TRASH` | String |  | **Values:** `No` = No; `Yes` = Yes · len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 67: Labels - Pavement Fines - (Street-Year)

- **Records:** 2,862
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GEONAME` | String |  | len 60 |
| `XSTREETA` | String |  | len 80 |
| `XSTREETB` | String |  | len 80 |
| `CLID` | Integer |  |  |
| `YEARPAVED` | Integer |  |  |
| `COMMENTS` | String |  | len 255 |
| `ARCHYEAR` | Integer |  |  |
| `SINUOUSITY` | Double |  |  |
| `LINESEGS` | Integer |  |  |
| `FRACDIM` | Double |  |  |
| `YEARPROPOSED` | Integer |  |  |
| `FCC` | String |  | len 4 |
| `FUNC_CLASS` | String |  | len 3 |
| `PAVECLASS` | String |  | **Values:** `Class 1` = Concrete Pavement; `Class 2` = Brick Wearing Course on Concrete Base; `Class 3` = Asphalt on Concrete Base; `Class 4` = Asphalt on Brick Base; `Class 5` = Asphalt Pavement on Stone or Gravel Base; `Class 6` = Gravel Roadway (plain or oiled); `Class 7` = Concrete Sidewalks and Driveways; `Class 8` = Sodded Areas; `Class 9` = Unimproved Areas · len 10 |
| `VECTRENCIPYR` | String |  | len 4 |
| `FIELD_NOTE` | String |  | len 255 |
| `WC_SERVICE` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `NEED_PAVED` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 10 |
| `CDBG` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 255 |
| `ENG_CHECK` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure · len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `A_PAVE_COND` | String |  | **Values:** `Good` = Good; `Fair` = Fair; `Poor` = Poor; `None` = None; `Vacated` = Vacated · len 10 |
| `A_PHOLE_PATCH` | String |  | **Values:** `No` = No; `Yes` = Yes · len 10 |
| `A_VEGETATION` | String |  | **Values:** `No` = No; `Yes` = Yes · len 10 |
| `A_BULK_TRASH` | String |  | **Values:** `No` = No; `Yes` = Yes · len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 68: Street Maintenance Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 69: De-Ice Route Area Labels

- **Records:** 61
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `DEICE_RT` | SmallInteger |  |  |
| `RT_OR_MSK` | String |  | len 16 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE_LENG` | Double |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 70: Leaf Zone Labels

- **Records:** 78
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `NHBHD_CODE` | String |  | len 8 |
| `PRIORTY_BD` | String |  | len 10 |
| `NHBHD_NAME` | String |  | len 50 |
| `ST_DISTRIC` | String |  | len 15 |
| `LEAF_ZONE` | String |  | len 5 |
| `STMNTDST` | String |  | len 2 |
| `LEAFZONE` | String |  | len 3 |
| `ZONE_` | String |  | len 255 |
| `WEEK_ONE` | String |  | len 255 |
| `WEEK_TWO` | String |  | len 255 |
| `LEAFDT1` | Date |  |  |
| `LEAFDT2` | Date |  |  |
| `LEAFDT3` | Date |  |  |
| `LEAFDT4` | Date |  |  |
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

## Layer 71: Vacant Land Mowing Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 72: Waste Collection Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 73: Recycle Labels

- **Records:** 364
- **Geometry:** Polygon

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
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 74: Bulk Labels

- **Records:** 235
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `NHBHD_CODE` | String |  | len 8 |
| `PRIORTY_BD` | String |  | len 10 |
| `NHBHD_NAME` | String |  | len 50 |
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
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 75: Container Labels

- **Records:** 202
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `NHBHD_CODE` | String |  | len 8 |
| `PRIORTY_BD` | String |  | len 10 |
| `NHBHD_NAME` | String |  | len 50 |
| `ZONE_` | String |  | len 10 |
| `COLL_DAY` | String |  | len 12 |
| `CONT_RT` | String |  | len 10 |
| `DAY_` | String |  | len 1 |
| `WC_RT_CONT` | String |  | len 10 |
| `RT` | String |  | len 10 |
| `HANEMPID` | String |  | len 10 |
| `SECTION_` | String |  | len 10 |
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
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 76: Metal-Tire-Lightning Loader Labels

- **Records:** 195
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `NHBHD_CODE` | String |  | len 8 |
| `PRIORTY_BD` | String |  | len 10 |
| `NHBHD_NAME` | String |  | len 50 |
| `COLL_DAY` | String |  | len 12 |
| `DAY_` | String |  | len 1 |
| `ZONE_` | String |  | len 1 |
| `WC_RT_METL` | Integer |  |  |
| `WC_RT_TIRE` | Integer |  |  |
| `WC_RT_LLDR` | Integer |  |  |
| `METAL_RT` | String |  | len 10 |
| `TIRE_RT` | String |  | len 10 |
| `LT_LDR_RT` | String |  | len 10 |
| `SECTION_` | SmallInteger |  |  |
| `MTRT` | String |  | len 10 |
| `TRRT` | String |  | len 10 |
| `LLRT` | String |  | len 10 |
| `MTHANEMPID` | String |  | len 10 |
| `TRHANEMPID` | String |  | len 10 |
| `LLHANEMPID` | String |  | len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 77: Trash Labels

- **Records:** 432
- **Geometry:** Polygon

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
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 78: Administrative Boundaries

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 79: CDBG Eligible Labels

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

## Layer 80: Neighborhood Low Labels

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

## Layer 81: Neighborhood High Labels

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

## Layer 82: County-City-Twp Boundary Labels

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

## Layer 83: Topographic

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 84: Spot Elevation Labels

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

## Layer 85: Intermediate Contour Labels

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

## Layer 86: Index Contour Labels

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

## Layer 87: Best Management Pratices

- **Records:** 61
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Site` | String |  | len 255 |
| `Address` | String |  | len 255 |
| `bmptype` | String |  | len 255 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OWN` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 255 |
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

## Layer 88: swBMP__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ATTACHMENTID` | OID |  |  |
| `REL_GLOBALID` | GUID |  |  |
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
| `GLOBALID` | GlobalID |  |  |

</details>

