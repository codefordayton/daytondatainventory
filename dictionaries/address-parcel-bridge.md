# Address → Parcel Bridge (code enforcement join)

> Built 2026-08-02. Joins Dayton code enforcement incidents — which carry no parcel id —
> to parcel-level data. **99.97% matched.** This was the last structural blocker to
> cross-system housing analysis.

Scripts: [`build_address_bridge.py`](../scripts/build_address_bridge.py) ·
[`harvest_accela.py`](../scripts/harvest_accela.py) ·
[`match_accela_parcels.py`](../scripts/match_accela_parcels.py)

---

## Why it was needed

Accela code enforcement incidents have `ADDRESS`, `ADDRKEY`, and street components — but
no parcel id. Everything else in the housing inventory keys on parcel. Without a bridge,
12,879 housing complaints could not be joined to condition, ownership, tenure, or tax
status.

## What made it easy

It turned out **not** to be a fuzzy address-matching problem. The City's
**`Dayton Used Address`** layer carries both `ADDRKEY` — the same integer key Accela uses —
and `TAXPINNO`, the county-format parcel id. So the primary join is an exact integer
lookup.

```
Accela.ADDRKEY  →  Dayton_Used_Address.ADDRKEY  →  TAXPINNO (= County PARID)
```

- Source: `https://maps.daytonohio.gov/gisservices/rest/services/Basemaps/Dayton_Used_Address/MapServer/0`
- **163,184 address records**, of which **163,052 (99.9%) carry a parcel id**
- 163,182 distinct `ADDRKEY` entries · 127,916 distinct normalized addresses

## Results

| Method | Incidents | Share |
|---|---|---|
| `ADDRKEY` exact key | 12,865 | 99.89% |
| normalized address fallback | 10 | 0.08% |
| **unmatched** | **4** | **0.03%** |

**12,875 of 12,879 incidents matched → 6,866 distinct parcels.**

The four failures are all high `ADDRKEY` values (299411, 299558, 299631, 234451) — new
addresses not yet in the address layer. Nothing was force-matched; a wrong parcel is worse
than a null.

**94.0% of the matched parcels (6,457 of 6,866) exist in the County taxroll.** The 409 that
don't are consistent with exempt, demolished, or recently split parcels — plausible for
code-enforcement targets, and worth a look rather than a fix.

## Validation: it produces a real signal

Joining matched incidents to the 2025 Housing Condition Survey grade
(6,496 of 6,866 parcels, 94.6%):

| HCS grade | Parcels citywide | With ≥1 complaint | **Complaint rate** |
|---|---|---|---|
| Vacant lot | 18,954 | 481 | **2.5%** |
| Sound | 30,822 | 1,863 | **6.0%** |
| Minor repair | 13,128 | 1,569 | **12.0%** |
| Major repair | 9,169 | 2,057 | **22.4%** |
| Rehabilitation | 902 | 430 | **47.7%** |
| Dilapidated | 181 | 96 | **53.0%** |

The complaint rate climbs monotonically with worsening condition — a dilapidated parcel is
**21× more likely** to carry a 2026 code complaint than a vacant lot, and ~9× more likely
than a sound one. Random or sloppy matching would produce a flat line. This is the
strongest available evidence that the join is sound.

## Repeat complaints

12,879 incidents across 6,866 parcels — **mean 1.88 per parcel** in six months.

| Complaints | Parcels |
|---|---|
| 1 | 4,347 |
| 2 | 1,287 |
| 3 | 501 |
| 4 | 283 |
| 5 | 159 |
| 6–10 | 391 |

**2,519 parcels (37%) have 2+ complaints.** The most-complained parcels carry 36 in six
months — 31 N Delmar Ave and 408 W Norman Ave. Repeat-complaint concentration is now
directly measurable and joinable to ownership via the taxroll.

## Usage

```bash
python3 scripts/build_address_bridge.py data/raw/address_bridge.json
python3 scripts/harvest_accela.py       data/raw/accela_incidents.json
python3 scripts/match_accela_parcels.py data/raw/accela_incidents.json \
        data/raw/address_bridge.json    data/raw/accela_parcel_matched.json
```

Output rows: `complaint_no`, `record_date`, `status`, `neighborhood`, `address`,
`addrkey`, `parcel`, `match_method`. Join `parcel` to County `PARCELID`/`PARID` or City
`PARCELID`.

## Gotchas

**Paging: `resultRecordCount` is silently capped.** The address service caps at 1,000 per
page. Requesting 2,000 returns 1,000, and a naive `len(features) < page_size` termination
test reads that full page as the last one — this initially produced a bridge with 1,000 of
163,184 records that looked successful. **Terminate on `exceededTransferLimit`**, not on
page length. Both harvesters here do.

**`KEY_PARCELID` and `K_PID` are not usable alternates** — blank in the HCS rows inspected.
`TAXPINNO` is the populated parcel id in the address layer; `PARCELID` in the HCS.

**Match method is recorded per row.** Filter on `match_method='addrkey'` if you need only
the highest-confidence joins; the 10 normalized-address matches are a rounding error either
way.

**Code enforcement is 2026 YTD only** (see `CAVEATS.md`), so complaint *rates* above are
six-month rates, not annual. Don't annualize without confirming the service's coverage.

**Parcels ≠ addresses.** Multi-unit buildings produce several addresses on one parcel, so
complaint counts per parcel aggregate across units. That is usually what you want for
owner-level analysis, but not for per-unit rates.
