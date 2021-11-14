#!/bin/sh

docker build  -t local/tshark . \
&& \
docker run --privileged --net=host 
--rm -v /Users/yannicklarrivee/Dev/homeassistant-addons-master/tshark/test_data:/data local/tshark
