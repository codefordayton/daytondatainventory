# Source Register

Every portal found, how to get data out of it, and what state it's in.
Verified 2026-08-01.

---

## 1. City of Dayton — ArcGIS Online

- **Org:** `DaytonOhio` · org ID `3dDB2Kk6kuA2gIGw`
- **Portal:** https://daytonohio.maps.arcgis.com
- **Public items:** 1,271 (374 are Feature/Map Services)
- **Access:** fully open REST. No key, no auth, no rate limiting hit during harvest.

Enumerate everything:
```
https://www.arcgis.com/sharing/rest/search?q=orgid:3dDB2Kk6kuA2gIGw&f=json&num=100&start=1
```
Data services live on `https://services2.arcgis.com/3dDB2Kk6kuA2gIGw/arcgis/rest/services/`.

**Item mix:** 307 Feature Services, 245 Web Maps, 122 Dashboards, 114 Web Mapping Apps,
111 Images, 67 Forms, 67 Map Services, 39 Hub Pages, 25 StoryMaps, 14 Hub Sites.

**Most prolific publishers:** `Richard.Bailey@DaytonOhio.gov` (570 items — including the
Housing Condition Survey), `Frank.Boateng_DaytonOhio` (221), `emma.jewell` (123),
`Jennifer.Hanauer` (87). Useful to know who to ask about what.

### Hub sites (14)
| Site | URL |
|---|---|
| **Dayton Housing Condition Survey** | https://dayton-housing-condition-survey-DaytonOhio.hub.arcgis.com |
| Dayton Transparency Portal | https://dayton-transparency-portal-1-DaytonOhio.hub.arcgis.com |
| Dayton Recovery Plan (ARPA) | https://dayton-recovery-plan-daytonohio.hub.arcgis.com |
| Plan & Build Guidebook | https://zoning-daytonohio.hub.arcgis.com |
| Permitting Knowledge Center | https://city-of-dayton-zoning-administration-DaytonOhio.hub.arcgis.com |
| Dayton Forward (2040 plan) | https://dayton-forward-2040-daytonohio.hub.arcgis.com |
| AdaptDayton (zoning rewrite) | https://adaptdayton-DaytonOhio.hub.arcgis.com |
| Your Dollars Your Neighborhood | https://your-dollars-your-neighborhood-DaytonOhio.hub.arcgis.com |
| Sustainability Hub | https://sustainability-hub-DaytonOhio.hub.arcgis.com |
| Dayton Mediation Response Unit | https://dayton-mediation-response-unit-DaytonOhio.hub.arcgis.com |
| Adopt-A-Drain | https://adopt-a-storm-drain-daytonohio.hub.arcgis.com |
| Dept of Water — Capital Improvement | https://department-of-water-capital-improvement-projects3-DaytonOhio.hub.arcgis.com |
| Water Career Conference | https://water-career-conference-daytonohio.hub.arcgis.com |
| America 250 | https://america-250-dayton-ohio-DaytonOhio.hub.arcgis.com |

---

## 2. City of Dayton — on-premise ArcGIS Server

- **Root:** https://maps.daytonohio.gov/gisservices/rest/services
- **Version:** ArcGIS Server 11.4 · **352 services across 35 folders**
- **Access:** open REST, but **slower and less reliable** than the AGOL org — expect
  occasional 503s on heavy queries.

This is a **separate and larger catalog** than the ArcGIS Online org, and it's not
surfaced through any Hub site. It's where the operational data lives.

Notable folders: `Accela` + `Accela_UPDATES` (code enforcement), `BuildingServices`
(housing inspection areas), `OpenData` (police: arrests, calls for service, crimes,
officer-involved shootings, use of force), `Planning`, `PublicWorks` (36 services incl.
service requests, city-owned parcels), `Water` (63), `Environmental` (42), `Police` (34),
`Fire` (29), `LCRR` (lead service lines).

---

## 3. Montgomery County Auditor / Treasurer — bulk downloads

- **Index:** https://go.mcohio.org/applications/treasurer/search/filedownloads.cfm
- **9 datasets · 3,856 archived files** · plain HTTP, no auth
- Layout PDFs mirrored locally in `docs/mc_file_layouts/`

