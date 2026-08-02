# Housing Data Inventory — What We Have, and What It Unlocks
### A briefing for the Housing Data Subcommittee · August 2026

We set out to complete the **"inventory & assess current datasets"** deliverable. This is
a first read of what the **City of Dayton, Montgomery County, and MVRPC already publish**,
assembled so we can build on it rather than duplicate effort or file records requests for
things that are already open.

Everything here was obtained from the agencies' own public sources.

---

## What we can now answer (that we largely couldn't before)

- **Tenure & ownership, parcel by parcel, citywide.** The County's public tax roll flags
  owner-occupancy (≈135,900 owner-occupied vs. ≈118,800 not), rental registration (17,454
  parcels), homestead status, and — via owner vs. mailing address — absentee and
  multi-parcel (institutional) ownership. *This was assumed to require a records request;
  it's a public bulk file.*
- **Housing condition, and how it's changing.** The City's 2025 Housing Condition Survey
  grades **88,922 parcels** on a 0–5 scale and carries the **2023 grade in the same record**,
  so condition *change* is computable today, down to the individual parcel and street.
- **The distress pipeline.** Delinquency (≈13,600 parcels), foreclosure (≈1,070), housing
  code complaints (≈12,900 in 2026 so far, with status and outcome), and vacancy signals —
  all parcel-linked.
- **Housing production and loss.** The County's assessment extract holds **≈251,600
  building permits back to 1960** — including **≈9,500 demolition permits** — plus
  living-unit counts and dwelling condition ratings on the whole stock.
- **Affordability at risk.** No local agency publishes an income-restricted inventory, but
  the federal sources do: **≈120 LIHTC properties and ≈83 project-based Section 8
  properties** in the county, with **23 subsidized contracts (~800 units) expiring by 2030.**
- **Regional affordability & cost burden.** MVRPC's regional study gives owner/renter cost
  burden, rent bands, and tenure at the block-group level (Montgomery County: ~42% of
  renters cost-burdened vs. ~18% of owners) — the affordability layer the City's own data
  doesn't provide.

**The most important finding: it all connects.** These datasets **join at the parcel
level** (and everything ties to a census tract for ACS work). We validated it — code-complaint
rates climb straight up the condition scale, from ~2.5% on vacant lots to ~53% on dilapidated
structures, a 21× spread. That means condition, complaints, ownership, tenure, and distress
can be looked at *together*, not in silos.

---

## The backbone datasets (the short list)

| Dataset | Publisher | What it gives us |
|---|---|---|
| Housing Condition Survey 2025 (+2023) | City of Dayton | Parcel-level condition grades & change |
| Housing Code Enforcement (Accela) | City of Dayton | Live complaints, status, outcomes |
| County Tax Roll | Montgomery County | Tenure, ownership, delinquency, foreclosure, tract |
| County CAMA (assessment) extract | Montgomery County | Building permits, unit counts, condition, ~15-yr history |
| County Sales & Delinquent files | Montgomery County | Transfers, prices, distress leading indicators |
| Subsidized / LIHTC + Section 8 | HUD (federal) | Income-restricted inventory + affordability roll-off |
| MVRPC Regional Housing Study | MVRPC | Cost burden, rent bands, tenure by block group |
| City Housing Projects | City of Dayton | Funded projects by program, affordability & tenure |

*(In total we catalogued ~1,780 published datasets; **261 are housing-relevant.** The full
catalog and per-dataset dictionaries are available as a working reference.)*

---

## Read these caveats before quoting any numbers
- **Rental registration ≠ rental stock.** 17,454 *registered* parcels against ~118,800 that
  aren't owner-occupied — the gap is itself a policy finding, not a count of rentals.
- **LIHTC roll-off dates are derived** (placed-in-service + 30 years), not published; they
  need verification against the state (OHFA) and national (NHPD) sources.
- **The City Housing Projects layer is a one-time snapshot,** not a maintained feed — confirm
  cadence and ownership with the publisher before relying on it.
- **Some things aren't in any open portal** and still need direct requests — notably
  evictions (Municipal Court) and utility shutoffs. We've flagged the remaining gaps openly.

---

## What this is — and isn't
This is a **catalog of what these agencies already make public**, surfaced so the
subcommittee can move faster and avoid duplicate requests. Full credit to the City, County,
and MVRPC teams whose data this is. It is **not** a substitute for the partners who own and
steward these sources — they remain the experts on their own data; this is raw material for
the committee's decisions, offered to that end.

---

## The ask: help us prioritize
The inventory deliberately leaves the **priority** of each dataset **blank** — that's the
committee's judgment call, not something a catalog should decide. Proposed next step:

1. A short **data-team working session** to weight these against our deliverables (the
   housing dashboard, the policy/governance guide) and the questions other subcommittees
   are asking (e.g., Market Analysis's affordability-and-tenure inventory).
2. From that, a **prioritized shortlist** the committee stands behind — which becomes the
   backbone of the assessment deliverable and tells us where to point effort next.

The material is ready; what we need now is the committee's steer on what matters most.
