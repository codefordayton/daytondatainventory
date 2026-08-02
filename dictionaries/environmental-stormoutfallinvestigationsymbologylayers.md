# Environmental/StormOutfallInvestigationSymbologyLayers

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/StormOutfallInvestigationSymbologyLayers/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_StormOutfallInvestigationSymbologyLayers
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

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
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
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
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.GlobalID_1` | GUID | GlobalID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swDischargePoint.GlobalID` | String | GlobalID | len 38 |

## Layer 1: Storm Inlets

- **Records:** 22,689
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.swInlet.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.swInlet.FACILITYID` | String | Facility ID | len 20 |
| `GISADMIN.swInlet.INSTALLDATE` | Date | Install Date |  |
| `GISADMIN.swInlet.INLETTYPE` | String | Inlet Type | **Values:** `OTM` = OPEN TOP MANHOLE; `DAD` = DOUBLE ALLEY DRIP (TYPE E); `GINLET` = GRATE INLET; `EEAD` = END TO END ALLEY DRIP (TYPE C); `CCB` = CURB CATCH BASIN; `CINLET` = CURB INLET; `SAD` = SINGLE ALLEY DRIP; `CATBSN` = CATCH BASIN; `HEDWAL` = HEAD WALL; `DWNSP` = DOWNSPOUT; `DWTRWL` = DEWATERING WELL; `CULVERT` = CULVERT; …(+1 more) · len 50 |
| `GISADMIN.swInlet.ACCESSDIAM` | Double | Access Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `GISADMIN.swInlet.INVERTELEV` | Double | Invert Elevation |  |
| `GISADMIN.swInlet.ACCESSMAT` | String | Access Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `GISADMIN.swInlet.ACCESSTYPE` | String | Access Type | **Values:** `Door` = Door; `Grate` = Grate; `Cover` = Cover; `Hand` = Hand; `Lid` = Lid; `Unknown` = Unknown · len 20 |
| `GISADMIN.swInlet.ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `GISADMIN.swInlet.ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `GISADMIN.swInlet.MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `GISADMIN.swInlet.LASTUPDATE` | Date | LastUpdate |  |
| `GISADMIN.swInlet.LASTEDITOR` | String | Last Editor | len 50 |
| `GISADMIN.swInlet.AncillaryRole` | SmallInteger | AncillaryRole | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `GISADMIN.swInlet.COMPKEY` | Integer | COMPKEY |  |
| `GISADMIN.swInlet.UNITID` | String | Inlet ID | len 16 |
| `GISADMIN.swInlet.COMPTYPE` | Double | COMPTYPE |  |
| `GISADMIN.swInlet.SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `GISADMIN.swInlet.ROTATION` | Integer | ROTATION |  |
| `GISADMIN.swInlet.VERSIONNAME` | String | Version | len 50 |
| `GISADMIN.swInlet.EDITTOOL` | String | Tool | len 50 |
| `GISADMIN.swInlet.EDITTASK` | String | Task | len 50 |
| `GISADMIN.swInlet.ADDRKEY` | Integer | Address |  |
| `GISADMIN.swInlet.ADDRQUAL` | String | Address Info | len 254 |
| `GISADMIN.swInlet.ASBLT` | String | AsBuilt # | len 10 |
| `GISADMIN.swInlet.COMPLEXKEY` | Integer | Complex |  |
| `GISADMIN.swInlet.CONNLEN` | Double | Connection Length |  |
| `GISADMIN.swInlet.CONNPIPETY` | String | Connection Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 6 |
| `GISADMIN.swInlet.CONNSZ` | Double | Connection Pipe Size |  |
| `GISADMIN.swInlet.DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `GISADMIN.swInlet.DWNCONN` | String | Connection Type | len 4 |
| `GISADMIN.swInlet.DWNDIR` | String | Inlet Direction | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `GISADMIN.swInlet.DWNDIS` | Double | Inlet Distance |  |
| `GISADMIN.swInlet.DWNFR` | String | Inlet Distance From | len 2 |
| `GISADMIN.swInlet.DWNINV` | Double | Downstream Invert |  |
| `GISADMIN.swInlet.DWNSTINKEY` | Integer | Connections Inlet ID |  |
| `GISADMIN.swInlet.GRATETYPE` | String | Grate Type | len 6 |
| `GISADMIN.swInlet.INLDPTH` | Double | Inlet Depth |  |
| `GISADMIN.swInlet.INLLEN` | Double | Length |  |
| `GISADMIN.swInlet.INLWID` | Double | Width |  |
| `GISADMIN.swInlet.INTKEY` | Integer | Intersection |  |
| `GISADMIN.swInlet.LOC` | String | Location Information | len 4 |
| `GISADMIN.swInlet.MAINKEY` | Integer | Main |  |
| `GISADMIN.swInlet.MATL` | String | Material | len 6 |
| `GISADMIN.swInlet.OUTLDPTH` | Double | Outlet Depth |  |
| `GISADMIN.swInlet.PRCLKEY` | Integer | Parcel Key |  |
| `GISADMIN.swInlet.SEGKEY` | Integer | Street Segment Key |  |
| `GISADMIN.swInlet.SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `GISADMIN.swInlet.STKEY` | Integer | Street Segment |  |
| `GISADMIN.swInlet.SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `GISADMIN.swInlet.UPSINV` | Double | Upstream Invert |  |
| `GISADMIN.swInlet.ZCOORD` | String | Z Coord | len 15 |
| `GISADMIN.swInlet.OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `GISADMIN.swInlet.AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `GISADMIN.swInlet.GLOBALID` | GlobalID | GLOBALID |  |
| `GISADMIN.swInlet.SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `GISADMIN.swInlet.created_user` | String | created_user | len 255 |
| `GISADMIN.swInlet.created_date` | Date | created_date |  |
| `GISADMIN.swInlet.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.swInlet.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.swInlet.XCOORD` | Double | XCOORD |  |
| `GISADMIN.swInlet.YCOORD` | Double | YCOORD |  |
| `GISADMIN.swInlet.OLD_AREAS` | String | OLD_AREAS | len 50 |
| `GISADMIN.swInlet.COMMENTS` | String | Comments | len 250 |
| `GISADMIN.swInlet.UtilNetFlag` | String | UtilNetFlag | len 255 |
| `GISADMIN.swInlet.Shape` | Geometry | Shape |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Date` | Date | Date_Time |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Initials` | String | Initials | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.WaterTemperature` | Double | WaterTemperature |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.pH` | Double | pH |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.DO` | Double | DO |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.NO3` | Double | NO3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.CI2` | Double | CI2 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.PO4` | Double | PO4 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.NH3` | Double | NH3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.LabData` | String | LabData | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Color` | String | Color | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Odor` | String | Odor | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Clarity` | String | Clarity | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 25 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.CCTV` | String | CCTV | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.CCTV_Notes` | String | CCTV_Notes | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.LateralsVerified` | String | LateralsVerified | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Comments` | String | Comments | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.ProblemAsset` | String | ProblemAsset | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Year` | String | Year | len 4 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Picture` | String | Picture | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.UNITID` | String | UNITID | len 20 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.FlowDirection_1` | String | FlowDirection_1 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.FlowDirection_2` | String | FlowDirection_2 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.FlowDirection_3` | String | FlowDirection_3 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.FlowDirection_4` | String | FlowDirection_4 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.FlowDirection_5` | String | FlowDirection_5 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.GlobalID` | GUID | GlobalID |  |

