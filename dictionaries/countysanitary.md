# CountySanitary

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/CountySanitary/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=CountySanitary
- **Created:** None  ·  **Item modified:** None

## Layer 0: County Labels

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 1: County Sanitary Manhole Labels

- **Records:** 31,713
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `LOCATION` | String |  | len 255 |
| `LEGACYID` | String | Legacy ID | len 20 |
| `JURISDICTION` | String |  | len 90 |
| `SUBSYSTEM` | String |  | len 90 |
| `SUBDISTRICT` | String |  | **Values:** `BEAR` = Bear Creek; `BVCK` = Beaver Creek; `BLMT` = Belmont; `BACR` = Broad Acres; `BRUM` = Brumbaugh; `CARR` = Carrmonte; `CHAT` = Chatauqua; `CLCK` = Clear Creek; `CRAIN` = Crains Run; `DREX` = Drexel; `EMNT` = Eastmont; `FRVW` = Fairview; …(+21 more) · len 90 |
| `NOTES` | String |  | len 255 |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCATIONDESCRIPTION` | String | Location Description | len 255 |
| `SYMBOLROTATION` | Double | SymbolRotation |  |
| `SUBTYPECD` | Integer | Subtype |  |
| `GROUNDSURFACETYPE` | String | Ground Surface Type | **Values:** `CRK` = Creek; `DITCH` = Ditch; `DRV` = Driveway; `FLD` = Field; `GRAVEL` = Gravel; `HILL` = Hill Side; `INSTR` = Inside Structure; `LAWN` = Lawn; `OTH` = Other; `PKLOT` = Parking Lot; `SWALK` = Sidewalk; `STREET` = Street; …(+4 more) · len 8 |
| `ELEVATION` | Double |  |  |
| `RIMELEVATION` | Double | Rim Elevation |  |
| `GROUNDELEVATION` | Double |  |  |
| `MANHOLEDEPTH` | Double | Manhole Depth |  |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 2: County Sanitary Force Main Labels

- **Records:** 151
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `LOCATION` | String |  | len 255 |
| `WARRANTYDATE` | Date | Warranty Date |  |
| `LEGACYID` | String | Legacy ID | len 20 |
| `CONDITION` | String |  | len 20 |
| `CONDITIONDATE` | Date | Condition Date |  |
| `SOURCE` | String | Source | **Values:** `ASB` = As Built; `CNSTPLN` = Construction Plan; `FLD` = Field Data; `GCERT` = Grade Certification; `INSP` = Inspector Notes; `CONV` = Conversion; `UNK` = Unknown; `DAY` = Dayton; `OTH` = Other · len 20 |
| `PLACEMENTMETHOD` | String | PlacementMethod | **Values:** `DIG` = Digitize CAD; `DCD` = Digitize Construction Drawing; `DAS` = Digitize As Built; `DLS` = Digitize Laying Schedule; `DIM` = Dimensional Construction; `GPSD` = GPS - Differential; `GPSK` = GPS - Kinematic; `COGO` = COGO/Total Station; `SPOT` = Spot Alignment; `FLD` = Field Observation; `OTH` = Other; `UNK` = Unknown · len 20 |
| `MAPSHEETID` | String |  | len 90 |
| `ASSETMAINTAINER` | String | AssetMaintainer | **Values:** `BRK` = Brookville; `DAY` = Dayton; `CLA` = Clayton; `ENG` = Englewood; `GRE` = Greene County; `HH` = Huber Heights; `MCSED` = MCSED; `MSBG` = Miamisburg; `OAK` = Oakwood; `TROT` = Trotwood; `VAN` = Vandalia; `WC` = West Carrollton; …(+4 more) · len 90 |
| `JURISDICTION` | String |  | len 90 |
| `SUBSYSTEM` | String |  | len 90 |
| `SUBDISTRICT` | String |  | **Values:** `BEAR` = Bear Creek; `BVCK` = Beaver Creek; `BLMT` = Belmont; `BACR` = Broad Acres; `BRUM` = Brumbaugh; `CARR` = Carrmonte; `CHAT` = Chatauqua; `CLCK` = Clear Creek; `CRAIN` = Crains Run; `DREX` = Drexel; `EMNT` = Eastmont; `FRVW` = Fairview; …(+21 more) · len 90 |
| `NOTES` | String |  | len 255 |
| `SUBTYPECD` | Integer | Subtype |  |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String |  | **Values:** `HDPE` = HDPE; `PLA` = Plastic; `DCI` = Ductile Cast Iron; `CI` = Cast Iron/Black Pipe; `UNK` = Unknown; `PCP` = Prestressed Concrete; `PVC` = PVC · len 5 |
| `WORKORDERID` | String | Work Order ID | len 20 |
| `MEASUREDLENGTH` | Double | MeasuredLength |  |
| `LENGTHSOURCE` | String | Length Source | **Values:** `FM` = Field Measurement; `MS` = Mapping System · len 5 |
| `WASTEWATERTRACEWEIGHT` | Integer | Wastewater Trace Weight |  |
| `LININGTYPE` | String | Lining Type | len 20 |
| `PIPECLASS` | String | Pipe Class | **Values:** `AIRREL` = Air Release; `AIRVAC` = Air/Vaccum Release; `BLOFF` = Blow Off; `SURREL` = Surge Relief; `UNK` = Unknown · len 20 |
| `ROUGHNESS` | Double |  |  |
| `CONSTRUCTIONMETHOD` | String | ConstructionMethod | **Values:** `BORE` = Bore; `OPENENC` = Encased/Open Cut; `OPEN` = Not Encased/Open Cut; `SUSP` = Suspended; `TUNN` = Tunnel; `UNK` = Unknown · len 255 |
| `INEASEMENTINDICATOR` | String |  | **Values:** `YES` = Yes; `NO` = No; `UNK` = Unknown · len 20 |
| `DEPTH` | Double |  |  |
| `GROUNDSURFACETYPE` | String | Ground Surface Type | **Values:** `CRK` = Creek Bed; `DITCH` = Ditch; `DRV` = Driveway; `FLD` = Field; `GRAVEL` = Gravel; `HILL` = Hill Side; `INSTR` = Inside Structure; `LAWN` = Lawn; `OTH` = Other; `PKLOT` = Parking Lot; `SWALK` = Sidewalk; `STREET` = Street; …(+4 more) · len 10 |
| `UPSTREAMINVERT` | Double |  |  |
| `DOWNSTREAMINVERT` | Double |  |  |
| `DIAMETER` | Double |  | **Values:** `-2` = Other; `-1` = Unknown; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; `16` = 16"; `18` = 18"; `36` = 36"; `54` = 54"; `30` = 30" |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |

</details>

## Layer 3: County Sanitary Gravity Main Labels

- **Records:** 32,399
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `LOCATION` | String |  | len 255 |
| `LEGACYID` | String | Legacy ID | len 20 |
| `JURISDICTION` | String |  | len 90 |
| `SUBSYSTEM` | String |  | len 90 |
| `SUBDISTRICT` | String |  | **Values:** `BEAR` = Bear Creek; `BVCK` = Beaver Creek; `BLMT` = Belmont; `BACR` = Broad Acres; `BRUM` = Brumbaugh; `CARR` = Carrmonte; `CHAT` = Chatauqua; `CLCK` = Clear Creek; `CRAIN` = Crains Run; `DREX` = Drexel; `EMNT` = Eastmont; `FRVW` = Fairview; …(+21 more) · len 90 |
| `NOTES` | String |  | len 255 |
| `SUBTYPECD` | Integer | Subtype |  |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String |  | **Values:** `ABS` = ABS; `CI` = Cast Iron; `CONC` = Concrete; `DCI` = Ductile Iron; `HDPE` = HDPE; `MIX` = Mix; `PLA` = Other Plastic; `PCP` = Prestressed Concrete; `PVC` = PVC; `PVCCP` = PVC - Closed profile; `VYLON` = PVC - Open Profile; `ASB` = Transite Asbestos; …(+3 more) · len 5 |
| `MEASUREDLENGTH` | Double | MeasuredLength |  |
| `LENGTHSOURCE` | String | Length Source | **Values:** `FM` = Field Measurement; `MS` = Mapping System · len 5 |
| `LININGTYPE` | String | Lining Type | len 20 |
| `PIPECLASS` | String | Pipe Class | len 20 |
| `ROUGHNESS` | Double |  |  |
| `CONSTRUCTIONMETHOD` | String | ConstructionMethod | **Values:** `BORE` = Bore; `OPENENC` = Encased/Open Cut; `OPEN` = Not Encased/Open Cut; `SUSP` = Suspended; `TUNN` = Tunnel; `UNK` = Unknown · len 255 |
| `UPSTREAMINVERT` | Double | Upstream Invert |  |
| `DOWNSTREAMINVERT` | Double | Downstream Invert |  |
| `PERCENTSLOPE` | Double | Percent Slope |  |
| `DIAMETER` | Double | Diameter | **Values:** `-1` = Unknown; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; `14` = 14"; `15` = 15"; `16` = 16"; `18` = 18"; `20` = 20"; `21` = 21"; …(+12 more) |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |
| `UPSTREAMFACILITYID` | String | Upstream FacilityID | len 20 |
| `DOWNSTREAMFACILITYID` | String | Downstream FacilityID | len 20 |
| `TAPERRORS` | Integer |  |  |
| `UPSTREAMMH` | String | Upstream Manhole Name | len 20 |
| `DOWNSTREAMMH` | String | Downstream Manhole Name | len 20 |
| `REL_LS` | String | Related Lift Station | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |

</details>

## Layer 4: County Water

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 5: County Water Hydrant

- **Records:** 12,440
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `FACILITYID` | String | Facility ID | len 20 |
| `LOCATION` | String |  | len 255 |
| `LEGACYID` | String | Legacy ID | len 20 |
| `JURISDICTION` | String |  | len 90 |
| `NOTES` | String |  | len 255 |
| `INSTALLDATE` | Date | Install Date |  |
| `SYMBOLROTATION` | Double | SymbolRotation |  |
| `SUBTYPECD` | Integer | Subtype |  |
| `MANUFACTURER` | String | Manufacturer | **Values:** `CLOWST` = CLOW Eddy Standard; `CLOWSW` = CLOW Eddy Swivel Head; `PACR` = Pacer; `MUEL` = Mueller; `OTH` = Other; `UNK` = Unknown · len 20 |
| `STANDARDPRESSUREPSI` | Integer |  | **Range:** [50, 250] |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 6: County Water Network Structure

- **Records:** 76
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ANCILLARYROLE` | SmallInteger |  |  |
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `FACILITYID` | String | Facility ID | len 20 |
| `LOCATION` | String |  | len 255 |
| `WARRANTYDATE` | Date | Warranty Date |  |
| `LEGACYID` | String | Legacy ID | len 20 |
| `CONDITION` | String |  | len 20 |
| `CONDITIONDATE` | Date | Condition Date |  |
| `SOURCE` | String | Source | **Values:** `ASB` = As Built; `CNSTPLN` = Construction Plan; `FLD` = Field Data; `GCERT` = Grade Certification; `INSP` = Inspector Notes; `CONV` = Conversion; `UNK` = Unknown; `DAY` = Dayton; `OTH` = Other · len 20 |
| `PLACEMENTMETHOD` | String | PlacementMethod | **Values:** `DIG` = Digitize CAD; `DCD` = Digitize Construction Drawing; `DAS` = Digitize As Built; `DLS` = Digitize Laying Schedule; `DIM` = Dimensional Construction; `GPSD` = GPS - Differential; `GPSK` = GPS - Kinematic; `COGO` = COGO/Total Station; `SPOT` = Spot Alignment; `FLD` = Field Observation; `OTH` = Other; `UNK` = Unknown · len 20 |
| `MAPSHEETID` | String |  | len 90 |
| `ASSETMAINTAINER` | String | AssetMaintainer | **Values:** `BRK` = Brookville; `DAY` = Dayton; `CLA` = Clayton; `ENG` = Englewood; `GRE` = Greene County; `HH` = Huber Heights; `MCSED` = MCSED; `MSBG` = Miamisburg; `OAK` = Oakwood; `TROT` = Trotwood; `VAN` = Vandalia; `WC` = West Carrollton; …(+4 more) · len 90 |
| `JURISDICTION` | String |  | len 90 |
| `NOTES` | String |  | len 255 |
| `INSTALLDATE` | Date | Install Date |  |
| `WORKORDERID` | String | Work Order ID | len 20 |
| `ELEVATION` | Double |  |  |
| `WATERTYPE` | String | Water Type | **Values:** `POT` = Potable; `NOP` = Non-Potable · len 5 |
| `SYMBOLROTATION` | Double | SymbolRotation |  |
| `WATERTRACEWEIGHT` | Integer | Water Trace Weight |  |
| `SUBTYPECD` | Integer | Subtype |  |
| `NAME` | String |  | len 20 |
| `OPERATIONALDATE` | Date | Operational Date |  |
| `NETWORKUSAGE` | String | Network Usage | **Values:** `POT` = Potable; `NOP` = Non-Potable · len 5 |
| `CAPACITY` | Integer |  |  |
| `SOPIN` | Integer | Inlet Pressure |  |
| `SOPOUT` | Integer | Outlet Pressure |  |
| `EMERISOLATIONSYSSTATUS` | String | Emergency Isolation System Status | len 20 |
| `WATERPRESSURESYSTEMSTATUS` | Integer | Water Pressure System Status | **Values:** `0` = Not Barrier; `1` = Barrier |
| `WATERSYSTEMSTATUS` | String | Water System Status | len 20 |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |
| `OVERFLOWELEVATION` | Double | OVERFLOW ELEVATION |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 7: County Water System Valve

