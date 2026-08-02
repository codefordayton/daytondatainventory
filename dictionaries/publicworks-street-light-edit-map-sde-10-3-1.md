# PublicWorks/Street_Light_Edit_Map_SDE_10_3_1

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/Street_Light_Edit_Map_SDE_10_3_1/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_Street_Light_Edit_Map_SDE_10_3_1
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 0: Street Light

- **Records:** 20,816
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Owner` | String |  | **Values:** `COD` = City of Dayton; `MVL` = Miami Valley Lighting; `Unknown` = Unknown; `Unknown-Tagged` = Unknown - Tag Added During Survey; `CODO` = City of Dayton-Other; `ODOT` = ODOT · len 30 |
| `PoleNumber` | String |  | len 15 |
| `Suffix` | String |  | **Values:** `A` = A; `B` = B; `C` = C; `D` = D; `E` = E; `F` = F · len 1 |
| `ExistingTagNumber` | String |  | len 15 |
| `PoleType` | String |  | **Values:** `Wood` = Wood; `Aluminum` = Aluminum; `Steel` = Steel; `Decorative` = Decorative; `Building Mount` = Building Mount; `Underpass Mount` = Underpass Mount; `Decorative Other` = Decorative Other · len 30 |
| `LuminaireHeight` | String |  | **Values:** `5` = 5; `10` = 10; `15` = 15; `20` = 20; `25` = 25; `30` = 30; `35` = 35; `40` = 40; `45` = 45; `50` = 50; `55` = 55; `60` = 60; …(+9 more) · len 50 |
| `LuminaireWattage` | String |  | **Values:** `5` = 5; `7` = 7; `10` = 10; `15` = 15; `17` = 17; `20` = 20; `25` = 25; `31` = 31; `40` = 40; `54` = 54; `73` = 73; `110` = 110; …(+16 more) · len 15 |
| `LuminaireArmLength` | String |  | **Values:** `2` = 2; `4` = 4; `6` = 6; `8` = 8; `10` = 10; `12` = 12; `14` = 14; `16` = 16; `18` = 18; `20` = 20; `22` = 22; `24` = 24; …(+6 more) · len 5 |
| `LuminaireBulbType` | String |  | **Values:** `Blue` = Blue; `Red` = Red; `Yellow` = Yellow; `White` = White; `Unknown` = Unknown; `Unreadable` = Unreadable; `LED No Sticker` = LED No Sticker; `N/A` = N/A · len 30 |
| `LensType` | String |  | **Values:** `Drop Globe` = Drop Globe; `Flat` = Flat; `Globe` = Globe; `N/A` = N/A · len 20 |
| `SurveyDate` | Date |  |  |
| `InstallationDate` | Date |  |  |
| `RepairDate` | Date | RepaireDate |  |
| `Comments` | String |  | len 100 |
| `StreetView` | String |  | len 254 |
| `Comments_QAQC` | String |  | len 100 |
| `OID_num` | SmallInteger |  |  |
| `OID_txt` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `ENG_CHECK` | String |  | **Values:** `Y` = Yes; `N` = No · len 255 |
| `LED_PHASE` | String |  | len 10 |
| `Key_PoleNumber` | String |  | len 15 |
| `ArchiveYear` | SmallInteger |  |  |
| `ExpireDate` | Date |  |  |
| `NoPinsReceptacle` | SmallInteger | Number Pins Receptacle | **Values:** `0` = 0; `1` = 1; `3` = 3; `5` = 5; `7` = 7 |
| `Dimmable` | String |  | **Values:** `Y` = Yes; `N` = No · len 255 |
| `PoleStatus` | String | Pole Status | **Values:** `In Service` = In Service; `Down` = Down; `Missing` = Missing; `Tilting` = Tilting · len 25 |
| `PoleStatusDate` | Date |  |  |
| `SL_DIST` | String |  | len 50 |
| `SL_INT` | String |  | **Values:** `Y` = Yes; `N` = No · len 5 |
| `SL_HWAY` | String |  | **Values:** `Y` = Yes; `N` = No · len 5 |
| `LED` | String |  | **Values:** `Y` = Yes; `N` = No · len 5 |
| `Neighborhood` | String |  | **Values:** `Arlington Heights` = Arlington Heights; `Belmont` = Belmont; `Burkhardt` = Burkhardt; `Carillon` = Carillon; `College Hill` = College Hill; `Cornell Heights` = Cornell Heights; `Dayton View Triangle` = Dayton View Triangle; `DeWeese` = DeWeese; `Downtown` = Downtown; `Eastern Hills` = Eastern Hills; `Eastmont` = Eastmont; `Edgemont` = Edgemont; …(+54 more) · len 50 |
| `LightStatus` | String | Light Status | **Values:** `In Service` = In Service; `Out` = Out; `Cycling` = Cycling; `Flickering` = Flickering; `Other` = Other · len 25 |
| `LightStatusDate` | Date | Light Status Date |  |
| `NearestAddress` | String |  | len 100 |
| `PoleCondition` | String | Pole Condition | **Values:** `Needs Painted` = Needs Painted; `Needs Replaced` = Needs Replaced · len 25 |
| `Controller_ID` | Double |  |  |
| `Metered` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA · len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

