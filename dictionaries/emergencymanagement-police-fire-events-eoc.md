# EmergencyManagement/Police_Fire_Events_eoc

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/EmergencyManagement/Police_Fire_Events_eoc/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=EmergencyManagement_Police_Fire_Events_eoc
- **Created:** None  ·  **Item modified:** None
- **Tags:** EmergencyManagement

## Layer 0: Event

- **Records:** 0
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer |  |  |
| `EventName` | String |  | len 254 |
| `EventDesc` | String |  | len 254 |
| `StartDate` | Date |  |  |
| `EndDate` | Date |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: Fire Post Type

- **Records:** 15
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ContactName` | String | Contact Name | len 50 |
| `ContactPhone` | String | Contact Phone | len 50 |
| `Supervisor` | String |  | len 50 |
| `FirePostType` | String | Fire Post Type | **Values:** `ATV` = ATV; `Bicycle Unit` = Bicycle Unit; `Boat` = Boat; `Car` = Car; `Command Post` = Command Post; `On Foot` = On Foot; `SUV` = SUV; `Engine` = Engine; `Medic` = Medic; `Ladder Truck` = Ladder Truck; `Foam Truck` = Foam Truck; `HAZMAT` = HAZMAT; …(+2 more) · len 50 |
| `PostStatus` | String | Post Status | **Values:** `Active` = Active; `Planned` = Planned; `Cancelled` = Cancelled · len 50 |
| `PostStartTime` | Date | Post Start Time |  |
| `PostEndTime` | Date | Post End Time |  |
| `Notes` | String |  | len 225 |
| `PostAddress` | String | Post Address | len 50 |
| `NumberOfFirefighters` | SmallInteger | Number Of Firefighters |  |
| `EventNumber` | String |  | len 50 |
| `EventName` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 2: Police Post Type

- **Records:** 62
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OfficerName` | String | Officer Name | len 50 |
| `OfficerPhone` | String | Officer Phone | len 50 |
| `Supervisor` | String |  | len 50 |
| `PolicePostType` | String | Police Post Type | **Values:** `On Foot` = On Foot; `Bicycle Unit` = Bicycle Unit; `K9` = K9; `Motorcycle` = Motorcycle; `ATV` = ATV; `Boat` = Boat; `Tactical Team` = Tactical Team; `Tactical Vehicle` = Tactical Vehicle; `Prisoner Transport Van` = Prisoner Transport Van; `Sniper` = Sniper; `Negotiator` = Negotiator; `Command Post` = Command Post; …(+5 more) · len 50 |
| `PostStatus` | String | Post Status | **Values:** `Active` = Active; `Planned` = Planned; `Cancelled` = Cancelled · len 50 |
| `PostStartTime` | Date | Post Start Time |  |
| `PostEndTime` | Date | Post End Time |  |
| `Notes` | String |  | len 225 |
| `PostAddress` | String | Post Address | len 50 |
| `NumberOfOfficers` | SmallInteger | Number Of Officers |  |
| `EventNumber` | String |  | len 50 |
| `EventName` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 3: Public Works Post Type

