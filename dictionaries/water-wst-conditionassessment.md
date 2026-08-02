# Water/WST_ConditionAssessment

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Water/WST_ConditionAssessment/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Water_WST_ConditionAssessment
- **Created:** None  ·  **Item modified:** None
- **Tags:** Water

## Layer 0: Water Supply and Treatment Assets

- **Records:** 2,553
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ASSETID` | String | Asset ID | len 30 |
| `DESCRIPTION` | String | Desciption | len 50 |
| `MANUFACTURER` | String | Manufacturer | len 50 |
| `MODEL` | String | Model | len 50 |
| `SERIAL` | String | Serial Number | len 50 |
| `CAPACITY` | String | Capacity | len 50 |
| `MOTOR` | String | Motor | len 50 |
| `EQUIPMENTTYPE` | String | Equipment Type | len 50 |
| `INSTALLDATE` | String | Install Date | len 50 |
| `XCOORD` | Double | X Coordinate |  |
| `YCOORD` | Double | Y Coordinate |  |
| `ZCOORD` | String | Z Coordinate | len 15 |
| `LOCATION` | String | Location | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `TotalDepth` | String |  | len 50 |
| `ScreenLength` | String |  | len 50 |
| `SlotSize` | String |  | len 50 |
| `GravelSize` | String |  | len 50 |
| `CasingDiameter` | String |  | len 50 |
| `MaterialTypes` | String |  | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |

</details>

## Layer 1: Ancillary Electrical

- **Records:** 15

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ConcreteSupports_SurfaceCrackin` | String | Concrete Supports - Surface Cracking | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `ConcreteSupports_Cracks` | String | Concrete Supports - Cracks | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `ConcreteSupports_Missing` | String | Concrete Supports - Missing | **Values:** `None` = None; `1` = 1 or More · len 50 |
| `SteelSupports_SurfaceCorrosion` | String | Steel Supports - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `SteelSupports_StructuralCorrosi` | String | Steel Supports - Structural Corrosion | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `SteelSupports_DamagedAnchors` | String | Steel Supports - Damaged Anchors | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `Conduit_SurfaceCorrosion` | String | Conduit - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Conduit_StructuralCorrosion` | String | Conduit - Structural Corrosion | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `Conduit_SupportDamage` | String | Conduit - Support Damage | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `Conduit_ExposedWiring` | String | Conduit - Exposed Wiring | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Conduit_DamageGaskets` | String | Conduit - Damage Gaskets | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Conduit_Connections` | String | Conduit - Connections | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Door_Damage` | String | Door - Damage | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `AssetID` | String | Asset ID | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 2: Ancillary HVAC

- **Records:** 54

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PipingValves_Gaskets` | String | Piping/Valves - Gaskets | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `PipingValves_Holes` | String | Piping/Valves - Holes | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `PipingValves_SurfaceCorrosion` | String | Piping/Valves - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `PipingValves_StructuralCorrosio` | String | Piping/Valves - Structural Corrosion | **Values:** `None` = None; `< 10` = < 10 %; `10 - 20` = 10 - 20 %; `> 20` = > 20 % · len 50 |
| `PipingValves_Support_Damage` | String | Piping/Valves - Support Damage | **Values:** `None` = None; `<5` = < 5 %; `5-20` = 5 - 20 %; `> 20` = > 20 % · len 50 |
| `Ductwork_Holes` | String | Ductwork - Holes | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Ductwork_SurfaceCorrosion` | String | Ductwork - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Ductwork_StructuralCorrosion` | String | Ductwork - Structural Corrosion | **Values:** `None` = None; `<20` = < 20 %; `20` = 20 %; `>20` = > 20 % · len 50 |
| `Ductwork_SupportDamage` | String | Ductwork - Support Damage | **Values:** `None` = None; `<20` = < 20 %; `20` = 20 %; `>20` = > 20 % · len 50 |
| `Instruments_Damage` | String | Instruments - Damage | **Values:** `None` = None; `<20` = < 20 %; `20` = 20 %; `>20` = > 20 % · len 50 |
| `Instruments_Leakage` | String | Instruments - Leakage | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `LocalPanels_SurfaceCorrosion` | String | Local Panels - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `LocalPanels_StructuralDamage` | String | Local Panels - Structural Damage | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `LocalPanels_InternalCorrosion` | String | Local Panels - Internal Corrosion | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `LocalPanels_Instruments` | String | Local Panels - Instruments | **Values:** `None` = None; `<20` = < 20 %; `20` = 20 %; `>20` = > 20 % · len 50 |
| `Filters_Damage` | String | Filters - Damage | len 50 |
| `Filters_SurfaceCorrosion` | String | Filters - Surface Corrosion | len 50 |
| `Filters_Clogging` | String | Filters - Clogging | len 50 |
| `Motors_SurfaceCorrosion` | String | Motors - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Motors_SurfaceDamage` | String | Motors -Surface Damage | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Motors_NFDevices` | String | Motors - NF Devices | **Values:** `None` = None; `<20` = < 20 %; `20` = 20 %; `>20` = > 20 % · len 50 |
| `Insulation_Holes` | String | Insulation - Holes | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Insulation_Damage` | String | Insulation - Damage | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `AssetID` | String | Asset ID | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 3: Ancillary Mechanical

