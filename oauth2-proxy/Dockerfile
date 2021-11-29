# Docker file to create an image for a hass.io add-on that contains enough software to listen to events via RTL_SDR/RTL_433 and then publish them to a MQTT broker.
# The script resides in a volume and can be modified to meet your needs.
# This hass.io addon is based on Chris Kacerguis' project here: https://github.com/chriskacerguis/honeywell2mqtt,
# which is in turn based on Marco Verleun's rtl2mqtt image here: https://github.com/roflmao/rtl2mqtt

# IMPORTANT: The container needs privileged access to /dev/bus/usb on the host.

ARG BUILD_FROM=homeassistant/amd64-base:latest
FROM $BUILD_FROM

ENV LANG C.UTF-8

LABEL Maintainer = "Yannick Larrivée"
 
LABEL Description="This image is used to start a oauth2 proxy for authentication."

#
# Copy run file
#
COPY ./run.sh ./run.sh
#cd
# Install tshark
#
RUN apk add --no-cache go
RUN go get github.com/oauth2-proxy/oauth2-proxy/v7 && go clean --modcache
#
# Start monitoring and make output file available
#
CMD chmod +x /run.sh && /run.sh
