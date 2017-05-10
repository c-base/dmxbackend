#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import asyncio
import logging
import json
import paho.mqtt.client as mqtt
from collections import deque

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
        self.client.conntect(mqtt_server)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        self.client.subscribe("/dmx-mainhall/state")
        self.client.publish("/dmx-mainall/fixtures", payload=json.dumps(), retain=True)

    def on_message(self, client, userdata, message):
        self.message_queue.append(message.payload.decode('utf8'))
    
    async def every_semisecond(self, loop):
        while loop.is_running():
            if self.message_queue:
                log.debug(self.message_queue)
                log.debug(self.message_queue.popleft())
            else:
                log.debug('MQTT waiting ...')
                await asyncio.sleep(.5)
