# AsBuiltProcessManagement/AsBuilt_Process_Management_ReferenceLayers

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/AsBuiltProcessManagement/AsBuilt_Process_Management_ReferenceLayers/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=AsBuiltProcessManagement_AsBuilt_Process_Management_ReferenceLayers
- **Created:** None  ·  **Item modified:** None
- **Tags:** AsBuiltProcessManagement

## Layer 10: Water Utilities

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 11: Water System Valve

- **Records:** 23,223
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `Air` = Air Release Valve; `Ball` = Ball; `Bloff` = Blow Off Valve; `Butterfly` = Butterfly; `Bypass` = Bypass Valve; `Check` = Check Valve; `Cone` = Cone; `Curb` = Curb Stop; `Ford` = Ford Valve; `Gate` = Gate; `GATE` = Gate; `Hyd` = Hydrant Valve; …(+12 more) · len 30 |
| `INSTALLDATE` | Date | Install Date |  |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `ASBLT` | String | AsBuilt # | len 10 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 12: Water Curb Stop Valve

- **Records:** 5,026
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `INSTALLDATE` | Date | Install Date |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DIR` | String | Direction To Open | len 1 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 13: Water Control Valve

- **Records:** 203
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `ROTATION` | Double | Rotation |  |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DIR` | String | Direction To Open | len 1 |
| `NOTURNS` | String | Number of Turns | len 6 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `UNITTYPE` | String |  | len 6 |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `COMMENTS` | String | Comments | len 255 |
| `CloseDir` | String |  | **Values:** `L` = L; `R` = R · len 2 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 14: Water Hydrant

- **Records:** 6,163
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Hydrant ID | len 16 |
| `INSTALLDATE` | Date | Install Date |  |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `MANUFACTURER` | String | Manufacturer | **Values:** `American Darling` = American Darling; `Clow Corporation` = Clow Corporation; `Corey` = Corey; `Dresser` = Dresser; `Kennedy Valve` = Kennedy Valve; `M&H Valve` = M&H Valve; `M&H Valve / Dresser` = M&H Valve / Dresser; `Mueller Company` = Mueller Company; `US Pipe` = US Pipe; `Wood-Matthews` = Wood-Matthews; `Other` = Other; `Unknown` = Unknown; …(+7 more) · len 30 |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `LASTSERVICE` | Date | Last Service Date |  |
| `FLOW` | Double | Flow Rate (GPM) |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `AUXVALVE` | String | Aux Valve | len 1 |
| `BARRELSIZE` | Double | Barrel Size |  |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `FEEDERDIAM` | Double | Feeder Diameter |  |
| `FEEDERLEN` | Double | Feeder Length |  |
| `FEEDERTYPE` | String | Feeder Type | **Values:** `0` = No Code · len 6 |
| `HT` | Double | Height |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `OUTLSZ1` | Double | Size of Outlet1 |  |
| `OUTLSZ2` | Double | Size of Outlet2 |  |
| `OUTLSZ3` | Double | Size of Outlet3 |  |
| `OUTLSZ4` | Double | Size of Outlet4 |  |
| `PACKING` | String | Packing | **Values:** `0` = No Code · len 4 |
| `PAINTTYPE` | String | Paint Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 8 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `SERNO` | String | Serial # | len 20 |
| `COLOR` | String | Paint Color | **Values:** `BLUE` = BLUE - LOW; `GREEN` = GREEN - HIGH; `ORANGE` = ORANGE - MEDIUM · len 8 |
| `INSPECTIONGROUP` | String |  | len 50 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |
| `ADDRESS` | String |  | len 254 |
| `FlowTest` | String | Flow Test | **Values:** `Static` = Static; `Not Completed` = Not Completed; `Completed` = Completed · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 15: Water Fitting

- **Records:** 40,067
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Node ID | len 16 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `FITTINGTYPE` | String | Fitting Type | **Values:** `ANGLE` = < 45 DEGREE BEND; `ENDPT` = END POINT/PLUG; `JNT-T` = T-JOINT; `JNT-X` = CROSS JOINT; `VLV` = VALVE; `RED` = REDUCER; `45` = 45 DEGREE BEND; `90` = 90 DEGREE BEND; `SRV` = LARGE SERVICE LINE NODE; `JUNC` = JUNCTION CHAMBER; `PLUG` = MAIN LINE PLUG; `COUPLING` = COUPLING; …(+25 more) · len 50 |
| `LOCDESC` | String | Location Description | len 200 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 16: Water Sampling Station