- **Records:** 30,549
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `FACILITYID` | String | Facility ID | len 20 |
| `LOCATION` | String |  | len 255 |
| `LEGACYID` | String | Legacy ID | len 20 |
| `JURISDICTION` | String |  | len 90 |
| `NOTES` | String |  | len 255 |
| `INSTALLDATE` | Date | Install Date |  |
| `SYMBOLROTATION` | Double | SymbolRotation |  |
| `SUBTYPECD` | Integer | Subtype |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 0.75"; `1` = 1"; `1.5` = 1.5"; `2` = 2"; `2.5` = 2.5"; `3` = 3"; `4` = 4"; `5` = 5"; `5.25` = 5.25"; `6` = 6"; `8` = 8"; `10` = 10"; …(+8 more) |
| `MATERIAL` | String |  | **Values:** `CI` = Cast Iron; `DCI` = Ductile Cast Iron; `PCP` = Prestressed Concrete; `HDPE` = HDPE; `C900` = C-900; `SAND` = Sand Cast; `PLA` = Plastic; `OTH` = Other; `UNK` = Unknown · len 5 |
| `NORMALPOSITION` | Integer | Normal Position | **Values:** `0` = Closed; `1` = Open |
| `OPERATINGSTATUS` | String | OperatingStatus | **Values:** `OPER` = Operable; `BROKE` = Inoperable - broken; `BURIED` = Inoperable - buried; `UNK` = Unknown · len 8 |
| `ACCESSTYPE` | String | AccessType | **Values:** `VBOX` = Box; `VMH` = Manhole; `VAUL` = Vault; `NONE` = None; `UNK` = Unknown · len 8 |
| `BYPASSINDICATOR` | Integer | ByPassIndicator | **Values:** `0` = No; `1` = Yes |
| `MANUFACTURER` | String |  | len 25 |
| `VALVETYPE` | String |  | **Values:** `GATE` = Gate; `BFLY` = Butterfly; `TSV` = Tapping; `HORO` = Horizontal Sliding; `INST` = Insert-A-Valve; `HYDR` = Hydro Stop; `UNK` = Unknown; `OTH` = Other · len 8 |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 8: County Water Control Valve