- **Records:** 636

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PipingValves_Gaskets` | String | Piping/Valves Leaks - Gaskets | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `PipingValves_HolesFailures` | String | Piping/Valves Holes-Failures | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `PipingValves_StructuralCorrosio` | String | Piping/Valves - Structural Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `PipingValves_SupportDamage` | String | Piping/Valves - Support Damage | **Values:** `None` = None; `<5` = < 5 %; `5-20` = 5 - 20 %; `> 20` = > 20 % · len 50 |
| `LocalPanels_SurfaceCorrosion` | String | Local Panels - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `LocalPanels_StructuralDamage` | String | Local Panels - Structural Damage | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `LocalPanels_InternalCorrosion` | String | Local Panels - Internal Corrosion | len 50 |
| `LocalPanels_PanelInstruments` | String | Local Panels - Panel NF | **Values:** `None` = None; `<20` = < 20 %; `20` = 20 %; `>20` = > 20 % · len 50 |
| `FieldInstruments_Damaged` | String | Field Instruments - Damaged | **Values:** `None` = None; `<20` = < 20 %; `20` = 20 %; `>20` = > 20 % · len 50 |
| `FieldInstruments_Leakage` | String | Field Instruments - Leakage | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `ElectricalConnections_Conduit` | String | Electrical Connections - Conduit | **Values:** `None` = None; `<20` = < 20 %; `20-50` = 20 - 50 %; `> 50` = > 50 % · len 50 |
| `ElectricalConnections_Damage` | String | Electrical Connections - Damage | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `ElectricalConnections_ExposedWi` | String | Electrical Connections -Exposed Wiring | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `PipingValves_SurfaceCorrosion` | String | Piping/Valves - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `AssetID` | String | Asset ID | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 4: Ancillary Structural

- **Records:** 9

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Wood_DryRot` | String | Wood - Dry Rot | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Wood_Warping` | String | Wood - Warping | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Wood_ConnectionFailure` | String | Wood - Connection Failure | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Wood_LossOfSection` | String | Wood - Loss Of Section | **Values:** `None` = None; `<10` = < 10 %; `10-30` = 10 - 30 %; `>30` = > 30 % · len 50 |
| `Roof_CracksJoints` | String | Roof - Cracks/Joint Leaks | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `Roof_Penetrations` | String | Roof - Penetration Leaks | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Roof_Sagging` | String | Roof - Sagging | **Values:** `None` = None; `Minor` = Minor; `Moderate` = Moderate; `Major` = Major; `Excessive` = Excessive · len 50 |
| `Roof_SupportDamage` | String | Roof - Support Damage | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `Interior_Flooring` | String | Interior - Flooring | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Interior_Partitions` | String | Interior - Partitions | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Interior_Ceiling` | String | Interior - Ceiling | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Interior_DoorsTrim` | String | Interior - Doors/Trim | **Values:** `None` = None; `1` = 1 or More · len 50 |
| `AssetID` | String | Asset ID | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 5: Core Electrical

- **Records:** 137

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Corrosion_Surface` | String | Corrosion - Surface | **Values:** `None` = None; `<20` = < 20 %; `20-50` = 20 - 50 %; `> 50` = > 50 % · len 50 |
| `Corrosion_Structural` | String | Corrosion - Structural | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `DielectricLeakage_Connections` | String | Dielectric Leakage - Connections | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `DielectricLeakage_Holes` | String | Dielectric Leakage - Holes | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Vibration_VibrationApparent` | String | Vibration - Vibration Apparent | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Vibration_NonStructural` | String | Vibration - Non Structural | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Vibration_Structural` | String | Vibration - Structural | len 50 |
| `Electrical_Overheating` | String | Electrical - Overheating | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Electrical_WaterDamage` | String | Electrical - Water Damage | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Electrical_Grounding` | String | Electrical - Grounding | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Electrical_Insulation` | String | Electrical - Insulation | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Electrical_Cooling` | String | Electrical - Cooling | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `AssetID` | String | Asset ID | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 6: Core HVAC

- **Records:** 88

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Corrosion_SurfaceOnly` | String | Corrosion - Surface Only | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Corrosion_Structural` | String | Corrosion - Structural (loss of metal) | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Leakage_Gaskets` | String | Leakage - Gaskets/Connections | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `Leakage_Holes` | String | Leakage - Holes/Failures | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Vibration_VibrationApparent` | String | Vibration - Vibration Apparent | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Vibration_NonStructuralDamage` | String | Vibration - Non Structural Damage | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Vibration_StructuralDamage` | String | Vibration - Structural Damage | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Concrete_Cracking` | String | Concrete - Surface Cracking | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Concrete_Cracks` | String | Concrete - Through Cracks | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `Concrete_MissingPieces` | String | Concrete - Missing Pieces | **Values:** `None` = None; `1` = 1 or More · len 50 |
| `Steel_SurfaceCorrosion` | String | Steel - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Steel_StructuralCorrosion` | String | Steel - Structural Corrosion | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `Steel_DamagedAnchors` | String | Steel - Damaged Anchors | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `AssetID` | String | Asset ID | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 7: Core Mechanical

