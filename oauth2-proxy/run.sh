#!/bin/sh

# A simple script that will set configuration and run aut-odelte python script.
# Author: Yannick Larrivée <yannicklarrivee@gmail.com>

CONFIG_PATH=/data/options.json
export PROVIDER="$(jq --raw-output '.provider' $CONFIG_PATH)"
export CLIENT_ID="$(jq --raw-output '.clientid' $CONFIG_PATH)"
export CLIENT_SECRET="$(jq --raw-output '.clientsecret' $CONFIG_PATH)"
export EMAIL_DOMAIN="$(jq --raw-output '.emaildomain' $CONFIG_PATH)"
export COOKIE_SECRET="$(jq --raw-output '.cookiesecret' $CONFIG_PATH)"
export CALLBACK_URL="$(jq --raw-output '.callbackurl' $CONFIG_PATH)"
export PATH=/root/go/bin:$PATH 

# Start the listener and enter an endless loop
echo "Starting oauth2-proxy with parameters:"
echo "Auth provider =" $PROVIDER
echo "Client ID=" $CLIENT_ID
echo "Client secret=" $CLIENT_SECRET
echo "Email domain allowed=" "${EMAIL_DOMAIN}"
echo "Cookie secret=" $COOKIE_SECRET
echo "Callback url=" $CALLBACK_URL

oauth2-proxy --client-id $CLIENT_ID --client-secret $CLIENT_SECRET --cookie-secret $COOKIE_SECRET  --email-domain $EMAIL_DOMAIN --provider $PROVIDER --http-address=0.0.0.0:4180 --redirect-url $CALLBACK_URL