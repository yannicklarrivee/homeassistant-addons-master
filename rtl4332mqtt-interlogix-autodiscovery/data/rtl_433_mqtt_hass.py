#!/usr/bin/env python3
# coding=utf-8

"""MQTT Home Assistant auto discovery for rtl_433 events."""

# It is strongly recommended to run rtl_433 with "-C si" and "-M newmodel".

# Needs Paho-MQTT https://pypi.python.org/pypi/paho-mqtt
# Option: PEP 3143 - Standard daemon process library
# (use Python 3.x or pip install python-daemon)
# import daemon

from __future__ import print_function
from __future__ import with_statement

import time
import json
import paho.mqtt.client as mqtt

options_file = open("/data/options.json", 'r', encoding='utf-8')
json_data = options_file.read()
options_dict = json.loads(json_data)
MQTT_HOST = options_dict["mqtt_host"] #"homeassistant"
MQTT_PORT = 1883
MQTT_TOPIC_1 = options_dict["mqtt_topic"] + "/devices/+/+/+/events"
MQTT_TOPIC_2 = options_dict["mqtt_topic"] + "/devices/+/+/events"
# When MQTT_USERNAME is set to None it will disable username and password for mqtt
MQTT_USERNAME = options_dict["mqtt_user"]
MQTT_PASSWORD = options_dict["mqtt_password"]
DISCOVERY_PREFIX = "homeassistant"
DISCOVERY_INTERVAL = 600  # Seconds before refreshing the discovery

discovery_timeouts = {}

sensors = options_dict["sensors"]

mappings_file = open("/data/mappings.json")
mappings = json.loads(mappings_file.read())


def mqtt_connect(client, userdata, flags, rc):
    """Callback for MQTT connects."""
    print("MQTT connected: " + mqtt.connack_string(rc))
    if rc != 0:
        print("Could not connect. Error: " + str(rc))
    else:
        client.subscribe(MQTT_TOPIC_1)
        client.subscribe(MQTT_TOPIC_2)


def mqtt_disconnect(client, userdata, rc):
    """Callback for MQTT disconnects."""
    print("MQTT disconnected: " + mqtt.connack_string(rc))


def mqtt_message(client, userdata, msg):
    """Callback for MQTT message PUBLISH."""
    try:
        # Decode JSON payload
        data = json.loads(msg.payload.decode())
        print("data 0:" + json.dumps(data))
        topicprefix = "/".join(msg.topic.split("/", 2)[:2])
        bridge_event_to_hass(client, topicprefix, data)

    except json.decoder.JSONDecodeError:
        print("JSON decode error: " + msg.payload.decode())
        return


def sanitize(text):
    """Sanitize a name for Graphite/MQTT use."""
    return (text
            .replace(" ", "_")
            .replace("/", "_")
            .replace(".", "_")
            .replace("&", ""))


def publish_config(mqttc, topic, model, instance, mapping):
    """Publish Home Assistant auto discovery data."""
    global discovery_timeouts
    global sensors

    print("Instance 1 " + instance)
    for sensor in sensors:
        if instance == sensor["id"]:
            instance = str(sensor["name"])
    instance_no_slash = instance.replace("/", "-")
    print("Instance 2 " + instance)
    device_type = mapping["device_type"]
    object_suffix = mapping["object_suffix"]
    object_id = "-".join([model, instance_no_slash])
    object_name = "-".join([object_id,object_suffix])

    path = "/".join([DISCOVERY_PREFIX, device_type, object_id, object_name, "config"])

    # check timeout
    now = time.time()
    if path in discovery_timeouts:
        if discovery_timeouts[path] > now:
            return

    discovery_timeouts[path] = now + DISCOVERY_INTERVAL

    config = mapping["config"].copy()
    config["name"] = object_name
    config["state_topic"] = topic
    config["unique_id"] = object_name
    config["device"] = { "identifiers": object_id, "name": object_id, "manufacturer": "rtl_433" }

    mqttc.publish(path, json.dumps(config))


def bridge_event_to_hass(mqttc, topicprefix, data):
    """Translate some rtl_433 sensor data to Home Assistant auto discovery."""

    print("data: " + json.dumps(data))
    if "model" not in data:
        # not a device event
        return
    model = sanitize(data["model"])
    instance = None
    if "subtype" in data:
        subtype = str(data["subtype"])
    else:
        subtype = "nosubtype"
    if "channel" in data:
        channel = str(data["channel"])
        instance = channel
    if "id" in data:
        device_id = str(data["id"])
        if not instance:
            instance = device_id
        else:
            instance = channel + "/" + device_id
    print("Instance 0 " + instance)
    if not instance:
        # no unique device identifier
        return

    # detect known attributes
    for key in data.keys():
        if key in mappings:
            topic = "/".join([topicprefix,model,subtype,instance,key])
            publish_config(mqttc, topic, model, instance, mappings[key])


def rtl_433_bridge():
    """Run a MQTT Home Assistant auto discovery bridge for rtl_433."""
    mqttc = mqtt.Client()
    if MQTT_USERNAME is not None:
        mqttc.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    mqttc.on_connect = mqtt_connect
    mqttc.on_disconnect = mqtt_disconnect
    mqttc.on_message = mqtt_message
    mqttc.connect_async(MQTT_HOST, MQTT_PORT, 60)
    mqttc.loop_start()

    while True:
        time.sleep(1)


def run():
    """Run main or daemon."""
    # with daemon.DaemonContext(files_preserve=[sock]):
    #  detach_process=True
    #  uid
    #  gid
    #  working_directory
    rtl_433_bridge()


if __name__ == "__main__":
    run()