- **Records:** 112
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ANCILLARYROLE` | SmallInteger |  |  |
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `FACILITYID` | String | Facility ID | len 20 |
| `LOCATION` | String |  | len 255 |
| `WARRANTYDATE` | Date | Warranty Date |  |
| `LEGACYID` | String | Legacy ID | len 20 |
| `CONDITION` | String |  | len 20 |
| `CONDITIONDATE` | Date | Condition Date |  |
| `SOURCE` | String | Source | **Values:** `ASB` = As Built; `CNSTPLN` = Construction Plan; `FLD` = Field Data; `GCERT` = Grade Certification; `INSP` = Inspector Notes; `CONV` = Conversion; `UNK` = Unknown; `DAY` = Dayton; `OTH` = Other · len 20 |
| `PLACEMENTMETHOD` | String | PlacementMethod | **Values:** `DIG` = Digitize CAD; `DCD` = Digitize Construction Drawing; `DAS` = Digitize As Built; `DLS` = Digitize Laying Schedule; `DIM` = Dimensional Construction; `GPSD` = GPS - Differential; `GPSK` = GPS - Kinematic; `COGO` = COGO/Total Station; `SPOT` = Spot Alignment; `FLD` = Field Observation; `OTH` = Other; `UNK` = Unknown · len 20 |
| `MAPSHEETID` | String |  | len 90 |
| `ASSETMAINTAINER` | String | AssetMaintainer | **Values:** `BRK` = Brookville; `DAY` = Dayton; `CLA` = Clayton; `ENG` = Englewood; `GRE` = Greene County; `HH` = Huber Heights; `MCSED` = MCSED; `MSBG` = Miamisburg; `OAK` = Oakwood; `TROT` = Trotwood; `VAN` = Vandalia; `WC` = West Carrollton; …(+4 more) · len 90 |
| `JURISDICTION` | String |  | len 90 |
| `NOTES` | String |  | len 255 |
| `INSTALLDATE` | Date | Install Date |  |
| `WORKORDERID` | String | Work Order ID | len 20 |
| `ELEVATION` | Double |  |  |
| `WATERTYPE` | String | Water Type | **Values:** `POT` = Potable; `NOP` = Non-Potable · len 5 |
| `SYMBOLROTATION` | Double | SymbolRotation |  |
| `WATERTRACEWEIGHT` | Integer | Water Trace Weight |  |
| `SUBTYPECD` | Integer | Subtype |  |
| `DIAMETER` | Double | Diameter | **Values:** `-8` = Other; `-9` = Unknown; `1.5` = 1.5"; `2` = 2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; `16` = 16"; `18` = 18"; …(+8 more) |
| `BONDEDINDICATOR` | String | Bonded Indicator | **Values:** `NO` = No; `YES` = Yes · len 5 |
| `MATERIAL` | String |  | **Values:** `DI` = Ductile Iron; `CI` = Cast Iron; `PVC` = PVC; `AC` = Asbestos Concrete; `ST` = Steel; `WOOD` = Wood; `UNK` = Unknown; `OTH` = Other; `GS` = Galvanized Steel · len 5 |
| `NORMALPOSITION` | Integer | Normal Position | **Values:** `0` = Closed; `1` = Open |
| `OPERATINGSTATUS` | String | OperatingStatus | **Values:** `OPER` = Operable; `BROKE` = Inoperable - broken; `BURIED` = Inoperable - buried; `UNK` = Unknown · len 8 |
| `OPERATINGCLASSIFICATION` | String | Operating Classification | **Values:** `CIR` = Critical/Inspection Required; `CINR` = Critical/Inspection Not Required; `NC` = Non-Critical · len 5 |
| `CPSYSTEMSTATUS` | Integer | CP System Status | **Values:** `0` = Closed; `1` = Open |
| `EMERISOLATIONSYSSTATUS` | String | Emergency Isolation System Status | len 20 |
| `WATERPRESSURESYSTEMSTATUS` | Integer | Water Pressure System Status | **Values:** `0` = Not Barrier; `1` = Barrier |
| `WATERSYSTEMSTATUS` | String | Water System Status | len 20 |
| `ACCESSTYPE` | String | AccessType | **Values:** `VBOX` = Box; `VMH` = Manhole; `VAUL` = Vault; `NONE` = None; `UNK` = Unknown · len 8 |
| `CONTROLVALVETYPE` | String | Control Valve Type | **Values:** `AIR` = Air Release; `ALT` = Altitude; `BYP` = Bypass; `CHK` = Check; `GLB` = Globe; `PRV` = Pressure Reduction; `SWNG` = Swing; `OTH` = Other; `UNK` = Unknown · len 5 |
| `MANUFACTURER` | String |  | len 25 |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 9: County Water Main

- **Records:** 37,976
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `FACILITYID` | String | Facility ID | len 20 |
| `LOCATION` | String |  | len 255 |
| `LEGACYID` | String | Legacy ID | len 20 |
| `JURISDICTION` | String |  | len 90 |
| `NOTES` | String |  | len 255 |
| `SUBTYPECD` | Integer | Subtype |  |
| `MATERIAL` | String | Material | **Values:** `CI` = Cast Iron; `DCI` = Ductile Cast Iron; `PCP` = Prestressed Concrete; `HDPE` = HDPE; `C900` = C-900; `SAND` = Sand Cast; `PLA` = Plastic; `OTH` = Other; `UNK` = Unknown · len 5 |
| `OPERATINGPRESSURE` | Double |  |  |
| `PRESSUREZONE` | String |  | len 255 |
| `INSTALLDATE` | Date | Install Date |  |
| `MEASUREDLENGTH` | Double | Measured Length | **Range:** [1, 1000000000] |
| `DIAMETER` | Double | Diameter | **Values:** `-8` = Other; `-9` = Unknown; `1.5` = 1.5"; `2` = 2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; `16` = 16"; `18` = 18"; …(+8 more) |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |
| `CRITICAL_INDICATOR` | String |  | **Values:** `N` = No; `Y` = Yes · len 1 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |

</details>

## Layer 10: County Sanitary

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 11: County Sanitary Manhole

- **Records:** 31,713
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CREATIONUSER` | String |  | len 20 |
| `DATECREATED` | Date |  |  |
| `DATEMODIFIED` | Date |  |  |
| `LASTUSER` | String | LastUser | len 20 |
| `LOCATION` | String |  | len 255 |
| `LEGACYID` | String | LegacyID | len 20 |
| `JURISDICTION` | String |  | len 90 |
| `SUBSYSTEM` | String |  | len 90 |
| `SUBDISTRICT` | String |  | **Values:** `BEAR` = Bear Creek; `BVCK` = Beaver Creek; `BLMT` = Belmont; `BACR` = Broad Acres; `BRUM` = Brumbaugh; `CARR` = Carrmonte; `CHAT` = Chatauqua; `CLCK` = Clear Creek; `CRAIN` = Crains Run; `DREX` = Drexel; `EMNT` = Eastmont; `FRVW` = Fairview; …(+21 more) · len 90 |
| `NOTES` | String |  | len 255 |
| `FACILITYID` | String | FacilityID | len 20 |
| `INSTALLDATE` | Date | InstallDate |  |
| `LOCATIONDESCRIPTION` | String | LocationDescription | len 255 |
| `SYMBOLROTATION` | Double | SymbolRotation |  |
| `SUBTYPECD` | Integer | Subtypecd |  |
| `GROUNDSURFACETYPE` | String | GroundSurfaceType | **Values:** `CRK` = Creek; `DITCH` = Ditch; `DRV` = Driveway; `FLD` = Field; `GRAVEL` = Gravel; `HILL` = Hill Side; `INSTR` = Inside Structure; `LAWN` = Lawn; `OTH` = Other; `PKLOT` = Parking Lot; `SWALK` = Sidewalk; `STREET` = Street; …(+4 more) · len 8 |
| `ELEVATION` | Double |  |  |
| `RIMELEVATION` | Double | RimElevation |  |
| `GROUNDELEVATION` | Double |  |  |
| `MANHOLEDEPTH` | Double | ManholeDepth |  |
| `LIFECYCLESTATUS` | String | LifecycleStatus | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