## Layer 2: Storm Manholes

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
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
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
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.GlobalID_1` | GUID | GlobalID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_swManhole.GlobalID` | String | GlobalID | len 38 |

## Layer 3: Sewer Manholes

- **Records:** 20,284
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.ssManhole.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.ssManhole.FACILITYID` | String | Facility ID | len 20 |
| `GISADMIN.ssManhole.INSTALLDATE` | Date | Install Date |  |
| `GISADMIN.ssManhole.HIGHELEV` | Double | High Pipe Elevation |  |
| `GISADMIN.ssManhole.INVERT` | Double | Invert |  |
| `GISADMIN.ssManhole.INVERTELEV` | Double | Invert Elevation |  |
| `GISADMIN.ssManhole.RIMELEV` | Double | Rim Elevation |  |
| `GISADMIN.ssManhole.CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `GISADMIN.ssManhole.WALLMAT` | String | Wall Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 25 |
| `GISADMIN.ssManhole.CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `GISADMIN.ssManhole.CUTDEPTH` | Double | Pavement Cut Depth |  |
| `GISADMIN.ssManhole.FLOWDIR` | String | Flow Direction | len 5 |
| `GISADMIN.ssManhole.LINED` | String | Lined | len 3 |
| `GISADMIN.ssManhole.GPSDATE` | Date | GPS Date |  |
| `GISADMIN.ssManhole.WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `GISADMIN.ssManhole.LOCDESC` | String | Location Description | len 200 |
| `GISADMIN.ssManhole.ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `GISADMIN.ssManhole.ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `GISADMIN.ssManhole.MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `GISADMIN.ssManhole.SUMFLOW` | Double | Flow Summary |  |
| `GISADMIN.ssManhole.LASTUPDATE` | Date | LastUpdate |  |
| `GISADMIN.ssManhole.LASTEDITOR` | String | Last Editor | len 50 |
| `GISADMIN.ssManhole.COMPKEY` | Integer | COMPKEY |  |
| `GISADMIN.ssManhole.COMPTYPE` | Integer | COMPTYPE |  |
| `GISADMIN.ssManhole.SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `GISADMIN.ssManhole.UNITID` | String | Manhole ID | len 16 |
| `GISADMIN.ssManhole.MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `GISADMIN.ssManhole.BOUNDARY` | String | Boundary | len 3 |
| `GISADMIN.ssManhole.SUGGESTREM` | String | SUGGESTREM | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `GISADMIN.ssManhole.LOCATIONMO` | String | LOCATIONMO | len 3 |
| `GISADMIN.ssManhole.SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `GISADMIN.ssManhole.EDITORNAME` | String | EditorName | len 50 |
| `GISADMIN.ssManhole.VERSIONNAME` | String | Version | len 50 |
| `GISADMIN.ssManhole.EDITTOOL` | String | Tool | len 50 |
| `GISADMIN.ssManhole.EDITTASK` | String | Task | len 50 |
| `GISADMIN.ssManhole.ADDRKEY` | Integer | Address |  |
| `GISADMIN.ssManhole.ADDRQUAL` | String | Address Info | len 254 |
| `GISADMIN.ssManhole.ASBLT` | String | Asbuilt # | len 10 |
| `GISADMIN.ssManhole.BARLDIAM` | Double | Barrel Diameter |  |
| `GISADMIN.ssManhole.BASETYPE` | String | Base Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.ssManhole.BENCHTYPE` | String | Bench Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.ssManhole.CHNLTYPE` | String | Channel Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.ssManhole.COMPLEXKEY` | Integer | Complex |  |
| `GISADMIN.ssManhole.CONETYPE` | String | Cone Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.ssManhole.CVRDIAM` | Double | Cover Diameter |  |
| `GISADMIN.ssManhole.DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `GISADMIN.ssManhole.DROPMH` | String | Drop Manhole | len 1 |
| `GISADMIN.ssManhole.FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `GISADMIN.ssManhole.HYDIST` | Double | Dist to Hydrant |  |
| `GISADMIN.ssManhole.INTKEY` | Integer | Intersection |  |
| `GISADMIN.ssManhole.LOC` | String | Location Information | len 4 |
| `GISADMIN.ssManhole.MAPNO` | String | Map # | len 14 |
| `GISADMIN.ssManhole.METERED` | String | Metered | len 1 |
| `GISADMIN.ssManhole.PRCLKEY` | Integer | Parcel Key |  |
| `GISADMIN.ssManhole.RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.ssManhole.SEGKEY` | Integer | Street Segment Key |  |
| `GISADMIN.ssManhole.SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `GISADMIN.ssManhole.STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `GISADMIN.ssManhole.STKEY` | Integer | Street Segment |  |
| `GISADMIN.ssManhole.SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `GISADMIN.ssManhole.SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `GISADMIN.ssManhole.UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `DRAIN` = DRAIN · len 6 |
| `GISADMIN.ssManhole.ZCOORD` | String | Z Coord | len 15 |
| `GISADMIN.ssManhole.CHNGDT` | Date | Change Date |  |
| `GISADMIN.ssManhole.EXPBY` | String | Expired By | len 12 |
| `GISADMIN.ssManhole.EXPDATE` | Date | Expired |  |
| `GISADMIN.ssManhole.OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `GISADMIN.ssManhole.AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `GISADMIN.ssManhole.GLOBALID` | GlobalID | GLOBALID |  |
| `GISADMIN.ssManhole.LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `GISADMIN.ssManhole.DATELINED` | Date | Date Lined |  |
| `GISADMIN.ssManhole.created_user` | String | created_user | len 255 |
| `GISADMIN.ssManhole.created_date` | Date | created_date |  |
| `GISADMIN.ssManhole.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.ssManhole.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.ssManhole.XCOORD` | Double | XCOORD |  |
| `GISADMIN.ssManhole.YCOORD` | Double | YCOORD |  |
| `GISADMIN.ssManhole.OLD_AREAS` | String | OLD_AREAS | len 50 |
| `GISADMIN.ssManhole.COMMENTS` | String | Comments | len 250 |
| `GISADMIN.ssManhole.UtilNetFlag` | String | UtilNetFlag | len 255 |
| `GISADMIN.ssManhole.Shape` | Geometry | Shape |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Date` | Date | Date_Time |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Initials` | String | Initials | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.WaterTemperature` | Double | WaterTemperature |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.pH` | Double | pH |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.DO` | Double | DO |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.NO3` | Double | NO3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.CI2` | Double | CI2 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.PO4` | Double | PO4 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.NH3` | Double | NH3 |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.LabData` | String | LabData | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Color` | String | Color | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Odor` | String | Odor | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 15 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Clarity` | String | Clarity | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 25 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.CCTV` | String | CCTV | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.CCTV_Notes` | String | CCTV_Notes | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.LateralsVerified` | String | LateralsVerified | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Comments` | String | Comments | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.ProblemAsset` | String | ProblemAsset | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Year` | String | Year | len 4 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.Picture` | String | Picture | len 255 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.UNITID` | String | UNITID | len 20 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.FlowDirection_1` | String | FlowDirection_1 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.FlowDirection_2` | String | FlowDirection_2 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.FlowDirection_3` | String | FlowDirection_3 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.FlowDirection_4` | String | FlowDirection_4 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.FlowDirection_5` | String | FlowDirection_5 | **Values:** `East` = East; `North` = North; `South` = South; `West` = West; `Northeast` = Northeast; `Northwest` = Northwest; `Southeast` = Southeast; `Southwest` = Southwest · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.GlobalID_1` | GUID | GlobalID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssManhole.GlobalID` | String | GlobalID | len 38 |

