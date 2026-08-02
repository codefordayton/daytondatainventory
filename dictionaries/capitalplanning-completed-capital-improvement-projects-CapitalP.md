# CapitalPlanning/Completed_Capital_Improvement_Projects

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/CapitalPlanning/Completed_Capital_Improvement_Projects/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=CapitalPlanning_Completed_Capital_Improvement_Projects
- **Created:** None  ·  **Item modified:** None
- **Tags:** CapitalPlanning

## Layer 0: Capital Imrpovement Project

- **Records:** 264
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PROJID` | String | Project Identifer | len 50 |
| `PROJNAME` | String | Project Name | len 255 |
| `PROJDESC` | String | Description | len 2000 |
| `PROJTYPE` | String | Project Type | len 50 |
| `FISCALYR` | String | Fiscal Year | len 10 |
| `PRIMARYFUND` | String | Primary Funding Source | len 50 |
| `PLANSTART` | Date | Planned Start Date |  |
| `PLANEND` | Date | Planned End Date |  |
| `FUNDED` | String | Funded Project | len 5 |
| `PROJPHASE` | String | Project Phase | len 255 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `DESIGNER` | String | Project Designer | len 255 |
| `SECONDFUND` | String | Secondary Funding Source | len 255 |
| `FUNDCOMMENT` | String | Funding Comments | len 255 |
| `PROJECTMANAGER` | String | Project Manager Name | len 255 |
| `PMPHONE` | String | Project Manager Phone Number | len 255 |
| `PMEMAIL` | String | Project Manager Email Address | len 255 |
| `CONSULTANT` | String | Consultant Name | len 255 |
| `CONSULTANTPHONE` | String | Consultant Phone Number | len 255 |
| `CONSULTANTEMAIL` | String | Consultant Email | len 255 |
| `CONTRACTOR` | String | Contractor Name | len 255 |
| `CONTRACTORPHONE` | String | Contractor Phone Number | len 255 |
| `CONTRACTOREMAIL` | String | Contractor Email | len 255 |
| `ContractNumber` | String | Contract Number | len 255 |
| `ActivityCode` | String | Activity Code | len 255 |
| `ProjectRationale` | String | Rationale | len 255 |
| `ProjectRationaleComments` | String | Rationale Comments | len 255 |
| `ProjectDivision` | String | Division | len 255 |
| `PrimaryFundingAmount` | Double | Primary Funding Amount |  |
| `SecondaryFundingAmount` | Double | Secondary Funding Amount |  |
| `JointFundBreakdown` | String | Joint Funding Breakdown | len 255 |
| `EstDesignCost` | Double | Estimated Design Cost |  |
| `EstConstructionCost` | Double | Estimated Construction Cost |  |
| `AwdDesignCost` | Double | Awarded Design Cost |  |
| `AwdConstructionCost` | Double | Awarded Construction Cost |  |
| `SurveyorName` | String | Surveyor Name | len 255 |
| `SurveyorPhone` | String | Surveyor Phone Number | len 255 |
| `SurveyorEmail` | Integer | Surveyor Email |  |
| `SurveyPath` | String | Survey Path | len 255 |
| `ConsultantPOCName` | String | Consultant POC Name | len 255 |
| `ConsultantPOCPhone` | String | Consultant POC Phone Number | len 255 |
| `ConsultantPOCEmail` | String | Consultant POC Email | len 255 |
| `AwardedBidPath` | String | Awarded Bid Path | len 255 |
| `DrawingNumber` | String | ConstructionDrawing Number | len 255 |
| `ConstructionPlansPath` | String | Construction Plans Path | len 255 |
| `ConstructionPOCName` | String | Construction POC Name | len 255 |
| `ConstructionPOCPhone` | String | Construction POC Phone Number | len 255 |
| `ConstructionPOCEmail` | String | Construction POC Email | len 255 |
| `InspectorName` | String | Inspector Name | len 255 |
| `InspectorPhone` | String | Inspector Phone Number | len 255 |
| `InspectorEmail` | String | Inspector Email | len 255 |
| `AsBuiltNumber` | String | AsBuilt Number | len 255 |
| `AsBuiltPath` | String | AsBuilt Path | len 255 |
| `ConstructionStrtDate` | DateOnly | Construction Start Date |  |
| `ConstructionEndDate` | DateOnly | Construction End Date |  |
| `ActualDesignCost` | Double | Actual Design Cost |  |
| `ActualCnstrctnCost` | Double | Actual Construction Cost |  |
| `AOWPath` | String | Acceptance of Work Path | len 255 |
| `ProjectPath` | String | Project Folder Path | len 255 |
| `ORIG_FID` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: City of Dayton Limits

- **Records:** 2
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PERIMETER` | Double |  |  |
| `BIGBNDY_` | Integer |  |  |
| `BIGBNDY_ID` | Integer |  |  |
| `NAME` | String |  | len 50 |
| `NAME_CODE` | Integer |  |  |
| `EDITORNAME` | String |  | len 50 |
| `VERSIONNAM` | String |  | len 50 |
| `EDITTOOL` | String |  | len 50 |
| `EDITTASK` | String |  | len 50 |
| `LASTUPDATE` | Date |  |  |
| `Done` | String |  | len 254 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID_1` | OID |  |  |
| `OBJECTID` | Integer |  |  |
| `Shape_STAr` | Double |  |  |
| `Shape_STLe` | Double |  |  |
| `Shape` | Geometry |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 2: City of Dayton Neighborhood

- **Records:** 66
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GISADMIN_N` | String |  | len 14 |
| `LAYER` | String |  | len 32 |
| `LEVEL_` | Double |  |  |
| `COLOR` | Integer |  |  |
| `MSLINK_ORA` | Double |  |  |
| `PRI_BOARD` | String |  | len 5 |
| `HOOD` | String |  | len 50 |
| `ABR` | String |  | len 35 |
| `PLC_BEAT` | Integer |  |  |
| `PLC_DISTR` | Integer |  |  |
| `GISADMIN_1` | Double |  |  |
| `ACRES` | Double |  |  |
| `PERIMETER` | Double |  |  |
| `OLD_ABR` | String |  | len 15 |
| `OLD_HOOD` | String |  | len 50 |
| `Done` | String |  | len 254 |
| `PRIBD` | String |  | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | String |  | len 38 |
| `Shape` | Geometry |  |  |
| `GlobalID_1` | GlobalID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

