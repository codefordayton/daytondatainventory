#!/usr/bin/env python3
"""Generate the browsable inventory explorer page from the catalog.

Usage:
    ./build_explorer.py <out.html>

Reads catalog/master_catalog.csv and the harvested findings, and emits a
self-contained page (no external assets — the artifact CSP blocks them).
"""
import csv
import html
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Headline findings, each traced to the dictionary that documents it.
FINDINGS = [
    ("Housing Condition Survey 2025", "88,922", "parcels graded 0–5, with the 2023 grade "
     "in the same row — parcel-level condition change is computable today.",
     "dayton-housing-condition-survey-parcels-2025"),
    ("Code enforcement", "12,879", "housing complaints, 2026 YTD, with status and outcome. "
     "Served from maps.daytonohio.gov via the REST API.",
     "address-parcel-bridge"),
    ("County bulk archive", "3,856", "files of sales, tax roll, delinquency and full CAMA "
     "property characteristics — some back to 2001.", "mc-taxroll"),
    ("Building permits", "251,570", "parcel-linked permits, 1960–2026, inside the CAMA "
     "extract. $20.0B of declared valuation.", "mc-cama"),
    ("Subsidized housing", "203", "properties across LIHTC and project-based Section 8. "
     "23 contracts covering 812 units expire by 2030.", "subsidized-housing-rolloff"),
    ("Address → parcel bridge", "99.97%", "of code enforcement incidents joined to a parcel, "
     "clearing the last structural blocker to cross-system analysis.", "address-parcel-bridge"),
    ("Rental registrations", "18,321", "registered rental parcels covering 44,033 units, with "
     "the responsible agent, phone and unit count on every row.", "rental-registrations"),
    ("City permits", "4,852", "permit records across 49 types for 2026 H1, pulled from the "
     "live permitting portal — not in any GIS layer.", "accela-permits-aca"),
]

# The validation finding: complaint rate by condition grade.
GRADIENT = [
    ("Vacant lot", 18954, 481, 2.5),
    ("Sound", 30822, 1863, 6.0),
    ("Minor repair", 13128, 1569, 12.0),
    ("Major repair", 9169, 2057, 22.4),
    ("Rehabilitation", 902, 430, 47.7),
    ("Dilapidated", 181, 96, 53.0),
]

SYSTEMS = [
    ("City of Dayton — ArcGIS Online", "1,271 items · 374 data services",
     "https://daytonohio.maps.arcgis.com", "Open REST, no auth."),
    ("City of Dayton — on-premise server", "352 services · 35 folders",
     "https://maps.daytonohio.gov/gisservices/rest/services",
     "A larger catalog than the ArcGIS Online org, reached through the REST API. "
     "Code enforcement is served from here."),
    ("County Auditor / Treasurer — bulk files", "9 datasets · 3,856 files",
     "https://go.mcohio.org/applications/treasurer/search/filedownloads.cfm",
     "Plain HTTP. Official record layouts published as PDFs."),
    ("County Auditor — GIS server", "12 services",
     "https://gis.mcohio.org/server/rest/services",
     "Parcels, voter geography, and a geocoder."),
    ("Board of Elections", "precinct shapefiles + extracts",
     "https://www.montgomery.boe.ohio.gov/forms-and-information/",
     "Shapefile download needs a browser User-Agent."),
    ("MVRPC — regional", "3,422 items · 1,011 data services",
     "https://mvrpc.maps.arcgis.com",
     "Regional affordability, tenure and cost-burden indicators derived from ACS."),
]

