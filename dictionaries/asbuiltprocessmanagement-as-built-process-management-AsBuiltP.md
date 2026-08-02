# AsBuiltProcessManagement/As_Built_Process_Management

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/AsBuiltProcessManagement/As_Built_Process_Management/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=AsBuiltProcessManagement_As_Built_Process_Management
- **Created:** None  ·  **Item modified:** None
- **Tags:** AsBuiltProcessManagement

## Layer 0: Water Asset Collection

- **Records:** 2,501
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Asset_Code` | String | Survey Code | **Values:** `2301  Water Manhole` = Water Manhole; `2302  Water Valve (Street)` = Water Valve (Street); `2303  Curb Stop Valve` = Curb Stop Valve; `2304  Ford Meter Box` = Ford Meter Box; `2305  Hydrant` = Hydrant; `2306  Water Trace` = Water Trace; `2307  Water Meter Pit (Center)` = Water Meter Pit (Center); `2317  Siamese Fire Connection` = Siamese Fire Connection; `2318  Water Spigot - Hose Bibb` = Water Spigot - Hose Bibb; `2320  Reducer` = Reducer; `2321  Sampling Station` = Sampling Station; `2322  Water Misc.` = Water Misc.; …(+16 more) · len 255 |
| `ValveType` | String | Type of Valve | **Values:** `Air` = Air Release Valve; `Ball` = Ball; `Bloff` = Blow Off Valve; `Butterfly` = Butterfly; `Bypass` = Bypass Valve; `Check` = Check Valve; `Cone` = Cone; `Curb` = Curb Stop; `Ford` = Ford Valve; `Gate` = Gate; `GATE` = Gate; `Hyd` = Hydrant Valve; …(+12 more) · len 255 |
| `Diameter` | Double | Asset Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `Material` | String | Asset Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 255 |
| `Depth` | Single | Depth of Asset |  |
| `Comments` | String |  | len 1000 |
| `created_user` | String | Inspector | len 255 |
| `created_date` | Date | Inspection Date |  |
| `AsBuiltNumber` | String | As Built Number | len 25 |
| `JobName` | String | Name of Job | len 255 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | Double |  |  |
| `Ownership` | String | Asset Owner | **Values:** `Public` = Public; `Private` = Private; `County` = County · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 1: Storm Asset Collection

- **Records:** 440
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Asset_Code` | String | Survey Code | **Values:** `2401  Storm Manhole` = Storm Manhole; `2402  Open Top Storm MH` = Open Top Storm MH; `2403  A CB - 1 Lid on Curb` = A CB - 1 Lid on Curb; `2404  B CB - 2 Lids on Curb` = B CB - 2 Lids on Curb; `2405  C CB - 1 or 2 Grates in Street` = C CB - 1 or 2 Grates in Street; `2406  D CB - default` = D CB - default; `2407  E CB - in Parking Lots - 2 Grates` = E CB - in Parking Lots - 2 Grates; `2408  E CB - in Parking Lot - 1 Grate` = E CB - in Parking Lot - 1 Grate; `2409  Toilet Lid CB - Curb Inlet` = Toilet Lid CB - Curb Inlet; `2410  ODOT Large Grate CB` = ODOT Large Grate CB; `2411  ODOT Small Grate CB` = ODOT Small Grate CB; `2412  Strip Trench Drain (Center Shot)` = Strip Trench Drain (Center Shot); …(+5 more) · len 255 |
| `ValveType` | String | Type of Valve | **Values:** `Air` = Air Release Valve; `Ball` = Ball; `Bloff` = Blow Off Valve; `Butterfly` = Butterfly; `Bypass` = Bypass Valve; `Check` = Check Valve; `Cone` = Cone; `Curb` = Curb Stop; `Ford` = Ford Valve; `Gate` = Gate; `GATE` = Gate; `Hyd` = Hydrant Valve; …(+12 more) · len 255 |
| `Diameter` | Double | Asset Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `Material` | String | Asset Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 255 |
| `Comments` | String |  | len 1000 |
| `created_user` | String | Inspector | len 255 |
| `created_date` | Date | Inspection Date |  |
| `AsBuiltNumber` | String | As Built Number | len 25 |
| `JobName` | String | Name of Job | len 255 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | Double |  |  |
| `Ownership` | String | Asset Owner | **Values:** `Public` = Public; `Private` = Private; `County` = County · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 2: Sanitary Asset Collection

