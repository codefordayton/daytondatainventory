#!/bin/sh
set -e

if [ -z "$AUTH_PASSWORD" ]; then
	echo "ERROR: set the AUTH_PASSWORD variable in Railway before deploying." >&2
	exit 1
fi

# Default the username to "team" if not provided.
export AUTH_USER="${AUTH_USER:-team}"

# Hash the plaintext password at boot so no hash is ever stored in the repo.
export AUTH_HASH="$(caddy hash-password --plaintext "$AUTH_PASSWORD")"

exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile
