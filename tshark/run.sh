#!/bin/sh

# A simple script that will set configuration and run aut-odelte python script.
# Author: Yannick Larrivée <yannicklarrivee@gmail.com>

CONFIG_PATH=/data/options.json
export FILTER="$(jq --raw-output '.filter' $CONFIG_PATH)"
export INTERFACE="$(jq --raw-output '.interface' $CONFIG_PATH)"
export PCAP_FILE="$(jq --raw-output '.pcap_file' $CONFIG_PATH)"
export AUTOSTOP="$(jq --raw-output '.autostop' $CONFIG_PATH)"

# Start the listener and enter an endless loop
echo "Starting tshark with parameters:"
echo "Packet filter =" $FILTER
echo "Network interface=" $INTERFACE
echo "pcap file name=" $PCAP_FILE
echo "Autostop condition=" $AUTOSTOP

tshark -i $INTERFACE -f "${FILTER}" -a $AUTOSTOP -w $PCAP_FILE
#tshark -i $INTERFACE -a $AUTOSTOP -w $PCAP_FILE