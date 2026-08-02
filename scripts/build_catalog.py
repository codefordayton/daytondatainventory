#!/usr/bin/env python3
"""Merge all harvested sources into the subcommittee's master catalog.

Usage:
    ./build_catalog.py

Columns follow the per-dataset schema the Housing Data Subcommittee asked for
(see PRIOR_RESEARCH_CONTEXT.md). Inferred columns (theme, granularity, cadence)
are best-effort from titles/metadata; current_use_state, desired_use_state and
priority are intentionally left blank for the team to fill in by hand.

Only public agency endpoints are harvested; licensed third-party platforms are
out of scope.
"""
import csv
import datetime
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "data", "raw")
OUT = os.path.join(ROOT, "catalog")

THEMES = [
    ("condition/quality", r"condition|housing.?condition|hcs|blight|dilapidat|inspect|repair"),
    ("vacancy", r"vacan|abandon|boarded|mowing|demoli|demo\b"),
    ("code enforcement", r"accela|code.?enforc|violation|nuisance|complaint|citation"),
    ("tax/delinquency", r"delinquen|tax|lien|foreclos|treasurer|taxroll|refund"),
    ("ownership/transfers", r"sale|transfer|deed|conveyance|owner|cama|parcel|propert"),
    ("affordability/tenure", r"afford|tenure|rent|cost.?burden|income|lihtc|subsid|ami"),
    ("investment/projects", r"project|program|arpa|recovery|funding|invest|rehab"),
    ("zoning/land use", r"zoning|land.?use|plan|district|opportunity.?zone"),
    ("demographics", r"census|population|demographic|acs|block.?group|tract"),
    ("geography/reference", r"neighborhood|boundar|address|basemap|street|precinct"),
    ("public safety", r"police|crime|arrest|fire|use.?of.?force|calls.?for.?service"),
    ("infrastructure", r"water|sewer|storm|utilit|pavement|light|bridge|traffic"),
]

GRAN = [
    ("parcel", r"parcel|propert|cama|taxroll|sale|hcs|housing.?condition|nuisance"),
    ("address/point", r"address|incident|complaint|point|request|stop|arrest"),
    ("block group", r"block.?group"),
    ("tract", r"tract"),
    ("neighborhood", r"neighborhood|district|precinct|ward"),
    ("jurisdiction/county", r"jurisdiction|count(y|ies)|city|region"),
]

HOUSING_KW = re.compile(
    r"housing|parcel|propert|vacant|abandon|nuisance|blight|demoli|code.?enforc|"
    r"violation|rental|landlord|tenant|evict|permit|inspect|zoning|land.?bank|"
    r"foreclos|tax|deed|sale|address|neighborhood|lead|rehab|assess|delinquen|"
    r"afford|tenure|cost.?burden|lihtc|subsid|income", re.I)


def classify(text, table, default=""):
    for label, pat in table:
        if re.search(pat, text, re.I):
            return label
    return default


def ms_to_date(ms):
    try:
        return datetime.datetime.fromtimestamp(ms / 1000).strftime("%Y-%m-%d")
    except Exception:
        return ""


def load(name):
    p = os.path.join(RAW, name)
    return json.load(open(p)) if os.path.exists(p) else None


def rec(**kw):
    base = dict.fromkeys(COLS, "")
    base.update(kw)
    return base