- **Records:** 93
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `STATIONID` | String | Station ID | len 20 |
| `NAME` | String | Name | len 50 |
| `UNITID` | String |  | len 16 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `ADDRESS` | String | Address | len 255 |
| `DISINFRULE` | String | Disinfection Rule | len 3 |
| `Comments` | String |  | len 255 |
| `Indoor_Outdoor` | String | Indoor/Outdoor | **Values:** `I` = Inside; `O` = Outside · len 50 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 17: Water Pump

- **Records:** 211
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Pump ID | len 20 |
| `NAME` | String | Name | len 50 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `PUMPTYPE` | String | Pump Type | **Values:** `Axial Flow` = Axial Flow; `Centrifugal` = Centrifugal; `Jet` = Jet; `Reciprocating` = Reciprocating; `Rotary` = Rotary; `Turbine` = Turbine; `Other` = Other; `Unknown` = Unknown; `UNK` = Unknown; `CENT01` = Centrifugal; `Line Shaft Turbine Pump` = Turbine; `LST` = Submersible; …(+2 more) · len 50 |
| `LOCDESC` | String | Location Description | len 200 |
| `INLETDIAM` | Double | Inlet Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `DISCHDIAM` | Double | Discharge Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `RATEDFLOW` | String | Rated Flow | len 20 |
| `RATEDPRESS` | String | Rated Pressure | len 20 |
| `DYNHEAD` | String | Total Dynamic Head | len 20 |
| `SHUTHEAD` | Double | Shutoff Head |  |
| `DESHEAD` | Double | Design Head |  |
| `MAXOPHEAD` | Double | Max Operating Head |  |
| `DESIGNGPM` | Double | Design GPM |  |
| `MAXOPDISC` | Double | Max Operating Discharge |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `AVGMONUSG` | Double | Average Monthly Usage |  |
| `FLOW` | Double | Flow |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `MODELNO` | String | Model # | len 20 |
| `MOSERNO` | String | Motor Serial # | len 20 |
| `PMRPM` | String | RPM's | len 7 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `PUMPTRIM` | String | Trim | len 6 |
| `SERNO` | String | Serial # | len 20 |
| `SITEKEY` | Integer | Site |  |
| `USGDATE` | Date |  |  |
| `USGTOT` | Double | Usage Total |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 18: Water Network Structure

