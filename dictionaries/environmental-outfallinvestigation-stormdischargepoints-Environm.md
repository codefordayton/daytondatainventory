# Environmental/OutfallInvestigation_StormDischargePoints

> Feature Later used for Storm Investigation Application

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/OutfallInvestigation_StormDischargePoints/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_OutfallInvestigation_StormDischargePoints
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Publisher description

Feature Later used for Storm Investigation Application

## Layer 0: Storm Discharge Points

- **Records:** 536
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.swDischargePoint.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.swDischargePoint.FACILITYID` | String | Facility Identifier | len 20 |
| `GISADMIN.swDischargePoint.AVGDISCH` | String | Average Discharge | len 10 |
| `GISADMIN.swDischargePoint.DISCHID` | String | Discharge Identifier | len 20 |
| `GISADMIN.swDischargePoint.DISCHRGTYP` | String | Discharge Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `OVERFLOW` = OVERFLOW · len 50 |
| `GISADMIN.swDischargePoint.PEAKDISCH` | String | Peak Discharge | len 10 |
| `GISADMIN.swDischargePoint.PERMIT` | String | Permitted | len 30 |
| `GISADMIN.swDischargePoint.PERMITID` | String | Permit Identifier | len 20 |
| `GISADMIN.swDischargePoint.INSTALLDATE` | Date | Install Date |  |
| `GISADMIN.swDischargePoint.LOCDESC` | String | Location Description | len 200 |
| `GISADMIN.swDischargePoint.ROTATION` | Double | Rotation |  |
| `GISADMIN.swDischargePoint.DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `GISADMIN.swDischargePoint.ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `GISADMIN.swDischargePoint.ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `GISADMIN.swDischargePoint.MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `GISADMIN.swDischargePoint.LASTUPDATE` | Date | LastUpdate |  |
| `GISADMIN.swDischargePoint.LASTEDITOR` | String | Last Editor | len 50 |
| `GISADMIN.swDischargePoint.AncillaryRole` | SmallInteger | AncillaryRole | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `GISADMIN.swDischargePoint.COMPKEY` | Integer | COMPKEY |  |
| `GISADMIN.swDischargePoint.UNITID` | String | Outfall ID | len 16 |
| `GISADMIN.swDischargePoint.COMPTYPE` | Integer | COMPTYPE |  |
| `GISADMIN.swDischargePoint.SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `GISADMIN.swDischargePoint.ROTATION_1` | Integer | ROTATION |  |
| `GISADMIN.swDischargePoint.VERSIONNAME` | String | Version | len 50 |
| `GISADMIN.swDischargePoint.EDITTOOL` | String | Tool | len 50 |
| `GISADMIN.swDischargePoint.EDITTASK` | String | Task | len 50 |
| `GISADMIN.swDischargePoint.ADDRKEY` | Integer | Address |  |
| `GISADMIN.swDischargePoint.ADDRQUAL` | String | Address Info | len 254 |
| `GISADMIN.swDischargePoint.ASBLT` | String | Asbuilt # | len 10 |
| `GISADMIN.swDischargePoint.BARLDIAM` | Double | Barrel Diameter |  |
| `GISADMIN.swDischargePoint.BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swDischargePoint.BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swDischargePoint.CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swDischargePoint.COMPLEXKEY` | Integer | Complex |  |
| `GISADMIN.swDischargePoint.CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swDischargePoint.CVRDIAM` | Double | Cover Diameter |  |
| `GISADMIN.swDischargePoint.CVRTYPE` | String | Cover Type | **Values:** `DUC` = DUCTILE; `BOL` = BOLTED; `PRE` = PRESSURE; `MLT` = MULTI-HOLE; `FOR` = FOUR-HOLE; `TWO` = TWO-HOLE; `SID` = SIDE SLOTS-SOLID; `PIC` = CONCEALED PICKHOLES; `OTH` = OTHER · len 4 |
| `GISADMIN.swDischargePoint.DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `GISADMIN.swDischargePoint.DROPMH` | String | Drop Manhole | len 1 |
| `GISADMIN.swDischargePoint.FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `GISADMIN.swDischargePoint.HYDIST` | Double | Dist To Hydrant |  |
| `GISADMIN.swDischargePoint.INTKEY` | Integer | Intersection |  |
| `GISADMIN.swDischargePoint.METERED` | String | Metered | len 1 |
| `GISADMIN.swDischargePoint.MHDPTH` | Double | Manhole Depth |  |
| `GISADMIN.swDischargePoint.PRCLKEY` | Integer | Parcel |  |
| `GISADMIN.swDischargePoint.RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swDischargePoint.SEGKEY` | Integer | Street Segemt Key |  |
| `GISADMIN.swDischargePoint.SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `GISADMIN.swDischargePoint.STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swDischargePoint.STKEY` | Integer | Street Segment |  |
| `GISADMIN.swDischargePoint.SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `GISADMIN.swDischargePoint.SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `GISADMIN.swDischargePoint.WALLTYPE` | String | Wall Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.swDischargePoint.ZCOORD` | String | Z Coord | len 15 |
| `GISADMIN.swDischargePoint.OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `GISADMIN.swDischargePoint.AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `GISADMIN.swDischargePoint.GLOBALID` | GlobalID | GLOBALID |  |
| `GISADMIN.swDischargePoint.IMAGE01` | String | Image01 | len 100 |
| `GISADMIN.swDischargePoint.IMAGE02` | String | Image02 | len 100 |
| `GISADMIN.swDischargePoint.IMAGE03` | String | Image03 | len 100 |
| `GISADMIN.swDischargePoint.SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `GISADMIN.swDischargePoint.created_user` | String | created_user | len 255 |
| `GISADMIN.swDischargePoint.created_date` | Date | created_date |  |
| `GISADMIN.swDischargePoint.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.swDischargePoint.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.swDischargePoint.XCOORD` | Double | XCOORD |  |
| `GISADMIN.swDischargePoint.YCOORD` | Double | YCOORD |  |
| `GISADMIN.swDischargePoint.OLD_AREAS` | String | OLD_AREAS | len 50 |
| `GISADMIN.swDischargePoint.BACKFLOW` | String | Backflow | len 5 |
| `GISADMIN.swDischargePoint.COMMENTS` | String | Comments | len 250 |
| `GISADMIN.swDischargePoint.UtilNetFlag` | String | UtilNetFlag | len 255 |
| `GISADMIN.swDischargePoint.DEST` | String | DEST | **Values:** `Primary` = Primary; `Secondary` = Secondary; `Not in Dayton` = Not in Dayton; `Does Not Exist` = Does Not Exist; `Other` = Other; `N/A` = N/A · len 255 |
| `GISADMIN.swDischargePoint.Shape` | Geometry | Shape |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Date` | Date | Date_Time |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Initials` | String | Initials | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.DryWeather` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Flow` | String | FlowPresent | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.WaterTemperature` | Double | WaterTemperature |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.pH` | Double | pH |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.DO` | Double | DO |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.NO3` | Double | NO3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.CI2` | Double | CI2 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.PO4` | Double | PO4 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.NH3` | Double | NH3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.LabData` | String | LabData | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Color` | String | Color | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Odor` | String | Odor | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Clarity` | String | Clarity | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 25 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.CCTV` | String | CCTV | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.CCTV_Notes` | String | CCTV_Notes | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.LateralsVerified` | String | LateralsVerified | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Comments` | String | Comments | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.ProblemAsset` | String | ProblemAsset | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Year` | String | Year | len 4 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Picture` | String | Picture | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.UNITID` | String | UNITID | len 20 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.FlowDirection_1` | String | FlowDirection_1 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.FlowDirection_2` | String | FlowDirection_2 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.FlowDirection_3` | String | FlowDirection_3 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.FlowDirection_4` | String | FlowDirection_4 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.FlowDirection_5` | String | FlowDirection_5 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.GlobalID` | String | GlobalID | len 38 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.GlobalID_1` | GUID | GlobalID_1 |  |

## Layer 1: SDE.GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint

- **Records:** 43

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

## Layer 2: SDE.GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint__ATTACH

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

