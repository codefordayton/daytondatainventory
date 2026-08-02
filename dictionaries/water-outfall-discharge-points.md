# Water/Outfall_Discharge_Points

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Water/Outfall_Discharge_Points/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Water_Outfall_Discharge_Points
- **Created:** None  ·  **Item modified:** None
- **Tags:** Water

## Layer 0: Storm Discharge Points

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
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `UNITID` | String | Outfall ID | len 16 |
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
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `IMAGE01` | String | Image01 | len 100 |
| `IMAGE02` | String | Image02 | len 100 |
| `IMAGE03` | String | Image03 | len 100 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `BACKFLOW` | String | Backflow | len 5 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `DEST` | String |  | **Values:** `Primary` = Primary; `Secondary` = Secondary; `Not in Dayton` = Not in Dayton; `Does Not Exist` = Does Not Exist; `Other` = Other; `N/A` = N/A · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GLOBALID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

