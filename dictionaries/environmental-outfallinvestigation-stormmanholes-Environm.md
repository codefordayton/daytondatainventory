# Environmental/OutfallInvestigation_StormManholes

> Feature Layer for Storm Investigation Application

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/OutfallInvestigation_StormManholes/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_OutfallInvestigation_StormManholes
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Publisher description

Feature Layer for Storm Investigation Application

## Layer 0: Storm Manholes

- **Records:** 14,984
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.swManhole.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.swManhole.FACILITYID` | String | Facility ID | len 20 |
| `GISADMIN.swManhole.INSTALLDATE` | Date | Install Date |  |
| `GISADMIN.swManhole.HIGHELEV` | Double | High Pipe Elevation |  |
| `GISADMIN.swManhole.INVERTELEV` | Double | Invert Elevation |  |
| `GISADMIN.swManhole.INVERT` | Double | Invert |  |
| `GISADMIN.swManhole.RIMELEV` | Double | Rim Elevation |  |
| `GISADMIN.swManhole.CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 50 |
| `GISADMIN.swManhole.WALLMAT` | String | Wall Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 25 |
| `GISADMIN.swManhole.MHTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `INSIDE DROP` = INSIDE DROP; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFALL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 15 |
| `GISADMIN.swManhole.CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `GISADMIN.swManhole.LOCDESC` | String | Location Description | len 200 |
| `GISADMIN.swManhole.CUTDEPTH` | Double | Pavement Cut Depth |  |
| `GISADMIN.swManhole.FLOWDIR` | String | Flow Direction | len 5 |
| `GISADMIN.swManhole.LINED` | String | Lined | len 3 |
| `GISADMIN.swManhole.GPSDATE` | Date | GPS Date |  |
| `GISADMIN.swManhole.ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `GISADMIN.swManhole.ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `GISADMIN.swManhole.MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `GISADMIN.swManhole.SUMFLOW` | Double | Flow Summary |  |
| `GISADMIN.swManhole.LASTUPDATE` | Date | LastUpdate |  |
| `GISADMIN.swManhole.LASTEDITOR` | String | Last Editor | len 50 |
| `GISADMIN.swManhole.COMPKEY` | Integer | COMPKEY |  |
| `GISADMIN.swManhole.UNITID` | String | Manhole ID | len 16 |
| `GISADMIN.swManhole.COMPTYPE` | Integer | COMPTYPE |  |
| `GISADMIN.swManhole.SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `GISADMIN.swManhole.ROTATION` | Integer | ROTATION |  |
| `GISADMIN.swManhole.VERSIONNAME` | String | Version | len 50 |
| `GISADMIN.swManhole.EDITTOOL` | String | Tool | len 50 |
| `GISADMIN.swManhole.EDITTASK` | String | Task | len 50 |
| `GISADMIN.swManhole.ADDRKEY` | Integer | Address |  |
| `GISADMIN.swManhole.ADDRQUAL` | String | Address Info | len 254 |
| `GISADMIN.swManhole.ASBLT` | String | Asbuilt # | len 10 |
| `GISADMIN.swManhole.BARLDIAM` | Double | Barrel Diameter |  |
| `GISADMIN.swManhole.BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swManhole.BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swManhole.CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swManhole.COMPLEXKEY` | Integer | Complex |  |
| `GISADMIN.swManhole.CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swManhole.CVRDIAM` | Double | Cover Diameter |  |
| `GISADMIN.swManhole.DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `GISADMIN.swManhole.DROPMH` | String | Drop Manhole | len 1 |
| `GISADMIN.swManhole.FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `GISADMIN.swManhole.HYDIST` | Double | Dist To Hydrant |  |
| `GISADMIN.swManhole.INTKEY` | Integer | Intersection |  |
| `GISADMIN.swManhole.METERED` | String | Metered | len 1 |
| `GISADMIN.swManhole.MHDPTH` | Double | Manhole Depth |  |
| `GISADMIN.swManhole.PRCLKEY` | Integer | Parcel |  |
| `GISADMIN.swManhole.RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swManhole.SEGKEY` | Integer | Street Segemt Key |  |
| `GISADMIN.swManhole.SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `GISADMIN.swManhole.STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swManhole.STKEY` | Integer | Street Segment |  |
| `GISADMIN.swManhole.SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `GISADMIN.swManhole.SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `GISADMIN.swManhole.ZCOORD` | String | Z Coord | len 15 |
| `GISADMIN.swManhole.OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `GISADMIN.swManhole.AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `GISADMIN.swManhole.GLOBALID` | GlobalID | GLOBALID |  |
| `GISADMIN.swManhole.SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `GISADMIN.swManhole.LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `GISADMIN.swManhole.DATELINED` | Date | Date Lined |  |
| `GISADMIN.swManhole.created_user` | String | created_user | len 255 |
| `GISADMIN.swManhole.created_date` | Date | created_date |  |
| `GISADMIN.swManhole.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.swManhole.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.swManhole.XCOORD` | Double | XCOORD |  |
| `GISADMIN.swManhole.YCOORD` | Double | YCOORD |  |
| `GISADMIN.swManhole.OLD_AREAS` | String | OLD_AREAS | len 50 |
| `GISADMIN.swManhole.COMMENTS` | String | Comments | len 250 |
| `GISADMIN.swManhole.UtilNetFlag` | String | UtilNetFlag | len 255 |
| `GISADMIN.swManhole.Shape` | Geometry | Shape |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Date` | Date | Date_Time |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Initials` | String | Initials | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.DryWeather` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Flow` | String | FlowPresent | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.WaterTemperature` | Double | WaterTemperature |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.pH` | Double | pH |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.DO` | Double | DO |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.NO3` | Double | NO3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.CI2` | Double | CI2 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.PO4` | Double | PO4 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.NH3` | Double | NH3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.LabData` | String | LabData | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Color` | String | Color | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Odor` | String | Odor | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Clarity` | String | Clarity | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 25 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.CCTV` | String | CCTV | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.CCTV_Notes` | String | CCTV_Notes | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.LateralsVerified` | String | LateralsVerified | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Comments` | String | Comments | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.ProblemAsset` | String | ProblemAsset | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Year` | String | Year | len 4 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Picture` | String | Picture | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.UNITID` | String | UNITID | len 20 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.FlowDirection_1` | String | FlowDirection_1 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.FlowDirection_2` | String | FlowDirection_2 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.FlowDirection_3` | String | FlowDirection_3 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.FlowDirection_4` | String | FlowDirection_4 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.FlowDirection_5` | String | FlowDirection_5 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.GlobalID` | String | GlobalID | len 38 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.GlobalID_1` | GUID | GlobalID_1 |  |

## Layer 1: SDE.GISADMIN.EnvMgmtOutfallInvestigation_swManhole

- **Records:** 339

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

## Layer 2: SDE.GISADMIN.EnvMgmtOutfallInvestigation_swManhole__ATTACH

- **Records:** 4

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