## Layer 4: Sewer Lateral Lines

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
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
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
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.GlobalID_1` | GUID | GlobalID |  |
| `GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine.GlobalID` | String | GlobalID | len 38 |

## Layer 5: EnvMgmtOutfallInvestigation_ssLateralLine

- **Records:** 5

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Date` | Date | Date_Time |  |
| `Initials` | String |  | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `WaterTemperature` | Double |  |  |
| `pH` | Double |  |  |
| `DO` | Double |  |  |
| `NO3` | Double |  |  |
| `CI2` | Double |  |  |
| `PO4` | Double |  |  |
| `NH3` | Double |  |  |
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

## Layer 6: EnvMgmtOutfallInvestigation_ssLateralLine__ATTACH

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

## Layer 7: EnvMgmtOutfallInvestigation_ssManhole

- **Records:** 14

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Date` | Date | Date_Time |  |
| `Initials` | String |  | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `WaterTemperature` | Double |  |  |
| `pH` | Double |  |  |
| `DO` | Double |  |  |
| `NO3` | Double |  |  |
| `CI2` | Double |  |  |
| `PO4` | Double |  |  |
| `NH3` | Double |  |  |
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

## Layer 8: EnvMgmtOutfallInvestigation_ssManhole__ATTACH

- **Records:** 2

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

## Layer 9: EnvMgmtOutfallInvestigation_swDischargePoint

- **Records:** 43

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Date` | Date | Date_Time |  |
| `Initials` | String |  | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `WaterTemperature` | Double |  |  |
| `pH` | Double |  |  |
| `DO` | Double |  |  |
| `NO3` | Double |  |  |
| `CI2` | Double |  |  |
| `PO4` | Double |  |  |
| `NH3` | Double |  |  |
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