- **Records:** 436
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Asset_Code` | String | Survey Code | **Values:** `2351  Sanitary Manhole` = Sanitary Manhole; `2353  Cleanout (Sanitary)` = Cleanout (Sanitary); `2354  Sanitary Lamphole` = Sanitary Lamphole; `2355  Sanitary Misc.` = Sanitary Misc.; `2356  Sanitary Wye` = Sanitary Wye; `2357  Sanitarty Tee` = Sanitary Tee; `2358  Sanitary Lateral` = Sanitary Lateral; `2327  Top Sanitary Line` = Top Sanitary Line; `0000  Sanitary Abandoned Feature` = Sanitary Abandoned Feature · len 255 |
| `ValveType` | String | Type of Valve | **Values:** `Air` = Air Release Valve; `Ball` = Ball; `Bloff` = Blow Off Valve; `Butterfly` = Butterfly; `Bypass` = Bypass Valve; `Check` = Check Valve; `Cone` = Cone; `Curb` = Curb Stop; `Ford` = Ford Valve; `Gate` = Gate; `GATE` = Gate; `Hyd` = Hydrant Valve; …(+12 more) · len 255 |
| `Diameter` | Double | Asset Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `Material` | String | Asset Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 255 |
| `Comments` | String |  | len 1000 |
| `created_user` | String | Inspector | len 255 |
| `created_date` | Date | Inspection Date |  |
| `AsBuiltNumber` | String | As Built Number | len 25 |
| `JobName` | String | Name of Job | len 255 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Integer |  |  |
| `ZCOORD` | Double |  |  |
| `Ownership` | String | Asset Owner | **Values:** `Public` = Public; `Private` = Private; `County` = County · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 3: Ground Asset Collection

- **Records:** 11
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Asset_Code` | String | Survey Code | **Values:** `2201  Ground Shot` = Ground Shot; `2221  Edge of Asphalt` = Edge of Asphalt; `2222  On Asphalt` = On Asphalt; `2223  Edge Concrete` = Edge Concrete; `2224  On Concrete` = On Concrete; `2241  Face of Curb Base` = Face of Curb Base; `2247  Sidewalk - Edge` = Sidewalk - Edge; `0000  Abandoned Ground Feature` = Abandoned Ground Feature · len 255 |
| `Comments` | String |  | len 1000 |
| `created_user` | String | Inspector | len 255 |
| `created_date` | Date | Inspection Date |  |
| `AsBuiltNumber` | String | As Built Number | len 25 |
| `JobName` | String | Name of Job | len 255 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | Double |  |  |
| `Ownership` | String | Asset Owner | **Values:** `Public` = Public; `Private` = Private; `County` = County · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 4: Gas Asset Collection

- **Records:** 6
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Asset_Code` | String | Survey Code | **Values:** `2601  Gas Manhole` = Gas Manhole; `2602  Gas Valve (In Street)` = Gas Valve (In Street); `2603  Curb Stop` = Curb Stop; `2605  GAS OUPS` = GAS OUPS; `2326  Top Gas Line` = Top Gas Line; `0000  Abandoned Gas Feature` = Abandoned Gas Feature · len 255 |
| `Diameter` | Double | Asset Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `Comments` | String |  | len 1000 |
| `created_user` | String | Inspector | len 255 |
| `created_date` | Date | Inspection Date |  |
| `AsBuiltNumber` | String | As Built Number | len 25 |
| `JobName` | String | Name of Job | len 255 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCOORD` | Double |  |  |
| `Ownership` | String | Asset Owner | **Values:** `Public` = Public; `Private` = Private; `County` = County · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 5: Electric/Communication Asset Collection

- **Records:** 34
- **Geometry:** Point

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Asset_Code` | String | Survey Code | **Values:** `2611  Electric Manhole` = Electric Manhole; `2612  Electric Pullbox` = Electric Pullbox; `2621  Telephone Manhole` = Telephone Manhole; `2631  Fiberoptic Manhole` = Fiberoptic Manhole; `2329  Top Telephone Line` = Top Telephone Line; `2330  Top Fiber Line` = Top Fiber Line; `2331  Top Electric Line` = Top Electric Line; `0000  Electric_Comm Abandoned Feature` = Electric_Comm Abandoned Feature · len 255 |
| `Diameter` | Double | Asset Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `Comments` | String |  | len 1000 |
| `created_user` | String | Inspector | len 255 |
| `created_date` | Date | Inspection Date |  |
| `AsBuiltNumber` | String | As Built Number | len 25 |
| `JobName` | String | Name of Job | len 255 |
| `XCOORD` | Double |  |  |
| `YCOORD` | Double |  |  |
| `ZCoordinate` | Double | ZCOORD |  |
| `Ownership` | String | Asset Owner | **Values:** `Public` = Public; `Private` = Private; `County` = County · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 6: Utility Line Feature

- **Records:** 0
- **Geometry:** Polyline

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LineType` | String | Type of Utility Line | **Values:** `Water Line` = Water Line; `Sanitary Line` = Sanitary Line; `Storm Line` = Storm Line; `Abandoned Line` = Abandoned Line; `Gas Line` = Gas Line; `Electric Line` = Electric Line; `COMM Line` = COMM Line · len 255 |
| `Material` | String | Utility Material | **Values:** `AC` = ASBESTOS CEMENT; `BRICK` = BRICK; `CIP` = CAST IRON PIPE; `CNCONC` = CAST-IN-PLACE CONCRETE; `CL` = CEMENT LINED; `CONC` = CONCRETE; `CBI` = CONCRETE BRICK INVERT; `CSB` = CONCRETE SEGMENTS (BOLTED); `COPPER` = COPPER; `CMP` = CORRUGATED METAL PIPE; `COR` = CURRUGATED PLASTIC; `DCI` = DUCTILE CAST IRON; …(+15 more) · len 255 |
| `Diameter` | Double | Utility Diameter | **Values:** `0.75` = 3/4"; `1` = 1"; `1.25` = 1 1/4"; `1.5` = 1 1/2"; `2` = 2"; `2.5` = 2 1/2"; `3` = 3"; `4` = 4"; `6` = 6"; `8` = 8"; `10` = 10"; `12` = 12"; …(+66 more) |
| `Comments` | String | Inspector Comments | len 1000 |
| `Depth` | Double | Utility Depth |  |
| `created_user` | String | Inspector | len 255 |
| `created_date` | Date | Inspection Date |  |
| `AsBuiltNumber` | String |  | len 25 |
| `JobName` | String | Name of Job | len 255 |
| `XCoord` | Double | X Coordinate |  |
| `YCoord` | Double | Y Coordinate |  |
| `ZCoord` | Double | Z Coordinate |  |
| `Ownership` | String | Asset Owner | **Values:** `Public` = Public; `Private` = Private; `County` = County · len 255 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

