# CapitalPlanning/Capital_Improvement_Outlines_PUBLIC

> Layers used for Public CIP Dashboard

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Map Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/CapitalPlanning/Capital_Improvement_Outlines_PUBLIC/MapServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=CapitalPlanning_Capital_Improvement_Outlines_PUBLIC
- **Created:** None  ·  **Item modified:** None
- **Tags:** CapitalPlanning

## Publisher description

Layers used for Public CIP Dashboard

## Layer 0: CIP Project Outlines

- **Records:** 231
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PROJNAME` | String | Project Name | len 50 |
| `TOTCOST` | Double | Total Cost |  |
| `TOTLEN` | Double | Total Length |  |
| `TOTAREA` | Double | Total Area |  |
| `TOTPNT` | Double | Point Count |  |
| `DATESTART` | Date | Expected Start Date |  |
| `DATECOMP` | Date | Date Completed |  |
| `CIPSTAT` | String | CIP Status | **Values:** `Proposed` = Proposed; `Completed` = Completed; `Approved` = Approved; `Funded` = Funded; `Under Construction` = Under Construction; `Canceled` = Canceled · len 50 |
| `NOTES` | String | Notes | len 200 |
| `PRJMAN` | String | Project Manager | len 50 |
| `CREATNAM` | String | Created By | len 50 |
| `CREATDAT` | Date | Date Created |  |
| `LINK` | String | Link to Report | len 175 |
| `LASTEDITOR` | String | Last Editor | len 50 |
| `LASTUPDATE` | Date | Last Update |  |
| `PROJTYPE` | String | Project Type | **Values:** `Water Distribution` = Water Distribution; `Sewer Collection` = Sewer Collection; `Storm Drainage` = Storm Drainage; `Streets` = Streets; `Other` = Other; `Unknown` = Unknown · len 80 |
| `FUNDSOUR` | String | Funding Source | **Values:** `Unknown` = Unknown; `General Revenue` = General Revenue; `Revenue Bonds` = Revenue Bonds; `System Revenues` = System Revenues; `Connection Fees` = Connection Fees; `Other` = Other · len 80 |
| `MANPHONE` | String | Contact Phone | len 80 |
| `MANEMAIL` | String | Contact Email | len 80 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |
| `YEAR` | Integer | Year |  |
| `CASH` | Double | Cash |  |
| `DEBT` | Double | Debt |  |
| `ACTIVITYCODE` | String | Activity Code | len 15 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `SHAPE.STArea()` | Double |  |  |
| `SHAPE.STLength()` | Double |  |  |
| `OBJECTID` | OID |  |  |
| `Shape` | Geometry |  |  |

</details>

