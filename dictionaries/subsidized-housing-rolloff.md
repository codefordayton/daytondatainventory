# Subsidized Housing & Affordability Roll-Off

> The priority theme with no local source. There is no City or County dataset of
> income-restricted units or expiration dates — this has to be assembled from federal
> and state sources. Three are now in hand; NHPD still requires registration.

Harvested 2026-08-01. Scripts: [`harvest_lihtc.py`](../scripts/harvest_lihtc.py),
[`harvest_hud_assisted.py`](../scripts/harvest_hud_assisted.py).

---

## ⚠️ Read this before using any number below

**"Roll-off date" is not one thing.** Three different clocks can end affordability, and
a single property often sits on more than one:

| Clock | Ends when | Source with real dates |
|---|---|---|
| LIHTC initial compliance | 15 yrs after placed in service | derived only |
| LIHTC extended use | ≥30 yrs after PIS (per recorded agreement) | **OHFA — obtained, see §3** |
| Project-based Section 8 | contract expiration date | **HUD (published)** |

**HUD's LIHTC database contains no expiration field** — only `YR_PIS` and `YR_ALLOC`.
Any LIHTC roll-off year in this repository is **derived from statute**, not published.

**Do not add LIHTC units to Section 8 units.** 15 Montgomery County properties appear in
both datasets under matching names; the true overlap is likely higher, since this was a
name match. Double-counting is the most likely error with these sources.

---

## 1. LIHTC properties — HUD LIHTC Database *(derived dates)*

**120 properties · 8,696 total units · 8,412 low-income units** in Montgomery County.
**88 properties / 5,762 LI units are in Dayton.**

- Layer: `https://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services/LIHTC/FeatureServer/0`
- 121 fields · open REST, no auth · filter `PROJ_ST='OH' AND CURCNTY_NM LIKE '%Montgomery%'`
- Raw: `data/raw/lihtc_montgomery_oh.json`

Key fields: `PROJECT`, `PROJ_ADD`, `PROJ_CTY`, `YR_PIS`, `YR_ALLOC`, `N_UNITS`,
`LI_UNITS`, `N_0BR`–`N_4BR`, `TYPE` (new/rehab), `CREDIT`, `BOND`, `TRGT_POP`,
`TRGT_ELD`, `TRGT_DIS`, `TRGT_HML`, `RENTASSIST`, `INC_CEIL`, `ALLOCAMT`, `TRACT2KX`.

### Derived affordability horizon