| Dataset | Code | Files | Coverage | Newest file |
|---|---|---|---|---|
| Taxroll | TR | 1,572 | 2019-03 → 2026-07 | 32.9 MB |
| Available Tax Refunds | RF | 1,589 | 2019-03 → 2026-07 | 15 KB |
| Weekly Sales | WS | 301 | 2011-01 → 2026-07 | 32 KB |
| Monthly Sales | MS | 110 | 2009-03 → 2026-07 | 121 KB |
| Street Light Districts | ST | 93 | 2010-04 → 2026-07 | 22.2 MB |
| Delinquent Files | DQ | 81 | 2005-01 → 2026-07 | 4.9 MB |
| CAMA Characteristics | CC | 76 | 2011-01 → 2026-06 | 125.7 MB |
| Yearly Sales | YS | 18 | 2001-12 → 2026-08 | 846 KB |
| Neighborhood Codes | NC | 16 | 2025-05 → 2026-08 | HTML |

URL pattern (verified working):
```
https://go.mcohio.org/applications/treasurer/search/data/Monthly/SALES_20260701_TO_20260731.zip
```
Listings are generated per type at `fdpopup.cfm?dtype=<CODE>`. See `CAVEATS.md` for the
HTML parsing trap.

**Related county tools:** MCRealEstate property search (https://www.mcrealestate.org),
conveyance/deed transfer search
(https://go.mcohio.org/applications/auditor/deed_transfer/index.cfm).

---

## 4. Montgomery County Auditor — GIS server

- **Root:** https://gis.mcohio.org/server/rest/services
- **Version:** ArcGIS Server 11.3 · 12 services
- Folders: `Imagery`, `TestData`, `Utilities`, `VantagePoints`

Key services: `TestData/mc_parcel_polygon` (parcel geometry, Feature + Map Server),
`VantagePoints/AUDGIS_PUBLIC` (12 layers), `AUDGIS_A1` (22), `AUDGIS_Advance` (21),
`AUDGIS_Dayton` (2), **`AUDGIS_VOTER` (5 layers — voter/precinct geography)**,
`MC_ProLocator` (geocoding service — useful for the address-matching problem).

Public viewer: https://gis.mcohio.org/VPCore/VP.html?config=aud

---

## 5. Montgomery County Board of Elections

- **Main:** https://www.montgomery.boe.ohio.gov
- **Forms & data:** https://www.montgomery.boe.ohio.gov/forms-and-information/

| Product | URL | Access |
|---|---|---|
| BOE shapefiles (precincts) | `/download/607/shape-files/13747/shapefile_board_of_elections.zip` | ✅ 200, 1.2 MB — **needs browser User-Agent** |
| Street Lists | https://lookup.boe.ohio.gov/vtrapp/montgomery/streetreport.aspx | Interactive form |
| Walk Lists / voter reports | https://lookup.boe.ohio.gov/vtrapp/montgomery/vtrreport.aspx | Interactive form |
| Absentee Download | https://lookup.boe.ohio.gov/vtrapp/montgomery/avreport.aspx | Interactive form |
| Ballot List Display | https://lookup.boe.ohio.gov/vtrapp/montgomery/ballotlist.aspx | Interactive form |
| Election results (precinct) | https://app.enhancedvoting.com/results/public/Montgomery-County-OH | ✅ 200 |
| Voter lookup | https://lookup.boe.ohio.gov/vtrapp/montgomery/vtrlookup.aspx | Per-voter |

**Ohio Secretary of State bulk voter file** (statewide, county extracts, incl. vote
history) — https://www6.ohiosos.gov/ords/f?p=VOTERFTP:HOME — is the canonical source
for registration + turnout, but **blocks scripted access (403)**. Download via browser.

⚠️ The BOE's "GIS Database Download" link (`mcauditor.org/downloads/gis_download_geodb.cfm`)
is **dead (404)**. Use source #4 instead.

---

## Not yet swept

- **Dayton Metro Library — Ohio Votes** (https://www.daytonmetrolibrary.org/ohiovotes/)
- **MVRPC** (regional planning; https://www.mvrpc.org/data-mapping/gis-resources) —
  regional housing/transportation data, and a statewide/county resource index
- **OGRIP / GeoOhio** (https://ogrip-geohio.opendata.arcgis.com/) — state GIS clearinghouse
- **DataOhio Portal** — state open data
- **Montgomery County CountyStat / dashboards** — performance data
- **Greater Dayton Premier Management** (public housing authority) — likely the biggest
  remaining gap for housing policy specifically; not an open-data publisher
- **HUD / Census (ACS, CHAS, LIHTC, AFFH)** — federal, authoritative for tenure,
  cost burden, and subsidized inventory
