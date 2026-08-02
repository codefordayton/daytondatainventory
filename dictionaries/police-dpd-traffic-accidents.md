# Police/DPD_Traffic_Accidents

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Police/DPD_Traffic_Accidents/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Police_DPD_Traffic_Accidents
- **Created:** None  ·  **Item modified:** None
- **Tags:** Police

## Layer 0: Accidents

- **Records:** 743
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `street_name` | String |  | len 255 |
| `crashdate` | Date |  |  |
| `severity` | Double |  | **Values:** `1` = Fatal; `2` = Serious Injury Suspected; `3` = Minor Injury Suspected; `4` = Injury Possible; `5` = Property Damage Only |
| `mode` | String |  | **Values:** `Pedestrian` = Pedestrian; `Bicyclist` = Bicyclist; `Motorist` = Motorist · len 255 |
| `day` | Double |  | **Values:** `1` = Sunday; `2` = Monday; `3` = Tuesday; `4` = Wednesday; `5` = Thursday; `6` = Friday; `7` = Saturday |
| `month` | Double |  | **Values:** `1` = January; `2` = February; `3` = March; `4` = April; `5` = May; `6` = June; `7` = July; `8` = August; `9` = September; `10` = October; `11` = November; `12` = December |
| `hour` | Double |  | **Values:** `0` = 00:00:00; `1` = 01:00:00; `2` = 02:00:00; `3` = 03:00:00; `4` = 04:00:00; `5` = 05:00:00; `6` = 06:00:00; `7` = 07:00:00; `8` = 08:00:00; `9` = 09:00:00; `10` = 10:00:00; `11` = 11:00:00; …(+12 more) |
| `longitude` | Double |  |  |
| `latitude` | Double |  |  |
| `documentnumber` | Double |  |  |
| `reportlink` | String |  | len 255 |
| `year` | Double |  |  |
| `distracteddriver` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `freeway` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `incapacitatinginjuries` | Double |  |  |
| `commercialvehicle` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `lightconditions` | Double |  | **Values:** `1` = Daylight; `2` = Dawn/Dusk; `3` = Dark - Lighted Roadway; `4` = Dark - Roadway Not Lighted; `5` = Dark - Unknown Roadway Lighting; `9` = Other/Unknown |
| `LOCAL_REPORT_NUMBER_ID` | Double |  |  |
| `injuriesreported` | Double |  |  |
| `nonincapacitatinginjuries` | Double |  |  |
| `youngdriver` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `alcoholinvolved` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `druginvolved` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `motorcycleinvilved` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `schoolzone` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `seniordriver` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `speed` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `numberoffatalities` | Double |  |  |
| `workzonetype` | Double |  | **Values:** `1` = Lane Closure; `2` = Lane Shift/Crossover; `3` = Work on Shoulder or Median; `4` = Intermittent or Moving Work; `5` = Other |
| `workzone` | String |  | **Values:** `N` = No; `Y` = Yes · len 255 |
| `possibleinjuries` | Double |  |  |
| `roadconditions` | Double |  | **Values:** `1` = Dry; `2` = Wet; `3` = Snow; `4` = Ice; `5` = Sand, Mud, Dirt, Oil, Gravel; `6` = Water (Standing,Moving); `7` = Slush; `8` = Other/Unknown |
| `roadcontour` | Double |  | **Values:** `1` = Straight Level; `2` = Straight Grade; `3` = Curve Level; `4` = Curve Grade; `9` = Other/Unknown |
| `U1_Age` | Double |  |  |
| `U1_Distraction` | Double |  | **Values:** `0` = Not Distracted; `1` = Not Distracted; `2` = Manually Operating an Electronic Device; `3` = Talking on Hands-Free Device; `4` = Talking on Hand-Held Device; `5` = Other Activity with an Electronic Device; `6` = Passenger; `7` = Other Distraction Inside the Vehicle; `8` = Other Distraction Outside the Vehicle; `9` = Other/Unknown |
| `U1_SpecialFunction` | Double |  | **Values:** `1` = None; `2` = Taxi; `3` = Electronic Ride Sharing; `4` = School Transport; `5` = Bus - Transit/Commuter; `6` = Bus - Charter/Tour; `7` = Bus - Intercity; `8` = Bus - Shuttle; `9` = Bus - Other; `10` = Ambulance; `11` = Fire; `12` = Military; …(+10 more) |
| `U1_TrafficControl` | Double |  | **Values:** `1` = Roundabout; `2` = Signal; `3` = Flasher; `4` = Stop Sign; `5` = Yield Sign; `6` = No Control |
| `U2_Age` | Double |  |  |
| `U2_Distraction` | Double |  | **Values:** `0` = Not Distracted; `1` = Not Distracted; `2` = Manually Operating an Electronic Device; `3` = Talking on Hands-Free Device; `4` = Talking on Hand-Held Device; `5` = Other Activity with an Electronic Device; `6` = Passenger; `7` = Other Distraction Inside the Vehicle; `8` = Other Distraction Outside the Vehicle; `9` = Other/Unknown |
| `U2_SpecialFunction` | Double |  | **Values:** `1` = None; `2` = Taxi; `3` = Electronic Ride Sharing; `4` = School Transport; `5` = Bus - Transit/Commuter; `6` = Bus - Charter/Tour; `7` = Bus - Intercity; `8` = Bus - Shuttle; `9` = Bus - Other; `10` = Ambulance; `11` = Fire; `12` = Military; …(+10 more) |
| `U2_TrafficControl` | Double |  | **Values:** `1` = Roundabout; `2` = Signal; `3` = Flasher; `4` = Stop Sign; `5` = Yield Sign; `6` = No Control |
| `unrestrainedoccupants` | Double |  |  |
| `weatherconditions` | Double |  | **Values:** `1` = Clear; `2` = Cloudy; `3` = Fog,Smoke,Smog; `4` = Rain; `5` = Sleet,Hail; `6` = Snow; `7` = Severe Crosswinds; `8` = Blowing Sand, Soil, Dirt, Snow; `9` = Freezing Rain or Freezing Drizzle; `99` = Other/Unknown |
| `crashtype` | Double | Crash Type | **Values:** `0` = Unknown; `1` = Head On; `2` = Rear End; `3` = Backing; `4` = Sideswipe - Meeting; `5` = Sideswipe - Passing; `6` = Angle; `7` = Parked Vehicle; `8` = Pedestrian; `9` = Animal; `10` = Train; `11` = Pedacycles; …(+8 more) |
| `crashlocation` | Double | Crash Location | **Values:** `0` = Data Not Valid or Not Provided; `1` = Not An Intersection; `2` = Four-Way Intersection; `3` = T-Intersection; `4` = Y-Intersection; `5` = Traffic Circle/Roundabout; `6` = 5 or More Point Intersection; `7` = On Ramp; `8` = Off Ramp; `9` = Crossover; `10` = Driveway/Alley Access; `11` = Railroad Grade Crossing; …(+2 more) |
| `U3_SpecialFunction` | Double | U3 Special Function | **Values:** `1` = None; `2` = Taxi; `3` = Electronic Ride Sharing; `4` = School Transport; `5` = Bus - Transit/Commuter; `6` = Bus - Charter/Tour; `7` = Bus - Intercity; `8` = Bus - Shuttle; `9` = Bus - Other; `10` = Ambulance; `11` = Fire; `12` = Military; …(+10 more) |
| `U3_TrafficControl` | Double | U3 Traffic Control | **Values:** `1` = Roundabout; `2` = Signal; `3` = Flasher; `4` = Stop Sign; `5` = Yield Sign; `6` = No Control |
| `roadwaydepartureflag` | String | Roadway Departure Flag | **Values:** `N` = No; `Y` = Yes · len 255 |
| `undividedroadflag` | String | Undivided Road Flag | **Values:** `N` = No; `Y` = Yes · len 255 |
| `U1_marijuanaflag` | String | Unit 1 Marijuana Flag | **Values:** `N` = No; `Y` = Yes · len 255 |
| `U1_otherdrugflag` | String | Unit 1 Other Drug Flag | **Values:** `N` = No; `Y` = Yes · len 255 |
| `accident_location` | String |  | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `fatal` | String | Fatal Flag | **Values:** `N` = No; `Y` = Yes · len 255 |
| `Beat` | String |  | len 255 |
| `Sector` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID | ObjectID |  |
| `Shape` | Geometry |  |  |

</details>