Method (matches NHPD's published methodology — they also assume PIS + 30):
15-year compliance (IRC §42(i)(1)) + 15-year minimum extended use (§42(h)(6)).
Allocations before 1990 predate the extended-use requirement and are flagged separately.

| Estimated extended-use end | Properties | LI units |
|---|---|---|
| already past (≤2026) | 42 | 2,175 |
| 2027–2030 | 12 | 1,586 |
| 2031–2035 | 21 | 1,654 |
| 2036–2040 | 22 | 1,894 |
| 2041+ | 22 | 1,103 |

19 properties / 832 LI units are pre-1990 allocations with no extended-use requirement.

**Largest properties with estimated exits in the next decade:**

| Est. exit | LI units | Property | City |
|---|---|---|---|
| 2029 | 350 | Country Woods Apts | Dayton |
| 2033 | 250 | Bella Vista Homes | Dayton |
| 2035 | 230 | The Biltmore Apts | Dayton |
| 2036 | 182 | Northcrest Gardens Apts | Dayton |
| 2027 | 176 | Lyons Gate Apt Homes | Miamisburg |
| 2036 | 171 | Cambridge Commons | West Carrollton |
| 2033 | 165 | Kettering Square Apts | Kettering |
| 2030 | 156 | Creekside Villas | Moraine |
| 2036 | 154 | Summit Square Apts | Dayton |
| 2029 | 144 | Hoover Place Apartments | Dayton |
| 2028 | 144 | Fieldstone Apts | Trotwood |

✅ **Now validated against OHFA (§3): 91% of matched projects agree within ±1 year.**
The derivation is sound in aggregate. But it misses **re-syndications** badly — Mad River
Manor and Jaycee Towers are 47–52 years off — because a new allocation is invisible in the
original placed-in-service year. **Use §3 for any named property.**

⚠️ The "42 properties already past" figure has now been checked against OHFA (§3):
**39 are absent from OHFA's active list** (consistent with genuinely exiting), but
**2 were re-syndicated and run to 2050 and 2056**. Never cite this bucket per-property.

⚠️ One record (`WINDCLIFF VILLAGE PHASE II`) has `YR_PIS = '8888'` — a placeholder. It is
excluded from the horizon table.

---

## 2. Project-based Section 8 — HUD Multifamily Assisted *(published dates)*

**83 properties · 6,025 total units · 5,586 assisted units.**
**57 properties / 4,239 assisted units in Dayton.** 81 of 83 have active assistance.

- Layer: `https://services.arcgis.com/VTyQ9soqVukalItT/arcgis/rest/services/Multifamily_Properties_Assisted/FeatureServer/0`
- 284 fields · open REST, no auth · refreshed monthly by HUD
- Raw: `data/raw/hud_assisted_montgomery_oh.json`

**`EXPIRATION_DATE1` / `EXPIRATION_DATE2` are real published contract expiration dates** —
the only genuine expiration dates available without registration. Format `DD-MON-YY`.
Paired with `CONTRACT1`/`CONTRACT2` and `UNITS1`/`UNITS2`.

| Contract expiration | Contracts | Units |
|---|---|---|
| ≤2026 | 3 | 58 |
| **2027–2030** | **20** | **754** |
| 2031–2035 | 22 | 1,998 |
| 2036–2040 | 20 | 1,510 |
| 2041–2045 | 15 | 1,209 |

80 of 83 properties carry an expiration date; 4 have none (7 assisted units).

**Expiring on or before 2030 — the actionable near-term list:**

| Date | Units | Property | City |
|---|---|---|---|
| 2026-06-30 | 5 | Outreach II / Arbor House | Dayton |
| 2026-08-31 | 8 | Briar Place | Dayton |
| 2026-08-31 | 45 | Siena Springs | Dayton |
| 2027-01-31 | 20 | St. Mark Community | Dayton |
| 2027-03-31 | 21 | Canaan Manor | Dayton |
| 2027-03-31 | 8 | Eastway Home | Kettering |
| 2027-05-31 | 15 | Spring Valley Apartments | Miamisburg |
| 2027-12-31 | 23 | Kettering Park II | Kettering |
| 2028-01-31 | 13 | Eastway Quinby Lane Apts | Dayton |
| 2028-09-30 | 24 | Acorn Walk | Kettering |
| 2028-11-30 | 24 | Riverside Park | Dayton |
| 2029-01-31 | 35 | Siena Springs II | Dayton |
| 2029-04-30 | 40 | Lyons Place II | Dayton |
| 2029-05-31 | 50 | Parkview Place | Centerville |
| 2029-08-31 | 35 | Woodsview Place | Huber Heights |
| **2029-09-22** | **232** | **Chevy Chase Park** | Centerville |
| 2029-09-29 | 26 | Lakeview Cooperative Estates B | Dayton |
| 2029-09-29 | 28 | Lakeview Cooperative Estates A | Dayton |
| 2029-09-29 | 36 | Lakeview Cooperative Estates C | Dayton |
| 2029-11-30 | 23 | Birchwood Place | Kettering |
| 2029-11-30 | 23 | Kettering Park Manor | Kettering |
| 2030-01-31 | 23 | Germantown Park | Germantown |
| 2030-02-28 | 55 | Lyons Place | Dayton |

⚠️ **Contract expiration ≠ units lost.** Most Section 8 contracts are renewed, often for
short terms, so expirations recur. Treat this as an engagement calendar, not a loss
forecast. NHPD's `S8_1_RenewalStatus` field tracks renewal status.

---

## 3. OHFA — ⭐ OBTAINED, and it corrects section 1

**104 Montgomery County projects · 8,861 units** (statewide: 1,504 projects / 113,265 units).
Downloaded 2026-08-02 from the Tableau dashboard.
Raw: `data/raw/ohfa/data.csv` · parsed: `data/raw/ohfa_montgomery_validated.json`
· parser: [`scripts/parse_ohfa.py`](../scripts/parse_ohfa.py)

Columns: `Project Number`, `Project Name`, `County`, `Region`, `Appalachia`,
`Population`, `Total Units`, `Est. Program Exit`.

⚠️ **Even OHFA labels it "Est. Program Exit."** The allocating agency is publishing an
estimate, not a legal date. For a binding term you still need the recorded restrictive
covenant on the specific property.

### Montgomery County exits by window

| Window | Projects | Units |
|---|---|---|
| ≤2026 | 3 | 324 |
| **2027–2030** | **8** | **922** |
| 2031–2035 | 25 | 1,994 |
| 2036–2040 | 21 | 1,821 |
| 2041+ | 47 | 3,800 |

Population served: General Occupancy 62 · Senior 34 · Service Enriched 8.
Exits run out to **2065** — far beyond any PIS+30 horizon.

### How it compares to the derived dates in section 1

68 projects matched by strict name (phase numerals preserved — `Foo II` ≠ `Foo`):

- **91% agree within ±1 year.** The PIS + 30 derivation is sound for the typical property.
- 31 cases OHFA is 1 year earlier, 29 exact, 8 later — the −1 cluster is a counting
  convention, not a substantive disagreement.
- **The exceptions are large and matter.** Re-syndicated properties get a new allocation
  that HUD's original placed-in-service year cannot see:

| Project | PIS | Derived | OHFA | Δ |
|---|---|---|---|---|
| Mad River Manor | 1989 | 2004 | **2056** | +52 |
| Jaycee Towers | 1988 | 2003 | **2050** | +47 |
| Summit Square Apts | 2006 | 2036 | **2052** | +16 |
| Riverside Commons II | 1999 | 2029 | 2038 | +9 |
| Courtyards of Kettering | 2000 | 2030 | 2035 | +5 |

### The correction to "42 properties already past"

Section 1 flagged 42 properties / 2,175 LI units as past their derived 30-year minimum.
Checked against OHFA's active list:

- **39 properties (1,766 LI units) do not appear in OHFA's active projects at all** —
  consistent with having genuinely left the program.
- **2 properties (278 LI units) were re-syndicated and run decades longer**:
  Jaycee Towers (204 LI units) to **2050**, Mad River Manor (74) to **2056**.

So the "already past" bucket was broadly right in direction but wrong on specific
properties — exactly the reason not to name individual properties off derived dates.

### Other OHFA resources

- **Map of Multifamily Rental Properties** —
  `https://analytics.das.ohio.gov/t/OHFAPUB/views/MultifamilyProjects/MultifamilyProjects`
  All OHFA-funded properties, filterable by county. Not yet pulled.

⚠️ **Not scriptable.** Appending `.csv` to the view URL returns only the dashboard's first
sheet — a filter control (`Appalachia: Yes/No`), 21 bytes. The `.pdf` renders charts, not
tables. The real export requires the dashboard's own download control in a browser
(Crosstab → CSV). The file arrives **UTF-16, TAB-delimited, despite the `.csv` extension**.

- **Qualified Contract Listing** — `https://ohiohome.org/compliance/propertysales.aspx`
  Properties seeking early exit from affordability. **Currently empty**, which is itself
  a useful finding: no Montgomery County property is presently trying to exit early.
- OHFA LIHTC program report: `https://ohiohome.org/research/documents/LIHTC-Report.pdf`
- Contact: (614) 466-7970

---

## 4. NHPD — best cross-program inventory *(free registration required)*

`https://preservationdatabase.org` — the National Housing Preservation Database
(PAHRC + NLIHC). Address-level inventory of federally assisted rental housing combining
LIHTC, Section 8, Section 202/811, USDA 515, HOME, and Housing Trust Fund into **one
record per property with subsidy end dates**, plus inspection scores, owner type, and
`S8_1_RenewalStatus`.

⚠️ **NHPD will NOT give you better LIHTC end dates.** Per its own documentation:
*"LIHTC subsidies are now automatically assumed to have a subsidy end date 30 years past
the year the tax credit was placed in service."* That is **the same derivation used in
section 1** — NHPD would reproduce those numbers, not validate them. Only OHFA's recorded
agreements can do that.

**What NHPD does add, which nothing else here provides:**
- **One deduplicated record per property across programs** — directly solves the
  double-counting problem between sections 1 and 2.
- **`S8_1_RenewalStatus`** — actual renewal status of each Section 8 contract, which turns
  the expiration calendar in section 2 into a real risk assessment.
- **Other subsidy programs** absent from both sections above: Section 202, Section 811,
  USDA 515, HOME, and the National Housing Trust Fund.
- Inspection scores and owner type (for/non-profit, PHA).

Requires a **free account** — not created here, since that is the committee's call.
Registration: `https://preservationdatabase.org/register-as-a-new-user/`
· Data dictionary: `https://preservationdatabase.org/wp-content/uploads/2025/02/Data-Dictionary.pdf`

## Which source for which question

| Question | Go to |
|---|---|
| When does a specific LIHTC property's affordability actually end? | **OHFA** (recorded agreements) |
| How many subsidized units are there, without double-counting? | **NHPD** |
| Will this Section 8 contract be renewed? | **NHPD** (`S8_1_RenewalStatus`) |
| What Section 8 contracts expire and when? | **HUD Multifamily** (already pulled, section 2) |
| Rough screening horizon across all LIHTC? | **section 1 above** — no further source needed |
| Section 202/811, USDA 515, HOME, HTF units? | **NHPD** |

Neither OHFA nor NHPD dominates. OHFA is authoritative for LIHTC *dates*; NHPD is
authoritative for *inventory and renewal status* across programs.

---

## Still missing

- **Greater Dayton Premier Management** (the PHA, formerly DMHA) — public housing and
  Housing Choice Voucher inventory. Not an open-data publisher; needs a direct request.
- **Local/non-federal restrictions** — units affordable via City HOME/CDBG agreements,
  land bank covenants, or NOAH (naturally occurring affordable housing) are in none of
  these datasets. The City's `HousingRequest_ExportFeature1` (376 projects) is the closest
  local proxy.
