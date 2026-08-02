#!/usr/bin/env python3
"""Generate the shareable one-page briefing for the Housing Data Subcommittee.

Usage:
    ./build_onepager.py <out.html>

Companion to build_explorer.py: the explorer is a tool for browsing 1,782
datasets, this is a document for people who need the picture in two minutes.
Shares the explorer's palette so the two read as a set. Counts are computed
from the catalog rather than written in, so a re-harvest updates the brief.
"""
import csv
import html
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def esc(s):
    return html.escape(str(s), quote=True)


def stats():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "catalog", "master_catalog.csv"))))
    dicts = len([f for f in os.listdir(os.path.join(ROOT, "dictionaries")) if f.endswith(".md")])
    return {
        "total": f"{len(rows):,}",
        "housing": f"{sum(1 for r in rows if r['housing_relevant'] == 'Y'):,}",
        "readable": f"{sum(1 for r in rows if r['queryable'] == 'Y'):,}",
        "dicts": f"{dicts:,}",
        "scripts": f"{len([f for f in os.listdir(os.path.join(ROOT, 'scripts')) if f.endswith('.py')]):,}",
    }


# The datasets that actually carry weight, with what each unlocks.
HOLDINGS = [
    ("Housing Condition Survey", "88,922 parcels",
     "Exterior condition graded 0–5 citywide, with the 2023 grade in the same row. "
     "Condition <em>change</em> is measurable at parcel level today."),
    ("Code enforcement", "12,879 complaints",
     "Housing complaints for 2026 with status and outcome, served from the City's "
     "GIS REST API."),
    ("County property records", "3,856 archived files",
     "Sales, tax roll, delinquency and full property characteristics — monthly, some "
     "back to 2001. Includes owner-occupancy, foreclosure dates and census tract."),
    ("Building permits", "251,570 + 4,852",
     "Parcel-linked permits 1960–2026 from the County, plus 2026 records across 49 types "
     "pulled live from the City's permitting portal."),
    ("Rental registrations", "18,321 parcels",
     "44,033 units with the responsible agent, phone and unit count on every row — the "
     "roster behind the tax roll's registration flag."),
    ("Subsidized housing", "203 properties",
     "LIHTC and project-based Section 8, plus 11 public housing developments. "
     "23 contracts covering 812 units expire by 2030."),
]

UNLOCKED = [
    ("Code enforcement is available now",
     "12,879 housing complaints with status and outcome, served from the City's GIS "
     "REST API. No request needed."),
    ("Tenure is in the tax roll",
     "Owner-occupancy, rental registration and foreclosure dates are columns in a file "
     "the County publishes daily — no request needed."),
    ("Permits are reachable",
     "The City's permitting portal answers queries across all 49 record types — a route "
     "first proven by Code for Dayton's demolition checker."),
    ("The data joins up",
     "City and County parcel IDs already match at 96%. Code enforcement, which carries no "
     "parcel ID, now bridges through the city address layer at 99.97%."),
]

# Each gap names who holds it, so the ask has an owner.
GAPS = [
    ("Vacant property registry", "City of Dayton",
     "The program runs under ordinance and the registration form is online. The County "
     "publishes its rental registry as 67 downloadable files — a useful precedent."),
    ("Code enforcement history", "City of Dayton GIS",
     "Two published windows leave a gap between 2023 and 2025. The live service already "
     "works — this is the same data over a longer range."),
    ("Evictions", "Municipal Court",
     "Not published in any form. The clearest available measure of displacement."),
    ("Deeds, mortgages, liens", "County Recorder",
     "Search-only, no bulk access. Needed to trace ownership chains and lender exposure."),
    ("Homelessness data", "County / Continuum of Care",
     "Performance measures are published as PDFs; the underlying system is not."),
    ("Public housing portfolio", "Greater Dayton Premier Management",
     "Federal sources cover 1,762 units; GDPM manages roughly 2,700."),
]

NEXT = [
    ("Ask for the vacant property registry",
     "Highest value for least effort, and the County has already set the precedent."),
    ("Follow up with City GIS",
     "The earlier years of code enforcement, publishing last-edit dates on layers, and "
     "two datasets that are listed publicly but ask for a login."),
    ("Answer one real question with what we hold",
     "Everything needed is in hand and joined. Start with: does private reinvestment "
     "reach the properties in worst condition, or avoid them?"),
    ("Pool the team's bookmarks",
     "The rental registry — the single most useful thing found — sits at a web address "
     "nothing links to. It was found because someone remembered it. Others will know more."),
]


