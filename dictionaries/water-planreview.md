# Water/PlanReview

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `City of Dayton GIS (on-premise)`)
- **Service type:** Feature Service
- **Service URL:** https://maps.daytonohio.gov/gisservices/rest/services/Water/PlanReview/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=Water_PlanReview
- **Created:** None  ·  **Item modified:** None
- **Tags:** Water

## Layer 0: Water Plan Review

- **Records:** 24
- **Geometry:** Polygon

| Field | Type | Alias | Notes |
|---|---|---|---|
| `PROJECTID` | String | Project ID | len 50 |
| `ADDRESS` | String | Address | len 50 |
| `PROJECTNAME` | String | Project Name | len 50 |
| `PUBLICIMPROVEMENTSTATUS` | String | Public Improvement Status | **Values:** `Investigation` = Investigation; `Preliminary` = Preliminary; `Under Review` = Under Review; `Approved/Construction` = Approved/Construction; `Complete` = Complete; `N/A` = N/A · len 50 |
| `PRIVATEIMPROVEMENTSTATUS` | String | Private Improvement Status | **Values:** `Investigation` = Investigation; `Preliminary` = Preliminary; `Under Review` = Under Review; `Approved/Construction` = Approved/Construction; `Complete` = Complete; `N/A` = N/A · len 50 |
| `RECORDPLAN` | String | Record Plan Status | **Values:** `Investigation` = Investigation; `Preliminary` = Preliminary; `Under Review` = Under Review; `Approved/Construction` = Approved/Construction; `Complete` = Complete; `N/A` = N/A · len 50 |
| `REVIEWLINK` | String | Plan Review Link | len 50 |
| `created_user` | String |  | len 255 |
| `created_date` | Date |  |  |
| `last_edited_user` | String |  | len 255 |
| `last_edited_date` | Date |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `GlobalID` | GlobalID |  |  |
| `Shape__Area` | Double | SHAPE.STArea() |  |
| `Shape__Length` | Double | SHAPE.STLength() |  |
| `OBJECTID` | OID |  |  |

</details>

