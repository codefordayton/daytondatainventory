# Environmental/StormOutfallInvestigationStormInletEditing

> Feature layer for Storm Investigation Application

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/StormOutfallInvestigationStormInletEditing/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_StormOutfallInvestigationStormInletEditing
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Publisher description

Feature layer for Storm Investigation Application

## Layer 0: Storm Inlets

- **Records:** 22,689
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `INLETTYPE` | String | Inlet Type | **Values:** `OTM` = OPEN TOP MANHOLE; `DAD` = DOUBLE ALLEY DRIP (TYPE E); `GINLET` = GRATE INLET; `EEAD` = END TO END ALLEY DRIP (TYPE C); `CCB` = CURB CATCH BASIN; `CINLET` = CURB INLET; `SAD` = SINGLE ALLEY DRIP; `CATBSN` = CATCH BASIN; `HEDWAL` = HEAD WALL; `DWNSP` = DOWNSPOUT; `DWTRWL` = DEWATERING WELL; `CULVERT` = CULVERT; …(+1 more) · len 50 |
| `ACCESSDIAM` | Double | Access Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `INVERTELEV` | Double | Invert Elevation |  |
| `ACCESSMAT` | String | Access Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `ACCESSTYPE` | String | Access Type | **Values:** `Door` = Door; `Grate` = Grate; `Cover` = Cover; `Hand` = Hand; `Lid` = Lid; `Unknown` = Unknown · len 20 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `AncillaryRole` | SmallInteger |  | **Values:** `0` = None; `1` = Source; `2` = Sink |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Inlet ID | len 16 |
| `COMPTYPE` | Double |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `ROTATION` | Integer |  |  |
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
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; `FR-9` = SANTA CLARA NEIGHBORHOOD; …(+83 more) · len 10 |
| `SMP_PII` | SmallInteger | STORM MASTER PLAN PHASE II |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `UtilNetFlag` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 1: EnvMgmtOutfallInvestigation_swInlet

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

## Layer 2: EnvMgmtOutfallInvestigation_swInlet__ATTACH

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

