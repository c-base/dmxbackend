#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
import asyncio
import logging
import json
import paho.mqtt.client as mqtt
from collections import deque
from amqtt.client import MQTTClient, ConnectError
from amqtt.mqtt.constants import *

from dmxbackend import channel_state

log = logging.getLogger(__name__)


class AsyncMQTT(object):
    def __init__(self):
        self.C = None
        self.last_automode = None

    async def update_mqtt(self):
        await self.C.publish('dmx-mainhall/current_state', json.dumps(channel_state.as_dict()).encode('utf-8'), qos=0x00, retain=True)
        if channel_state._enabled != self.last_automode:
            await self.C.publish('dmx-mainhall/automode', json.dumps(channel_state._enabled).encode('utf-8'), qos=0x00, retain=True)
            self.last_automode = channel_state._enabled

    async def discovery_loop(self, loop):
        while loop.is_running():
            msg = {
                "protocol":"discovery",
                "command":"participant",
                "payload":{
                    "component":"c-base/dmx",
                    "label":"station light control",
                    "icon":"lightbulb-o",
                    "inports":[
                        {
                            "queue":"dmx-mainhall/state",
                            "type":"object",
                            "description":"set the current light state",
                            "id":"set_channels"
                        }
                    ],
                    "outports":[
                        {
                            "queue":"dmx-mainhall/fixtures",
                            "type":"object",
                            "description":"light fixtures",
                            "id":"fixtures"
                        },
                        {
                            "queue":"dmx-mainhall/current_state",
                            "type":"object",
                            "description":"the current channel state",
                            "id":"channels"
                        },
                        {
                            "queue":"dmx-mainhall/automode",
                            "type":"boolean",
                            "description":"is the automatic mode enabled",
                            "id":"automode"
                        }
                    ],
                    "role":"mainhall",
                    "id":"mainhall"
                }
            }
            log.debug(json.dumps(msg, indent=2))
            await self.C.publish('fbp', json.dumps(msg).encode('utf-8'), qos=0x00, retain=False)
            await asyncio.sleep(20.0)

    async def mqtt_loop(self, loop, mqtt_server):
        self.C = MQTTClient(config={
            'auto_reconnect': True,
            'reconnect_max_interval': 10,
            'reconnect_retries': 100000,
        })
        url = "mqtt://{}:{}/".format(mqtt_server, 1883)
        log.debug("Connecting to MQTT server '{}'".format(url))
        await self.C.connect(url)
        channel_state.subscribe(self.update_mqtt)
        fix = json.dumps(channel_state.fixtures()).encode('utf-8')
        await self.C.publish('dmx-mainhall/fixtures', fix, qos=0x00, retain=True)
        await self.C.publish('dmx-mainhall/current_state', json.dumps(channel_state.as_list()).encode('utf-8'), qos=0x00, retain=True)
        await self.C.publish('dmx-mainhall/automode', json.dumps(channel_state._enabled).encode('utf-8'), qos=0x00, retain=True)
        await self.C.subscribe([ ('dmx-mainhall/state', QOS_0), ])
        asyncio.ensure_future(self.discovery_loop(loop))
        while loop.is_running():
            message = None 
            try:
                message = await self.C.deliver_message(timeout=600)
            except asyncio.TimeoutError as e:
                pass

            # after a successful reconnect we need to resubscribe
            if message is None:
                try:
                    await self.C.unsubscribe(['dmx-mainhall/state', ])
                    await self.C.subscribe([ ('dmx-mainhall/state', QOS_0), ])
                except:
                    pass
                continue

            packet = message.publish_packet
            # log.debug("%d: %s => %s" % (i, packet.variable_header.topic_name, str(packet.payload.data)))
            topic = packet.variable_header.topic_name
            if topic == 'dmx-mainhall/state':
                decoded = None
                try:
                    # bytearrays need to be decoded before running json.loads - but only in python3.5
                    decoded = json.loads(packet.payload.data.decode('utf-8'))
                except:
                    pass
                if decoded is not None and isinstance(decoded, list):
                    channel_state.update_channels(decoded)
                else:
                    log.warning("Something went wrong deserializing the string '%s'" % packet.payload.data)
            else:
                log.info("Got unknown topic '%s'" % topic)