- **Records:** 988
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NAME` | String | Name | len 20 |
| `UNITID` | String | Well ID | len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Enclosed Storage Facility` = Enclosed Storage Facility; `Production Well` = Production Well; `Pump Station` = Pump Station; `Storage Basin` = Storage Basin; `Treatment Plant` = Treatment Plant; `Meter Station` = Meter Station; `Other` = Other; `Investigation` = Investigation Well; `Monitoring` = Monitoring Well; `Recharge` = Recharge Pond; `RechargeValve` = Recharge Pond Valve; `Water Manhole` = Water Manhole; …(+7 more) · len 30 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `OPDATE` | Date | Operational Date |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `AIRLINE` | Integer | Air Line |  |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CASINGDIAM` | Double | Casing Diameter |  |
| `CASINGDPTH` | Double | Casing Depth |  |
| `CASINGTYPE` | String | Casing Type | **Values:** `BRASS` = BRASS CASING; `CICASE` = CAST IRON CASING; `COND` = CONDUCTOR CASING; `DUCT` = DUCTILE IRON CASING; `ENL` = ENAMEL CASING; `WELDED` = WELDED STEEL CASING; `RIVET` = RIVETED STEEL CASING; `GLVTHR` = THREADED GALVANIZED PIPE · len 6 |
| `DRAWDOWN` | Double | Drawdown |  |
| `FLOW` | Double | Flow |  |
| `MFGKEY` | Integer | Manufacturer |  |
| `PUMPTIME` | Double | Pumping Time |  |
| `SCRNTO` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `UNITTYPE` | String | Well Type | **Values:** `GRAVPK` = GRAVEL PACK; `TUBULA` = TUBULAR 17.5 INCH; `GRAVEL PACK` = GRAVEL PACK; `PIEDO` = Pit; `PIT` = Pit; `STAND` = Standard; `UGWR` = Underground Water Reservoir · len 6 |
| `WELLDPTH` | Double | Well Depth |  |
| `CAP` | Double | Capacity |  |
| `CAPUM` | String | Capacity Units | len 4 |
| `MODELNO` | String | Model # | len 20 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `SUDESC` | String | Storage Unit Description | len 30 |
| `THICKNESS_1` | Double | Thickness |  |
| `UNITTYPE_1` | String | Storage Unit Type | **Values:** `STAND` = WATER TOWER; `UGWR` = UNDER GROUND WATER RESERVOIR · len 6 |
| `TWC_EL` | Double |  |  |
| `SURF_EL` | Double |  |  |
| `SCREEN` | String |  | len 254 |
| `Well_Field` | String |  | **Values:** `Miami` = Miami Well Field; `Mad` = Mad Well Field · len 50 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `OLD_AREAS` | String |  | len 50 |
| `COMMENTS` | String | Comments | len 250 |
| `Telemetry` | String |  | **Values:** `Y` = Yes; `N` = No; `U` = Unknown; `NA` = NA; `Other` = Other; `Unsure` = Unsure; `Yes` = Yes; `No` = No · len 50 |
| `WELLZONE` | String | Well Zone | **Values:** `EASTWOOD` = Eastwood; `FTC` = FTC; `HUFFMAN` = Huffman; `MADNORTH` = Mad North; `NEEDMORE` = Needmore; `OLDDAYNORTH` = Old Dayton North; `RIPRAP` = Rip Rap; `ROHRERS` = Rohrers; `UNKNOWN` = Unknown/Other; `MIAMISOUTH` = Miami South · len 255 |
| `SCREENLENGTH` | Integer | Screen Length |  |
| `SURVEYDATASOURCE` | String | Survey Data Source | len 255 |
| `SCREENTO` | Integer | Screen To |  |
| `SCREENFROM` | Integer | Screen From |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 19: Water Meter

- **Records:** 68,854
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ACCOUNT_ST` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 21: Water Service Line

- **Records:** 66,296
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Service Line ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `PRVT_MATERIAL` | String | Private Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 255 |
| `INSTALLDATE` | Date | Install Date |  |
| `LINETYPE` | String | Line Type | **Values:** `Hydrant` = Hydrant; `Irrigation` = Irrigation; `Other` = Other; `Unknown` = Unknown; `Domestic` = Domestic; `Fire` = Fire; `Industrial` = Industrial; `Commercial` = Commercial; `UNKNOWN` = Unknown; `DOMEST` = Domestic; `FIRE` = Fire; `HYDRANT` = Hydrant; …(+1 more) · len 30 |
| `LOCDESC` | String | Location Description | len 50 |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `CRITSRV` | String | Critical Service | **Values:** `ADULT` = ANY AGES ADULT DAY CARE; `ALTA` = ALTA NURSING HOME; `CATMAN` = CATALPA MANOR NURSING CENTER; `DHEALT` = DAYTON HEALTH CARE CENTER; `EASTMAN` = EASTVIEW MANOR RESIDENTIAL CTR; `FORVIEW` = FOREST VIEW NURSING CENTER; `GOODSM` = GOOD SAMARITAN HOSP. & TRAUMA; `GRAFT` = GRAFTON OAKS NURSING CENTER; `GRNDVW` = GRANDVIEW HOSPITAL; `GRNHLT` = GRANDVIEW HEALTH CARE CENTER; `LOVCAR` = LOVING CARE NURSING CENTER; `MAPLE` = MAPLEVIEW MANOR; …(+7 more) · len 9 |
| `CURBSTOP` | String | Curb Stop Location | len 254 |
| `FIRELINE` | String | Fire Line | len 1 |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `TAPLOC` | String | Water Tap Location | len 254 |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 20: Water Main