- **Records:** 1,413

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Corrosion_Surface` | String | Corrosion - Surface Only | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Corrosion_Structural` | String | Corrosion - Structural (loss of metal) | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Leakage_Gaskets` | String | Lekeage - Gaskets/Connections | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `Leakage_Holes` | String | Leakage - Holes/Failures | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Vibration_VibrationApparent` | String | Vibration - Vibration Apparent with Noise | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Vibration_NonStructural` | String | Vibration - Non-Structural Damage | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Vibration_Structural` | String | Vibration - Structural Damage | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `Concrete_SurfaceCracking` | String | Concrete - Surface Cracking | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Concrete_ThroughCracks` | String | Concrete - Through Cracks | len 50 |
| `Concrete_MissingPieces` | String | Concrete - Missing Pieces | **Values:** `None` = None; `1` = 1 or More · len 50 |
| `Steel_SurfaceCorrosion` | String | Steel - Surface Corrosion | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Steel_StructuralCorrosion` | String | Steel - Structural Corrosion | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `Steel_DamagedAnchors` | String | Steel - Damaged Anchors | **Values:** `< 25` = < 25 %; `> 25` = >= 25 %; `None` = None · len 50 |
| `AssetID` | String | Asset ID | len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 8: Core Structural

- **Records:** 260

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Leakage_Surface` | String | Leakage - Surface | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Leakage_Cracks` | String | Leakage - Cracks | **Values:** `None` = None; `Historic` = Historic Only; `Drip` = Drip Only; `Stream1` = Stream 1 Location; `Stream2` = Stream > 1 Location · len 50 |
| `Leakage_Penetrations` | String | Leakage - Penetrations | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Concrete_Cracking` | String | Concrete - Cracking | **Values:** `None` = None; `<1` = < 1 mm; `1-2` = 1 - 2 mm; `>2` = > 2 mm; `NS` = Not Servicable · len 50 |
| `Concrete_ExposedReinforcement` | String | Concrete - Exposed Reinforcement | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Concrete_Damage` | String | Concrete - Damage | **Values:** `None` = None; `<10` = < 10 %; `10-30` = 10 - 30 %; `>30` = > 30 % · len 50 |
| `Joint_Deterioration` | String | Joint - Deterioration | **Values:** `< 10` = < 10 %; `10 - 50` = 10 - 50 %; `50 - 75` = 50 - 75 %; `> 75` = > 75 %; `None` = None · len 50 |
| `Settling_Magnitude` | String | Settling - Magnitude | **Values:** `None` = None; `Minor` = Minor; `Moderate` = Moderate; `Major` = Major; `Excessive` = Excessive · len 50 |
| `Steel_Fatigue` | String | Steel - Fatigue | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Steel_LossOfSection` | String | Steel - Loss Of Section | **Values:** `None` = None; `<10` = < 10 %; `10-30` = 10 - 30 %; `>30` = > 30 % · len 50 |
| `AssetID` | String | Asset ID | len 50 |
| `Steel_Cracking` | String |  | **Values:** `None` = None; `1` = 1 Location; `2` = > 1 Location · len 50 |
| `Steel_Deformation` | String |  | **Values:** `None` = None; `Minor` = Minor; `Moderate` = Moderate; `Major` = Major; `Excessive` = Excessive · len 50 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

## Layer 9: Attachments

- **Records:** 3,768

| Field | Type | Alias | Notes |
|---|---|---|---|
| `REL_OBJECTID` | Integer |  |  |
| `CONTENT_TYPE` | String |  | len 150 |
| `ATT_NAME` | String |  | len 250 |
| `DATA_SIZE` | Integer |  |  |
| `DATA` | Blob |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `GlobalID_1` | GlobalID |  |  |

</details>

