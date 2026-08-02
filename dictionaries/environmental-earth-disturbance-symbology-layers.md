# Environmental/Earth_Disturbance_Symbology_Layers

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Environmental/Earth_Disturbance_Symbology_Layers/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Environmental_Earth_Disturbance_Symbology_Layers
- **Created:** None  ·  **Item modified:** None
- **Tags:** Environmental

## Layer 4: Active Inspections <1 Acre

- **Records:** unknown
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ProjectTitle` | String |  | len 500 |
| `AreaofED` | Double |  |  |
| `ActiveProject` | String |  | len 50 |
| `ProjectLocation` | String |  | len 255 |
| `RowNumber` | OID |  |  |
| `DaysSince` | Integer |  |  |
| `IsFinal` | String |  | len 19 |
| `app_ObjectID` | Integer |  |  |
| `app_GlobalID` | GUID |  |  |
| `AssInspector` | String |  | len 55 |
| `app_created_date` | Date |  |  |
| `VIOLATIONNUM` | String |  | len 255 |
| `insp_ObjectID` | Integer |  |  |
| `insp_GlobalID` | GUID |  |  |
| `insp_created_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Shape` | Geometry |  |  |

</details>

## Layer 3: Active Inspections >1 Acre

- **Records:** unknown
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ProjectTitle` | String |  | len 500 |
| `AreaofED` | Double |  |  |
| `ActiveProject` | String |  | len 50 |
| `ProjectLocation` | String |  | len 255 |
| `RowNumber` | OID |  |  |
| `DaysSince` | Integer |  |  |
| `IsFinal` | String |  | len 19 |
| `app_ObjectID` | Integer |  |  |
| `app_GlobalID` | GUID |  |  |
| `AssInspector` | String |  | len 55 |
| `app_created_date` | Date |  |  |
| `VIOLATIONNUM` | String |  | len 255 |
| `insp_ObjectID` | Integer |  |  |
| `insp_GlobalID` | GUID |  |  |
| `insp_created_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Shape` | Geometry |  |  |

</details>

## Layer 5: Violation Found

- **Records:** 54
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OwnerCompanyName` | String |  | len 255 |
| `OwnerContactName` | String |  | len 255 |
| `OwnerStreetAddress` | String |  | len 255 |
| `OwnerCity` | String |  | len 255 |
| `OwnerState` | String |  | len 255 |
| `OwnerZip` | Double |  |  |
| `OwnerPhoneNumber` | String |  | len 30 |
| `OwnerEmail` | String |  | len 255 |
| `ContractCompanyName` | String |  | len 255 |
| `ContractContactName` | String |  | len 255 |
| `ContractStreetAddress` | String |  | len 255 |
| `ContractCity` | String |  | len 255 |
| `ContractState` | String |  | len 255 |
| `ContractZip` | Double |  |  |
| `ContractPhone` | String |  | len 30 |
| `ContractEmail` | String |  | len 255 |
| `EngCompanyName` | String |  | len 255 |
| `EngContactPerson` | String |  | len 255 |
| `EngStreetAddress` | String |  | len 255 |
| `EngCity` | String |  | len 255 |
| `EngState` | String |  | len 255 |
| `EngZip` | Double |  |  |
| `EngPhone` | String |  | len 30 |
| `EngEmail` | String |  | len 255 |
| `ProjectTitle` | String |  | len 500 |
| `ProjectAddess` | String |  | len 255 |
| `ProjectType` | String |  | len 50 |
| `ProjectType1` | String |  | len 50 |
| `ProjectType2` | String |  | len 50 |
| `ProjectType3` | String |  | len 50 |
| `ProjectType4` | String |  | len 50 |
| `ProjectType5` | String |  | len 50 |
| `ProjectType6` | String |  | len 50 |
| `ProjectType7` | String |  | len 50 |
| `AreaofED` | Double |  |  |
| `ProjectStart` | Date |  |  |
| `ProjectComplete` | Date |  |  |
| `OverOneAcre` | String |  | len 25 |
| `SedPlan` | String |  | len 25 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `ActiveProject` | String |  | len 50 |
| `ProjectLocation` | String |  | len 255 |
| `ProjectContact` | String |  | len 255 |
| `PersonOnSite` | String |  | len 255 |
| `Weather` | String |  | len 500 |
| `ApplicationRecieved` | String |  | len 50 |
| `SWPOnSite` | String |  | len 50 |
| `EPALetterOnSite` | String |  | len 50 |
| `ContractorInspection` | String |  | len 50 |
| `SoilLog` | String |  | len 50 |
| `TempStableReq` | String |  | len 50 |
| `TempStableTime` | String |  | len 50 |
| `MulchBlown` | String |  | len 50 |
| `TempStableFinding` | String |  | len 1000 |
| `PermStableReq` | String |  | len 50 |
| `PermStableTime` | String |  | len 50 |
| `PermStableFinding` | String |  | len 1000 |
| `HighVelocityRunoff` | String |  | len 50 |
| `CheckDam` | String |  | len 50 |
| `OtherErosionControlFind` | String |  | len 1000 |
| `SiltFenceReq` | String |  | len 50 |
| `SiltFenceMaintain` | String |  | len 50 |
| `AddFenceNeed` | String |  | len 50 |
| `SedBarrierFinding` | String |  | len 1000 |
| `InletProtectReq` | String |  | len 50 |
| `InletProtectMain` | String |  | len 50 |
| `AddInlet` | String |  | len 50 |
| `InletProtectFinding` | String |  | len 1000 |
| `SettlePondReq` | String |  | len 50 |
| `PondPerPlan` | String |  | len 50 |
| `PondMain` | String |  | len 50 |
| `PondFinding` | String |  | len 1000 |
| `ConstDriveReq` | String |  | len 50 |
| `ConstDesign` | String |  | len 50 |
| `ConstDriveMain` | String |  | len 50 |
| `MuddyTruck` | String |  | len 50 |
| `StreetSweep` | String |  | len 50 |
| `ConstEntranceFinding` | String |  | len 1000 |
| `ActiveDischarge` | String |  | len 50 |
| `IllDischarge` | String |  | len 50 |
| `DischargeFinding` | String |  | len 1000 |
| `ConcreteWash` | String |  | len 50 |
| `FuelTank` | String |  | len 50 |
| `IllDischargeNon` | String |  | len 50 |
| `NonSedFinding` | String |  | len 1000 |
| `BMPReq` | String |  | len 50 |
| `BMPInstall` | String |  | len 50 |
| `BMPFinding` | String |  | len 1000 |
| `FinalStable` | String |  | len 50 |
| `TempRemoved` | String |  | len 50 |
| `PostConstStorm` | String |  | len 50 |
| `NOTSubmit` | String |  | len 50 |
| `InspectionType` | String |  | len 125 |
| `created_user2` | String |  | len 255 |
| `created_date2` | Date |  |  |
| `last_edited_user2` | String |  | len 255 |
| `last_edited_date2` | Date |  |  |
| `RowNumber` | OID |  |  |
| `DaysSince` | Integer |  |  |
| `AssInspector` | String |  | len 55 |
| `VIOLATIONNUM` | String |  | len 255 |
| `EDASubmit` | String |  | len 255 |
| `SWPPONSITE` | String |  | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Shape` | Geometry |  |  |
| `GlobalID` | GUID |  |  |

</details>

## Layer 6: City of Dayton Corp Limit

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