- **Records:** 24
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ContactName` | String | Contact Name | len 50 |
| `ContactPhone` | String | Contact Phone | len 50 |
| `Supervisor` | String |  | len 50 |
| `PW_PostType` | String | PW Post Type | **Values:** `Dump Truck` = Dump Truck; `Backhoe` = Backhoe; `Trash Truck` = Trash Truck; `Pickup Truck` = Pickup Truck; `Trailer` = Trailer; `Street Sweeper` = Street Sweeper; `Other` = Other · len 50 |
| `PostStatus` | String | Post Status | **Values:** `Active` = Active; `Planned` = Planned; `Cancelled` = Cancelled · len 50 |
| `PostStartTime` | Date | Post Start Time |  |
| `PostEndTime` | Date | Post End Time |  |
| `Notes` | String |  | len 225 |
| `PostAddress` | String | Post Address | len 50 |
| `NumberOfPW` | SmallInteger | Number Of PW |  |
| `EventNumber` | String |  | len 50 |
| `EventName` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 4: Special Event Assets

- **Records:** 7
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `EventNumber` | String | Event Number | len 50 |
| `EventName` | String | Event Name | len 50 |
| `EventAssetType` | String | Event Asset Type | **Values:** `ATM` = ATM; `Barricade` = Barricade; `Bleacher` = Bleacher; `Drinking Water` = Drinking Water; `Event Sign` = Event Sign; `Fire Extinguisher` = Fire Extinguisher; `Fireworks Launch Site` = Fireworks Launch Site; `First Aid` = First Aid; `Food Concessions` = Food Concessions; `Food Preperation Equipment` = Food Preperation Equipment; `Gate` = Gate; `Generator` = Generator; …(+25 more) · len 50 |
| `LocationDescription` | String | Location Description | len 50 |
| `TimeSetUp` | Date | Time Set Up |  |
| `TimeTakenDown` | Date | Time Taken Down |  |
| `PostStatus` | String | Post Status | **Values:** `Under Review` = Under Review; `Submitted` = Submitted; `More Information Needed` = More Information Needed; `Approved` = Approved; `Denied` = Denied; `Other` = Other · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 5: Special Event Routes

- **Records:** 27
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `EventNumber` | String | Event Number | len 50 |
| `EventName` | String | Event Name | len 50 |
| `EventRouteType` | String | Event Route Type | **Values:** `Event Route` = Event Route; `Fire Lane` = Fire Lane; `Other` = Other; `Parking Restriction` = Parking Restriction; `Pedestrian Route` = Pedestrian Route; `Staging Route` = Staging Route; `Temporary Fencing` = Temporary Fencing; `Vehicular Egress Route` = Vehicular Egress Route; `Vehicular Ingress Route` = Vehicular Ingress Route; `Road Closure` = Road Closure · len 50 |
| `LocationDescription` | String | Location Description | len 50 |
| `TimeSetUp` | Date | Time Set Up |  |
| `TimeTakenDown` | Date | Time Taken Down |  |
| `Status` | String |  | **Values:** `Under Review` = Under Review; `Submitted` = Submitted; `More Information Needed` = More Information Needed; `Approved` = Approved; `Denied` = Denied; `Other` = Other · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 6: Special Event Areas

- **Records:** 11
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `EventNumber` | String | Event Number | len 50 |
| `EventName` | String | Event Name | len 50 |
| `EventAreaType` | String | Event Area Type | **Values:** `Bus Loading Zone` = Bus Loading Zone; `Dining Area` = Dining Area; `Event Parking Area` = Event Parking Area; `Fireworks Fallout Area` = Fireworks Fallout Area; `Gaming Area` = Gaming Area; `Grandstand - Bleacher Area` = Grandstand - Bleacher Area; `No Parking Area` = No Parking Area; `Pedestrian Traffic Only` = Pedestrian Traffic Only; `Press Area` = Press Area; `Protest Area` = Protest Area; `Public Access Area` = Public Access Area; `Reservered Parking Area` = Reservered Parking Area; …(+8 more) · len 50 |
| `TimeSetUp` | Date | Time Set Up |  |
| `TimeTakenDown` | Date | Time Taken Down |  |
| `Status` | String |  | **Values:** `Under Review` = Under Review; `Submitted` = Submitted; `More Information Needed` = More Information Needed; `Approved` = Approved; `Denied` = Denied; `Other` = Other · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 7: Special Event Zones

- **Records:** 5
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ZoneType` | String | Zone Type | **Values:** `Command` = Command; `Evacuation Zone` = Evacuation Zone; `Free Speech Zone` = Free Speech Zone; `HLZ - Primary` = HLZ - Primary; `HLZ - Secondary` = HLZ - Secondary; `Inner Perimeter` = Inner Perimeter; `Line of Fire` = Line of Fire; `Media` = Media; `Medical` = Medical; `No Access` = No Access; `Parking` = Parking; `Rally Point` = Rally Point; …(+4 more) · len 50 |
| `SupervisorContact` | String | Supervisor Contact | len 50 |
| `Notes` | String |  | len 225 |
| `DateStart` | Date | Date Start |  |
| `DateEnd` | Date | Date End |  |
| `EventNumber` | String |  | len 50 |
| `EventName` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