## Layer 10: EnvMgmtOutfallInvestigation_swDischargePoint__ATTACH

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

## Layer 11: EnvMgmtOutfallInvestigation_swInlet

- **Records:** 21

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Date` | Date | Date_Time |  |
| `Initials` | String |  | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `WaterTemperature` | Double |  |  |
| `pH` | Double |  |  |
| `DO` | Double |  |  |
| `NO3` | Double |  |  |
| `CI2` | Double |  |  |
| `PO4` | Double |  |  |
| `NH3` | Double |  |  |
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
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 12: EnvMgmtOutfallInvestigation_swInlet__ATTACH

- **Records:** 2

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
| `OBJECTID` | OID | ATTACHMENTID |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 13: EnvMgmtOutfallInvestigation_swManhole

- **Records:** 339

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Date` | Date | Date_Time |  |
| `Initials` | String |  | **Values:** `EB` = EB; `Intern` = Intern; `KN` = KN; `PF` = PF; `TM` = TM; `ZS` = ZS; `Visual` = Visual Inspector; `WUFO` = WUFO; `LD` = Light Duty · len 10 |
| `DryWeather` | String | Initials | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `Flow` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `WaterTemperature` | Double |  |  |
| `pH` | Double |  |  |
| `DO` | Double |  |  |
| `NO3` | Double |  |  |
| `CI2` | Double |  |  |
| `PO4` | Double |  |  |
| `NH3` | Double |  |  |
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

