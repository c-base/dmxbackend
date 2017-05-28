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
    def __init__(self):
        self.C = None

    async def update_mqtt(self):
        await self.C.publish('dmx-mainhall/current_state', json.dumps(channel_state.as_dict()).encode('utf-8'), qos=0x00, retain=True)

    async def mqtt_loop(self, loop, mqtt_server):
        self.C = MQTTClient()
        url = "mqtt://{}:{}/".format(mqtt_server, 1883)
        log.debug("Connecting to MQTT server '{}'".format(url))
        await self.C.connect(url)
        channel_state.subscribe(self.update_mqtt)
        fix = json.dumps(channel_state.fixtures()).encode('utf-8')
        await self.C.publish('dmx-mainhall/fixtures', fix, qos=0x00, retain=True)
        await self.C.publish('dmx-mainhall/current_state', json.dumps(channel_state.as_list()).encode('utf-8'), qos=0x00, retain=True)
        await self.C.subscribe([ ('dmx-mainhall/state', QOS_1), ])
        i = 0
        while loop.is_running():
            i += 1
            message = await self.C.deliver_message()
            packet = message.publish_packet
            log.debug("%d: %s => %s" % (i, packet.variable_header.topic_name, str(packet.payload.data)))
            topic = packet.variable_header.topic_name
            if topic == 'dmx-mainhall/state':
                decoded = None
                try:
                    decoded = json.loads(packet.payload.data)
                except:
                    pass
                if decoded is not None and isinstance(decoded, list):
                    channel_state.update_channels(decoded)
                else:
                    log.warning("Something went wrong deserializing the string '%s'" % packet.payload.data)
            else:
                log.info("Got unknown topic '%s'" % topic)
                    
