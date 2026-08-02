# Police/DPD_ForensicService

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Police/DPD_ForensicService/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Police_DPD_ForensicService
- **Created:** None  ·  **Item modified:** None
- **Tags:** Police

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

## Layer 1: Storm Inlets

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
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `UNITID` | String | Inlet ID | len 16 |
| `COMPTYPE` | Double |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CONNLEN` | Double | Connection Length |  |
| `CONNPIPETY` | String | Connection Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 6 |
| `CONNSZ` | Double | Connection Pipe Size |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DWNCONN` | String | Connection Type | len 4 |
| `DWNDIR` | String | Inlet Direction | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DWNDIS` | Double | Inlet Distance |  |
| `DWNFR` | String | Inlet Distance From | len 2 |
| `DWNINV` | Double | Downstream Invert |  |
| `DWNSTINKEY` | Integer | Connections Inlet ID |  |
| `GRATETYPE` | String | Grate Type | len 6 |
| `INLDPTH` | Double | Inlet Depth |  |
| `INLLEN` | Double | Length |  |
| `INLWID` | Double | Width |  |
| `INTKEY` | Integer | Intersection |  |
| `LOC` | String | Location Information | len 4 |
| `MAINKEY` | Integer | Main |  |
| `MATL` | String | Material | len 6 |
| `OUTLDPTH` | Double | Outlet Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `UPSINV` | Double | Upstream Invert |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `ROTATION` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GLOBALID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 2: Storm Manholes

- **Records:** 14,939
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
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
| `LINED` | String | Lined | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `UNITID` | String | Manhole ID | len 16 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
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
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `ROTATION` | Integer |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GLOBALID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 3: Sewer Manholes

- **Records:** 20,207
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
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
| `LINED` | String | Lined | len 3 |
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Manhole ID | len 16 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `EDITORNAME` | String | EditorName | len 50 |
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
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `FRAMETYPE` | String | Frame Type | **Values:** `STD` = CITY OF DAYTON STANDARD; `NON` = NON-STANDARD · len 4 |
| `HYDIST` | Double | Dist to Hydrant |  |
| `INTKEY` | Integer | Intersection |  |
| `LOC` | String | Location Information | len 4 |
| `MAPNO` | String | Map # | len 14 |
| `METERED` | String | Metered | len 1 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RINGSTYPE` | String | Ring Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 6 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `EXPBY` | String | Expired By | len 12 |
| `EXPDATE` | Date | Expired |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GLOBALID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

