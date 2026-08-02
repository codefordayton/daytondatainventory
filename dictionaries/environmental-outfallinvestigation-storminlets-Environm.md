# Environmental/OutfallInvestigation_StormInlets

> Feature layer for Storm Investigation Application

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/OutfallInvestigation_StormInlets/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_OutfallInvestigation_StormInlets
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Publisher description

Feature layer for Storm Investigation Application

## Layer 0: Storm Inlets

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
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.DryWeather` | String | DryWeather | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
| `GISADMIN.EnvMgmtOutfallInvestigation_swInlet.Flow` | String | FlowPresent | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 10 |
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

## Layer 1: SDE.GISADMIN.EnvMgmtOutfallInvestigation_swInlet

- **Records:** 21

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
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 2: SDE.GISADMIN.EnvMgmtOutfallInvestigation_swInlet__ATTACH

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

