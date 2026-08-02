# Environmental/OutfallInvestigation_SewerLaterals

> Feature layer used for Outfall Investigation App

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/OutfallInvestigation_SewerLaterals/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_OutfallInvestigation_SewerLaterals
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Publisher description

Feature layer used for Outfall Investigation App

## Layer 0: Sewer Lateral Lines

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
| `LASTUPDATE` | Date | LastUpdate |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `COMPKEY` | Integer |  |  |
| `UNITID` | String | Service ID | len 16 |
| `COMPTYPE` | Integer |  |  |
| `SOURCE` | String | Data Source | **Values:** `GUS` = DATA PLACED VIA GUS; `PRPLAT` = PROPOSED PLAT; `PRCONS` = PROPOSED CONSTRUCTION; `SRVY` = SURVEY ASBUILT; `NSRVY` = NON SURVEY ASBUILT; `DSPCH` = DISPATCH CALL IN; `DAYTON` = CITY OF DAYTON; `MCSED` = MONTGOMERY COUNTY SANITARY; `GISD` = NPDES STORM OUTFALL GPS COLLECTION PROJECT (GIS DYNAMICS); `STONE` = STONE ENVIRONMENTAL GPS; `SMPPII` = STORM MASTER PLAN PHASE II; `SMPPIIEST` = STORM MASTER PLAN PHASE II - ESTIMATED; …(+2 more) · len 10 |
| `VERSIONNAME` | String | Version | len 50 |
| `EDITTOOL` | String | Tool | len 50 |
| `EDITTASK` | String | Task | len 50 |
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
| `GLOBALID` | GlobalID |  |  |

</details>

## Layer 1: SDE.GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine

- **Records:** 5

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
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 2: SDE.GISADMIN.EnvMgmtOutfallInvestigation_ssLateralLine__ATTACH

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

