# Water/SampleStationEditing

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Water/SampleStationEditing/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Water_SampleStationEditing
- **Created:** None  ·  **Item modified:** None
- **Tags:** Water

## Layer 0: Water Sampling Stations

- **Records:** 93
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `STATIONID` | String | Station ID | len 20 |
| `ROTATION` | Double | Rotation |  |
| `INSTALLDATE` | Date | Install Date |  |
| `ELEVATION` | Double | Elevation |  |
| `NAME` | String | Name | len 50 |
| `ADDRESS` | String | Address | len 255 |
| `SPDATE` | Date | Sample Date |  |
| `SAMPLEVAL` | String | Sample Value | len 3 |
| `THRESHHIT` | String | Threshold Hit | len 3 |
| `DISINFRULE` | String | Disinfection Rule | len 3 |
| `ENABLED` | SmallInteger | Enabled | **Values:** `0` = False; `1` = True |
| `ACTIVEFLAG` | SmallInteger | Active Flag | **Values:** `0` = False; `1` = True |
| `OWNEDBY` | SmallInteger | Owned By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `MAINTBY` | SmallInteger | Managed By | **Values:** `1` = Our Agency; `-1` = Private; `-2` = Other |
| `LASTUPDATE` | Date | Last Update Date |  |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `DistributionSystem` | String | Distribution System | **Values:** `M` = Miami; `O` = Ottawa · len 50 |
| `Indoor_Outdoor` | String | Indoor/Outdoor | **Values:** `I` = Inside; `O` = Outside · len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `FACILITYID` | String | Facility ID | len 20 |
| `AREAS` | String | Area | **Values:** `DN-1` = DOWNTOWN NEIGHBORHOOD; `DN-2` = MIDTOWN NEIGHBORHOOD; `DN-3` = WEBSTER STATION NEIGHBORHOOD; `FR-1` = FAIRVIEW NEIGHBORHOOD; `FR-10` = PHILADELPHIA WOODS NEIGHBORHOO; `FR-2` = FIVE OAKS NEIGHBORHOOD; `FR-3` = GRAFTON HILLS NEIGHBORHOOD; `FR-4` = HILLCREST NEIGHBORHOOD; `FR-5` = MCPHERSON NEIGHBORHOOD; `FR-6` = MOUNT VERNON NEIGHBORHOOD; `FR-7` = NORTH RIVERDALE NEIGHBORHOOD; `FR-8` = RIVERDALE NEIGHBORHOOD; …(+83 more) · len 10 |
| `SUBAREA` | String | Sub-Area | **Values:** `NCTY` = NON-CITY; `DNPB` = DOWNTOWN PRIORITY BOARD; `FRPB` = F.R.O.C. PRIORITY BOARD; `IWPB` = INNERWEST PRIORITY BOARD; `NEPB` = NORTHEAST PRIORITY BOARD; `NONC` = NON-CITY(DREXEL,BROOKVILLE,ETC; `NWPB` = NORTHWEST PRIORITY BOARD; `SEPB` = SOUTHEAST PRIORITY BOARD; `SWPB` = SOUTHWEST PRIORITY BOARD; `WD` = WD; `AIRD` = DAYTON INTERNATIONAL AIRPORT; `AIRW` = DAYTON-WRIGHT BROTHERS AIRPORT · len 4 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `XCOORD` | Double | X Coord |  |
| `YCOORD` | Double | Y Coord |  |
| `ZCOORD` | String | Z Coord | len 15 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `Route` | String |  | **Values:** `A` = A; `B` = B; `C` = C; `D` = D; `E` = E; `F` = F · len 50 |
| `Comments` | String |  | len 255 |
| `COMPKEY` | Integer |  |  |
| `COMPTYPE` | Integer |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `UtilNetFlag` | String |  | len 255 |
| `UNITID` | String |  | len 16 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

