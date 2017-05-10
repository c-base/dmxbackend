#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import asyncio
import logging
import json
import paho.mqtt.client as mqtt
from collections import deque
from hbmqtt.client import MQTTClient, ConnectException
from hbmqtt.mqtt.constants import *

from dmxbackend import channel_state

log = logging.getLogger(__name__)

class AsyncMQTT(object):
    def __init__(self, client=None, mqtt_server='localhost'):
        if client is None:
            self.client = mqtt.Client()
        else:
            self.client = client
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.message_queue = deque()
        self.mqtt_server = mqtt_server

    def on_connect(self, client, userdata, flags, rc):
        log.debug("Connected with result code " + str(rc))
        self.client.subscribe("dmx-mainhall/state")
        self.client.publish("dmx-mainhall/fixtures", payload=json.dumps(), retain=True)

    def on_message(self, client, userdata, message):
        self.message_queue.append(message.payload.decode('utf8'))
    
    async def every_semisecond(self, loop):
        self.client.connect(self.mqtt_server)
        while loop.is_running():
            if self.message_queue:
                log.debug(self.message_queue)
                log.debug(self.message_queue.popleft())
            else:
                await asyncio.sleep(.5)

async def mqtt_loop(loop, mqtt_server):
    C = MQTTClient()
    url = "mqtt://{}:{}/".format(mqtt_server, 1883)
    log.debug("Connecting to MQTT server '{}'".format(url))
    await C.connect(url)
    fix = json.dumps(channel_state.fixtures()).encode('utf-8')
    await C.publish('dmx-mainhall/fixtures', fix, qos=0x00)
