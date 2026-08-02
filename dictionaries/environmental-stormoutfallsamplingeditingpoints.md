# Environmental/StormOutfallSamplingEditingPoints

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/StormOutfallSamplingEditingPoints/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_StormOutfallSamplingEditingPoints
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Layer 1: Storm Discharge Point

- **Records:** 536
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
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
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
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `IMAGE01` | String | Image01 | len 100 |
| `IMAGE02` | String | Image02 | len 100 |
| `IMAGE03` | String | Image03 | len 100 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
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

</details>

## Layer 4: emDischargePointConditionAssessment

- **Records:** 414

| Field | Type | Alias | Notes |
|---|---|---|---|
| `pipeMaterial` | String | Pipe Material | **Values:** `Concrete` = Concrete; `Plastic` = Plastic; `Metal` = Metal; `Other` = Other; `N/A` = Not Applicable · len 50 |
| `pipeCondition` | String | Pipe Condition (likelihood) | **Values:** `Like New` = Like New; `Minor Cracking` = Minor Cracking; `Crack Through Wall` = Crack Through Wall; `Pieces Missing` = Pieces Missing; `Structure Missing` = Structure Missing; `N/A` = Not Applicable · len 50 |
| `pipeBackflowPreventer` | String | Pipe Backflow Preventer | **Values:** `None` = None; `Flap Gate` = Flap Gate; `Sluice Gate` = Sluice Gate; `Other` = Other; `Inline` = Inline (neoprene); `Duckbill` = Duckbill (neoprene); `Unknown` = Unknown · len 50 |
| `headwallPresent` | String | Headwall Present? | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `headwallMaterial` | String | Headwall Material | **Values:** `Concrete` = Concrete; `Plastic` = Plastic; `Metal` = Metal; `Other` = Other; `N/A` = Not Applicable · len 50 |
| `headwallCondition` | String | Headwall Condition (likelihood) | **Values:** `Like New` = Like New; `Minor Cracking` = Minor Cracking; `Crack Through Wall` = Crack Through Wall; `Pieces Missing` = Pieces Missing; `Structure Missing` = Structure Missing; `N/A` = Not Applicable · len 50 |
| `channelPresent` | String | Chanel Present? | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `channelMaterial` | String | Channel Material | **Values:** `Earth` = Earth; `Concrete` = Concrete; `Riprap` = Riprap; `Other` = Other; `Stone` = Stone; `NA` = N/A · len 50 |
| `channelCondition` | String | Channel Condition (likelihood) | **Values:** `Like New` = Like New; `Minor Cracking` = Minor Cracking; `Crack Through Wall` = Crack Through Wall; `Pieces Missing` = Pieces Missing; `Structure Missing` = Structure Missing; `N/A` = Not Applicable · len 50 |
| `UNITID` | String |  | len 16 |
| `pipeErosion` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `headwallErosion` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `channelErosion` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `outfallInLevee` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Photos` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Comments` | String |  | len 1000 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 5: emDischargePointConditionAssessment_ATTACH

- **Records:** 196

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
| `GlobalID_1` | String |  | len 38 |
| `GlobalID_2` | GlobalID |  |  |

</details>

## Layer 6: emOutfall_Inspection_Update

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