CAVEATS = [
    ("Paging silently truncates", "ArcGIS caps <code>resultRecordCount</code> at the "
     "server's maximum. A full page then looks like the last page — this produced an "
     "address bridge with 1,000 of 163,184 records that reported success. Terminate on "
     "<code>exceededTransferLimit</code>."),
    ("Sale prices are mostly zero", "County sales files carry "
     "<code>PRICE = 000000000.00</code> with <code>SALEVALIDITY = NOT VALIDATED</code> for "
     "non-arm's-length transfers. Filter before computing any price statistic."),
    ("Null grade is not zero", "13,544 parcels in the condition survey have no grade — "
     "they were not surveyed. Treating null as a category distorts every rollup."),
    ("Layout docs disagree with the data", "The CAMA layout PDF is off by one byte from "
     "<code>GRADE</code> onward, and <code>DWELL.DAT</code> records span three physical "
     "lines — naive reading gives a 3× overcount."),
    ("Rental registration ≠ rental stock", "17,454 parcels are registered against ~118,834 "
     "non-owner-occupied. The gap measures compliance, not tenure."),
    ("Not every service holds data", "59 of the city's published feature services are "
     "Survey123 <code>_form</code> endpoints — write-only, <code>Create,Editing</code>, no "
     "Query. Another 40 declare Query but contain no layers. They are listed here and "
     "marked <b>not readable</b> — a map viewer cannot open them, by design."),
    ("Don't add LIHTC to Section 8", "15 properties appear in both federal datasets. "
     "Summing them inflates the subsidized-unit count."),
]


def load_catalog():
    path = os.path.join(ROOT, "catalog", "master_catalog.csv")
    rows = []
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            rows.append({
                "n": r["name"][:120],
                "p": r["publisher"],
                "t": r["theme"],
                "g": r["granularity"],
                "r": r["records"][:40],
                "u": r["updated"],
                "h": r["housing_relevant"] == "Y",
                "a": r["access"][:90],
                "c": r["cadence"][:60],
                "l": r["url"],
                "q": r.get("queryable", ""),
                "cap": r.get("capabilities", "")[:44],
                "o": r["notes"][:180],
            })
    return rows


def esc(s):
    return html.escape(str(s), quote=True)


def build(rows):
    # Counted, not hardcoded — these drift every time the harvest is re-run.
    dict_count = len([f for f in os.listdir(os.path.join(ROOT, "dictionaries"))
                      if f.endswith(".md")])
    readable = sum(1 for r in rows if r["q"] == "Y")
    housing = sum(1 for r in rows if r["h"])
    pubs = sorted({r["p"] for r in rows})
    themes = sorted({r["t"] for r in rows if r["t"]})
    maxrate = max(g[3] for g in GRADIENT)

    finding_cards = "\n".join(
        f'''      <article class="find">
        <p class="find-k">{esc(k)}</p>
        <p class="find-v">{esc(v)}</p>
        <p class="find-d">{esc(d)}</p>
        <p class="find-src">{esc(src)}.md</p>
      </article>''' for k, v, d, src in FINDINGS)

    grad_rows = "\n".join(
        f'''        <div class="g-row">
          <div class="g-lab">{esc(lab)}</div>
          <div class="g-track"><div class="g-bar" style="width:{rate / maxrate * 100:.1f}%"
               title="{esc(lab)}: {rate}% of {tot:,} parcels had a complaint"></div></div>
          <div class="g-val">{rate}%</div>
          <div class="g-ctx">{comp:,} of {tot:,}</div>
        </div>''' for lab, tot, comp, rate in GRADIENT)

    sys_rows = "\n".join(
        f'''      <li class="sys">
        <div class="sys-h"><span class="sys-n">{esc(n)}</span><span class="sys-c">{esc(c)}</span></div>
        <p class="sys-d">{esc(d)}</p>
        <a class="sys-l" href="{esc(u)}" rel="noopener">{esc(u)}</a>
      </li>''' for n, c, u, d in SYSTEMS)

    cav_rows = "\n".join(
        f'''      <li class="cav"><p class="cav-t">{esc(t)}</p><p class="cav-b">{b}</p></li>'''
        for t, b in CAVEATS)

    pub_opts = "\n".join(f'<option value="{esc(p)}">{esc(p)}</option>' for p in pubs)
    theme_opts = "\n".join(f'<option value="{esc(t)}">{esc(t)}</option>' for t in themes)

    return TEMPLATE.format(
        total=f"{len(rows):,}", housing=f"{housing:,}",
        dicts=f"{dict_count:,}", readable=f"{readable:,}",
        harvested=time.strftime("%Y-%m-%d"),
        findings=finding_cards, gradient=grad_rows, systems=sys_rows, caveats=cav_rows,
        pub_opts=pub_opts, theme_opts=theme_opts,
        data=json.dumps(rows, separators=(",", ":")),
    )


