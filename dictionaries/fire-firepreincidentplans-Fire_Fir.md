# Fire/FirePreIncidentPlans

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Fire/FirePreIncidentPlans/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Fire_FirePreIncidentPlans
- **Created:** None  ·  **Item modified:** None
- **Tags:** Fire

## Layer 0: Alarm Control Panels

- **Records:** 5
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 30 |
| `PANELTYPE` | String | Type | **Values:** `Fire Alarm Control Panel` = Fire Alarm Control Panel; `Fire Alarm Reset Panel` = Fire Alarm Reset Panel; `Fire Annunciator` = Fire Annunciator Panel; `Other` = Other · len 100 |
| `FLOOR` | String | Floor Number | len 5 |
| `LOCDESC` | String | Location Description | len 255 |
| `COMMENTS` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 1: Building Access

- **Records:** 5
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 30 |
| `ACCESSTYPE` | String | Type | **Values:** `Attic Access` = Attic Access; `Basement Access` = Basement Access; `Elevator` = Elevator; `Escalator` = Escalator; `Fire Escape` = Fire Escape; `Roof Access` = Roof Access; `Stairs` = Stairs; `Other` = Other · len 100 |
| `FLOOR` | String | Floor Number | len 5 |
| `LOCDESC` | String | Location Description | len 255 |
| `COMMENTS` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 2: Fire Supression Systems

- **Records:** 4
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 30 |
| `SUPPTYPE` | String | Type | **Values:** `Fire Department Connection` = Fire Department Connection; `Hose Connection` = Hose Connection; `Riser Valve` = Riser Valve; `Sprinkler Control Valve` = Sprinkler Control Valve; `Suppression Control Panel` = Suppression Control Panel; `Other` = Other · len 100 |
| `FLOOR` | String | Floor Number | len 5 |
| `LOCDESC` | String | Location Description | len 255 |
| `COMMENTS` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 3: Hazardous Materials

- **Records:** 2
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `HAZARDID` | String | Hazard ID | len 30 |
| `UNNUM` | String | UN ID | len 6 |
| `FLAMMABLE` | Integer | Flammability | **Values:** `4` = 4 Flammable gas or extremely flammable liquid.; `3` = 3 Flammable liquid flash point below 100° F.; `2` = 2 Combustible liquid flash point of 100° to 200° F.; `1` = 1 Combustible if heated.; `0` = 0 Not combustible. |
| `HEALTH` | Integer | Health | **Values:** `4` = 4 Danger: May be fatal on short exposure. Specialized protective equipment required.; `3` = 3 Warning: Corrosive or toxic. Avoid skin contact or inhalation.; `2` = 2 Warning: May be harmful if inhaled or absorbed.; `1` = 1 Caution: May be irritating.; `0` = 0 No unusual hazard. |
| `REACTIVITY` | Integer | Reactivity | **Values:** `4` = 4 Danger: Explosive material at room temperature.; `3` = 3 Danger: May be explosive if shocked, heated under confinement or mixed with water.; `2` = 2 Warning: Unstable or may react violently if mixed with water.; `1` = 1 Caution: May react if heated or mixed with water but not violently.; `0` = 0 Stable: Not reactive when mixed with water. |
| `SPECIAL` | String | Special Hazard | **Values:** `ACID` = Acid; `ALK` = Alkaline; `BIO` = Biohazards; `CG` = Compressed Gas; `COR` = Corrosive; `CYL` = Cryogenics; `EX` = Explosive; `F` = Flammable; `OX` = Oxidizer; `P` = Polymerization; `POI` = Poison; `R` = Radioactive; …(+1 more) · len 4 |
| `FLOOR` | String | Floor Number | len 5 |
| `STATIONARY` | String | Stationary Enclosure | len 5 |
| `LOCDESC` | String | Location Description | len 255 |
| `COMMENTS` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 4: Key Boxes

- **Records:** 1
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 30 |
| `BOXTYPE` | String | Type | **Values:** `Box` = Box; `Cabinet` = Cabinet; `Card` = Card; `Drug Vault` = Drug Vault; `Electric Shunt Switch` = Electric Shunt Switch; `Residential` = Residential; `Vault` = Vault; `Other` = Other · len 100 |
| `FLOOR` | String | Floor Number | len 5 |
| `LOCDESC` | String | Location Description | len 255 |
| `COMMENTS` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 5: Occupancies

