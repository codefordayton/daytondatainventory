# Environmental/OutfallInvestigation_SewerLaterals

> Feature layer used for Outfall Investigation App

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/OutfallInvestigation_SewerLaterals/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_OutfallInvestigation_SewerLaterals
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Publisher description

Feature layer used for Outfall Investigation App

## Layer 0: Sewer Lateral Lines

- **Records:** 50,271
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.ssLateralLine.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.ssLateralLine.FACILITYID` | String | Facility Identifier | len 20 |
| `GISADMIN.ssLateralLine.INSTALLDATE` | Date | Install Date |  |
| `GISADMIN.ssLateralLine.MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `GISADMIN.ssLateralLine.LINETYPE` | String | Line Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 30 |
| `GISADMIN.ssLateralLine.LOCDESC` | String | Location Description | len 50 |
| `GISADMIN.ssLateralLine.DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `GISADMIN.ssLateralLine.DISTANCE` | Integer | Distance |  |
| `GISADMIN.ssLateralLine.WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `GISADMIN.ssLateralLine.ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `GISADMIN.ssLateralLine.ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `GISADMIN.ssLateralLine.MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `GISADMIN.ssLateralLine.LASTUPDATE` | Date | LastUpdate |  |
| `GISADMIN.ssLateralLine.LASTEDITOR` | String | Last Editor | len 50 |
| `GISADMIN.ssLateralLine.COMPKEY` | Integer | COMPKEY |  |
| `GISADMIN.ssLateralLine.UNITID` | String | Service ID | len 16 |
| `GISADMIN.ssLateralLine.COMPTYPE` | Integer | COMPTYPE |  |
| `GISADMIN.ssLateralLine.SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `GISADMIN.ssLateralLine.VERSIONNAME` | String | Version | len 50 |
| `GISADMIN.ssLateralLine.EDITTOOL` | String | Tool | len 50 |
| `GISADMIN.ssLateralLine.EDITTASK` | String | Task | len 50 |
| `GISADMIN.ssLateralLine.ADDRKEY` | Integer | Address |  |
| `GISADMIN.ssLateralLine.ADDRQUAL` | String | Address Info | len 254 |
| `GISADMIN.ssLateralLine.ASBLT` | String | Asbuilt # | len 10 |
| `GISADMIN.ssLateralLine.BLDGKEY` | Integer | Building |  |
| `GISADMIN.ssLateralLine.CLNOUT` | String | CleanOut Loc | len 20 |
| `GISADMIN.ssLateralLine.COMPLEXKEY` | Integer | Complex |  |
| `GISADMIN.ssLateralLine.DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `GISADMIN.ssLateralLine.EPAID` | String | EPA ID # | len 12 |
| `GISADMIN.ssLateralLine.MAINKEY` | Integer | Main |  |
| `GISADMIN.ssLateralLine.MFGKEY` | Integer | Manufacturer |  |
| `GISADMIN.ssLateralLine.MUNICOND` | String | Municipal Cond | **Values:** `DEAD` = DEAD/NOT WORKING; `DETR` = DETERIORATED; `FAIR` = FAIR; `GOOD` = GOOD; `NEW` = NEW; `POOR` = POOR; `SCHR` = SCHEDULE FOR REPLACEMENT · len 4 |
| `GISADMIN.ssLateralLine.NOTAPS` | Integer | # of Taps |  |
| `GISADMIN.ssLateralLine.NPDESID` | String | NPDES # | len 12 |
| `GISADMIN.ssLateralLine.OWNCOND` | String | Owner Cond | **Values:** `DEAD` = DEAD/NOT WORKING; `DETR` = DETERIORATED; `FAIR` = FAIR; `GOOD` = GOOD; `NEW` = NEW; `POOR` = POOR; `SCHR` = SCHEDULE FOR REPLACEMENT · len 4 |
| `GISADMIN.ssLateralLine.PIPELEN` | Double | Pipe Length |  |
| `GISADMIN.ssLateralLine.PRCLKEY` | Integer | Parcel Key |  |
| `GISADMIN.ssLateralLine.PROPLNDPTH` | Double | Property Ln Depth |  |
| `GISADMIN.ssLateralLine.SEGKEY` | Integer | Street Segment Key |  |
| `GISADMIN.ssLateralLine.SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `GISADMIN.ssLateralLine.SIC` | String | SIC | len 4 |
| `GISADMIN.ssLateralLine.SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `GISADMIN.ssLateralLine.STKEY` | Integer | Street Segment |  |
| `GISADMIN.ssLateralLine.SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `GISADMIN.ssLateralLine.SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `GISADMIN.ssLateralLine.TAPADDRKEY` | Integer | Tap Address |  |
| `GISADMIN.ssLateralLine.TAPDIST` | Double | Tap Location |  |
| `GISADMIN.ssLateralLine.TAPFROM` | String | From Node | len 1 |
| `GISADMIN.ssLateralLine.UICID` | String | UIC ID # | len 14 |
| `GISADMIN.ssLateralLine.UNITTYPE` | String | Service Line Type | **Values:** `COPPER` = COPPER; `DOMEST` = DOMESTIC; `FIRE` = FIRE; `IRRIGA` = IRRIGATION · len 6 |
| `GISADMIN.ssLateralLine.XCOORD` | String | X Coord | len 15 |
| `GISADMIN.ssLateralLine.YCOORD` | String | Y Coord | len 15 |
| `GISADMIN.ssLateralLine.ZCOORD` | String | Z Coord | len 15 |
| `GISADMIN.ssLateralLine.OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `GISADMIN.ssLateralLine.AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `GISADMIN.ssLateralLine.GLOBALID` | GlobalID | GLOBALID |  |
| `GISADMIN.ssLateralLine.created_user` | String | created_user | len 255 |
| `GISADMIN.ssLateralLine.created_date` | Date | created_date |  |
| `GISADMIN.ssLateralLine.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.ssLateralLine.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.ssLateralLine.OLD_AREAS` | String | OLD_AREAS | len 50 |
| `GISADMIN.ssLateralLine.COMMENTS` | String | Comments | len 250 |
| `GISADMIN.ssLateralLine.UtilNetFlag` | String | UtilNetFlag | len 255 |
| `GISADMIN.ssLateralLine.PriorityBoard` | String | PriorityBoard | len 10 |
| `GISADMIN.ssLateralLine.Shape` | Geometry | Shape |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Date` | Date | Date_Time |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Initials` | String | Initials | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.DryWeather` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Flow` | String | FlowPrsent | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.WaterTemperature` | Double | WaterTemperature |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.pH` | Double | pH |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.DO` | Double | DO |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.NO3` | Double | NO3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.CI2` | Double | CI2 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.PO4` | Double | PO4 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.NH3` | Double | NH3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.LabData` | String | LabData | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Color` | String | Color | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Odor` | String | Odor | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Clarity` | String | Clarity | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 25 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.CCTV` | String | CCTV | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.CCTV_Notes` | String | CCTV_Notes | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.LateralsVerified` | String | LateralsVerified | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Comments` | String | Comments | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.ProblemAsset` | String | ProblemAsset | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Year` | String | Year | len 4 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Picture` | String | Picture | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.UNITID` | String | UNITID | len 20 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.FlowDirection_1` | String | FlowDirection_1 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.FlowDirection_2` | String | FlowDirection_2 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.FlowDirection_3` | String | FlowDirection_3 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.FlowDirection_4` | String | FlowDirection_4 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.FlowDirection_5` | String | FlowDirection_5 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.GlobalID` | String | GlobalID | len 38 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.GlobalID_1` | GUID | GlobalID_1 |  |

## Layer 1: SDE.GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine

- **Records:** 5

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Date` | Date | Date_Time |  |
| `DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `WaterTemperature` | Double |  |  |
| `pH` | Double |  |  |
| `DO` | Double |  |  |
| `NO3` | Double |  |  |
| `CI2` | Double |  |  |
| `PO4` | Double |  |  |
| `NH3` | Double |  |  |
| `Initials` | String |  | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `LabData` | String |  | len 255 |
| `Color` | String |  | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 15 |
| `Odor` | String |  | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 15 |
| `Clarity` | String |  | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 25 |
| `CCTV` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `CCTV_Notes` | String |  | len 255 |
| `LateralsVerified` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Comments` | String |  | len 255 |
| `ProblemAsset` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Year` | String |  | len 4 |
| `Picture` | String |  | len 255 |
| `UNITID` | String |  | len 20 |
| `FlowDirection_1` | String |  | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `FlowDirection_2` | String |  | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `FlowDirection_3` | String |  | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `FlowDirection_4` | String |  | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `FlowDirection_5` | String |  | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 2: SDE.GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

