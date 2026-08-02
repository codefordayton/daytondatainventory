# PublicWorks/CityofDaytonSafetyActionPlanReferenceLayers

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/CityofDaytonSafetyActionPlanReferenceLayers/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_CityofDaytonSafetyActionPlanReferenceLayers
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 3: City of Dayton Intersections

- **Records:** 17,375
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
| `LotNumber` | String |  | len 20 |
| `PRI_AREA` | String |  | len 255 |
| `PRI_DISTRICT` | String |  | len 255 |
| `PRI_SUFFIX` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 4: Roadway Calculation

- **Records:** 102,629
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FNODE_` | Double |  |  |
| `TNODE_` | Double |  |  |
| `LPOLY_` | Double |  |  |
| `RPOLY_` | Double |  |  |
| `LENGTH` | Double |  |  |
| `GEONAME` | String |  | len 60 |
| `GEONAME_ID` | Double |  |  |
| `ONE_WAY` | String |  | len 2 |
| `CODE` | String |  | len 10 |
| `DOMAIN_` | String |  | len 10 |
| `STATUS` | String |  | len 10 |
| `TYPE_` | String |  | len 10 |
| `GALTNAME2` | String |  | len 50 |
| `X_LINE` | String |  | len 2 |
| `CK` | String |  | len 3 |
| `X_SCTN_NM` | String |  | len 50 |
| `ST_NAME` | String |  | len 240 |
| `FEAT_ID` | Double |  |  |
| `ST_LANGCD` | String |  | len 3 |
| `NUM_STNMES` | SmallInteger |  |  |
| `ST_NM_PREF` | String |  | len 6 |
| `ST_TYP_BEF` | String |  | len 90 |
| `ST_NM_BASE` | String |  | len 105 |
| `ST_NM_SUFF` | String |  | len 6 |
| `ST_TYP_AFT` | String |  | len 90 |
| `ST_TYP_ATT` | String |  | len 1 |
| `ADDR_TYPE` | String |  | len 1 |
| `L_REFADDR` | String |  | len 10 |
| `L_NREFADDR` | String |  | len 10 |
| `L_ADDRSCH` | String |  | len 1 |
| `L_ADDRFORM` | String |  | len 2 |
| `R_REFADDR` | String |  | len 10 |
| `R_NREFADDR` | String |  | len 10 |
| `R_ADDRSCH` | String |  | len 1 |
| `R_ADDRFORM` | String |  | len 2 |
| `REF_IN_ID` | Double |  |  |
| `NREF_IN_ID` | Double |  |  |
| `N_SHAPEPNT` | Integer |  |  |
| `FUNC_CLASS` | String |  | len 1 |
| `SPEED_CAT` | String |  | len 1 |
| `FR_SPD_LIM` | Integer |  |  |
| `TO_SPD_LIM` | Integer |  |  |
| `TO_LANES` | SmallInteger |  |  |
| `FROM_LANES` | SmallInteger |  |  |
| `ENH_GEOM` | String |  | len 1 |
| `LANE_CAT` | String |  | len 1 |
| `DIVIDER` | String |  | len 1 |
| `DIR_TRAVEL` | String |  | len 1 |
| `L_AREA_ID` | Double |  |  |
| `R_AREA_ID` | Double |  |  |
| `L_POSTCODE` | String |  | len 11 |
| `R_POSTCODE` | String |  | len 11 |
| `L_NUMZONES` | SmallInteger |  |  |
| `R_NUMZONES` | SmallInteger |  |  |
| `NUM_AD_RNG` | SmallInteger |  |  |
| `AR_AUTO` | String |  | len 1 |
| `AR_BUS` | String |  | len 1 |
| `AR_TAXIS` | String |  | len 1 |
| `AR_CARPOOL` | String |  | len 1 |
| `AR_PEDEST` | String |  | len 1 |
| `AR_TRUCKS` | String |  | len 1 |
| `AR_TRAFF` | String |  | len 1 |
| `AR_DELIV` | String |  | len 1 |
| `AR_EMERVEH` | String |  | len 1 |
| `AR_MOTOR` | String |  | len 1 |
| `PAVED` | String |  | len 1 |
| `PRIVATE` | String |  | len 1 |
| `FRONTAGE` | String |  | len 1 |
| `BRIDGE` | String |  | len 1 |
| `TUNNEL` | String |  | len 1 |
| `RAMP` | String |  | len 1 |
| `TOLLWAY` | String |  | len 1 |
| `POIACCESS` | String |  | len 1 |
| `CONTRACC` | String |  | len 1 |
| `ROUNDABOUT` | String |  | len 1 |
| `INTERINTER` | String |  | len 1 |
| `UNDEFTRAFF` | String |  | len 1 |
| `FERRY_TYPE` | String |  | len 1 |
| `MULTIDIGIT` | String |  | len 1 |
| `MAXATTR` | String |  | len 1 |
| `SPECTRFIG` | String |  | len 1 |
| `INDESCRIB` | String |  | len 1 |
| `MANOEUVRE` | String |  | len 1 |
| `DIVIDERLEG` | String |  | len 1 |
| `INPROCDATA` | String |  | len 1 |
| `FULL_GEOM` | String |  | len 1 |
| `URBAN` | String |  | len 1 |
| `ROUTE_TYPE` | String |  | len 1 |
| `DIRONSIGN` | String |  | len 1 |
| `EXPLICATBL` | String |  | len 1 |
| `NAMEONRDSN` | String |  | len 1 |
| `POSTALNAME` | String |  | len 1 |
| `STALENAME` | String |  | len 1 |
| `VANITYNAME` | String |  | len 1 |
| `JUNCTIONNM` | String |  | len 1 |
| `EXITNAME` | String |  | len 1 |
| `SCENIC_RT` | String |  | len 1 |
| `SCENIC_NM` | String |  | len 1 |
| `TO_X_LANES` | Double |  |  |
| `FR_X_LANES` | Double |  |  |
| `FOURWHLDR` | String |  | len 1 |
| `COVERIND` | String |  | len 2 |
| `PLOT_ROAD` | String |  | len 1 |
| `REVERSIBLE` | String |  | len 1 |
| `EXPR_LANE` | String |  | len 1 |
| `CARPOOLRD` | String |  | len 1 |
| `PHYS_LANES` | SmallInteger |  |  |
| `VER_TRANS` | String |  | len 1 |
| `PUB_ACCESS` | String |  | len 1 |
| `LOW_MBLTY` | String |  | len 1 |
| `PARK_AVAIL` | SmallInteger |  |  |
| `PRIORITYRD` | String |  | len 1 |
| `SPD_LM_SRC` | String |  | len 2 |
| `EXPAND_INC` | String |  | len 1 |
| `TRANS_AREA` | String |  | len 1 |
| `L_FIPS` | Integer |  |  |
| `R_FIPS` | Integer |  |  |
| `L_STATE` | String |  | len 2 |
| `R_STATE` | String |  | len 2 |
| `L_CITY` | String |  | len 35 |
| `R_CITY` | String |  | len 35 |
| `MEANDER` | String |  | len 1 |
| `DRIVE_TIME` | Double |  |  |
| `L_ROUTE` | String |  | len 10 |
| `R_ROUTE` | String |  | len 10 |
| `FROM_ELEV` | SmallInteger |  |  |
| `TO_ELEV` | SmallInteger |  |  |
| `OLD_LROUTE` | String |  | len 10 |
| `OLD_RROUTE` | String |  | len 10 |
| `BREADTH` | Double |  |  |
| `WALK_TIME` | Double |  |  |
| `WALK_PEN` | Double |  |  |
| `NO_PARK_L` | String |  | len 1 |
| `NO_PARK_R` | String |  | len 1 |
| `TRAVCONS` | String |  | len 1 |
| `DISTANCE` | Double |  |  |
| `LEFT_NOTE` | String |  | len 100 |
| `RIGHT_NOTE` | String |  | len 100 |
| `FT_PENALTY` | Double |  |  |
| `TF_PENALTY` | Double |  |  |
| `fUturnRes` | String |  | len 1 |
| `tUturnRes` | String |  | len 1 |
| `LINK_ID` | Double |  |  |
| `ORIGINAL_L` | Double |  |  |
| `MM_MATCH_T` | String |  | len 254 |
| `MM_SOURCE_` | String |  | len 254 |
| `MM_TARGET_` | String |  | len 254 |
| `sourceFID` | Integer |  |  |
| `targetFID` | Integer |  |  |
| `MM_SCOR` | Double |  |  |
| `Serv_Time` | Double |  |  |
| `EMP` | String |  | len 3 |
| `MPH` | SmallInteger |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_12` | OID |  |  |
| `OBJECTID_1` | Integer |  |  |
| `FID_` | Integer |  |  |
| `OBJECTID` | Integer |  |  |
| `GLOBALID` | String |  | len 38 |
| `SHAPE_Leng` | Double |  |  |
| `Shape_Le_1` | Double |  |  |
| `Shape_Le_2` | Double |  |  |
| `Shape` | Geometry |  |  |
| `GlobalID_1` | GlobalID |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 2: City of Dayton Neighborhood

- **Records:** 64
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN_N` | String |  | len 14 |
| `LAYER` | String |  | len 32 |
| `LEVEL_` | Double |  |  |
| `COLOR` | Integer |  |  |
| `MSLINK_ORA` | Double |  |  |
| `PRI_BOARD` | String |  | len 5 |
| `HOOD` | String |  | len 50 |
| `ABR` | String |  | len 35 |
| `PLC_BEAT` | Integer |  |  |
| `PLC_DISTR` | Integer |  |  |
| `GISADMIN_1` | Double |  |  |
| `ACRES` | Double |  |  |
| `PERIMETER` | Double |  |  |
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
| `GlobalID_1` | GlobalID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