- **Records:** 1
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 25 |
| `OCCNAME` | String | Name | len 255 |
| `FULLADDR` | String | Full Address | len 255 |
| `LOCDESC` | String | Location Description | len 255 |
| `OCCTYPE` | String | Type | **Values:** `100` = Assembly, Other; `200` = Educational, Other; `300` = Health Care, Detention, and Correction, Other; `400` = Residential, Other; `500` = Mercantile, Business, Other; `600` = Industrial, Utility, Defense, Agriculture, Mining, Other; `700` = Manufacturing; `800` = Storage, Other; `900` = Outside or Special Property, Other; `000` = Property Use, Other; `NNN` = None; `UUU` = Undetermined · len 255 |
| `POCNAME` | String | Contact Name | len 50 |
| `POCPHONE` | String | Contact Phone | len 25 |
| `POCEMAIL` | String | Contact Email | len 25 |
| `FLOORCOUNT` | SmallInteger | Number of Floors |  |
| `SPRINKLED` | String | Sprinkled | len 5 |
| `KEYBOX` | String | Key Box | len 5 |
| `COMMENT` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 6: Utility Shutoffs

- **Records:** 2
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 30 |
| `SHUTOFFTYPE` | String | Type | **Values:** `CNG` = Compressed Natural Gas Shut Off; `Electrical` = Electrical Shut Off; `Gas` = Gas Shut Off; `LNG` = Liquefied Natural Gas Shut Off; `Oxygen` = Oxygen Shut Off; `Telco` = Telecommunications Shut Off; `Water` = Water Shut Off · len 100 |
| `FLOOR` | String | Floor Number | len 5 |
| `LOCDESC` | String | Location Description | len 255 |
| `COMMENTS` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 7: Fire Hose Lines

- **Records:** 0
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 30 |
| `HOSELENGTH` | SmallInteger | Length |  |
| `LOCDESC` | String | Location Description | len 255 |
| `COMMENTS` | String | Comments | len 255 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 8: Pre-Incident Plans

