# Environmental/StormOutfallSamplingVisualInspectionReferenceLayers

> Editing Layer for Storm Outfall Inspections

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/StormOutfallSamplingVisualInspectionReferenceLayers/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_StormOutfallSamplingVisualInspectionReferenceLayers
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Publisher description

Editing Layer for Storm Outfall Inspections

## Layer 0: Visual Inspection Completed Points

- **Records:** 92
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
| `GISADMIN.emOutfall_Inspection_UPDATE.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.UNITID` | String | UNITID | len 16 |
| `GISADMIN.emOutfall_Inspection_UPDATE.LastRain72` | String | Last Rain > 72 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.WaterFlowing` | String | Water Flowing | **Values:** `Yes` = Yes; `No` = No; `Standing` = Standing; `Not Located` = Not Located · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Temperature` | Double | Temperature |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.PH` | String | PH between 6.9 and 8.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.DO` | String | DO greater than 0.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Nitrates` | String | Nitrates greater than 10 mg/L | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Chlorine` | String | Chlorine level greater than 0.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Phosphate` | String | Phosphate level greater than 0.3 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Ammonia` | String | Ammonia level greater than 0.3 mg/L | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Structure` | String | Structure | **Values:** `Cracked` = CRACKED; `Buried` = BURIED; `Other` = OTHER (COMMENT; `NA` = N/A · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Clarity` | String | Clarity | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Deposits` | String | Deposits | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Biota` | String | Biota | **Values:** `Fish` = FISH; `Amphibian` = AMPHIBIAN; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Biological` | String | Biological | **Values:** `Vegetation` = VEGETATION; `Damage` = DAMAGE; `Excess` = EXCESS; `Algae` = ALGAE; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Color` | String | Color | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Odor` | String | Odor | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Comments` | String | Comments | len 254 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Collector1` | String | Collector 1 | **Values:** `UD` = UD; `EB` = EB; `Intern` = Intern; `KN` = KN; `LD` = Light Duty; `Visual` = Visual Inspector; `WUFO` = WUFO; `Other` = Other · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.PHSample` | Double | PH Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.DOSample` | Double | DO Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.NitratesSample` | Double | Nitrates Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.ChlorineSample` | Double | Chlorine Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.PhosephateSample` | Double | Phosephate Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.AmmoniaSample` | Double | Ammonia Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.created_user` | String | created_user | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.created_date` | Date | Date |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.Collector2` | String | Collector 2 | **Values:** `UD` = UD; `EB` = EB; `Intern` = Intern; `KN` = KN; `LD` = Light Duty; `Visual` = Visual Inspector; `WUFO` = WUFO; `Other` = Other · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Year` | SmallInteger | Year |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.Completed` | String | Completed | **Values:** `Y` = Yes; `N` = No; `V` = Visual Only · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.ReturnVisit` | String | ReturnVisit | **Values:** `Completed` = Completed; `Return` = Return · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.AmmoniaReturnVisit` | String | AmmoniaReturnVisit | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.LabData` | String | LabData | len 250 |
| `GISADMIN.emOutfall_Inspection_UPDATE.CulvertPipes_Condition` | String | CulvertPipes_Condition | **Values:** `Acceptable` = Acceptable; `Minimally Acceptable` = Minimally Acceptable; `Unacceptable` = Unacceptable; `NA` = Not Applicable · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Structure_Condition` | String | Structure_Condition | **Values:** `Acceptable` = Acceptable; `Minimally Acceptable` = Minimally Acceptable; `Unacceptable` = Unacceptable; `NA` = Not Applicable · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.GlobalID_1` | GUID | GlobalID |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.sdeobjid` | String | sdeobjid | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.SDE_GlobalID` | String | SDE_OBJID | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.SDE_RELOBJECT` | String | SDE_RELOBJECT | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Stains` | String | Stains | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.VegetationDamage` | String | Vegetation Damage | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.ExcessiveVegetation` | String | Excessive Vegetation | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.DamagetoStructures` | String | Damage to Structures | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Floatables` | String | Floatables | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.OilSheen` | String | Oil Sheen | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.FlowINT` | SmallInteger | Flow Number |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.Turbidity` | SmallInteger | Turbidity |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.MappingConcern` | String | MappingConcern | len 2000 |

## Layer 2: Visual Inspection Completed Polygons

- **Records:** 92
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN.swOutfallAreas.OBJECTID` | OID | OBJECTID |  |
| `GISADMIN.swOutfallAreas.REVIEWED` | Date | REVIEWED |  |
| `GISADMIN.swOutfallAreas.NO_OUTFALLS` | SmallInteger | NO_OUTFALLS |  |
| `GISADMIN.swOutfallAreas.NOTES` | String | NOTES | len 64 |
| `GISADMIN.swOutfallAreas.OUTFALL_NO` | String | OUTFALL_NO | len 16 |
| `GISADMIN.swOutfallAreas.SOURCE` | String | SOURCE | len 32 |
| `GISADMIN.swOutfallAreas.MODIFICATION` | String | MODIFICATION | len 16 |
| `GISADMIN.swOutfallAreas.STATUS` | String | STATUS | len 32 |
| `GISADMIN.swOutfallAreas.INFR_FOUND` | String | INFR_FOUND | len 16 |
| `GISADMIN.swOutfallAreas.UNIT_ID` | String | UNIT_ID | len 60 |
| `GISADMIN.swOutfallAreas.REVISIT` | String | REVISIT | len 4 |
| `GISADMIN.swOutfallAreas.ORIGINAL_BASIN` | String | ORIGINAL_BASIN | len 15 |
| `GISADMIN.swOutfallAreas.CODNOTES` | String | CODNOTES | len 80 |
| `GISADMIN.swOutfallAreas.ENVIRO_REVIEWED` | String | ENVIRO_REVIEWED | len 2 |
| `GISADMIN.swOutfallAreas.OWNER` | String | OWNER | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 10 |
| `GISADMIN.swOutfallAreas.GLOBALID` | GlobalID | GLOBALID |  |
| `GISADMIN.swOutfallAreas.EDITORNAME` | String | EditorName | len 50 |
| `GISADMIN.swOutfallAreas.VERSIONNAME` | String | Version | len 50 |
| `GISADMIN.swOutfallAreas.EDITTOOL` | String | Tool | len 50 |
| `GISADMIN.swOutfallAreas.EDITTASK` | String | Task | len 50 |
| `GISADMIN.swOutfallAreas.LASTUPDATE` | Date | LastUpdate |  |
| `GISADMIN.swOutfallAreas.IMAGE01` | String | Image01 | len 100 |
| `GISADMIN.swOutfallAreas.IMAGE02` | String | Image02 | len 100 |
| `GISADMIN.swOutfallAreas.IMAGE03` | String | Image03 | len 100 |
| `GISADMIN.swOutfallAreas.ACRES` | Double | ACRES |  |
| `GISADMIN.swOutfallAreas.SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `GISADMIN.swOutfallAreas.created_user` | String | created_user | len 255 |
| `GISADMIN.swOutfallAreas.created_date` | Date | created_date |  |
| `GISADMIN.swOutfallAreas.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.swOutfallAreas.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.swOutfallAreas.COMMENTS` | String | Comments | len 250 |
| `GISADMIN.swOutfallAreas.UtilNetFlag` | String | UtilNetFlag | len 255 |
| `GISADMIN.swOutfallAreas.Shape` | Geometry | Shape |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.OBJECTID` | Integer | OBJECTID |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.UNITID` | String | UNITID | len 16 |
| `GISADMIN.emOutfall_Inspection_UPDATE.LastRain72` | String | Last Rain > 72 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.WaterFlowing` | String | Water Flowing | **Values:** `Yes` = Yes; `No` = No; `Standing` = Standing; `Not Located` = Not Located · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Temperature` | Double | Temperature |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.PH` | String | PH between 6.9 and 8.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.DO` | String | DO greater than 0.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Nitrates` | String | Nitrates greater than 10 mg/L | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Chlorine` | String | Chlorine level greater than 0.5 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Phosphate` | String | Phosphate level greater than 0.3 | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Ammonia` | String | Ammonia level greater than 0.3 mg/L | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Structure` | String | Structure | **Values:** `Cracked` = CRACKED; `Buried` = BURIED; `Other` = OTHER (COMMENT; `NA` = N/A · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Clarity` | String | Clarity | **Values:** `Cloudy` = CLOUDY; `Solids` = SOLIDS; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Deposits` | String | Deposits | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Biota` | String | Biota | **Values:** `Fish` = FISH; `Amphibian` = AMPHIBIAN; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Biological` | String | Biological | **Values:** `Vegetation` = VEGETATION; `Damage` = DAMAGE; `Excess` = EXCESS; `Algae` = ALGAE; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Color` | String | Color | **Values:** `Red` = RED; `Green` = GREEN; `Brown` = BROWN; `Other` = OTHER (COMMENT); `NR` = No Response; `Blue` = BLUE; `Yellow` = YELLOW · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Odor` | String | Odor | **Values:** `Sulfur` = SULFUR; `Sewage` = SEWAGE; `Oil` = OIL; `Other` = OTHER (COMMENT); `NR` = No Response · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Comments` | String | Comments | len 254 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Collector1` | String | Collector 1 | **Values:** `UD` = UD; `EB` = EB; `Intern` = Intern; `KN` = KN; `LD` = Light Duty; `Visual` = Visual Inspector; `WUFO` = WUFO; `Other` = Other · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.PHSample` | Double | PH Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.DOSample` | Double | DO Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.NitratesSample` | Double | Nitrates Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.ChlorineSample` | Double | Chlorine Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.PhosephateSample` | Double | Phosephate Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.AmmoniaSample` | Double | Ammonia Value |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.created_user` | String | created_user | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.created_date` | Date | Date |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.last_edited_user` | String | last_edited_user | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.last_edited_date` | Date | last_edited_date |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.Collector2` | String | Collector 2 | **Values:** `UD` = UD; `EB` = EB; `Intern` = Intern; `KN` = KN; `LD` = Light Duty; `Visual` = Visual Inspector; `WUFO` = WUFO; `Other` = Other · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Year` | SmallInteger | Year |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.Completed` | String | Completed | **Values:** `Y` = Yes; `N` = No; `V` = Visual Only · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.ReturnVisit` | String | ReturnVisit | **Values:** `Completed` = Completed; `Return` = Return · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.AmmoniaReturnVisit` | String | AmmoniaReturnVisit | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.LabData` | String | LabData | len 250 |
| `GISADMIN.emOutfall_Inspection_UPDATE.CulvertPipes_Condition` | String | CulvertPipes_Condition | **Values:** `Acceptable` = Acceptable; `Minimally Acceptable` = Minimally Acceptable; `Unacceptable` = Unacceptable; `NA` = Not Applicable · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Structure_Condition` | String | Structure_Condition | **Values:** `Acceptable` = Acceptable; `Minimally Acceptable` = Minimally Acceptable; `Unacceptable` = Unacceptable; `NA` = Not Applicable · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.GlobalID_1` | GUID | GlobalID |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.sdeobjid` | String | sdeobjid | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.SDE_GlobalID` | String | SDE_OBJID | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.SDE_RELOBJECT` | String | SDE_RELOBJECT | len 255 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Stains` | String | Stains | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.VegetationDamage` | String | Vegetation Damage | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.ExcessiveVegetation` | String | Excessive Vegetation | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.DamagetoStructures` | String | Damage to Structures | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.Floatables` | String | Floatables | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.OilSheen` | String | Oil Sheen | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 50 |
| `GISADMIN.emOutfall_Inspection_UPDATE.FlowINT` | SmallInteger | Flow Number |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.Turbidity` | SmallInteger | Turbidity |  |
| `GISADMIN.emOutfall_Inspection_UPDATE.MappingConcern` | String | MappingConcern | len 2000 |

## Layer 6: Outfall Area Boundary

- **Records:** 545
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REVIEWED` | Date |  |  |
| `NO_OUTFALLS` | SmallInteger |  |  |
| `NOTES` | String |  | len 64 |
| `OUTFALL_NO` | String |  | len 16 |
| `SOURCE` | String |  | len 32 |
| `MODIFICATION` | String |  | len 16 |
| `STATUS` | String |  | len 32 |
| `INFR_FOUND` | String |  | len 16 |
| `UNIT_ID` | String |  | len 60 |
| `REVISIT` | String |  | len 4 |
| `ORIGINAL_BASIN` | String |  | len 15 |
| `CODNOTES` | String |  | len 80 |
| `ENVIRO_REVIEWED` | String |  | len 2 |
| `OWNER` | String |  | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 10 |
| `EDITORNAME` | String | EditorName | len 50 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `LASTUPDATE` | Date | LastUpdate |  |
| `IMAGE01` | String | Image01 | len 100 |
| `IMAGE02` | String | Image02 | len 100 |
| `IMAGE03` | String | Image03 | len 100 |
| `ACRES` | Double |  |  |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
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
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 4: Visual_Inspection_Table

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

## Layer 5: Visual_Inspection_Table__ATTACH

- **Records:** 911

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `ATTACHMENTID` | OID |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |

</details>

