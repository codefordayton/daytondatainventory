# Fire/Fire_Safety_Survey

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Fire/Fire_Safety_Survey/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Fire_Fire_Safety_Survey
- **Created:** None  ·  **Item modified:** None
- **Tags:** Fire

## Layer 0: Fire Saftey Surveys

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 1: Fire Safety Survey

- **Records:** 2,816
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSPECTID` | String | Inspection ID | len 10 |
| `FULLADDR` | String | Full Address | len 250 |
| `HOMETYPE` | String | Type of Home | **Values:** `Multi-Family` = Multi-Family; `Other` = Other; `1-2 Family` = 1-2 Family · len 50 |
| `REPRESENT` | String | Owner / Occupant | **Values:** `Owner/Occupant` = Owner/Occupant; `Owner` = Owner; `Occupant` = Occupant; `Other` = Other · len 30 |
| `TESTALLOW` | String | Inspection Permitted | **Values:** `ALARM` = Alarm Installation; `INFO` = Left Information · len 50 |
| `NUMSMKWRK` | SmallInteger | # Working Smoke Detectors |  |
| `NUMSMKINST` | SmallInteger | # Smoke Detectors Installed |  |
| `NUMSMKTST` | SmallInteger | # Smoke Detectors Tested |  |
| `NUMBATTERY` | SmallInteger | # Batteries Provided |  |
| `NUMCODWRK` | SmallInteger | # Working CO Detectors |  |
| `NUMCODINST` | SmallInteger | # CO Detectors Installed |  |
| `NUMCODTST` | SmallInteger | # CO Detectors Tested |  |
| `HAZARDS` | String | Hazardous Materials Observed | len 5 |
| `POISONS` | String | Poisons Observed | len 5 |
| `EDPACKET` | String | Left Educational Packet | len 5 |
| `COMMENTS` | String | Comments | len 250 |
| `LASTINSPEC` | Date | Inspected On |  |
| `INSPECTOR` | String | Inspector | len 50 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `NoEntryMade` | String |  | **Values:** `NotHome` = No one home; `Minor` = Only minor at home; `Language` = Language Barrier; `Vacant` = Vacant Home/Lot; `OccupantRefused` = Occupant Refused; `Other` = Other · len 50 |
| `ConductSurveys` | String |  | len 200 |
| `NumSmkAlarmsNotWork` | SmallInteger |  |  |
| `TotalAlarmsInstalled` | SmallInteger |  |  |
| `EducationProvided` | String |  | **Values:** `SmokeAlarms` = Smoke Alarms; `EscapePlanning` = Escape Planning; `SmokingSafety` = Smoking Safety; `ChildFireSafety` = Child Fire Safety; `HeatingSafety` = Heating Safety; `COSafety` = CO Safety; `CandleSafety` = CandleSafety; `CookingSafety` = Cooking Safety; `ResidentialSprinklers` = Residential Sprinklers; `NoInfo` = No Instructions or Written Materials Given; `Other` = Other · len 50 |
| `FireEscapePlan` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `EscapePlanPracticed` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `MeetingPlace` | String |  | len 50 |
| `WrittenMaterialsGiven` | String |  | **Values:** `SmokeAlarms` = Smoke Alarms; `EscapePlanning` = Escape Planning; `SmokingSafety` = Smoking Safety; `ChildFireSafety` = Child Fire Safety; `HeatingSafety` = Heating Safety; `COSafety` = CO Safety; `CandleSafety` = CandleSafety; `CookingSafety` = Cooking Safety; `ResidentialSprinklers` = Residential Sprinklers; `NoInfo` = No Instructions or Written Materials Given; `Other` = Other · len 50 |
| `OwnRent` | String |  | **Values:** `Own` = Own; `Rent` = Rent · len 50 |
| `PeopleInHome` | SmallInteger |  |  |
| `ChildrenUnder5` | SmallInteger |  |  |
| `Over65` | SmallInteger |  |  |
| `PhysicalMentalChallenge` | SmallInteger |  |  |
| `NumSmokers` | SmallInteger |  |  |
| `Race` | String |  | **Values:** `NativeAmerican` = Native American; `AsianPacific` = Asian Pacific Islander; `HispanicLatino` = Hispanic/Latino; `AfricanAmerican` = African American; `Other` = Other; `Caucasian` = Caucasian; `Asian` = Asian; `Multiple` = Multiple · len 50 |
| `HomeOther` | String |  | len 50 |
| `EducationProvidedOther` | String |  | len 50 |
| `WrittenMaterialsOther` | String |  | len 50 |
| `RaceOther` | String |  | len 50 |
| `CensusTract` | String |  | len 15 |
| `OriginRequest` | String |  | **Values:** `Other` = Other; `Media` = Media; `Dayton Website` = Dayton Website; `Friend` = Friend; `Door-to-Door` = Door-to-Door · len 50 |
| `RedCrossDetect` | SmallInteger |  |  |
| `People1864` | SmallInteger |  |  |
| `Smokers` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `PhysicalMental` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `GrantDetect` | String | Number of Grant Detectors | len 50 |
| `PrevDetect` | String | Number of Previous Detectors | len 50 |
| `Contact_Email` | String | Contact Email | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |

</details>