- **Records:** 89,906
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PLANID` | String | Plan ID | len 25 |
| `PLANNAME` | String | Plan Name | len 255 |
| `COMPNAME` | String | Complex | len 255 |
| `FULLADDR` | String | Full Address | len 255 |
| `LOCDESC` | String | Location Description | len 255 |
| `POCNAME` | String | Contact Name | len 50 |
| `POCPHONE` | String | Contact Phone | len 25 |
| `POCEMAIL` | String | Contact Email | len 25 |
| `BLDGAREA` | Double | Building Area |  |
| `BLDGHEIGHT` | Double | Building Height |  |
| `FLOORCOUNT` | SmallInteger | Number of Floors |  |
| `YEARBUILT` | Double | Year Built |  |
| `NFIRSCD` | String | NIFRS Code | **Values:** `100` = Assembly, Other; `200` = Educational, Other; `300` = Health Care, Detention, and Correction, Other; `400` = Residential, Other; `500` = Mercantile, Business, Other; `600` = Industrial, Utility, Defense, Agriculture, Mining, Other; `700` = Manufacturing; `800` = Storage, Other; `900` = Outside or Special Property, Other; `000` = Property Use, Other; `NNN` = None; `UUU` = Undetermined · len 255 |
| `FIRELOAD` | String | Fire Load | **Values:** `High` = High; `Medium` = Medium; `Low` = Low · len 255 |
| `CONSTRTYP` | String | Construction Type | **Values:** `Type I - Fire Resistive` = Type I - Fire Resistive; `Type II - Noncombustible` = Type II - Noncombustible; `Type III - Ordinary` = Type III - Ordinary; `Type IV - Heavy Timber` = Type IV - Heavy Timber; `Type V - Wood Frame` = Type V - Wood Frame; `Mixed Types` = Mixed Types; `Other` = Other · len 100 |
| `ROOFTYPE` | String | Roof Type | **Values:** `Concrete - Poured in Place` = Concrete - Poured in Place; `Concrete on Metal Deck` = Concrete on Metal Deck; `Concrete Panel` = Concrete Panel; `Metal Deck` = Metal Deck; `Panelized Wood` = Panelized Wood; `Plywood` = Plywood; `TongueGroove - Metal Beam` = TongueGroove - Metal Beam; `TongueGroove - Wood Beam` = TongueGroove - Wood Beam; `Truss - Light Weight Wood` = Truss - Light Weight Wood; `Truss - Metal` = Truss - Metal; `Truss - Wood Chord - Metal Web` = Truss - Wood Chord - Metal Web; `Other` = Other; …(+1 more) · len 100 |
| `ROOFCOVER` | String | Roof Cover | **Values:** `Composition` = Composition; `Concrete Poured` = Concrete Poured; `Concrete Tile` = Concrete Tile; `Hot Mopped Tar` = Hot Mopped Tar; `Masonite` = Masonite; `Membrane` = Membrane; `Metal` = Metal; `Plastic` = Plastic; `Tile` = Tile; `Wood Shake` = Wood Shake; `Other` = Other · len 100 |
| `WALLTYPE` | String | Wall Type | **Values:** `Fence` = Fence; `Interior Wall` = Interior Wall; `Fire Wall Seperation` = Fire Wall Seperation; `Exterior Wall` = Exterior Wall; `Fire Rating Wall - One Half Hour` = Fire Rating Wall - One Half Hour; `Fire Rating Wall - One Half Hour with Smoke Barrier` = Fire Rating Wall - One Half Hour with Smoke Barrier; `Fire Rating Wall - One Hour` = Fire Rating Wall - One Hour; `Fire Rating Wall - One Hour with Smoke Barrier` = Fire Rating Wall - One Hour with Smoke Barrier; `Fire Rating Wall - Two Hour` = Fire Rating Wall - Two Hour; `Fire Rating Wall - Two Hour with Smoke Barrier` = Fire Rating Wall - Two Hour with Smoke Barrier; `Fire Rating Wall - Three hour` = Fire Rating Wall - Three hour; `Fire Rating Wall - Three Hour with Smoke Barrier` = Fire Rating Wall - Three Hour with Smoke Barrier; …(+2 more) · len 100 |
| `BASEMENT` | String | Basement | len 5 |
| `SPRINKLED` | String | Sprinkled | len 5 |
| `KEYBOX` | String | Key Box | len 5 |
| `WTRSUPPLY` | String | Water Supply | len 5 |
| `STATION` | String | Station | len 50 |
| `SHIFT` | String | Shift | len 25 |
| `DUEDATE` | Date | Due Date |  |
| `INSPECTOR` | String | Inspected By | len 25 |
| `INSPECTDT` | Date | Last Inspected On |  |
| `COMMENT` | String | Comments | len 255 |
| `STATUS` | String | Status | **Values:** `Approved` = Approved; `Assigned` = Assigned; `Unassigned` = Unassigned; `Under Review` = Under Review · len 25 |
| `CreationDate` | Date |  |  |
| `Creator` | String |  | len 50 |
| `EditDate` | Date |  |  |
| `Editor` | String |  | len 50 |
| `BUILDINGTY` | String |  | **Values:** `0` = Building; `2` = Foundation; `3` = Assembly; `4` = Business; `5` = Educational; `6` = Factory; `7` = Mercantile; `8` = Residential; `9` = Storage; `10` = Other; `1` = Institutional · len 50 |
| `WFPA` | String |  | **Values:** `1-Year` = 1-Year; `5-Year` = 5-Year · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 9: SDE.GISADMIN.Utility_Shutoffs__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 10: SDE.GISADMIN.Pre_Incident_Plans__ATTACH

- **Records:** 36

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 11: SDE.GISADMIN.Occupancies__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 12: SDE.GISADMIN.Key_Boxes__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 13: SDE.GISADMIN.Hazardous_Materials__ATTACH

- **Records:** 1

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 14: SDE.GISADMIN.Fire_Suppression_Systems__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 15: SDE.GISADMIN.Alarm_Control_Panels__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 16: SDE.GISADMIN.Building_Access__ATTACH

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

