FROM caddy:2.8.4-alpine

COPY Caddyfile /etc/caddy/Caddyfile
COPY site /site
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# $PORT is injected by Railway at runtime.
ENTRYPOINT ["/entrypoint.sh"]