TEMPLATE = r"""<title>Dayton Housing Data Inventory</title>
<style>
  :root {{
    color-scheme: light;
    --page:#eceef1; --surf:#fbfbfc; --surf-2:#f4f5f7;
    --ink:#161b22; --ink-2:#59616c; --ink-3:#89919c;
    --rule:#dcdfe4; --rule-2:#c6cbd2;
    --accent:#9c4f2e; --accent-soft:#f0e2db;
    --data:#2a78d6;
    --warn:#8a6100; --warn-soft:#f7eed6;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:where(:not([data-theme="light"])) {{
      color-scheme: dark;
      --page:#101418; --surf:#181d23; --surf-2:#1e242b;
      --ink:#e7eaee; --ink-2:#a3acb7; --ink-3:#6d7681;
      --rule:#2a323b; --rule-2:#3a434e;
      --accent:#c47a55; --accent-soft:#33241d;
      --data:#3987e5;
      --warn:#d7a33c; --warn-soft:#2b2417;
    }}
  }}
  :root[data-theme="dark"] {{
    color-scheme: dark;
    --page:#101418; --surf:#181d23; --surf-2:#1e242b;
    --ink:#e7eaee; --ink-2:#a3acb7; --ink-3:#6d7681;
    --rule:#2a323b; --rule-2:#3a434e;
    --accent:#c47a55; --accent-soft:#33241d;
    --data:#3987e5;
    --warn:#d7a33c; --warn-soft:#2b2417;
  }}

  *, *::before, *::after {{ box-sizing:border-box; }}
  html {{ overflow-x:hidden; }}
  body {{
    margin:0; background:var(--page); color:var(--ink);
    font-family:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
    font-size:15px; line-height:1.55; -webkit-font-smoothing:antialiased;
    overflow-x:hidden;  /* wide content scrolls in its own container, never the page */
  }}
  .mono {{ font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace; }}
  .wrap {{ max-width:1120px; margin:0 auto; padding:0 24px; }}
  a {{ color:var(--accent); }}
  :focus-visible {{ outline:2px solid var(--accent); outline-offset:2px; border-radius:3px; }}

  .eyebrow {{
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
    font-size:11px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--ink-3); margin:0 0 10px;
  }}

  /* ---- masthead ---- */
  header.mast {{ border-bottom:1px solid var(--rule); background:var(--surf); }}
  .mast-in {{ padding:48px 0 40px; }}
  h1 {{
    margin:0 0 14px; font-size:clamp(30px,4.4vw,46px); line-height:1.06;
    letter-spacing:-.025em; font-weight:680; text-wrap:balance; max-width:19ch;
  }}
  .lede {{ margin:0; max-width:64ch; color:var(--ink-2); font-size:17px; }}
  .lede strong {{ color:var(--ink); font-weight:620; }}
  .mast-meta {{
    display:flex; flex-wrap:wrap; gap:8px 28px; margin-top:26px;
    padding-top:20px; border-top:1px solid var(--rule);
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12px; color:var(--ink-3);
  }}
  .mast-meta b {{ color:var(--ink); font-weight:600; font-variant-numeric:tabular-nums; }}

  section {{ padding:52px 0; }}
  section + section {{ border-top:1px solid var(--rule); }}
  h2 {{ margin:0 0 6px; font-size:21px; letter-spacing:-.012em; font-weight:660; }}
  .sub {{ margin:0 0 28px; color:var(--ink-2); max-width:66ch; }}

  /* ---- findings ---- */
  .finds {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(248px,1fr)); gap:1px;
            background:var(--rule); border:1px solid var(--rule); border-radius:8px; overflow:hidden; }}
  .find {{ background:var(--surf); padding:20px 20px 18px; }}
  .find-k {{ margin:0; font-size:12px; font-weight:620; letter-spacing:.01em; color:var(--ink-2); }}
  .find-v {{ margin:6px 0 8px; font-size:30px; font-weight:660; letter-spacing:-.03em;
             font-variant-numeric:tabular-nums; color:var(--ink);
             font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
  .find-d {{ margin:0; font-size:13.5px; color:var(--ink-2); line-height:1.5; }}
  .find-src {{ margin:12px 0 0; font-size:11px; color:var(--ink-3);
               font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}

  /* ---- gradient chart ---- */
  .chart {{ background:var(--surf); border:1px solid var(--rule); border-radius:8px; padding:24px; }}
  .g-head {{ display:grid; grid-template-columns:130px 1fr 58px 150px; gap:14px;
             font-size:11px; letter-spacing:.1em; text-transform:uppercase; color:var(--ink-3);
             font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
             padding-bottom:10px; border-bottom:1px solid var(--rule); }}
  .g-row {{ display:grid; grid-template-columns:130px 1fr 58px 150px; gap:14px;
            align-items:center; padding:9px 0; }}
  .g-row + .g-row {{ border-top:1px solid var(--rule); }}
  .g-lab {{ font-size:13.5px; font-weight:560; }}
  .g-track {{ background:var(--surf-2); border-radius:4px; height:18px; overflow:hidden; }}
  .g-bar {{ height:100%; background:var(--data); border-radius:0 4px 4px 0;
            transition:width .5s cubic-bezier(.2,.7,.3,1); }}
  .g-val {{ text-align:right; font-weight:640; font-variant-numeric:tabular-nums; font-size:14px;
            font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
  .g-ctx {{ font-size:12px; color:var(--ink-3); font-variant-numeric:tabular-nums;
            white-space:nowrap; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }}
  .g-note {{ margin:18px 0 0; font-size:13px; color:var(--ink-2); max-width:70ch; }}
  @media (prefers-reduced-motion:reduce) {{ .g-bar {{ transition:none; }} }}

  /* ---- filters + table ---- */
  .filters {{ display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-bottom:16px; }}
  input[type=search], select {{
    font:inherit; font-size:13.5px; padding:8px 11px; border:1px solid var(--rule-2);
    border-radius:6px; background:var(--surf); color:var(--ink); min-width:0;
  }}
  input[type=search] {{ flex:1 1 260px; }}
  .chk {{ display:inline-flex; align-items:center; gap:7px; font-size:13.5px; color:var(--ink-2);
          padding:8px 11px; border:1px solid var(--rule-2); border-radius:6px; background:var(--surf);
          cursor:pointer; user-select:none; }}
  .chk input {{ accent-color:var(--accent); margin:0; }}
  .count {{ font-size:12.5px; color:var(--ink-3); margin-left:auto;
            font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
            font-variant-numeric:tabular-nums; }}

  .tablewrap {{ overflow-x:auto; border:1px solid var(--rule); border-radius:8px; background:var(--surf); }}
  table {{ border-collapse:collapse; width:100%; min-width:820px; font-size:13.5px; }}
  thead th {{
    position:sticky; top:0; background:var(--surf-2); text-align:left; font-weight:600;
    font-size:11px; letter-spacing:.09em; text-transform:uppercase; color:var(--ink-3);
    padding:10px 14px; border-bottom:1px solid var(--rule); white-space:nowrap;
    font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
  }}
  tbody td {{ padding:11px 14px; border-top:1px solid var(--rule); vertical-align:top; }}
  tbody tr:hover {{ background:var(--surf-2); }}
  .c-name {{ font-weight:560; }}
  .c-name a {{ text-decoration:none; }}
  .c-name a:hover {{ text-decoration:underline; }}
  .c-note {{ display:block; color:var(--ink-3); font-size:12px; margin-top:3px; max-width:52ch; }}
  .c-rec {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-variant-numeric:tabular-nums;
            white-space:nowrap; font-size:12.5px; }}
  .pill {{ display:inline-block; font-size:11px; padding:2px 8px; border-radius:11px;
           background:var(--surf-2); border:1px solid var(--rule-2); color:var(--ink-2);
           white-space:nowrap; }}
  .pill.hz {{ background:var(--accent-soft); border-color:transparent; color:var(--accent); font-weight:600; }}
  .pill.no {{ background:var(--warn-soft); border-color:transparent; color:var(--warn); font-weight:600; }}
  .empty {{ padding:34px; text-align:center; color:var(--ink-3); }}

  /* ---- systems + caveats ---- */
  ul.plain {{ list-style:none; margin:0; padding:0; display:grid; gap:1px;
              background:var(--rule); border:1px solid var(--rule); border-radius:8px; overflow:hidden; }}
  .sys, .cav {{ background:var(--surf); padding:18px 20px; }}
  .sys-h {{ display:flex; flex-wrap:wrap; gap:6px 14px; align-items:baseline; }}
  .sys-n {{ font-weight:620; font-size:14.5px; }}
  .sys-c {{ font-size:12px; color:var(--ink-3);
            font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-variant-numeric:tabular-nums; }}
  .sys-d {{ margin:6px 0 8px; font-size:13.5px; color:var(--ink-2); max-width:72ch; }}
  .sys-l {{ font-size:12px; font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
            word-break:break-all; }}
  .cav {{ border-left:3px solid var(--warn); }}
  .cav-t {{ margin:0 0 4px; font-weight:620; font-size:14px; }}
  .cav-b {{ margin:0; font-size:13.5px; color:var(--ink-2); max-width:78ch; }}
  .cav-b code {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12.5px;
                 background:var(--surf-2); padding:1px 5px; border-radius:4px; }}

  footer {{ border-top:1px solid var(--rule); padding:30px 0 60px; color:var(--ink-3); font-size:13px; }}
  @media (max-width:640px) {{
    .g-head, .g-row {{ grid-template-columns:96px 1fr 48px; }}
    .g-ctx {{ display:none; }}
  }}
</style>

<header class="mast">
  <div class="wrap mast-in">
    <p class="eyebrow">City of Dayton · Housing Data Subcommittee</p>
    <h1>Housing data published by Dayton and Montgomery County</h1>
    <p class="lede">An inventory of <strong>{total} datasets</strong> across six source systems,
      built for the subcommittee's assess-current-datasets deliverable. Every count here was
      pulled live from the source and verified.</p>
    <div class="mast-meta">
      <span>Harvested <b>{harvested}</b></span>
      <span><b>{total}</b> datasets catalogued</span>
      <span><b>{housing}</b> housing-relevant</span>
      <span><b>{dicts}</b> data dictionaries</span>
      <span><b>{readable}</b> verified readable</span>
    </div>
  </div>
</header>

<section class="wrap">
  <p class="eyebrow">What we found</p>
  <h2>The things worth knowing first</h2>
  <p class="sub">Each of these is documented in a field-level dictionary in the repository.</p>
  <div class="finds">
{findings}
  </div>
</section>

<section class="wrap">
  <p class="eyebrow">Validation</p>
  <h2>Code complaints rise with housing condition</h2>
  <p class="sub">Code enforcement carries no parcel ID, so it was joined to parcels through the
    city's address layer. This is the check that the join is real: if matching were sloppy,
    this line would be flat.</p>
  <div class="chart">
    <div class="g-head">
      <div>Condition grade</div><div>Share of parcels with a complaint</div><div>Rate</div><div>Parcels</div>
    </div>
{gradient}
    <p class="g-note">A dilapidated parcel is <strong>21× more likely</strong> to carry a 2026
      code complaint than a vacant lot, and about 9× more likely than a sound one. Rates are
      six-month figures — the code enforcement service covers 2026 year-to-date only.</p>
  </div>
</section>

<section class="wrap">
  <p class="eyebrow">Where it comes from</p>
  <h2>Six source systems</h2>
  <p class="sub">Each is queryable directly. Two are reached through their REST APIs
    rather than a portal listing, so they are easy to miss when browsing.</p>
  <ul class="plain">
{systems}
  </ul>
</section>

<section class="wrap">
  <p class="eyebrow">The catalog</p>
  <h2>Every dataset found</h2>
  <p class="sub">Search by name, publisher, or theme. Of the 374 City services probed,
    <strong>256 hold readable data</strong> and 118 do not — form endpoints, empty services,
    and dead links. Both filters start on, so you see housing data you can actually open.</p>
  <div class="filters">
    <input type="search" id="q" placeholder="Search datasets, publishers, notes…" aria-label="Search datasets">
    <select id="pub" aria-label="Filter by publisher"><option value="">All publishers</option>
{pub_opts}
    </select>
    <select id="thm" aria-label="Filter by theme"><option value="">All themes</option>
{theme_opts}
    </select>
    <label class="chk"><input type="checkbox" id="hz" checked> Housing only</label>
    <label class="chk"><input type="checkbox" id="rd" checked> Readable data only</label>
    <span class="count" id="count"></span>
  </div>
  <div class="tablewrap">
    <table>
      <thead><tr>
        <th>Dataset</th><th>Publisher</th><th>Theme</th><th>Grain</th><th>Size</th><th>Updated</th>
      </tr></thead>
      <tbody id="rows"></tbody>
    </table>
  </div>
</section>

<section class="wrap">
  <p class="eyebrow">Read before analyzing</p>
  <h2>Notes to read before analyzing</h2>
  <p class="sub">Each of these was encountered during the harvest. None of them raise an
    error, so they are worth knowing in advance. Full detail in
    <span class="mono">docs/CAVEATS.md</span>.</p>
  <ul class="plain">
{caveats}
  </ul>
</section>

<footer class="wrap">
  <p>Built by the Code for Dayton data team for the City of Dayton Housing Data Subcommittee.
     All figures pulled directly from the agencies&rsquo; public endpoints.</p>
</footer>

<script>
const DATA = {data};
const q = document.getElementById('q'), pub = document.getElementById('pub'),
      thm = document.getElementById('thm'), hz = document.getElementById('hz'),
      rd = document.getElementById('rd'),
      rows = document.getElementById('rows'), count = document.getElementById('count');

const esc = s => String(s ?? '').replace(/[&<>"]/g, c => (
  {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));

function render() {{
  const term = q.value.trim().toLowerCase();
  const p = pub.value, t = thm.value, onlyH = hz.checked, onlyR = rd.checked;
  const out = DATA.filter(r => {{
    if (onlyH && !r.h) return false;
    if (onlyR && r.q === 'N') return false;
    if (p && r.p !== p) return false;
    if (t && r.t !== t) return false;
    if (term) {{
      const hay = (r.n + ' ' + r.p + ' ' + r.t + ' ' + r.o + ' ' + r.a).toLowerCase();
      if (!hay.includes(term)) return false;
    }}
    return true;
  }});
  count.textContent = out.length.toLocaleString() + ' of ' + DATA.length.toLocaleString();
  if (!out.length) {{
    rows.innerHTML = '<tr><td colspan="6" class="empty">No datasets match those filters.</td></tr>';
    return;
  }}
  rows.innerHTML = out.slice(0, 400).map(r => {{
    // Don't link a service that can't be opened — a dead link is worse than none.
    const name = (r.l && r.q !== 'N')
      ? '<a href="' + esc(r.l) + '" rel="noopener">' + esc(r.n) + '</a>'
      : esc(r.n);
    return '<tr>'
      + '<td class="c-name">' + name
        + (r.o ? '<span class="c-note">' + esc(r.o) + '</span>' : '')
      + '</td>'
      + '<td>' + esc(r.p) + (r.h ? ' <span class="pill hz">housing</span>' : '') + '</td>'
      + '<td>' + (r.t ? '<span class="pill">' + esc(r.t) + '</span>' : '') + '</td>'
      + '<td>' + esc(r.g || '') + '</td>'
      + '<td class="c-rec">' + esc(r.r || '') + '</td>'
      + '<td class="c-rec">' + esc(r.u || '') + '</td>'
      + '</tr>';
  }}).join('')
  + (out.length > 400
      ? '<tr><td colspan="6" class="empty">Showing the first 400 of '
        + out.length.toLocaleString() + '. Narrow the search to see more.</td></tr>'
      : '');
}}
[q, pub, thm, hz, rd].forEach(el => el.addEventListener('input', render));
render();
</script>
"""


if __name__ == "__main__":
    rows = load_catalog()
    out = build(rows)
    with open(sys.argv[1], "w") as f:
        f.write(out)
    print(f"{len(rows)} rows -> {sys.argv[1]} ({len(out):,} bytes)")