- **Records:** 58,517
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `INSTALLDATE` | Date | Install Date |  |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `WATERTYPE` | String | Water Type | **Values:** `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Storm` = Storm Runoff; `Treated` = Treated Water · len 30 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DPTH` | Double | Depth |  |
| `LOC` | String | Location Information | len 4 |
| `OWN` | String | Owner | **Values:** `CITY` = CITY OF DAYTON; `CNTY` = COUNTY; `PRIV` = PRIVATE; `AIRP` = DAYTON INTERNATIONAL AIRPORT; `CLAY` = CITY OF CLAYTON; `UNKN` = UNKNOWN; `OHIO` = STATE OF OHIO DEPARTMENT; `VAN` = VANDALIA · len 4 |
| `PIPELEN` | Double | Pipe Length |  |
| `PRESZONE` | String | Pressure Zone | **Values:** `High` = High; `Low` = Low; `SH` = Super High; `HIGH` = High; `LOW` = Low; `H` = High; `L` = Low · len 4 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 6 |
| `LINED` | String | Lined | len 2 |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 0: Sanitary Utilities

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 1: Sanitary System Valve

- **Records:** 133
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `Air` = Air Release Valve; `Ball` = Ball; `Bloff` = Blow Off Valve; `Butterfly` = Butterfly; `Bypass` = Bypass Valve; `Check` = Check Valve; `Cone` = Cone; `Curb` = Curb Stop; `Ford` = Ford Valve; `Gate` = Gate; `GATE` = Gate; `Hyd` = Hydrant Valve; …(+12 more) · len 30 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 2: Sanitary Control Valve

- **Records:** 169
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `VALVETYPE` | String | Valve Type | **Values:** `BFLY` = BUTTERFLY VALVE; `BLOFF` = BLOWOFF VALVE; `CHECK` = CHECK VALVE; `DCHCK` = DISCHARGE CHECK VALVE; `DISOL` = DISCHARGE ISOLATION VALVE; `GATE` = GATE VALVE; `GLOBE` = GLOBE VALVE; `BALL` = BALL VALVE; `RSWED` = RESILIENT WEDGE VALVE; `LAYDW` = LAY-DOWN VALVE; `BYPAS` = BYPASS GATE VALVE; `PIEDO` = PIEDOMETER VALVE; …(+16 more) · len 30 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DIR` | String | Direction to Open | len 1 |
| `NOTURNS` | String | # of Turns | len 6 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 3: Sanitary Fitting

- **Records:** 511
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Node ID | len 16 |
| `FITTINGTYPE` | String | Fitting Type | **Values:** `ANGLE` = < 45 DEGREE BEND; `ENDPT` = END POINT/PLUG; `JNT-T` = T-JOINT; `JNT-X` = CROSS JOINT; `VLV` = VALVE; `RED` = REDUCER; `45` = 45 DEGREE BEND; `90` = 90 DEGREE BEND; `SRV` = LARGE SERVICE LINE NODE; `JUNC` = JUNCTION CHAMBER; `PLUG` = MAIN LINE PLUG; `COUPLING` = COUPLING; …(+25 more) · len 50 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `DISTFRND` | Double | Node Location |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 4: Sanitary Manhole

- **Records:** 20,284
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Manhole ID | len 16 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERT` | Double | Invert |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 20 |
| `WALLMAT` | String | Wall Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 25 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String | Lined | len 3 |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `LOCDESC` | String | Location Description | len 200 |
| `SUMFLOW` | Double | Flow Summary |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `DROPMH` | String | Drop Manhole | len 1 |
| `LOC` | String | Location Information | len 4 |
| `METERED` | String | Metered | len 1 |
| `UNITTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `DRAIN` = DRAIN · len 6 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 5: Sanitary Cleanout

- **Records:** 11
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `INVERTELEV` | Double | Invert Elevation |  |
| `LOC` | String | Location Information | len 4 |
| `RIMELEV` | Double | Rim Elevation |  |
| `DEVICETYPE` | String | Clean Out Type | **Values:** `Flushing Structure` = Flushing Structure; `Lamp Hole` = Lamp Hole; `Other` = Other; `Unknown` = Unknown; `CLNOUT` = Cleanout; `PLUG` = Plug; `SS` = Sampling Station; `BMSO` = Bridge Maint Service Outlet; `DRNWEL` = DRNWEL; `AS` = AS; `NONWRK` = NON WORK ORDER RELATED ISSUE; `SW` = SW; …(+1 more) · len 30 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 6: Sanitary Network Structure

