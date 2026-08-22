#!/bin/sh
# Assemble deploy/site from the map sources. Run from map/deploy/.
set -e
cd "$(dirname "$0")"
mkdir -p site/data
cp ../developable_sites.html site/index.html
cp ../data/*.js site/data/
echo "site/ assembled:"
du -sh site
ls -la site site/data
