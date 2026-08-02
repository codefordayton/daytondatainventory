# Water/SanitaryUtilities

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Water/SanitaryUtilities/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Water_SanitaryUtilities
- **Created:** None  ·  **Item modified:** None
- **Tags:** Water

## Layer 0: SANITARY

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 1: Sewer Control Valves

- **Records:** 169
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `BFLY` = BUTTERFLY VALVE; `BLOFF` = BLOWOFF VALVE; `CHECK` = CHECK VALVE; `DCHCK` = DISCHARGE CHECK VALVE; `DISOL` = DISCHARGE ISOLATION VALVE; `GATE` = GATE VALVE; `GLOBE` = GLOBE VALVE; `BALL` = BALL VALVE; `RSWED` = RESILIENT WEDGE VALVE; `LAYDW` = LAY-DOWN VALVE; `BYPAS` = BYPASS GATE VALVE; `PIEDO` = PIEDOMETER VALVE; …(+16 more) · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DIR` | String | Direction to Open | len 1 |
| `DISTRICT` | String | District | len 4 |
| `INTKEY` | Integer | Intersection |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NOTURNS` | String | # of Turns | len 6 |
| `OBST` | String | Obstruction | len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
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
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 2: Sewer Fittings

- **Records:** 511
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `FITTINGTYPE` | String | Fitting Type | **Values:** `ANGLE` = < 45 DEGREE BEND; `ENDPT` = END POINT/PLUG; `JNT-T` = T-JOINT; `JNT-X` = CROSS JOINT; `VLV` = VALVE; `RED` = REDUCER; `45` = 45 DEGREE BEND; `90` = 90 DEGREE BEND; `SRV` = LARGE SERVICE LINE NODE; `JUNC` = JUNCTION CHAMBER; `PLUG` = MAIN LINE PLUG; `COUPLING` = COUPLING; …(+25 more) · len 50 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Node ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `CADTYPE` | String |  | len 32 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTFRND` | Double | Node Location |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FRND` | String | From Node | len 1 |
| `INTKEY` | Integer | Intersection |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `PRCLKEY` | Integer | Parcel |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `STKEY` | Integer | Street Segment |  |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
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
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 3: Sewer Manholes

- **Records:** 20,284
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Manhole ID | len 16 |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERT` | Double | Invert |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `WALLMAT` | String | Wall Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 25 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `LINED` | String | Lined | len 3 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
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
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `DRAIN` = DRAIN · len 6 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `EXPBY` | String | Expired By | len 12 |
| `EXPDATE` | Date | Expired |  |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
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
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 4: Sewer Manhole Labels

- **Records:** 20,284
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Manhole ID | len 16 |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERT` | Double | Invert |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `WALLMAT` | String | Wall Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 25 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `GPSDATE` | Date | GPS Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `LINED` | String | Lined | len 3 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
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
| `STEPSTYPE` | String | Steps Material | **Values:** `BRK` = BRICK CONCRETE; `CON` = POURED CONCRETE; `MBK` = MANHOLE BLOCK; `RCB` = REINFORCED CONCRETE BARREL; `UNK` = UNKNOWN; `CLA` = CLAY BRICK; `OTH` = OTHER; `COP` = PRECAST CONCRETE; `NKB` = NECK BLOCKED; `NKR` = NECK RINGS (CONCRETE); `DUC` = CAST/DUCTILE IRON (STEPS); `PVC` = PLASTIC (STEPS) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `DRAIN` = DRAIN · len 6 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `EXPBY` | String | Expired By | len 12 |
| `EXPDATE` | Date | Expired |  |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
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
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 5: Sewer Service Connections

- **Records:** 34
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `FACILITYNAME` | String | Facility Name | len 100 |
| `LARGEMETER` | SmallInteger | Large Meter Flag | **Values:** `0` = False; `1` = True |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `ACCOUNTID` | String | Account Identifier | len 20 |
| `LOCATIONID` | String | Location Identifier | len 20 |
| `CRITICAL` | SmallInteger | Critical Customer | **Values:** `0` = False; `1` = True |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Sum Flow |  |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `ID` | Integer |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
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
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 6: Sewer System Valves