- **Records:** 116
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NAME` | String | Name | len 20 |
| `UNITID` | String | Structure ID | len 16 |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Diversion Chamber` = Diversion Chamber; `Diversion Point` = Diversion Point; `Junction Chamber` = Junction Chamber; `Production Well` = Production Well; `Pump Station` = Pump Station; `Split Manhole` = Split Manhole; `Storage Basin` = Storage Basin; `Tide Chamber` = Tide Chamber; `Treatment Plant` = Treatment Plant; `Lift Station` = Lift Station; `Discharge Structure` = Discharge Structure; `Unknown` = Unknown; …(+10 more) · len 30 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `OPDATE` | Date | Operational Date |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `LSDESC` | String | Lift Station Description | len 30 |
| `NOPUMPS` | Integer | # of Pumps |  |
| `UNITTYPE` | String | Lift Station Type | **Values:** `B` = STORM - DRAINAGE; `A` = STORM - FLOOD CONTROL; `SANI` = SANITARY; `STORM` = STORM; `FLOOD` = STORM - FLOOD CONTROL; `DRAIN` = STORM - DRAINAGE; `JUNCMH` = JUNCTION CHAMBER · len 6 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 9: Sanitary Lateral Line

- **Records:** 50,271
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Service ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `LINETYPE` | String | Line Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 30 |
| `LOCDESC` | String | Location Description | len 50 |
| `DISTANCE` | Integer | Distance |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `NOTAPS` | Integer | # of Taps |  |
| `SRVTYPE` | String | Service Type | **Values:** `COM` = NON-INDUSTRIAL/MERCANTILE; `IND` = INDUSTRIAL; `MIL` = MILITARY; `MUN` = MUNICIPAL; `PRI` = PRIVATE SERVICE; `PUB` = PUBLIC SERVICE; `RES` = RESIDENTIAL; `DOM` = DOMESTIC/RESIDNTL - WATER ONLY; `IRRI` = IRRIGATION; `FIRE` = FIRE LINE; `SWRO` = SEWER ONLY; `SONM` = DOMESTIC SEWER ONLY - NO METER; …(+10 more) · len 4 |
| `SURF` | String | Surface Cover | **Values:** `ASPH` = ASPHALT STREET; `CONC` = CONCRETE STREET; `UNPV` = UNPAVED STREET; `SDWK` = SIDEWALK; `TREE` = TREE/SHRUBS; `FENC` = CLOSE TO FENCE; `OPEN` = OPEN AREA; `BLDM` = BUILDING MOVEABLE; `BLDU` = UNMOVABLE BUILDING; `OHUT` = OVERHEAD UTILITIES; `RWAY` = WATERWAY OR RAILWAY; `HIWY` = HIGHWAY OR RUNWAY; …(+13 more) · len 4 |
| `TAPADDRKEY` | Integer | Tap Address |  |
| `TAPDIST` | Double | Tap Location |  |
| `UNITTYPE` | String | Service Line Type | **Values:** `COPPER` = COPPER; `DOMEST` = DOMESTIC; `FIRE` = FIRE; `IRRIGA` = IRRIGATION · len 6 |
| `YCOORD` | String | Y Coord | len 15 |
| `ZCOORD` | String | Z Coord | len 15 |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 7: Sanitary Pressurized Main

- **Records:** 38
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `WATERTYPE` | String | Water Type | **Values:** `Treated` = Treated Water; `Combined` = Combined Waste Water; `Potable` = Potable Water; `Raw` = Raw Water; `Reclaimed` = Reclaimed Water; `Salt` = Salt Water; `Sewage` = Sewage; `Storm` = Storm Runoff; `Effluent` = Waste Water Effluent · len 30 |
| `HANSENID` | String | Hansen ID | len 50 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 20 |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 18 |
| `LOCATIONMO` | String |  | len 3 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `DISTRICT` | String | District | **Values:** `F` = F; `A` = A; `B` = B; `C` = C; `DIST` = WATER DISTRIBUTION; `2` = 2; `4` = 4; `8` = 8; `10` = 10; `11` = 11; `12` = 12; `13` = 13; …(+6 more) · len 4 |
| `LOC` | String | Location Information | len 4 |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 8: Sanitary Gravity Main

- **Records:** 21,093
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `HANSENID` | String | Hansen ID | len 50 |
| `SUMFLOW` | Double | Flow Summary |  |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 18 |
| `LOCATIONMO` | String |  | len 3 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `LOC` | String | Location Information | len 4 |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 32: Sanitary Gravity Main Citywide