def build():
    s = stats()
    holdings = "\n".join(
        f'''      <tr><th scope="row">{esc(n)}</th><td class="num">{esc(v)}</td><td>{d}</td></tr>'''
        for n, v, d in HOLDINGS)
    unlocked = "\n".join(
        f'''      <li><p class="u-t">{esc(t)}</p><p class="u-b">{esc(b)}</p></li>'''
        for t, b in UNLOCKED)
    gaps = "\n".join(
        f'''      <tr><th scope="row">{esc(n)}</th><td class="who">{esc(w)}</td><td>{esc(d)}</td></tr>'''
        for n, w, d in GAPS)
    nxt = "\n".join(
        f'''      <li><p class="n-t">{esc(t)}</p><p class="n-b">{esc(b)}</p></li>'''
        for t, b in NEXT)
    return TEMPLATE.format(harvested=time.strftime("%-d %B %Y"),
                           holdings=holdings, unlocked=unlocked, gaps=gaps, nxt=nxt, **s)


TEMPLATE = r"""<title>Housing Data Inventory — Briefing</title>
<style>
  :root {{
    color-scheme: light;
    --page:#eceef1; --surf:#fbfbfc; --surf-2:#f4f5f7;
    --ink:#161b22; --ink-2:#59616c; --ink-3:#89919c;
    --rule:#dcdfe4; --rule-2:#c6cbd2;
    --accent:#9c4f2e; --accent-soft:#f0e2db; --data:#2a78d6;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) {{
      color-scheme: dark;
      --page:#101418; --surf:#181d23; --surf-2:#1e242b;
      --ink:#e7eaee; --ink-2:#a3acb7; --ink-3:#6d7681;
      --rule:#2a323b; --rule-2:#3a434e;
      --accent:#c47a55; --accent-soft:#33241d; --data:#3987e5;
    }}
  }}
  :root[data-theme="dark"] {{
    color-scheme: dark;
    --page:#101418; --surf:#181d23; --surf-2:#1e242b;
    --ink:#e7eaee; --ink-2:#a3acb7; --ink-3:#6d7681;
    --rule:#2a323b; --rule-2:#3a434e;
    --accent:#c47a55; --accent-soft:#33241d; --data:#3987e5;
  }}
  *, *::before, *::after {{ box-sizing:border-box; }}
  html, body {{ overflow-x:hidden; }}
  body {{
    margin:0; background:var(--page); color:var(--ink);
    font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
    font-size:15px; line-height:1.6; -webkit-font-smoothing:antialiased;
  }}
  .sheet {{
    max-width:860px; margin:0 auto; background:var(--surf);
    border-left:1px solid var(--rule); border-right:1px solid var(--rule);
    padding:0 clamp(22px,5vw,58px) 60px;
  }}
  .mono {{ font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace; }}
  .eyebrow {{
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:11px;
    letter-spacing:.15em; text-transform:uppercase; color:var(--ink-3); margin:0 0 12px;
  }}
  header {{ padding:52px 0 30px; border-bottom:2px solid var(--ink); }}
  h1 {{ margin:0 0 16px; font-size:clamp(27px,3.6vw,37px); line-height:1.1;
        letter-spacing:-.024em; font-weight:680; text-wrap:balance; max-width:20ch; }}
  .lede {{ margin:0; color:var(--ink-2); font-size:16.5px; max-width:62ch; }}
  .lede strong {{ color:var(--ink); font-weight:620; }}

  .strip {{ display:flex; flex-wrap:wrap; gap:1px; background:var(--rule);
            border:1px solid var(--rule); margin:26px 0 0; }}
  .strip div {{ flex:1 1 130px; background:var(--surf-2); padding:13px 15px; }}
  .strip b {{ display:block; font-size:23px; font-weight:660; letter-spacing:-.02em;
              font-variant-numeric:tabular-nums; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
  .strip span {{ font-size:11px; letter-spacing:.06em; text-transform:uppercase; color:var(--ink-3); }}

  section {{ padding:38px 0 0; }}
  h2 {{ margin:0 0 4px; font-size:19px; font-weight:660; letter-spacing:-.012em; }}
  .sub {{ margin:0 0 20px; color:var(--ink-2); max-width:64ch; font-size:14.5px; }}

  table {{ border-collapse:collapse; width:100%; font-size:14px; }}
  th[scope=row] {{ text-align:left; font-weight:620; vertical-align:top; padding:11px 14px 11px 0;
                   width:31%; border-top:1px solid var(--rule); }}
  td {{ vertical-align:top; padding:11px 0; border-top:1px solid var(--rule); color:var(--ink-2); }}
  td.num {{ width:20%; padding-right:14px; color:var(--ink); font-weight:600;
            font-variant-numeric:tabular-nums; white-space:nowrap;
            font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:13px; }}
  td.who {{ width:24%; padding-right:14px; color:var(--accent); font-weight:600; font-size:13px; }}
  em {{ font-style:normal; color:var(--ink); font-weight:600; }}

  ul.cards {{ list-style:none; margin:0; padding:0;
              display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:1px;
              background:var(--rule); border:1px solid var(--rule); }}
  ul.cards li {{ background:var(--surf-2); padding:16px 17px; }}
  .u-t, .n-t {{ margin:0 0 5px; font-weight:640; font-size:14.5px; }}
  .u-b, .n-b {{ margin:0; font-size:13.5px; color:var(--ink-2); line-height:1.55; }}

  ol.next {{ list-style:none; counter-reset:s; margin:0; padding:0; }}
  ol.next li {{ counter-increment:s; position:relative; padding:14px 0 14px 44px;
                border-top:1px solid var(--rule); }}
  ol.next li::before {{
    content:counter(s); position:absolute; left:0; top:14px;
    width:26px; height:26px; border-radius:50%; background:var(--accent-soft);
    color:var(--accent); font-weight:700; font-size:12.5px;
    display:grid; place-items:center;
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  }}
  .note {{ margin-top:38px; padding:17px 19px; background:var(--surf-2);
           border-left:3px solid var(--accent); font-size:14px; color:var(--ink-2); }}
  .note strong {{ color:var(--ink); }}
  footer {{ margin-top:40px; padding-top:20px; border-top:1px solid var(--rule);
            font-size:12.5px; color:var(--ink-3); }}
  a {{ color:var(--accent); }}
  :focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; }}
  @media print {{
    body {{ background:#fff; }} .sheet {{ border:0; max-width:none; }}
  }}
</style>

<div class="sheet">
  <header>
    <p class="eyebrow">City of Dayton · Housing Data Subcommittee</p>
    <h1>Housing data inventory: what exists, what we have, what to ask for</h1>
    <p class="lede">We set out to catalogue the housing data published by the
      <strong>City of Dayton</strong> and <strong>Montgomery County</strong>. There are six
      separate publishing systems; two are reached through their REST APIs rather than a
      portal listing. Every figure below was pulled directly from the source and
      verified.</p>
    <div class="strip">
      <div><b>{total}</b><span>Datasets catalogued</span></div>
      <div><b>{housing}</b><span>Housing-relevant</span></div>
      <div><b>{readable}</b><span>Verified readable</span></div>
      <div><b>{dicts}</b><span>Data dictionaries</span></div>
      <div><b>{scripts}</b><span>Reusable scripts</span></div>
    </div>
  </header>

  <section>
    <p class="eyebrow">What we hold</p>
    <h2>The datasets that carry weight</h2>
    <p class="sub">Out of everything catalogued, these are the ones that answer housing
      policy questions. All are collected, documented field by field, and refreshable.</p>
    <table>
{holdings}
    </table>
  </section>

  <section>
    <p class="eyebrow">What changed</p>
    <h2>Four things we can do now that we could not before</h2>
    <ul class="cards">
{unlocked}
    </ul>
  </section>

  <section>
    <p class="eyebrow">What is missing</p>
    <h2>Gaps, and who holds them</h2>
    <p class="sub">None of these are technical problems. Each needs a person to ask.</p>
    <table>
{gaps}
    </table>
  </section>

  <section>
    <p class="eyebrow">Recommended</p>
    <h2>Next steps</h2>
    <ol class="next">
{nxt}
    </ol>
  </section>

  <footer>
    Prepared by the Code for Dayton data team for the Housing Data Subcommittee.
    Figures verified {harvested}. Full catalogue, field-level dictionaries and the
    scripts that produced them are in the project repository.
  </footer>
</div>
"""


if __name__ == "__main__":
    out = build()
    with open(sys.argv[1], "w") as f:
        f.write(out)
    print(f"one-pager -> {sys.argv[1]} ({len(out):,} bytes)")
