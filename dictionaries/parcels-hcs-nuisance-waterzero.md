# Parcels_HCS_Nuisance_WaterZero

## Source

- **Publisher:** City of Dayton (ArcGIS Online, owner `Richard.Bailey@DaytonOhio.gov`)
- **Service type:** Feature Service
- **Service URL:** https://services2.arcgis.com/3dDB2Kk6kuA2gIGw/arcgis/rest/services/Parcels_HCS_Nuisance_WaterZero/FeatureServer
- **Item page:** https://daytonohio.maps.arcgis.com/home/item.html?id=3c909a6de9d24f5bbdb1826b39bdbeb1
- **Created:** 2024-09-13  ·  **Item modified:** 2024-09-13
- **Tags:** 

## Layer 0: Parcels_ZeroConsumption_Q2_2024

- **Records:** 2,823
- **Geometry:** Polygon
- **Last edited:** 2024-09-13

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TAXPINNO` | String |  | len 20 |
| `K_PID` | String |  | len 18 |
| `OWNER1` | String |  | len 100 |
| `OWNER2` | String |  | len 100 |
| `Q1_2022` | String |  | len 254 |
| `Q2_2022` | String |  | len 254 |
| `Q3_2022` | String |  | len 254 |
| `Q4_2022` | String |  | len 254 |
| `Q1_2023` | String |  | len 254 |
| `Q2_2023` | String |  | len 254 |
| `Q3_2023` | String |  | len 254 |
| `Q4_2023` | String |  | len 254 |
| `Q1_2024` | String |  | len 254 |
| `Q2_2024` | String |  | len 254 |
| `Total` | String |  | len 254 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `FID` | OID |  |  |
| `GlobalID` | String |  | len 38 |
| `Shape__Area` | Double |  |  |
| `Shape__Length` | Double |  |  |

</details>

## Layer 1: Parcels_Nuisance_09132024

- **Records:** 1,547
- **Geometry:** Polygon
- **Last edited:** 2024-09-13

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TAXPINNO` | String |  | len 20 |
| `TAXAREA` | String |  | len 10 |
| `LOTNUMBER` | String |  | len 20 |
| `LOC_NBR` | Double |  |  |
| `LOC_DIR` | String |  | len 4 |
| `LOC_STREET` | String |  | len 50 |
| `LOC_SUFFIX` | String |  | len 10 |
| `PID_FLG01` | String |  | len 10 |
| `LOC_AREA` | String |  | len 30 |
| `NBHD_1` | String |  | len 10 |
| `K_PID` | String |  | len 18 |
| `STR_ID` | Integer |  |  |
| `MCSTR_ID` | Integer |  |  |
| `C_BLOCK` | String |  | len 20 |
| `C_TRACK` | String |  | len 20 |
| `OWNER1` | String |  | len 100 |
| `OWNER2` | String |  | len 100 |
| `LOC_ZIP` | String |  | len 5 |
| `CREATE_DATE` | String |  | len 8 |
| `HCS_PARCEL_ID` | String | HCS_PARCEL ID | len 8000 |
| `HCS_ADDRESS` | String |  | len 8000 |
| `HCS_GRADE` | Integer |  |  |
| `HCS_FPU` | Integer |  |  |
| `HCS_STATUS` | String |  | len 8000 |
| `HCS_NEIGHBORHOOD` | String |  | len 8000 |
| `HCS_NON_ARPA_ARPA` | String | HCS_NON ARPA_ARPA | len 8000 |
| `HCS_NOTES` | String |  | len 8000 |
| `N_Parcel_ID` | String | N_Parcel ID | len 8000 |
| `N_Address` | String |  | len 8000 |
| `N_ZIP` | Integer |  |  |
| `N_Location_Type` | String | N_Location Type | len 8000 |
| `N_Category` | String |  | len 8000 |
| `N_Date` | DateOnly |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape__Area` | Double |  |  |
| `Shape__Length` | Double |  |  |

</details>

## Layer 2: Parcels_HCS_Nuisance_09132024

- **Records:** 86,547
- **Geometry:** Polygon
- **Last edited:** 2024-09-13

| Field | Type | Alias | Notes |
|---|---|---|---|
| `TAXPINNO` | String |  | len 20 |
| `TAXAREA` | String |  | len 10 |
| `LOTNUMBER` | String |  | len 20 |
| `LOC_NBR` | Double |  |  |
| `LOC_DIR` | String |  | len 4 |
| `LOC_STREET` | String |  | len 50 |
| `LOC_SUFFIX` | String |  | len 10 |
| `PID_FLG01` | String |  | len 10 |
| `LOC_AREA` | String |  | len 30 |
| `NBHD_1` | String |  | len 10 |
| `K_PID` | String |  | len 18 |
| `STR_ID` | Integer |  |  |
| `MCSTR_ID` | Integer |  |  |
| `C_BLOCK` | String |  | len 20 |
| `C_TRACK` | String |  | len 20 |
| `OWNER1` | String |  | len 100 |
| `OWNER2` | String |  | len 100 |
| `LOC_ZIP` | String |  | len 5 |
| `CREATE_DATE` | String |  | len 8 |
| `HCS_PARCEL_ID` | String | HCS_PARCEL ID | len 8000 |
| `HCS_ADDRESS` | String |  | len 8000 |
| `HCS_GRADE` | Integer |  |  |
| `HCS_FPU` | Integer |  |  |
| `HCS_STATUS` | String |  | len 8000 |
| `HCS_NEIGHBORHOOD` | String |  | len 8000 |
| `HCS_NON_ARPA_ARPA` | String | HCS_NON ARPA_ARPA | len 8000 |
| `HCS_NOTES` | String |  | len 8000 |
| `N_Parcel_ID` | String | N_Parcel ID | len 8000 |
| `N_Address` | String |  | len 8000 |
| `N_ZIP` | Integer |  |  |
| `N_Location_Type` | String | N_Location Type | len 8000 |
| `N_Category` | String |  | len 8000 |
| `N_Date` | DateOnly |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |
| `GlobalID` | GlobalID |  |  |
| `Shape__Area` | Double |  |  |
| `Shape__Length` | Double |  |  |

</details>

## Layer 3: ALL 2023 Div Housing and Inspections_08272024.csv

- **Records:** 66,884
- **Last edited:** 2024-09-13

| Field | Type | Alias | Notes |
|---|---|---|---|
| `HCS_PARCEL_ID` | String | HCS_PARCEL ID | len 8000 |
| `HCS_ADDRESS` | String |  | len 8000 |
| `HCS_GRADE` | String |  | len 8000 |
| `HCS_FPU` | String |  | len 8000 |
| `HCS_STATUS` | String |  | len 8000 |
| `HCS_NEIGHBORHOOD` | String |  | len 8000 |
| `HCS_NON_ARPA_ARPA` | String | HCS_NON ARPA_ARPA | len 8000 |
| `HCS_NOTES` | String |  | len 8000 |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

## Layer 4: NuisanceParcels_06242024.csv

- **Records:** 1,855
- **Last edited:** 2024-09-13

| Field | Type | Alias | Notes |
|---|---|---|---|
| `N_Parcel_ID` | String | N_Parcel ID | len 8000 |
| `N_Address` | String |  | len 8000 |
| `N_ZIP` | String |  | len 8000 |
| `N_Location_Type` | String | N_Location Type | len 8000 |
| `N_Category` | String |  | len 8000 |
| `N_Date` | DateOnly |  |  |

<details><summary>System/geometry fields</summary>

| Field | Type | Alias | Notes |
|---|---|---|---|
| `OBJECTID` | OID |  |  |

</details>