- **Records:** 133
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `Air` = Air Release Valve; `Ball` = Ball; `Bloff` = Blow Off Valve; `Butterfly` = Butterfly; `Bypass` = Bypass Valve; `Check` = Check Valve; `Cone` = Cone; `Curb` = Curb Stop; `Ford` = Ford Valve; `Gate` = Gate; `GATE` = Gate; `Hyd` = Hydrant Valve; …(+12 more) · len 30 |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | len 4 |
| `INTKEY` | Integer | Intersection |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OBST` | String | Obstruction | len 6 |
| `OPERDPTH` | Double | Oper Depth |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
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
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 7: Sewer Clean Outs

- **Records:** 11
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Valve ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DIR` | String | Direction to Open | len 1 |
| `DISTRICT` | String | District | len 4 |
| `INTKEY` | Integer | Intersection |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `LOC` | String | Location Information | len 4 |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `NOTURNS` | String | # of Turns | len 6 |
| `OBST` | String | Obstruction | len 6 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `VALVESIZE` | Double | Valve Size |  |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `ACCESSMAT` | String | Access Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `ACESSTYPE` | String | Access Type | **Values:** `Door` = Door; `Grate` = Grate; `Cover` = Cover; `Hand` = Hand; `Lid` = Lid; `Unknown` = Unknown · len 20 |
| `INTDEPTH` | Double | Interior Depth |  |
| `DEVICETYPE` | String | Clean Out Type | **Values:** `Flushing Structure` = Flushing Structure; `Lamp Hole` = Lamp Hole; `Other` = Other; `Unknown` = Unknown; `CLNOUT` = Cleanout; `PLUG` = Plug; `SS` = Sampling Station; `BMSO` = Bridge Maint Service Outlet; `DRNWEL` = DRNWEL; `AS` = AS; `NONWRK` = NON WORK ORDER RELATED ISSUE; `SW` = SW; …(+1 more) · len 30 |
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
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |

</details>

## Layer 8: Sewer Gravity Mains

- **Records:** 21,093
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `root_treated` | String |  | **Values:** `Y` = Yes; `N` = No · len 10 |
| `date_treated` | Date |  |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 9: Sewer Gravity Main Labels

- **Records:** 21,093
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `SUMFLOW` | Double | Flow Summary |  |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `root_treated` | String |  | **Values:** `Y` = Yes; `N` = No · len 10 |
| `date_treated` | Date |  |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 10: Sewer Lateral Lines

- **Records:** 50,271
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `LINETYPE` | String | Line Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 30 |
| `LOCDESC` | String | Location Description | len 50 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `DISTANCE` | Integer | Distance |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Service ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `BLDGKEY` | Integer | Building |  |
| `CLNOUT` | String | CleanOut Loc | len 20 |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `EPAID` | String | EPA ID # | len 12 |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MUNICOND` | String | Municipal Cond | **Values:** `DEAD` = DEAD/NOT WORKING; `DETR` = DETERIORATED; `FAIR` = FAIR; `GOOD` = GOOD; `NEW` = NEW; `POOR` = POOR; `SCHR` = SCHEDULE FOR REPLACEMENT · len 4 |
| `NOTAPS` | Integer | # of Taps |  |
| `NPDESID` | String | NPDES # | len 12 |
| `OWNCOND` | String | Owner Cond | **Values:** `DEAD` = DEAD/NOT WORKING; `DETR` = DETERIORATED; `FAIR` = FAIR; `GOOD` = GOOD; `NEW` = NEW; `POOR` = POOR; `SCHR` = SCHEDULE FOR REPLACEMENT · len 4 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PROPLNDPTH` | Double | Property Ln Depth |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SIC` | String |  | len 4 |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `TAPADDRKEY` | Integer | Tap Address |  |
| `TAPDIST` | Double | Tap Location |  |
| `TAPFROM` | String | From Node | len 1 |
| `UICID` | String | UIC ID # | len 14 |
| `UNITTYPE` | String | Service Line Type | **Values:** `COPPER` = COPPER; `DOMEST` = DOMESTIC; `FIRE` = FIRE; `IRRIGA` = IRRIGATION · len 6 |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `PriorityBoard` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 11: Sewer Pressurized Mains

