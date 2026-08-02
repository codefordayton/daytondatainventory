# Fire/Hydrant_Completed_Inspections

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Fire/Hydrant_Completed_Inspections/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Fire_Hydrant_Completed_Inspections
- **Created:** None  ·  **Item modified:** None
- **Tags:** Fire

## Layer 0: 2025 Completed Inspections

- **Records:** unknown
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility Identifier | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `LASTSERVICE` | Date | Last Service Date |  |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `FLOW` | Double | Flow Rate (GPM) |  |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Hydrant ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `AUXVALVE` | String | Aux Valve | len 1 |
| `BARRELSIZE` | Double | Barrel Size |  |
| `COMPLEXKEY` | Integer | Complex |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FEEDERDIAM` | Double | Feeder Diameter |  |
| `FEEDERLEN` | Double | Feeder Length |  |
| `FEEDERTYPE` | String | Feeder Type | **Values:** `0` = No Code · len 6 |
| `HT` | Double | Height |  |
| `INTKEY` | Integer | Intersection |  |
| `MAINKEY` | Integer | Main |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `OUTLSZ1` | Double | Size of Outlet1 |  |
| `OUTLSZ2` | Double | Size of Outlet2 |  |
| `OUTLSZ3` | Double | Size of Outlet3 |  |
| `OUTLSZ4` | Double | Size of Outlet4 |  |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PACKING` | String | Packing | **Values:** `0` = No Code · len 4 |
| `PAINTTYPE` | String | Paint Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 8 |
| `PRCLKEY` | Integer | Parcel Key |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `SEGKEY` | Integer | Street Segment Key |  |
| `SERNO` | String | Serial # | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `SLKEY` | Integer | Service Line |  |
| `STKEY` | Integer | Street Segment |  |
| `SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `WVKEY` | Integer | Valve |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `COLOR` | String | Paint Color | **Values:** `BLUE` = BLUE - LOW; `GREEN` = GREEN - HIGH; `ORANGE` = ORANGE - MEDIUM · len 8 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `INSPECTIONGROUP` | String |  | len 50 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |
| `ADDRESS` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 1: Fire Hydrant Inspections

- **Records:** 2,567

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UnitID` | String | Hydrant ID | len 16 |
| `Comments` | String |  | len 255 |
| `Active` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `MeterShop` | String | MeterShoip | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `COMPTYPE1` | Integer |  |  |
| `WetDry` | String |  | **Values:** `Wet` = Wet; `Dry` = Dry · len 50 |
| `Completed` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `InspectionYear` | SmallInteger |  |  |
| `WO_Number` | String | Work Order Number | len 255 |
| `WO_Year` | Integer | Work Order Year |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