- **Records:** 21,093
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `INSTALLDATE` | Date | Install Date |  |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `HANSENID` | String | Hansen ID | len 50 |
| `SUMFLOW` | Double | Flow Summary |  |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `PIPETYPE` | String | Pipe Type | **Values:** `CONC` = CONCRETE; `CIP` = CAST IRON PIPE; `CMP` = CORRUGATED METAL PIPE; `DCI` = DUCTILE CAST IRON; `VCP` = VITRIFIED CLAY PIPE; `BRICK` = BRICK; `LCONC` = LINED CONCRETE; `COPPER` = COPPER; `REV` = REVERSE FLOW; `CBI` = CONCRETE BRICK INVERT; `PVC` = POLY VINYL CHLORIDE; `RCP` = REINFORCED CONCRETE PIPE; …(+4 more) · len 20 |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 18 |
| `LOCATIONMO` | String |  | len 3 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `LOC` | String | Location Information | len 4 |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `year_treated` | SmallInteger | Year_Treated |  |
| `YearTreatedJoin` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 22: Storm Utilities

- **Records:** unknown

| Field | Type | Alias | Notes |
|---|---|---|---|

## Layer 23: Storm System Valve

- **Records:** 68
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `VALVETYPE` | String | Valve Type | **Values:** `Air` = Air Release Valve; `Ball` = Ball; `Bloff` = Blow Off Valve; `Butterfly` = Butterfly; `Bypass` = Bypass Valve; `Check` = Check Valve; `Cone` = Cone; `Curb` = Curb Stop; `Ford` = Ford Valve; `Gate` = Gate; `GATE` = Gate; `Hyd` = Hydrant Valve; …(+12 more) · len 30 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `BYPASSVALVE` | SmallInteger | Bypass Valve | **Values:** `0` = False; `1` = True |
| `CLOCKTOCLOSE` | SmallInteger | Clockwise To Close | **Values:** `0` = False; `1` = True |
| `NORMALLYOPEN` | SmallInteger | Normally Open | **Values:** `0` = False; `1` = True |
| `TURNSTOCLOSE` | Integer | Turns To Close |  |
| `OPERABLE` | SmallInteger | Operable | **Values:** `0` = False; `1` = True |
| `CURROPEN` | SmallInteger | Currently Open | **Values:** `0` = False; `1` = True |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 24: Storm Control Valve

