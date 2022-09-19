#!/bin/sh
set -e

DHPARAMS_PATH=/data/dhparams.pem
CONFIG_PATH=/data/options.json

DOMAIN="$(jq --raw-output '.domain' $CONFIG_PATH)"
KEYFILE="$(jq --raw-output '.keyfile' $CONFIG_PATH)"
CERTFILE="$(jq --raw-output '.certfile' $CONFIG_PATH)"
HA_PORT="$(jq --raw-output '.homeassistant_port' $CONFIG_PATH)"
HOMEASSISTANT="$(jq --raw-output '.homeassistant' $CONFIG_PATH)"
OAUTH2_PROXY="$(jq --raw-output '.oauth2_proxy' $CONFIG_PATH)"
OAUTH2_PROXY_PORT="$(jq --raw-output '.oauth2_proxy_port' $CONFIG_PATH)"

# Generate dhparams
if ! [ -f "$DHPARAMS_PATH" ]; then
    echo "Generating dhparams (this will take some time)..."
    openssl dhparam -dsaparam -out "$DHPARAMS_PATH" 4096 > /dev/null
fi

# Prepare config file
sed -i "s#%%FULLCHAIN%%#$CERTFILE#g" /etc/nginx.conf
sed -i "s#%%PRIVKEY%%#$KEYFILE#g" /etc/nginx.conf
sed -i "s/%%DOMAIN%%/$DOMAIN/g" /etc/nginx.conf
sed -i "s/%%HA_PORT%%/$HA_PORT/g" /etc/nginx.conf
sed -i "s/%%HOMEASSISTANT%%/$HOMEASSISTANT/g" /etc/nginx.conf
sed -i "s/%%OAUTH2_PROXY%%/$OAUTH2_PROXY/g" /etc/nginx.conf
sed -i "s/%%OAUTH2_PROXY_PORT%%/$OAUTH2_PROXY_PORT/g" /etc/nginx.conf

# start server
echo "Running nginx..."
exec nginx -c /etc/nginx.conf < /dev/null
