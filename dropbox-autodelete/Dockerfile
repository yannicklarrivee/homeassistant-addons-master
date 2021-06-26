# Docker file to create an image for a hass.io add-on that contains enough software to listen to events via RTL_SDR/RTL_433 and then publish them to a MQTT broker.
# The script resides in a volume and can be modified to meet your needs.
# This hass.io addon is based on Chris Kacerguis' project here: https://github.com/chriskacerguis/honeywell2mqtt,
# which is in turn based on Marco Verleun's rtl2mqtt image here: https://github.com/roflmao/rtl2mqtt

# IMPORTANT: The container needs privileged access to /dev/bus/usb on the host.

ARG BUILD_FROM=homeassistant/amd64-base:latest
FROM $BUILD_FROM

ENV LANG C.UTF-8

LABEL Maintainer = "Yannick Larrivée"
 
LABEL Description="This image is used to start a script that will delete files from a Dropbox path and keep last X entries."

#
# Copy requirements file
#
COPY ./requirements.txt ./requirements.txt
COPY ./dropbox-autodelete.py ./dropbox-autodelete.py 
COPY ./run.sh ./run.sh

#
# Install software packages requirements
#
RUN apk add --no-cache jq python3 py3-pip && \
    pip3 install -r requirements.txt

#
# Define an environment variable
#
# Use this variable when creating a container to specify the MQTT broker host.
ENV ACCESS_TOKEN = "MY-ACCES-TOKEN"
ENV DROPBOX_PATH = "/backup"
ENV NUMBER_OF_FILES = 10

CMD chmod +x /run.sh && /run.sh
