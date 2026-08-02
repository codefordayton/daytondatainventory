# LCRR/LCRR_Data

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/LCRR/LCRR_Data/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=LCRR_LCRR_Data
- **Created:** None  ·  **Item modified:** None
- **Tags:** LCRR

## Layer 2: LCRR School and Childcare Facilities

- **Records:** 150
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `FACILITY_NAME` | String | Facility Name | len 255 |
| `FACILITY_TYPE` | String | Facility Type | **Values:** `Unknown` = Unknown; `School` = School; `Childcare` = Childcare · len 255 |
| `STRT_ADD` | String | Street Address | len 255 |
| `CITY` | String | City | len 255 |
| `STATE` | String | State | len 255 |
| `ZIP` | SmallInteger | Zip Code (5-Digit) |  |
| `CNTCT_NAME` | String | Contact Name | len 255 |
| `CNTCT_EMAIL` | String | Contact Email | len 255 |
| `CNTCT_PHONE` | String | Contact Phone | len 255 |
| `SMPL_GROUP` | String | Sample Group | **Values:** `Not Specified` = Not Specified; `By Request` = By Request; `Year 1` = Year 1; `Year 2` = Year 2; `Year 3` = Year 3; `Year 4` = Year 4; `Year 5` = Year 5 · len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 3: Service Connections

