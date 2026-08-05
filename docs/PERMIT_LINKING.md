# Permits: two sources, and how they relate

Dayton permit data exists in two places that do not overlap the way you would expect.
This documents what each holds, how fresh it is, how far they link, and — the part that
matters most — **why the link fails for half the permit types.**

Measured 2026-08-04. Linker: [`scripts/link_permits.py`](../scripts/link_permits.py).

---

## The two sources

| | **Accela Citizen Access** | **County CAMA `PERMIT.DAT`** |
|---|---|---|
| Role | The City's live permitting system | The Auditor's downstream copy |
| Freshness | **Live** — permits dated today | **Monthly**, cut 2026-06-30 |
| Coverage | 49 record types, all trades | Only permits bearing on assessed value |
| Volume | 4,852 (2026 H1) | 251,570 (1960–2026) |
| Parcel id | ✗ none | ✓ `PARID` |
| Valuation | ✗ not in the results grid | ~ `AMOUNT`, sparsely populated |
| Access | HTML search portal, scraped | Bulk fixed-width download |

Accela is the system of record. Nothing in the Accela extract postdates CAMA's cut, so
the ~5-week gap is entirely CAMA's publication cycle, not a data problem.

---

## They use the same permit numbers, written differently

```
CAMA    MECR26-0135        TYPE + R/C + YY   + SEQ
Accela  MEC2026R-00135     TYPE + YYYY + R/C + SEQ
```

Same four components, different order and zero-padding. Normalizing both to
`(type, R|C, 2-digit year, sequence)` raises the match rate from **6% to 43%** of
normalizable records (36% of all Accela records, which include licences and
registrations that carry no permit number at all).

One code differs: CAMA writes electrical permits as `ELE*`, Accela as `ELC`. That single
alias is handled in `TYPE_ALIAS`. `BLD`, `MEC`, `GAS` and `WRK` share a base code.

---

## Match rate by type — and what the zeros mean

| Type | Accela | Matched | Rate |
|---|---|---|---|
| Wrecking | 130 | 113 | **87%** |
| Mechanical | 628 | 519 | **83%** |
| Building | 417 | 339 | **81%** |
| Electrical | 876 | 667 | **76%** |
| Gas | 675 | 125 | 18% |
| Plumbing | 689 | 0 | **0%** |
| Water | 337 | 0 | **0%** |
| Sewer | 182 | 0 | **0%** |
| Fire alarm | 63 | 0 | **0%** |
| Fire sprinkler | 58 | 0 | **0%** |
| Zoning-only | 46 | 0 | **0%** |

⚠️ **The zeros are not a matching failure.** Those permits are absent from CAMA entirely.
The Auditor records permits that bear on assessed value; plumbing, water, sewer,
fire-protection and zoning-only work does not, so it never enters their system. No
improvement to the normalizer will recover them.

This is worth stating plainly because the obvious reaction to "0% match" is to keep
tuning the join. There is nothing to join to.

---

## What the link buys you

On the 1,763 matched records:

- **A parcel id on every one** — no address matching, no extra HTTP requests, no
  geocoding. This is the cheapest parcel join available anywhere in this inventory.
- A valuation on **265** of them. `AMOUNT` is zero or blank on the rest.
- The County's `WHY` category (`ALT`, `ADDN`, `FIRE REPR`, `DEMO`…), which is a coarser
  but independent classification of the work.

Worked example:

```
Accela  BLD2026C-00001   05 Jan 2026   1 WYOMING ST, DAYTON OH 45409
  -> CAMA parcel R72 17627 0003   amount 1,280,000   why 'ALT'
```

---

## The other route: Accela record detail pages

Every Accela result row carries a `record_details_link` to a `CapDetail.aspx` page. That
page holds fields the results grid does not:

```
Record Status:  Issued
Work Location:  321 NASSAU ST, DAYTON OH 45410-1930
DISTRICT: 13    FPU: 520 - TWO FAMILY DWELLING, PLATTED LOT    ZONING: B-2
Tabs: Record Details · Processing Status · Related Records ·
      Attachments · Inspections · Payments · Fees · Conditions
```

**Record status**, **structure type** and **zoning** are all absent from the grid. `FPU`
uses the same code set as the Housing Condition Survey's `FPU` field, so it joins cleanly
to condition data.

Cost: one extra request per record. For a 2026 H1 sweep that is ~4,850 additional hits on
a live permitting system.

---

## Recommended approach

**Link first, then follow detail links selectively.**

1. Run `link_permits.py`. It is free — no requests — and resolves parcel ids for the
   ~36% of records that CAMA carries, including demolitions and structural work.
2. Follow `record_details_link` only for records the link could not reach. That is
   ~3,100 requests instead of ~4,850, and it targets exactly the types where the detail
   page is the *only* option.
3. For anything still needing a parcel id, fall back to the
   [address→parcel bridge](../dictionaries/address-parcel-bridge.md).

Use CAMA when you need **valuation history or deep time depth** (1960–2026). Use Accela
when you need **current activity or the full range of trades**. They are not substitutes
and their counts should never be summed.

---

## Usage

```bash
python3 scripts/link_permits.py \
    data/raw/accela_permits_2026h1.json \
    PERMIT.DAT \
    data/raw/cama_spec.json \
    data/raw/accela_permits_linked.json 2026
```

`PERMIT.DAT` comes from the monthly CAMA archive — see
[`dictionaries/mc-cama.md`](../dictionaries/mc-cama.md) for extraction. Output adds
`parcel`, `cama_amount`, `cama_why`, `match_key` and `linked` to every Accela record, and
reports per-type rates so a future drop in match quality is visible rather than silent.

---

## Caveats

**CAMA has bad permit dates.** Filtering 2025+ surfaces a permit dated **2045**. Validate
date ranges before aggregating.

**CAMA mixes numbering conventions across eras.** Older records use forms like `17750-B`
and `MEC19-01818` that the normalizer returns `None` for. This is fine for recent years —
where the link is useful — but a historical backfill would need era-specific parsing.

**Accela record numbers are not all permits.** Licences and registrations (`011430`) carry
plain sequence numbers with no type or year, so they normalize to `None` and never match.
They are legitimately not permits.

**Match rate should be monitored, not assumed.** `by_type` in the output exists so that a
change in either system's numbering shows up as a rate drop rather than silently missing
records.
