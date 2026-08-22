# Deploying the developable sites map

Static site behind HTTP basic auth, served by Caddy on Railway. Same shape as the
`voterimpact` deploy, so the two behave identically.

Everything on the map is public record. The password is about **controlling how a
work-in-progress screening tool circulates**, not about protecting the data.

---

## Deploy

```bash
./build_site.sh          # copies the map + data into site/
```

Then on Railway, deploy this directory and set:

| Variable | Required | Notes |
|---|---|---|
| `AUTH_PASSWORD` | **yes** | plaintext; hashed at boot, never stored in the repo |
| `AUTH_USER` | no | defaults to `team` |
| `PORT` | injected | Railway sets this |

`entrypoint.sh` refuses to start without `AUTH_PASSWORD`, so an unprotected deploy is not
possible by accident.

`robots.txt` disallows everything and the Caddyfile sends
`X-Robots-Tag: noindex, nofollow, noarchive`, so the site stays out of search results even
if the URL leaks.

---

## Refreshing the data

The map is a **point-in-time snapshot** and does not update itself. To rebuild:

```bash
# 1. current tax roll (published daily)
curl -O https://go.mcohio.org/applications/treasurer/search/data/Taxroll/TAXROLL_YYYYMMDD.zip
unzip TAXROLL_YYYYMMDD.zip

# 2. rebuild the sites layer
python3 ../../scripts/build_developable_sites.py TAXROLL_YYYYMMDD.csv \
        ../../data/raw/hcs_grades.json ../../data/raw/address_bridge.json ../../data/derived

# 3. top up any parcel geometry that is missing
python3 ../../scripts/fetch_parcel_geometry.py ../../data/derived/developable_sites.csv \
        parcel ../../data/raw/parcel_centroids.json

# 4. regenerate the map payload, then reassemble
python3 ../../scripts/build_map_data.py ../../data/derived \
        ../../data/raw/dayton_neighborhoods.geojson ../data
./build_site.sh
```

**Update the dates in the sidebar and the methodology modal** when you do — they are written
into `developable_sites.html` deliberately rather than generated, so a refresh cannot
silently leave stale provenance on screen.

---

## Size

`site/` is about 4.3 MB, nearly all of it `sites_geojson.js` (11,639 points). Caddy gzips
it, so the wire cost is far smaller. If it grows enough to matter, the obvious lever is
dropping properties from the payload rather than dropping sites — the full attribute set
already lives in `data/derived/developable_sites.csv`.
