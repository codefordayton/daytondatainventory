# Viewer/MapLayers_StreetLightAdmin

> Portal Viewer bAckup

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Viewer/MapLayers_StreetLightAdmin/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Viewer_MapLayers_StreetLightAdmin
- **Created:** None  ·  **Item modified:** None
- **Tags:** Viewer

## Publisher description

Portal Viewer bAckup

## Layer 0: Controllers

- **Records:** 309
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TIEKEY` | Double |  |  |
| `SUBACCNUM` | Double |  |  |
| `MAINACC` | Double |  |  |
| `X` | Double |  |  |
| `Y` | Double |  |  |
| `ADDRESS` | String |  | len 254 |
| `METERLOC` | String |  | len 254 |
| `SOURCE` | String |  | len 254 |
| `LIGHTTYPE` | String |  | len 254 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FID_` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 3: Dayton Neightborhoods

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

## Layer 4: Dayton City Limits

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
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `Shape` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 5: Street Search Layer

- **Records:** 117,022
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FNODE_` | Double |  |  |
| `TNODE_` | Double |  |  |
| `LPOLY_` | Double |  |  |
| `RPOLY_` | Double |  |  |
| `LENGTH` | Double |  |  |
| `GEONAME_ID` | Double |  |  |
| `FEAT_ID` | Double |  |  |
| `REF_IN_ID` | Double |  |  |
| `NREF_IN_ID` | Double |  |  |
| `L_AREA_ID` | Double |  |  |
| `R_AREA_ID` | Double |  |  |
| `TO_X_LANES` | Double |  |  |
| `FR_X_LANES` | Double |  |  |
| `DRIVE_TIME` | Double |  |  |
| `BREADTH` | Double |  |  |
| `WALK_TIME` | Double |  |  |
| `WALK_PEN` | Double |  |  |
| `DISTANCE` | Double |  |  |
| `FT_PENALTY` | Double |  |  |
| `TF_PENALTY` | Double |  |  |
| `LINK_ID` | Double |  |  |
| `ORIGINAL_L` | Double |  |  |
| `MM_SCOR` | Double |  |  |
| `Serv_Time` | Double |  |  |
| `GEONAME` | String |  | len 60 |
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
| `L_ROUTE` | String |  | len 10 |
| `R_ROUTE` | String |  | len 10 |
| `FROM_ELEV` | SmallInteger |  |  |
| `TO_ELEV` | SmallInteger |  |  |
| `OLD_LROUTE` | String |  | len 10 |
| `OLD_RROUTE` | String |  | len 10 |
| `NO_PARK_L` | String |  | len 1 |
| `NO_PARK_R` | String |  | len 1 |
| `TRAVCONS` | String |  | len 1 |
| `LEFT_NOTE` | String |  | len 100 |
| `RIGHT_NOTE` | String |  | len 100 |
| `fUturnRes` | String |  | len 1 |
| `tUturnRes` | String |  | len 1 |
| `MM_MATCH_T` | String |  | len 254 |
| `MM_SOURCE_` | String |  | len 254 |
| `MM_TARGET_` | String |  | len 254 |
| `sourceFID` | Integer |  |  |
| `targetFID` | Integer |  |  |
| `EMP` | String |  | len 3 |
| `MPH` | SmallInteger |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `SHAPE_Leng` | Double |  |  |
| `Shape_Le_1` | Double |  |  |
| `Shape_Le_2` | Double |  |  |
| `GlobalID_1` | GlobalID |  |  |
| `Shape.STLength()` | Double |  |  |
| `OBJECTID_12` | OID |  |  |
| `OBJECTID_1` | Integer |  |  |
| `FID_` | Integer |  |  |
| `OBJECTID` | Integer |  |  |
| `GLOBALID` | String |  | len 38 |
| `Shape` | Geometry |  |  |

</details>

## Layer 6: SDE_Publish.GISADMIN.CAMA_LANDUSECODES

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

## Layer 7: sde_publish.GISADMIN.WEB_CAMA

- **Records:** 254,227

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DWEL_STORI` | Double |  |  |
| `DWEL_YRBLT` | Double |  |  |
| `DWEL_RMTOT` | Double |  |  |
| `DWEL_RMBED` | Double |  |  |
| `DWEL_FIXBA` | Double |  |  |
| `DWEL_FIXHA` | Double |  |  |
| `DWEL_SFLA` | Double |  |  |
| `DWEL_WBFP_` | Double |  |  |
| `DWEL_WBFP1` | Double |  |  |
| `COMM_YRBLT` | Double |  |  |
| `COMM_STORI` | Double |  |  |
| `COMM_UNITS` | Double |  |  |
| `COMM_SF` | Double |  |  |
| `COMM_BED` | Double |  |  |
| `OBY_UNITS` | Double |  |  |
| `OBY_AREA` | Double |  |  |
| `OBY_YRBLT` | Double |  |  |
| `OBY_VALUE` | Double |  |  |
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
| `DWEL_BSMT` | String |  | len 40 |
| `DWEL_HEAT` | String |  | len 40 |
| `DWEL_HEATS` | String |  | len 40 |
| `DWEL_FUEL` | String |  | len 40 |
| `COMM_STRUC` | String |  | len 30 |
| `OBY_IMPROV` | String |  | len 30 |
| `OBY_GRADE` | String |  | len 40 |
| `OBY_CONDIT` | String |  | len 40 |
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

