# Fire/Hydrant_Completed_Inspections

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Fire/Hydrant_Completed_Inspections/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Fire_Hydrant_Completed_Inspections
- **Created:** None  ·  **Item modified:** None
- **Tags:** Fire

## Layer 0: 2025 Completed Inspections

- **Records:** 2,567
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `wHydrant.OBJECTID` | OID | OBJECTID |  |
| `wHydrant.FACILITYID` | String | Facility Identifier | len 20 |
| `wHydrant.INSTALLDATE` | Date | Install Date |  |
| `wHydrant.LOCDESC` | String | Location Description | len 200 |
| `wHydrant.ROTATION` | Double | Rotation |  |
| `wHydrant.MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `wHydrant.OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `wHydrant.LASTSERVICE` | Date | Last Service Date |  |
| `wHydrant.ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `wHydrant.ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `wHydrant.MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `wHydrant.LASTUPDATE` | Date | LastUpdate |  |
| `wHydrant.LASTEDITOR` | String | Last Editor | len 50 |
| `wHydrant.FLOW` | Double | Flow Rate (GPM) |  |
| `wHydrant.COMPKEY` | Integer | COMPKEY |  |
| `wHydrant.UNITID` | String | Hydrant ID | len 16 |
| `wHydrant.COMPTYPE` | Integer | COMPTYPE |  |
| `wHydrant.SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `wHydrant.VERSIONNAME` | String | Version | len 50 |
| `wHydrant.EDITTOOL` | String | Tool | len 50 |
| `wHydrant.EDITTASK` | String | Task | len 50 |
| `wHydrant.ADDRKEY` | Integer | Address |  |
| `wHydrant.ADDRQUAL` | String | Address Info | len 254 |
| `wHydrant.ASBLT` | String | AsBuilt # | len 10 |
| `wHydrant.AUXVALVE` | String | Aux Valve | len 1 |
| `wHydrant.BARRELSIZE` | Double | Barrel Size |  |
| `wHydrant.COMPLEXKEY` | Integer | Complex |  |
| `wHydrant.DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `wHydrant.FEEDERDIAM` | Double | Feeder Diameter |  |
| `wHydrant.FEEDERLEN` | Double | Feeder Length |  |
| `wHydrant.FEEDERTYPE` | String | Feeder Type | **Values:** `0` = No Code · len 6 |
| `wHydrant.HT` | Double | Height |  |
| `wHydrant.INTKEY` | Integer | Intersection |  |
| `wHydrant.MAINKEY` | Integer | Main |  |
| `wHydrant.MFGKEY` | Integer | Manufacturer |  |
| `wHydrant.MODELNO` | String | Model # | len 20 |
| `wHydrant.OBST` | String | Obstruction | **Values:** `COVDIR` = COVERED WITH DIRT; `COVPAV` = COVERED BY PAVEMENT; `COVSHB` = COVERED WITH/BY SHRUBS; `WFENCE` = WITHIN FENCED IN AREA/YARD · len 6 |
| `wHydrant.OUTLSZ1` | Double | Size of Outlet1 |  |
| `wHydrant.OUTLSZ2` | Double | Size of Outlet2 |  |
| `wHydrant.OUTLSZ3` | Double | Size of Outlet3 |  |
| `wHydrant.OUTLSZ4` | Double | Size of Outlet4 |  |
| `wHydrant.OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `wHydrant.PACKING` | String | Packing | **Values:** `0` = No Code · len 4 |
| `wHydrant.PAINTTYPE` | String | Paint Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 8 |
| `wHydrant.PRCLKEY` | Integer | Parcel Key |  |
| `wHydrant.PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `wHydrant.SEGKEY` | Integer | Street Segment Key |  |
| `wHydrant.SERNO` | String | Serial # | len 20 |
| `wHydrant.SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `wHydrant.SLKEY` | Integer | Service Line |  |
| `wHydrant.STKEY` | Integer | Street Segment |  |
| `wHydrant.SUBAREA` | String | Sub-area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `wHydrant.WVKEY` | Integer | Valve |  |
| `wHydrant.ZCOORD` | String | Z Coord | len 15 |
| `wHydrant.COLOR` | String | Paint Color | **Values:** `BLUE` = BLUE - LOW; `GREEN` = GREEN - HIGH; `ORANGE` = ORANGE - MEDIUM · len 8 |
| `wHydrant.AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `wHydrant.GLOBALID` | GlobalID | GLOBALID |  |
| `wHydrant.created_user` | String | created_user | len 255 |
| `wHydrant.created_date` | Date | created_date |  |
| `wHydrant.last_edited_user` | String | last_edited_user | len 255 |
| `wHydrant.last_edited_date` | Date | last_edited_date |  |
| `wHydrant.INSPECTIONGROUP` | String | INSPECTIONGROUP | len 50 |
| `wHydrant.XCOORD` | Double | XCOORD |  |
| `wHydrant.YCOORD` | Double | YCOORD |  |
| `wHydrant.OLD_AREAS` | String | OLD_AREAS | len 50 |
| `wHydrant.COMMENTS` | String | Comments | len 250 |
| `wHydrant.UtilNetFlag` | String | UtilNetFlag | len 255 |
| `wHydrant.ADDRESS` | String | ADDRESS | len 254 |
| `wHydrant.Shape` | Geometry | Shape |  |
| `FireHydrantInspections.OBJECTID` | Integer | OBJECTID |  |
| `FireHydrantInspections.UnitID` | String | Hydrant ID | len 16 |
| `FireHydrantInspections.Comments` | String | Comments | len 255 |
| `FireHydrantInspections.Active` | String | Active | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `FireHydrantInspections.GlobalID_1` | GUID | GlobalID |  |
| `FireHydrantInspections.created_user` | String | created_user | len 255 |
| `FireHydrantInspections.created_date` | Date | created_date |  |
| `FireHydrantInspections.last_edited_user` | String | last_edited_user | len 255 |
| `FireHydrantInspections.last_edited_date` | Date | last_edited_date |  |
| `FireHydrantInspections.MeterShop` | String | MeterShoip | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `FireHydrantInspections.COMPTYPE1` | Integer | COMPTYPE1 |  |
| `FireHydrantInspections.WetDry` | String | WetDry | **Values:** `Wet` = Wet; `Dry` = Dry · len 50 |
| `FireHydrantInspections.Completed` | String | Completed | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `FireHydrantInspections.InspectionYear` | SmallInteger | InspectionYear |  |
| `FireHydrantInspections.WO_Number` | String | Work Order Number | len 255 |
| `FireHydrantInspections.WO_Year` | Integer | Work Order Year |  |
| `FireHydrantInspections.GlobalID` | String | GlobalID | len 38 |

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

