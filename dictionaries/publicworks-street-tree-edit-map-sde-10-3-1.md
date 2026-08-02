# PublicWorks/Street_Tree_Edit_Map_SDE_10_3_1

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/PublicWorks/Street_Tree_Edit_Map_SDE_10_3_1/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=PublicWorks_Street_Tree_Edit_Map_SDE_10_3_1
- **Created:** None  ·  **Item modified:** None
- **Tags:** PublicWorks

## Layer 0: Street Tree

- **Records:** 13,941
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `SPECIES` | String | Tree Species | len 50 |
| `DIAMETER` | String | Diameter DBH | len 50 |
| `STEMS` | SmallInteger | Number of Stems |  |
| `GSPACETP` | String | Growspace Type | len 50 |
| `CONDITION` | String | Condition | len 50 |
| `MAINTENANC` | String | Maintenance | len 50 |
| `UTILPROB` | String | Utility Problem | len 50 |
| `UTILDAMG` | String | Utility Damage | len 50 |
| `BLKSGN` | String | Blocking Sign | len 10 |
| `BLKSL` | String | Blocking Streetlight | len 10 |
| `STUMP` | String | Stump | len 10 |
| `INSPMORE` | String | Inspect More | len 10 |
| `NOTES` | String | Field Notes | len 50 |
| `OBS1` | String | Observation 1 | len 50 |
| `OBS2` | String | Observation 2 | len 50 |
| `NEIGHBORHOOD` | String | Neighborhood | len 50 |
| `ADDRES` | String | Nearest Address | len 100 |
| `LOCATION` | String | Location Note | len 75 |
| `created_user` | String | Added By | len 255 |
| `created_date` | Date | Added Date |  |
| `last_edited_user` | String | Edited By | len 255 |
| `last_edited_date` | Date | Edited Date |  |
| `TreeRemovedDt` | Date | Date Tree Removed |  |
| `StumpRemovedDt` | Date | Date Stump Removed |  |
| `OLD_NEIGHBORHOOD` | String |  | len 50 |
| `OID_Old` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID | Tree ID |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: Street Tree Inspection

- **Records:** 415

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TREEID` | Integer | Tree ID |  |
| `INSPTYPE` | String | Inspection Type
 | **Values:** `Inspection` = Inspection; `Maintenance` = Maintenance · len 50 |
| `MAINT` | String | Maintenance Need
 | **Values:** `Priority 1 Prune` = Priority 1 Prune; `Priority 1 Removal` = Priority 1 Removal; `Priority 2 Prune` = Priority 2 Prune; `Priority 2 Removal` = Priority 2 Removal; `Priority 3 Removal` = Priority 3 Removal; `Routine Prune` = Routine Prune; `Stump Removal` = Stump Removal; `Training Prune` = Training Prune; `None` = None; `Plant Tree` = Plant Tree · len 50 |
| `FAILPROB` | String | Probability of Failure
 | **Values:** `N/A` = N/A; `Low` = Low; `Moderate` = Moderate; `High` = High; `Extremely High` = Extremely High · len 50 |
| `DEFECTSZ` | String | Size of Defect
 | **Values:** `N/A` = N/A; `<4"` = <4"; `4-20"` = 4-20"; `>20"` = >20" · len 50 |
| `TARGETRISK` | String | Target Risk
 | **Values:** `N/A` = N/A; `Occasional` = Occasional; `Intermittent` = Intermittent; `Frequent` = Frequent · len 50 |
| `OTHERRISK` | String | Other Risk
 | **Values:** `None` = None; `Additional` = Additional; `High Additional` = High Additional · len 50 |
| `INOTE` | String | Inspection Notes
 | len 1073741822 |
| `created_user` | String | Inspected By | len 255 |
| `created_date` | Date | Inspection Date |  |
| `last_edited_user` | String | Edited By | len 255 |
| `last_edited_date` | Date | Edited Date |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID | Inspection ID |  |
| `GlobalID_1` | GlobalID |  |  |

</details>

