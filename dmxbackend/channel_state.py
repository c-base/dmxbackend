# -*- coding: utf-8 -*-
"""
Manages the current state of the lights. You can subscribe to updates.
"""
import asyncio
from collections import OrderedDict
from datetime import datetime

_state = None
_last_update = None
_subscribers = []
_dmx_subscribers = []
_dmx = None

def initialize_state(mapping):
    global _state
    global _last_update
    global _dmx
    _dmx = bytearray(512)
    _state = OrderedDict()
    for light in mapping:
        for id in light.channel_ids:
            _state[id] = 0x00
    _last_update = datetime.now()


def update_channels(new_data):
    for el in new_data:
        _state[el['channel_id']] = el['value']
    _last_update = datetime.now()
    notify()


def update_dmx(new_dmx):
    _dmx = new_dmx
    _last_update = datetime.now()
    notify()


def subscribe(call_when_updated):
    _subscribers.append(call_when_updated)


def notify():
    for call_when_updated in _subscribers:
        asyncio.ensure_future(call_when_updated())

def as_list():
    global _state
    ret = []
    for key, value in _state.items():
        ret += [{'channel_id': key, 'value': value}]
    return ret

def get():
    global _state
    return _state