## Layer 12: County Sanitary Force Main

- **Records:** 151
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ENABLED` | SmallInteger |  | **Values:** `0` = False; `1` = True |
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `LOCATION` | String |  | len 255 |
| `WARRANTYDATE` | Date | Warranty Date |  |
| `LEGACYID` | String | Legacy ID | len 20 |
| `CONDITION` | String |  | len 20 |
| `CONDITIONDATE` | Date | Condition Date |  |
| `SOURCE` | String | Source | **Values:** `ASB` = As Built; `CNSTPLN` = Construction Plan; `FLD` = Field Data; `GCERT` = Grade Certification; `INSP` = Inspector Notes; `CONV` = Conversion; `UNK` = Unknown; `DAY` = Dayton; `OTH` = Other · len 20 |
| `PLACEMENTMETHOD` | String | PlacementMethod | **Values:** `DIG` = Digitize CAD; `DCD` = Digitize Construction Drawing; `DAS` = Digitize As Built; `DLS` = Digitize Laying Schedule; `DIM` = Dimensional Construction; `GPSD` = GPS - Differential; `GPSK` = GPS - Kinematic; `COGO` = COGO/Total Station; `SPOT` = Spot Alignment; `FLD` = Field Observation; `OTH` = Other; `UNK` = Unknown · len 20 |
| `MAPSHEETID` | String |  | len 90 |
| `ASSETMAINTAINER` | String | AssetMaintainer | **Values:** `BRK` = Brookville; `DAY` = Dayton; `CLA` = Clayton; `ENG` = Englewood; `GRE` = Greene County; `HH` = Huber Heights; `MCSED` = MCSED; `MSBG` = Miamisburg; `OAK` = Oakwood; `TROT` = Trotwood; `VAN` = Vandalia; `WC` = West Carrollton; …(+4 more) · len 90 |
| `JURISDICTION` | String |  | len 90 |
| `SUBSYSTEM` | String |  | len 90 |
| `SUBDISTRICT` | String |  | **Values:** `BEAR` = Bear Creek; `BVCK` = Beaver Creek; `BLMT` = Belmont; `BACR` = Broad Acres; `BRUM` = Brumbaugh; `CARR` = Carrmonte; `CHAT` = Chatauqua; `CLCK` = Clear Creek; `CRAIN` = Crains Run; `DREX` = Drexel; `EMNT` = Eastmont; `FRVW` = Fairview; …(+21 more) · len 90 |
| `NOTES` | String |  | len 255 |
| `SUBTYPECD` | Integer | Subtype |  |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String |  | **Values:** `HDPE` = HDPE; `PLA` = Plastic; `DCI` = Ductile Cast Iron; `CI` = Cast Iron/Black Pipe; `UNK` = Unknown; `PCP` = Prestressed Concrete; `PVC` = PVC · len 5 |
| `WORKORDERID` | String | Work Order ID | len 20 |
| `MEASUREDLENGTH` | Double | MeasuredLength |  |
| `LENGTHSOURCE` | String | Length Source | **Values:** `FM` = Field Measurement; `MS` = Mapping System · len 5 |
| `WASTEWATERTRACEWEIGHT` | Integer | Wastewater Trace Weight |  |
| `LININGTYPE` | String | Lining Type | len 20 |
| `PIPECLASS` | String | Pipe Class | **Values:** `AIRREL` = Air Release; `AIRVAC` = Air/Vaccum Release; `BLOFF` = Blow Off; `SURREL` = Surge Relief; `UNK` = Unknown · len 20 |
| `ROUGHNESS` | Double |  |  |
| `CONSTRUCTIONMETHOD` | String | ConstructionMethod | **Values:** `BORE` = Bore; `OPENENC` = Encased/Open Cut; `OPEN` = Not Encased/Open Cut; `SUSP` = Suspended; `TUNN` = Tunnel; `UNK` = Unknown · len 255 |
| `INEASEMENTINDICATOR` | String |  | **Values:** `YES` = Yes; `NO` = No; `UNK` = Unknown · len 20 |
| `DEPTH` | Double |  |  |
| `GROUNDSURFACETYPE` | String | Ground Surface Type | **Values:** `CRK` = Creek Bed; `DITCH` = Ditch; `DRV` = Driveway; `FLD` = Field; `GRAVEL` = Gravel; `HILL` = Hill Side; `INSTR` = Inside Structure; `LAWN` = Lawn; `OTH` = Other; `PKLOT` = Parking Lot; `SWALK` = Sidewalk; `STREET` = Street; …(+4 more) · len 10 |
| `UPSTREAMINVERT` | Double |  |  |
| `DOWNSTREAMINVERT` | Double |  |  |
| `DIAMETER` | Double |  | **Values:** `-2` = Other; `-1` = Unknown; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; `16` = 16"; `18` = 18"; `36` = 36"; `54` = 54"; `30` = 30" |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |

</details>

## Layer 13: County Sanitary Gravity Main

- **Records:** 32,399
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `CREATIONUSER` | String | Creation User | len 20 |
| `DATECREATED` | Date | Date Created |  |
| `DATEMODIFIED` | Date | Date Modified |  |
| `LASTUSER` | String | Last User | len 20 |
| `LOCATION` | String |  | len 255 |
| `LEGACYID` | String | Legacy ID | len 20 |
| `JURISDICTION` | String |  | len 90 |
| `SUBSYSTEM` | String |  | len 90 |
| `SUBDISTRICT` | String |  | **Values:** `BEAR` = Bear Creek; `BVCK` = Beaver Creek; `BLMT` = Belmont; `BACR` = Broad Acres; `BRUM` = Brumbaugh; `CARR` = Carrmonte; `CHAT` = Chatauqua; `CLCK` = Clear Creek; `CRAIN` = Crains Run; `DREX` = Drexel; `EMNT` = Eastmont; `FRVW` = Fairview; …(+21 more) · len 90 |
| `NOTES` | String |  | len 255 |
| `SUBTYPECD` | Integer | Subtype |  |
| `FACILITYID` | String | Facility ID | len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MATERIAL` | String |  | **Values:** `ABS` = ABS; `CI` = Cast Iron; `CONC` = Concrete; `DCI` = Ductile Iron; `HDPE` = HDPE; `MIX` = Mix; `PLA` = Other Plastic; `PCP` = Prestressed Concrete; `PVC` = PVC; `PVCCP` = PVC - Closed profile; `VYLON` = PVC - Open Profile; `ASB` = Transite Asbestos; …(+3 more) · len 5 |
| `MEASUREDLENGTH` | Double | MeasuredLength |  |
| `LENGTHSOURCE` | String | Length Source | **Values:** `FM` = Field Measurement; `MS` = Mapping System · len 5 |
| `LININGTYPE` | String | Lining Type | len 20 |
| `PIPECLASS` | String | Pipe Class | len 20 |
| `ROUGHNESS` | Double |  |  |
| `CONSTRUCTIONMETHOD` | String | ConstructionMethod | **Values:** `BORE` = Bore; `OPENENC` = Encased/Open Cut; `OPEN` = Not Encased/Open Cut; `SUSP` = Suspended; `TUNN` = Tunnel; `UNK` = Unknown · len 255 |
| `UPSTREAMINVERT` | Double | Upstream Invert |  |
| `DOWNSTREAMINVERT` | Double | Downstream Invert |  |
| `PERCENTSLOPE` | Double | Percent Slope |  |
| `DIAMETER` | Double | Diameter | **Values:** `-1` = Unknown; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; `14` = 14"; `15` = 15"; `16` = 16"; `18` = 18"; `20` = 20"; `21` = 21"; …(+12 more) |
| `LIFECYCLESTATUS` | String | Lifecycle Status | **Values:** `OUTSERV` = Standby/Out of Service; `PROP` = Proposed; `UNK` = Unknown; `ACT` = In-Service/Active · len 8 |
| `UPSTREAMFACILITYID` | String | Upstream FacilityID | len 20 |
| `DOWNSTREAMFACILITYID` | String | Downstream FacilityID | len 20 |
| `TAPERRORS` | Integer |  |  |
| `UPSTREAMMH` | String | Upstream Manhole Name | len 20 |
| `DOWNSTREAMMH` | String | Downstream Manhole Name | len 20 |
| `REL_LS` | String | Related Lift Station | len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |
| `Shape_Length` | Double |  |  |

</details>