## Layer 14: EnvMgmtOutfallInvestigation_swManhole__ATTACH

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

## Layer 15: emOutfall_Inspection_UPDATE

- **Records:** 3,257

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String |  | len 16 |
| `LastRain72` | String | Last Rain > 72 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `WaterFlowing` | String | Water Flowing | **Values:** `Yes` = Yes; `No` = No; `Standing` = Standing; `Not Located` = Not Located · len 50 |
| `Temperature` | Double |  |  |
| `PH` | String | PH between 6.9 and 8.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `DO` | String | DO greater than 0.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `Nitrates` | String | Nitrates greater than 10 mg/L | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `Chlorine` | String | Chlorine level greater than 0.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `Phosphate` | String | Phosphate level greater than 0.3 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `Ammonia` | String | Ammonia level greater than 0.3 mg/L | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `Structure` | String |  | **Values:** `Cracked` = CRACKED; `Buried` = BURIED; `Other` = OTHER (COMMENT; `NA` = N/A · len 50 |
| `Clarity` | String |  | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `Deposits` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `Biota` | String |  | **Values:** `Fish` = FISH; `Amphibian` = AMPHIBIAN; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `Biological` | String |  | **Values:** `Vegetation` = VEGETATION; `Damage` = DAMAGE; `Excess` = EXCESS; `Algae` = ALGAE; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `Color` | String |  | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 50 |
| `Odor` | String |  | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `Comments` | String |  | len 254 |
| `Collector1` | String | Collector 1 | **Values:** `UD` = UD; `EB` = EB; `Intern` = Intern; `KN` = KN; `LD` = Light Duty; `Visual` = Visual Inspector; `WUFO` = WUFO; `Other` = Other · len 50 |
| `PHSample` | Double | PH Value |  |
| `DOSample` | Double | DO Value |  |
| `NitratesSample` | Double | Nitrates Value |  |
| `ChlorineSample` | Double | Chlorine Value |  |
| `PhosephateSample` | Double | Phosephate Value |  |
| `AmmoniaSample` | Double | Ammonia Value |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date | Date |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `Collector2` | String | Collector 2 | **Values:** `UD` = UD; `EB` = EB; `Intern` = Intern; `KN` = KN; `LD` = Light Duty; `Visual` = Visual Inspector; `WUFO` = WUFO; `Other` = Other · len 50 |
| `Year` | SmallInteger |  |  |
| `Completed` | String |  | **Values:** `Y` = Yes; `N` = No; `V` = Visual Only · len 50 |
| `ReturnVisit` | String |  | **Values:** `Completed` = Completed; `Return` = Return · len 50 |
| `AmmoniaReturnVisit` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `LabData` | String |  | len 250 |
| `CulvertPipes_Condition` | String |  | **Values:** `Acceptable` = Acceptable; `Minimally Acceptable` = Minimally Acceptable; `Unacceptable` = Unacceptable; `NA` = Not Applicable · len 50 |
| `Structure_Condition` | String |  | **Values:** `Acceptable` = Acceptable; `Minimally Acceptable` = Minimally Acceptable; `Unacceptable` = Unacceptable; `NA` = Not Applicable · len 50 |
| `sdeobjid` | String |  | len 255 |
| `SDE_GlobalID` | String | SDE_OBJID | len 255 |
| `SDE_RELOBJECT` | String |  | len 255 |
| `Stains` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `VegetationDamage` | String | Vegetation Damage | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `ExcessiveVegetation` | String | Excessive Vegetation | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `DamagetoStructures` | String | Damage to Structures | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `Floatables` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `OilSheen` | String | Oil Sheen | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `FlowINT` | SmallInteger | Flow Number |  |
| `Turbidity` | SmallInteger |  |  |
| `MappingConcern` | String |  | len 2000 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 16: emOutfall_Inspection_UPDATE__ATTACH

- **Records:** 911

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