- **Records:** 2
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Valve ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `VALVETYPE` | String | Valve Type | **Values:** `BFLY` = BUTTERFLY VALVE; `BLOFF` = BLOWOFF VALVE; `CHECK` = CHECK VALVE; `DCHCK` = DISCHARGE CHECK VALVE; `DISOL` = DISCHARGE ISOLATION VALVE; `GATE` = GATE VALVE; `GLOBE` = GLOBE VALVE; `BALL` = BALL VALVE; `RSWED` = RESILIENT WEDGE VALVE; `LAYDW` = LAY-DOWN VALVE; `BYPAS` = BYPASS GATE VALVE; `PIEDO` = PIEDOMETER VALVE; …(+16 more) · len 30 |
| `SERVSTAT` | String | Service Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `VALVESTAT` | String | Valve Status | **Values:** `C` = CLOSED; `O` = OPENED; `P` = PARTIALLY OPENED; `A` = ABANDONED; `B` = BROKEN; `BAL` = BALL INSERTED; `L` = LEAKING · len 3 |
| `INSTALLDATE` | Date | Install Date |  |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DIR` | String | Direction to Open | len 1 |
| `MFGKEY` | Integer | Manufacturer |  |
| `NOTURNS` | String | # of Turns | len 6 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 25: Storm Inlet

- **Records:** 22,689
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Inlet ID | len 16 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `INLETTYPE` | String | Inlet Type | **Values:** `OTM` = OPEN TOP MANHOLE; `DAD` = DOUBLE ALLEY DRIP (TYPE E); `GINLET` = GRATE INLET; `EEAD` = END TO END ALLEY DRIP (TYPE C); `CCB` = CURB CATCH BASIN; `CINLET` = CURB INLET; `SAD` = SINGLE ALLEY DRIP; `CATBSN` = CATCH BASIN; `HEDWAL` = HEAD WALL; `DWNSP` = DOWNSPOUT; `DWTRWL` = DEWATERING WELL; `CULVERT` = CULVERT; …(+1 more) · len 50 |
| `ACCESSDIAM` | Double | Access Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `INVERTELEV` | Double | Invert Elevation |  |
| `ACCESSMAT` | String | Access Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `ACCESSTYPE` | String | Access Type | **Values:** `Door` = Door; `Grate` = Grate; `Cover` = Cover; `Hand` = Hand; `Lid` = Lid; `Unknown` = Unknown · len 20 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `GRATETYPE` | String | Grate Type | len 6 |
| `LOC` | String | Location Information | len 4 |
| `MATL` | String | Material | len 6 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 26: Storm Fitting

- **Records:** 3,418
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Node ID | len 16 |
| `FITTINGTYPE` | String | Fitting Type | **Values:** `ANGLE` = < 45 DEGREE BEND; `ENDPT` = END POINT/PLUG; `JNT-T` = T-JOINT; `JNT-X` = CROSS JOINT; `VLV` = VALVE; `RED` = REDUCER; `45` = 45 DEGREE BEND; `90` = 90 DEGREE BEND; `SRV` = LARGE SERVICE LINE NODE; `JUNC` = JUNCTION CHAMBER; `PLUG` = MAIN LINE PLUG; `COUPLING` = COUPLING; …(+25 more) · len 50 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `LOCDESC` | String | Location Description | len 200 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | AsBuilt # | len 10 |
| `DISTFRND` | Double | Node Location |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 27: Storm Manhole

- **Records:** 14,984
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Manhole ID | len 16 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `HIGHELEV` | Double | High Pipe Elevation |  |
| `INVERTELEV` | Double | Invert Elevation |  |
| `INVERT` | Double | Invert |  |
| `RIMELEV` | Double | Rim Elevation |  |
| `CVTYPE` | String | Cover Type | **Values:** `Standard W/ Lock` = Standard W/ Lock; `Standard W/ Ears` = Standard W/ Ears; `Non-District` = Non-District; `Water Tight` = Water Tight; `27" Diameter` = 27" Diameter; `42" Diameter` = 42" Diameter; `Large - Water Tight` = Large - Water Tight; `Rectangular` = Rectangular; `Other` = Other; `Unknown` = Unknown; `DUC` = DUCTILE; `BOL` = BOLTED; …(+6 more) · len 50 |
| `WALLMAT` | String | Wall Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 25 |
| `MHTYPE` | String | Manhole Type | **Values:** `PRESS` = PRESSURE MANHOLE; `INSIDE DROP` = INSIDE DROP; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFALL` = OUTFALL; `TEEMH` = TEE MANHOLE · len 15 |
| `CONDITION` | String | Manhole Condition | **Values:** `Excellent` = Excellent; `Very Good` = Very Good; `Good` = Good; `Fair` = Fair; `Poor` = Poor; `Very Poor` = Very Poor; `Unknown` = Unknown · len 10 |
| `LOCDESC` | String | Location Description | len 200 |
| `CUTDEPTH` | Double | Pavement Cut Depth |  |
| `FLOWDIR` | String | Flow Direction | len 5 |
| `LINED` | String | Lined | len 3 |
| `SUMFLOW` | Double | Flow Summary |  |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `MHDPTH` | Double | Manhole Depth |  |
| `LININGTYPE` | String | Lining Type | **Values:** `CIPP` = Cured In Place Pipe; `CEM` = Cement; `EP` = Epoxy; `PUR` = Polyurethane · len 6 |
| `DATELINED` | Date | Date Lined |  |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 28: Storm Network Structure

- **Records:** 31
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `NAME` | String | Name | len 50 |
| `UNITID` | String | Lift Station ID | len 16 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `INSTALLDATE` | Date | Install Date |  |
| `UNITTYPE` | String | Lift Station Type | **Values:** `B` = STORM - DRAINAGE; `A` = STORM - FLOOD CONTROL; `SANI` = SANITARY; `STORM` = STORM; `FLOOD` = STORM - FLOOD CONTROL; `DRAIN` = STORM - DRAINAGE; `JUNCMH` = JUNCTION CHAMBER · len 6 |
| `LOCDESC` | String | Location Description | len 200 |
| `ROTATION` | Double | Rotation |  |
| `OPDATE` | Date | Operational Date |  |
| `STRUCTTYPE` | String | Structure Type | **Values:** `Diversion Chamber` = Diversion Chamber; `Diversion Point` = Diversion Point; `Junction Chamber` = Junction Chamber; `Pump Station` = Pump Station; `Split Manhole` = Split Manhole; `Storage Basin` = Storage Basin; `Tide Chamber` = Tide Chamber; `Lift Station` = Lift Station; `Discharge Structure` = Discharge Structure; `Unknown` = Unknown; `Other` = Other; `Virtual Junction` = Virtual Junction · len 30 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `LSDESC` | String | Lift Station Description | len 30 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 29: Storm Discharge Point

- **Records:** 536
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `UNITID` | String | Outfall ID | len 16 |
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `AVGDISCH` | String | Average Discharge | len 10 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `DISCHRGTYP` | String | Discharge Type | **Values:** `PRESS` = PRESSURE MANHOLE; `TRAP` = TRAP MANHOLE; `LAMP` = LAMPHOLE; `FORC` = FORCE MAIN MANHOLE; `JUNCMH` = JUNCTION CHAMBER; `STAND` = STANDARD MANHOLE; `ENDWAL` = END WALL; `DROP` = DROP MANHOLE; `OUTFAL` = OUTFALL; `TEEMH` = TEE MANHOLE; `OVERFLOW` = OVERFLOW · len 50 |
| `LOCDESC` | String | Location Description | len 200 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 30: Storm Gracity Main

- **Records:** 41,085
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `HANSENID` | String | Hansen ID | len 50 |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `INSTALLDATE` | Date | Install Date |  |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 6 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 4 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 31: Storm Gracity Main Citywide

- **Records:** 41,085
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `DIAMETER` | Double | Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `MATERIAL` | String | Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 20 |
| `SERVSTAT` | String | Status | **Values:** `T` = TEMPORARILY OUT OF SERVICE; `IS` = IN SERVICE; `OS` = OUT OF SERVICE; `A` = ABANDONED; `LM I` = LARGE METER IN SERVICE; `LM 0` = LARGE METER OUT OF SERVICE; `LM O` = LARGE METER OUT OF SERVICE; `LM T` = LRG MTR TEMPORARY OUT OF SERV; `LRGM` = LARGE METER; `SCRP` = SCRAPPED PERMANENTLY OUR OF SR; `LOST` = METER IS LOST !!!; `HELD` = METER HELD PER/FOR METER SHOP; …(+7 more) · len 4 |
| `HANSENID` | String | Hansen ID | len 50 |
| `MAINSHAPE` | String | Main Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 50 |
| `INSTALLDATE` | Date | Install Date |  |
| `LINEDYEAR` | String | Year Lined | len 4 |
| `LINERTYPE` | String | Liner Type | **Values:** `FF` = Fold and Form or Deform/Reform; `SN` = Segmented Panel; `SP` = Segmented Pipe; `SW` = Spiral Wound; `OTH` = Other; `NONE` = None; `CIPP` = Cured in Place · len 20 |
| `DOWNELEV` | Double | Downstream Elevation |  |
| `UPELEV` | Double | Upstream Elevation |  |
| `SLOPE` | Double | Slope |  |
| `UNITID` | String | Up MH ID | len 16 |
| `UNITID2` | String | Down MH ID | len 16 |
| `ADDRKEY` | Integer | Address |  |
| `ADDRQUAL` | String | Address Info | len 254 |
| `ASBLT` | String | Asbuilt # | len 10 |
| `PIPEDIAM` | Double | Pipe Diameter |  |
| `UNITTYPE` | String | Main Line Type | **Values:** `A` = DRAINAGE; `B` = SANITARY; `CONC` = CONCRETE; `D` = TRUNK LINE; `E` = INTERCEPTOR; `F` = OPEN CHANNEL/DITCH; `FORCE` = FORCE MAIN; `I` = COLLECTOR; `PARALN` = PARALLEL LINE; `SIPHON` = SIPHON; `STLAT` = STORM LATERAL; `TRANS` = TRANSITION PIECE; …(+7 more) · len 6 |
| `PIPESHP` | String | Pipe Shape | **Values:** `BOX` = BOX; `NCHN` = NATURAL CHANNEL; `OVAL` = OVAL; `RCHN` = RECTANGULAR OPEN CHANNEL; `SEMI` = SEMI-ELLIPTICAL; `VAR` = VARIABLE SHAPE; `CIRC` = CIRCULAR; `TRAN` = TRANSITION PIECE; `ARCH` = ARCHED; `EGG` = EGG; `OTH` = OTHER · len 4 |
| `LINED` | String | Lined | len 2 |
| `DATELINED` | Date | Date Lined |  |
| `COMMENTS` | String | Comments | len 250 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 33: City of Dayton Corp. Limits

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