def rows():
    out = []

    # Declared capabilities per service, merged across every probed org. Survey123
    # "_form" views and tile-only imagery are catalogued but are not readable as
    # data — see docs/CAVEATS.md. Keys are item ids, so orgs merge cleanly.
    caps = {}
    for f in ("capabilities_dayton.json", "capabilities_mvrpc.json"):
        caps.update((load(f) or {}).get("services", {}))

    counts = {}
    fields = load("fields_dayton_housing.json")
    if fields:
        for ds in fields["datasets"]:
            counts[ds["id"]] = sum(l.get("recordCount") or 0 for l in ds.get("layers", []))

    # --- ArcGIS Online orgs ------------------------------------------------
    for fname, publisher, contact, portal in [
        ("arcgis_cityofdayton.json", "City of Dayton", "City of Dayton GIS / PND",
         "https://daytonohio.maps.arcgis.com"),
        ("arcgis_mvrpc.json", "MVRPC (regional)", "msimpson_MVRPC",
         "https://mvrpc.maps.arcgis.com"),
    ]:
        d = load(fname)
        if not d:
            continue
        for i in d["items"]:
            if i["type"] not in ("Feature Service", "Map Service"):
                continue
            blob = i["title"] + " " + (i.get("snippet") or "") + " " + " ".join(i.get("tags") or [])
            cap = caps.get(i["id"], {})
            out.append(rec(
                queryable="Y" if cap.get("queryable") else ("N" if cap else ""),
                capabilities=(cap.get("capabilities") or cap.get("note") or "")[:60],
                name=i["title"], publisher=publisher,
                source_owner=f"{i.get('owner', '')} ({contact})",
                theme=classify(blob, THEMES),
                geography="City of Dayton" if publisher == "City of Dayton" else "Miami Valley region",
                granularity=classify(blob, GRAN),
                access="Public — ArcGIS REST API, no auth",
                cadence="live service (verify)",
                formats="ArcGIS FeatureServer/MapServer; GeoJSON, CSV, Shapefile export",
                records=counts.get(i["id"], ""),
                updated=ms_to_date(i.get("modified")),
                housing_relevant=("Y" if HOUSING_KW.search(blob)
                                  and cap.get("queryable", True) else ""),
                url=i.get("url") or "",
                item_page=f"{portal}/home/item.html?id={i['id']}",
                notes=(i.get("snippet") or "").replace("\n", " ")[:200],
            ))

    # --- ArcGIS Server catalogs -------------------------------------------
    for fname, publisher, contact, geo, root in [
        ("arcgis_dayton_server.json", "City of Dayton", "City of Dayton GIS",
         "City of Dayton", "https://maps.daytonohio.gov/gisservices/rest/services"),
        ("arcgis_mcohio_server.json", "Montgomery County Auditor", "Montgomery County GIS",
         "Montgomery County", "https://gis.mcohio.org/server/rest/services"),
    ]:
        d = load(fname)
        if not d:
            continue
        for s in d["services"]:
            if s["type"] in ("GeometryServer", "GeocodeServer"):
                continue
            label = f"{s['folder']}/{s['name'].split('/')[-1]}" if s.get("folder") else s["name"]
            blob = label + " " + (s.get("description") or "")
            out.append(rec(
                name=label, publisher=publisher, source_owner=contact,
                theme=classify(blob, THEMES), geography=geo,
                granularity=classify(blob, GRAN),
                access="Public — ArcGIS REST API, no auth",
                cadence="live service (verify)",
                formats=f"ArcGIS {s['type']}",
                records=f"{len(s.get('layers', []))} layers",
                housing_relevant="Y" if HOUSING_KW.search(blob) else "",
                url=s["url"], item_page=root,
                notes=re.sub(r"\s+", " ", (s.get("description") or ""))[:200],
            ))

    # --- Montgomery County Treasurer bulk files ---------------------------
    t = load("mc_treasurer_manifest.json")
    if t:
        for ds in t["datasets"]:
            if not ds["files"]:
                continue
            newest, oldest = ds["files"][0], ds["files"][-1]
            out.append(rec(
                name=f"MC {ds['name']}", publisher="Montgomery County Auditor/Treasurer",
                source_owner="Montgomery County Treasurer (lien data: Jennifer Connolly)",
                theme=classify(ds["name"], THEMES, "ownership/transfers"),
                geography="Montgomery County", granularity="parcel",
                access="Public — direct HTTP download, no auth",
                cadence=f"periodic archive ({oldest.get('created')} → {newest.get('created')})",
                formats="ZIP of CSV (see docs/mc_file_layouts/)",
                records=f"{ds['file_count']} files",
                updated=newest.get("created") or "",
                housing_relevant="Y" if HOUSING_KW.search(ds["name"]) else "",
                url=newest["url"],
                item_page="https://go.mcohio.org/applications/treasurer/search/filedownloads.cfm",
                notes=f"Newest file {newest.get('size_bytes') or 0:,} bytes. Official record layout PDF available.",
            ))

    manual = load("manual_sources.json")
    if manual:
        for r in manual["rows"]:
            out.append(rec(
                name=r["dataset"], publisher=r["publisher"], source_owner=r.get("owner", ""),
                theme=classify(r["dataset"] + " " + r.get("notes", ""), THEMES),
                geography="Montgomery County", granularity=classify(r["dataset"], GRAN),
                access=r.get("access", ""), formats=r.get("type", ""),
                housing_relevant=r.get("housing_relevant", ""),
                url=r.get("url", ""), item_page=r.get("item_page", ""),
                notes=r.get("notes", ""),
            ))

    return out


COLS = ["name", "publisher", "source_owner", "theme", "geography", "granularity",
        "access", "cadence", "formats", "key_fields", "records", "updated",
        "housing_relevant", "queryable", "capabilities", "priority",
        "current_use_state", "desired_use_state", "url", "item_page", "notes"]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    data = sorted(rows(), key=lambda r: (r["publisher"], r["name"].lower()))
    path = os.path.join(OUT, "master_catalog.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        w.writeheader()
        w.writerows(data)
    h = [r for r in data if r["housing_relevant"] == "Y"]
    print(f"wrote {len(data)} rows ({len(h)} housing-relevant) to {path}")
