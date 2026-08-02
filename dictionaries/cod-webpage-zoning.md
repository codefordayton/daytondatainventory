# COD_Webpage/Zoning

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/COD_Webpage/Zoning/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=COD_Webpage_Zoning
- **Created:** None  ·  **Item modified:** None
- **Tags:** COD_Webpage

## Layer 0: Urban Renewal Areas

- **Records:** 4
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `URBAN_RENE` | String |  | len 16 |
| `AREA_` | Double |  |  |
| `PERIMETER` | Double |  |  |
| `ACRES` | Double |  |  |
| `HECTARES` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry |  |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 1: Flood Plain

- **Records:** 29
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `LEVEL_` | SmallInteger |  |  |
| `COLOR` | SmallInteger |  |  |
| `TEXT` | String |  | len 50 |
| `MSLINK_DBA` | Integer |  |  |
| `MSCTLG_DBA` | Integer |  |  |
| `LABEL` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 2: Wellfield District

- **Records:** 6
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `Id` | Integer | ID |  |
| `Acreage` | Integer |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | Integer |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry | SHAPE |  |
| `OBJECTID_1` | OID |  |  |
| `Shape_Leng` | Double |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 3: Planned Development

- **Records:** 136
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `FEATURE` | String |  | len 16 |
| `DISTRICT` | String |  | len 16 |
| `YEAR` | Date |  |  |
| `ORDINANCE` | String |  | len 16 |
| `CPB` | String |  | len 10 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

## Layer 4: Historic District

- **Records:** 20
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `ID` | Integer |  |  |
| `FEATURE` | String |  | len 16 |
| `NAME` | String |  | len 16 |
| `DISTRICT` | String |  | len 16 |
| `YEAR` | Date |  |  |
| `ORDINANCE` | String |  | len 16 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | Integer |  |  |
| `GlobalID` | GlobalID | GLOBALID |  |
| `Shape` | Geometry | SHAPE |  |
| `OBJECTID_1` | OID |  |  |
| `Shape.STArea()` | Double |  |  |
| `Shape.STLength()` | Double |  |  |

</details>

## Layer 5: Zoning District

- **Records:** 970
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PERIMETER` | Double |  |  |
| `NEWZONING2` | Integer |  |  |
| `NEWZONIN_1` | Integer |  |  |
| `AREA_1` | Double |  |  |
| `PERIMETE_1` | Double |  |  |
| `NEWZONING_` | Integer |  |  |
| `NEWZONING1` | Integer |  |  |
| `ID` | Double |  |  |
| `FEATURE` | String |  | len 25 |
| `NAME` | String |  | len 50 |
| `DISTRICT` | String |  | len 5 |
| `MATCH_` | String |  | len 10 |
| `LAYER` | String |  | len 32 |
| `NEW_ZONE` | String |  | len 25 |
| `REZONED` | String |  | len 16 |
| `POLYGONID` | Integer |  |  |
| `SCALE` | Double |  |  |
| `ANGLE` | Integer |  |  |
| `DISTANCE` | Double |  |  |
| `GISADMIN_Plan_Zoning_AREA` | Double |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `SHAPE_LENG` | Double |  |  |
| `GLOBALID` | GlobalID |  |  |
| `Shape` | Geometry | SHAPE |  |
| `Shape.STArea()` | Double | SHAPE.STArea() |  |
| `Shape.STLength()` | Double | SHAPE.STLength() |  |

</details>