- **Records:** 38
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPTYPE` | Double |  |  |
| `ELEMENT_ID` | Double |  |  |
| `MAINCOMP1` | Double |  |  |
| `MAINCOMP2` | Double |  |  |
| `PARLINENO` | String |  | len 1 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 20 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 18 |
| `MODELOWNER` | String | Model Owner | **Values:** `Dayton` = City of Dayton; `MCSED` = Montgomery County Sanitary Engineering Department · len 6 |
| `BOUNDARY` | String | Boundary | len 3 |
| `SUGGESTREM` | String |  | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `LOCATIONMO` | String |  | len 3 |
| `MAINKEY1` | Integer |  |  |
| `MAINKEY2` | Integer |  |  |
| `SHAREDGIS` | String | Shared GIS | **Values:** `No` = No; `Yes` = Yes · len 3 |
| `HANSENID` | String | Hansen ID | len 50 |
| `COMPKEY` | Integer |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAME` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `COMPLEXKEY` | Integer | Complex |  |
| `CRIT` | String | Critical Rating | **Values:** `A` = CRITICAL/EMERGENCY; `B` = HIGH IMPORTANCE; `C` = STANDARD · len 4 |
| `DIRFRDWN` | String | Dir From Down | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DIRFRUPS` | String | Dir From Ups | **Values:** `E` = EAST; `N` = NORTH; `NE` = NORTHEAST; `NW` = NORTHWEST; `S` = SOUTH; `SE` = SOUTHEAST; `SW` = SOUTHWEST; `W` = WEST; `5` = 5; `8.5` = 8.5; `1/2` = HALF DESIGNATION FOR DOUBLES · len 3 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `DSGNFLOW` | Double | Design Flow |  |
| `DWNDPTH` | Double | Down MH Depth |  |
| `DWNELEV` | Double | Down MH Invert Elev |  |
| `FFACTOR` | Double | Friction Factor |  |
| `GROUNDWAT` | Double | Ground Water Level |  |
| `INSTDATE` | Date | Installed |  |
| `JTLEN` | Double | Joint Length |  |
| `JTTYPE` | String | Joint Type | **Values:** `CLKDBS` = CAULKED BELL AND SPIGOT; `CPLGPE` = COUPLING FOR PLAIN END PIPE; `FLANGE` = FLANGE JOINT D.I.; `MECHJT` = MECHANICAL JOINT D.I.; `MORTBS` = MORTAR/BITUM FILLED BELL/SPIGT; `PVCBS` = PVC/POLYGASKETS IN BELL/SPIGOT; `RBCPLG` = RUBBER GASKETED COUPLING; `RUBBS` = RUBBER GASKETED BELL & SPIGOT; `SLIPJT` = SLIP JOINT D.I.; `LEAD` = LEAD; `SNPRNG` = SNAP RING; `TFLX` = T-FLEX; …(+3 more) · len 6 |
| `LOC` | String | Location Information | len 4 |
| `MFGKEY` | Integer | Manufacturer |  |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `PIPEHT` | Double | Pipe Height |  |
| `PIPELEN` | Double | Pipe Length |  |
| `PRCLKEY` | Integer | Parcel Key |  |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SEGMENT` | String |  | len 6 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLP` | Double | Slope |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `UPSDPTH` | Double | Up MH Depth |  |
| `UPSELEV` | Double | Up MH Invert Elev |  |
| `XCOORD` | String | X Coord | len 15 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `CHNGDT` | Date | Change Date |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
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
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