- **Records:** 64,725
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PUB_PREDICTED_MAT` | String | Public Predicted Material | len 255 |
| `PUB_PREDICTED_PROB` | String | Public Predicted Probability | len 255 |
| `PRI_PREDICTED_MAT` | String | Private Predicted Material | len 255 |
| `PRI_PREDICTED_PROB` | String | Private Predicted Probability | len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `EPA_ID` | String | EPA Unique Identifier | len 255 |
| `STRT_ADD` | String | Street Address | len 255 |
| `CITY` | String | City | len 255 |
| `STATE` | String | State | len 255 |
| `CSTMR_NAME` | String | Customer Name | len 255 |
| `CSTMR_EMAIL` | String | Customer Email | len 255 |
| `CSTMR_PHONE` | String | Customer Phone | len 255 |
| `SENS_POP` | String | Sensitive Population? | **Values:** `Unknown` = Unknown; `No` = No; `Yes - School` = Yes - School; `Yes - Daycare` = Yes - Daycare; `Yes - Multifamily Home` = Yes - Multifamily Home; `Yes - Other` = Yes - Other · len 255 |
| `DISADV_NGHBR` | String | Disadvantaged Neighborhood? | **Values:** `Unknown` = Unknown; `No` = No; `Yes` = Yes · len 255 |
| `PUB_ASSETID` | String | Public Assett ID | len 255 |
| `PUB_MATERIAL` | String | Public Material Classification | **Values:** `Unknown` = Unknown; `Lead` = Lead; `Galvanized` = Galvanized; `Non-lead - Plastic` = Non-lead - Plastic; `Non-lead - Copper` = Non-lead - Copper; `Non-lead - Other` = Non-lead - Other; `Unknown - Likely Lead` = Unknown - Likely Lead; `Unknown - Unlikely Lead` = Unknown - Unlikely Lead; `Unknown - Lead Status Unknown` = Unknown - Lead Status Unknown · len 255 |
| `PUB_PREVLEAD` | String | Public Previously Lead | **Values:** `Unknown` = Unknown; `Yes` = Yes; `No` = No · len 255 |
| `PUB_INSTDATE` | Date | Public Install Date |  |
| `PUB_REPLDATE` | Date | Public Replacement Date |  |
| `PUB_REPSTATUS` | String | Public Replacement Status | **Values:** `Unknown` = Unknown; `Potential` = Potential; `Required` = Required; `Complete` = Complete; `Not Required` = Not Required · len 255 |
| `PUB_CLASSBASIS` | String | Public Basis of Classification | **Values:** `Previous Materials Classification` = Previous Materials Classification; `Installation Record (e.g. tap card)` = Installation Record (e.g. tap card); `Installation date after lead ban` = Installation date after lead ban; `Service line diameter is > 2 inches` = Service line diameter is > 2 inches; `Service line repair or replacement record` = Service line repair or replacement record; `Predictive Model` = Predictive Model; `Water sampling only with no records` = Water sampling only with no records; `Field inspection only with no records` = Field inspection only with no records; `Aerial Interpretation` = Aerial Interpretation; `Other` = Other; `Not Specified` = Not Specified; `Statistical Analysis` = Statistical Analysis · len 255 |
| `PUB_FLDVERSTATUS` | String | Public Field Verification Status | **Values:** `Not Required` = Not Required; `Required` = Required; `Completed` = Completed; `Not Specified` = Not Specified; `Yes` = Yes; `No` = No · len 255 |
| `PUB_FLDVERMETHOD` | String | Public Field Verification Method | **Values:** `Customer self-identification` = Customer self-identification; `CCTV investigation at curb stop - internal` = CCTV investigation at curb stop - internal; `CCTV investigation at curb stop - external` = CCTV investigation at curb stop - external; `Water quality sampling` = Water quality sampling; `Mechanical excavation at one location` = Mechanical excavation at one location; `Mechanical excavation at multiple locations` = Mechanical excavation at multiple locations; `Visual inspection at the meter pit` = Visual inspection at the meter pit; `Other` = Other; `Not Field Verified` = Not Field Verified; `Not Specified` = Not Specified · len 255 |
| `PUB_FLDVERDATE` | Date | Public Field Verification Date |  |
| `PUB_NOTES` | String | Public General Notes | len 255 |
| `PUB_LEADSTATUS` | String | Public Lead Status | **Values:** `Lead` = Lead; `Non-Lead` = Non-Lead; `Unknown` = Unknown; `Galvanized Requiring Replacement` = Galvanized Requiring Replacement · len 255 |
| `PRI_ASSETID` | String | Private Account ID | len 255 |
| `PRI_MATERIAL` | String | Private Material Classification | **Values:** `Unknown` = Unknown; `Lead` = Lead; `Galvanized` = Galvanized; `Non-lead - Plastic` = Non-lead - Plastic; `Non-lead - Copper` = Non-lead - Copper; `Non-lead - Other` = Non-lead - Other; `Unknown - Likely Lead` = Unknown - Likely Lead; `Unknown - Unlikely Lead` = Unknown - Unlikely Lead; `Unknown - Lead Status Unknown` = Unknown - Lead Status Unknown · len 255 |
| `PRI_INSTDATE` | Date | Private Install Date |  |
| `PRI_REPLDATE` | Date | Private Replacement Date |  |
| `PRI_REPLNOTIFDATE` | Date | Private Customer Reported Replacement Date |  |
| `PRI_REPSTATUS` | String | Private Replacement Status | **Values:** `Unknown` = Unknown; `Potential` = Potential; `Required` = Required; `Complete` = Complete; `Customer Reported` = Customer Reported; `Not Required` = Not Required · len 255 |
| `PRI_CLASSBASIS` | String | Private Basis of Classification | **Values:** `Previous Materials Classification` = Previous Materials Classification; `Installation Record (e.g. tap card)` = Installation Record (e.g. tap card); `Installation date after lead ban` = Installation date after lead ban; `Service line diameter is > 2 inches` = Service line diameter is > 2 inches; `Service line repair or replacement record` = Service line repair or replacement record; `Predictive Model` = Predictive Model; `Water sampling only with no records` = Water sampling only with no records; `Field inspection only with no records` = Field inspection only with no records; `Aerial Interpretation` = Aerial Interpretation; `Other` = Other; `Not Specified` = Not Specified; `Statistical Analysis` = Statistical Analysis · len 255 |
| `PRI_FLDVERSTATUS` | String | Private Field Verification Status | **Values:** `Not Required` = Not Required; `Required` = Required; `Completed` = Completed; `Not Specified` = Not Specified; `Yes` = Yes; `No` = No · len 255 |
| `PRI_FLDVERMETHOD` | String | Private Field Verification Method | **Values:** `Customer self-identification` = Customer self-identification; `CCTV investigation at curb stop - internal` = CCTV investigation at curb stop - internal; `CCTV investigation at curb stop - external` = CCTV investigation at curb stop - external; `Water quality sampling` = Water quality sampling; `Mechanical excavation at one location` = Mechanical excavation at one location; `Mechanical excavation at multiple locations` = Mechanical excavation at multiple locations; `Visual inspection at the meter pit` = Visual inspection at the meter pit; `Other` = Other; `Not Field Verified` = Not Field Verified; `Not Specified` = Not Specified · len 255 |
| `PRI_FLDVERDATE` | Date | Private Field Verification Date |  |
| `PRI_NOTES` | String | Private General Notes | len 255 |
| `PRI_LEADSTATUS` | String | Private Lead Status | **Values:** `Lead` = Lead; `Non-Lead` = Non-Lead; `Galvanized Requiring Replacement` = Galvanized Requiring Replacement; `Unknown` = Unknown · len 255 |
| `FULL_LEADSTATUS` | String | Full Line Lead Status | **Values:** `Lead` = Lead; `Non-Lead` = Non-Lead; `Galvanized Requiring Replacement` = Galvanized Requiring Replacement; `Unknown` = Unknown · len 255 |
| `LEADCONNECTOR` | String | Lead Connector Status | **Values:** `Unknown` = Unknown; `Removed` = Removed; `Not Present` = Not Present; `Present` = Present · len 255 |
| `LEADSOLDER` | String | Lead Solder Status | **Values:** `Unknown` = Unknown; `No` = No; `Yes` = Yes · len 255 |
| `OTHRFITTINGS` | String | Describe Other Lead Fittings/Equipment | len 255 |
| `SRVC_TYPE` | String | Facility Type Serviced | **Values:** `Single Family Residence` = Single Family Residence; `Muliple Family Residence` = Muliple Family Residence; `School/Childcare Facility` = School/Childcare Facility; `Business/Commercial` = Business/Commercial; `Medical Facility` = Medical Facility; `Elder Care Facility` = Elder Care Facility; `Other` = Other; `Unknown` = Unknown · len 255 |
| `PNT_TRTMNT` | String | Point-of-Entry or Point-of-Use Treatment | **Values:** `Unknown` = Unknown; `Yes` = Yes; `No` = No · len 255 |
| `INTERIORPLUMBING` | String | Interior Pre-Ban Copper w/Lead Solder | **Values:** `Unknown` = Unknown; `Yes` = Yes; `No` = No · len 255 |
| `CURRNT_SAMPL_STE` | String | Current Compliance Sampling Site? | **Values:** `Unknown` = Unknown; `Yes` = Yes; `No` = No · len 255 |
| `NRST_PRCL_DTE` | Date | Nearest Parcel Date |  |
| `NRST_MAIN_DTE` | Date | Nearest Main Install Date |  |
| `PUB_DIAM` | Double | Public Diameter | **Values:** `-1` = Unknown; `0` = Unknown | < 2"; `99` = Unknown || > 2"; `0.25` = 1/4"; `0.5` = 1/2"; `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `1.75` = 1 3/4"; `2` = 2"; `2.25` = 2 1/4"; …(+19 more) |
| `PRI_DIAM` | Double | Private Diameter | **Values:** `-1` = Unknown; `0` = Unknown | < 2"; `99` = Unknown || > 2"; `0.25` = 1/4"; `0.5` = 1/2"; `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `1.75` = 1 3/4"; `2` = 2"; `2.25` = 2 1/4"; …(+19 more) |
| `ADDRKEY` | Integer |  |  |
| `COMPKEY` | Integer |  |  |
| `FULL_PREDICTED_MAT` | String | Full Predicted Material | len 255 |
| `PUB_EPA_PRED_MAT` | String | State/EPA Public Material Classification | len 255 |
| `PRI_EPA_PRED_MAT` | String | State/EPA Private Predicted Material Classification | len 255 |
| `STNO` | String |  | len 255 |
| `STNAME` | String |  | len 255 |
| `COUNTY` | String |  | len 255 |
| `ZIP` | Integer |  |  |
| `POINT_X` | Double |  |  |
| `POINT_Y` | Double |  |  |
| `POINT_Z` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 5: Compliance Sampling

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `CS_DATE` | Date | Activity Date |  |
| `CS_COMMENTS` | String | Comments | len 255 |
| `CS_TYPE` | String | Sampling Type | len 255 |
| `CS_RESULTS` | Single | Results (µg/L) |  |
| `CS_STATUS` | String | STATUS | len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 6: Field Incident Coordination

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `FI_DATE` | Date | Activity Date |  |
| `FI_COMMENTS` | String | Comments | len 255 |
| `FI_TYPE` | String | Type | **Values:** `Property Damage` = Property Damage; `Leak (Utility Side)` = Leak (Utility Side); `Leak (Public Side)` = Leak (Public Side); `Leak (Both Sides)` = Leak (Both Sides) · len 255 |
| `FI_STATUS` | String | Status | **Values:** `Reported` = Reported; `Resolution In Progress` = Resolution In Progress; `Resolved` = Resolved · len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 7: Field Verification Coordination

- **Records:** 17

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `FV_DATE` | Date | Activity Date |  |
| `FV_COMMENTS` | String | Comments | len 255 |
| `FV_STATUS` | String | Status | **Values:** `Customer Not Reached` = Customer Not Reached; `Approved` = Approved; `Not Approved` = Not Approved · len 255 |
| `FV_EARLIESTDATE` | Date | Earliest Date |  |
| `FV_LATESTDATE` | Date | Latest Date |  |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 8: Flushing Coordination

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `FL_DATE` | Date | Activity Date |  |
| `FL_COMMENTS` | String | Comments | len 255 |
| `FL_STATUS` | String | Status | **Values:** `Customer Not Reached` = Customer Not Reached; `Customer Declined Flushing` = Customer Declined Flushing; `Customer Approved Flushing` = Customer Approved Flushing; `Flushing Completed` = Flushing Completed · len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 9: Pitcher Filter Coordination

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `PF_DATE` | Date | Activity Date |  |
| `PF_COMMENTS` | String | Comments | len 255 |
| `PF_METHOD` | String | Method Provided | **Values:** `In Person` = In Person; `Shipped` = Shipped; `Third Party` = Third Party · len 255 |
| `PF_TRACKING` | String | Tracking Info (If Shipped) | len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 10: Post-Replacement Sampling

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `PRS_DATE` | Date | Activity Date |  |
| `PRS_COMMENTS` | String | Comments | len 255 |
| `PRS_RES` | Single | Results (µg/L) |  |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 11: Replacement Coordination

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `RC_DATE` | Date | Activity Date |  |
| `RC_COMMENTS` | String | Comments | len 255 |
| `RC_STATUS` | String | Status | **Values:** `One Side | Customer Not Reached` = Customer Not Reached; `One Side | Customer Notified` = Customer Notified; `Both Sides | Customer Declined Replacement` = Both Sides | Customer Declined Replacement; `Both Sides | Customer Approved Replacement` = Both Sides | Customer Approved Replacement · len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 12: Sample Kit Coordination

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `SK_DATE` | Date | Activity Date |  |
| `SK_COMMENTS` | String | Comments | len 255 |
| `SK_STATUS` | String | Status | **Values:** `Customer Not Reached` = Customer Not Reached; `Customer Declined Sampling` = Customer Declined Sampling; `Customer Approved Sampling` = Customer Approved Sampling · len 255 |
| `SK_METHOD` | String | Method Provided | **Values:** `In Person` = In Person; `Shipped` = Shipped; `Third Party` = Third Party · len 255 |
| `SK_TRACKING` | String | Tracking Info (If Shipped) | len 255 |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 13: School and Childcare Facilities Sampling

- **Records:** 0

| Field | Type | Alias | Notes |
|---|---|---|---|
| `created_by` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_by` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `PARENTGUID` | GUID |  |  |
| `FACILITY_TYPE` | String | Facility Type | **Values:** `Unknown` = Unknown; `School` = School; `Childcare` = Childcare · len 255 |
| `SMPL_STATUS` | String | Samplng Approval Status | **Values:** `Accepted` = Accepted; `Declined` = Declined; `Not Reached` = Not Reached · len 255 |
| `STATUS_CMMNTS` | String | Samplng Approval Comments | len 255 |
| `SMPL_DATE` | Date | Sampling Date |  |
| `LOC_ONE` | String | Location One | len 255 |
| `LOC_ONE_RES` | Single | Location One Results (µg/L) |  |
| `LOC_TWO` | String | Location Two | len 255 |
| `LOC_TWO_RES` | Single | Location Two Results (µg/L) |  |
| `LOC_THREE` | String | Location Three (Schools Only) | len 255 |
| `LOC_THREE_RES` | Single | Location Three Results (µg/L, Schools Only) |  |
| `LOC_FOUR` | String | Location Four (Schools Only) | len 255 |
| `LOC_FOUR_RES` | Single | Location Four Results (µg/L, Schools Only) |  |
| `LOC_FIVE` | String | Location Five (Schools Only) | len 255 |
| `LOC_FIVE_RES` | Single | Location Five Results (µg/L, Schools Only) |  |
| `MAX_RES` | Single | Maximum Results Status |  |
| `created_user` | String |  | len 255 |
| `last_edited_user` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

