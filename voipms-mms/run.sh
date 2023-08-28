#!/bin/sh

# A simple script that will set configuration and run aut-odelte python script.
# Author: Yannick Larrivée <yannicklarrivee@gmail.com>

CONFIG_PATH=/data/options.json
export API_USERNAME="$(jq --raw-output '.api_username' $CONFIG_PATH)"
export API_PASSWORD="$(jq --raw-output '.api_password' $CONFIG_PATH)"
export DID="$(jq --raw-output '.did' $CONFIG_PATH)"

echo "Sending SMS"
while read -r msg; do
    echo "$msg"
    DESTINATION="$(echo "$msg" | jq --raw-output '.destination')"    
    SMS_MESSAGE="$(echo "$msg" | jq --raw-output '.message')"
    echo "Message: ${SMS_MESSAGE}" && python3 send-sms.py $API_USERNAME $API_PASSWORD $DID $DESTINATION "$SMS_MESSAGE"
done < /dev/stdin