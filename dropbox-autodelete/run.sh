#!/bin/sh

# A simple script that will set configuration and run aut-odelte python script.
# Author: Yannick Larrivée <yannicklarrivee@gmail.com>

CONFIG_PATH=/data/options.json
export ACCESS_TOKEN="$(jq --raw-output '.access_token' $CONFIG_PATH)"
export DROPBOX_PATH="$(jq --raw-output '.path' $CONFIG_PATH)"
export NUMBER_OF_FILES="$(jq --raw-output '.number_of_files' $CONFIG_PATH)"

# Start the listener and enter an endless loop
echo "Starting auto delete with parameters:"
echo "Acess token =" $ACCESS_TOKEN
echo "Dropbox path=" $DROPBOX_PATH
echo "Number of files=" $NUMBER_OF_FILES

python3 /dropbox-autodelete.py
