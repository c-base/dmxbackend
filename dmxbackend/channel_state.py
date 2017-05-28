# -*- coding: utf-8 -*-
"""
Manages the current state of the lights. You can subscribe to updates.
"""
import asyncio
from collections import OrderedDict
from datetime import datetime
import logging

_state = None
_last_update = None
_subscribers = []
_dmx_subscribers = []
_last_notify = datetime.now()
_last_dmx_notify = datetime.now()
_dmx = None
_mapping = None


log = logging.getLogger(__name__)


def initialize_state(mapping):
    global _state
    global _last_update
    global _dmx
    global _mapping
    _dmx = bytearray(512)
    _state = OrderedDict()
    _mapping = mapping
    for light in mapping:
        for id in light.channel_ids:
            _state[id] = 0x00
    _last_update = datetime.now()


def update_channels(new_data):
    global _last_update
    global _dmx
    global _state

    log.debug("Before update: {}".format(_state))
    for el in new_data:
        _state[el['channel_id']] = el['value']
    log.debug("After update:  {}".format(_state))

    # convert channels to DMX
    for light in _mapping:
        try:
            for dmx_addr, val in light.state_to_dmx(_state):
                _dmx[dmx_addr] = val
        except NotImplementedError:
            log.debug("state_to_dmx() not implemented in {}".format(light))

    _last_update = datetime.now()
    notify()


def update_dmx(new_dmx):
    global _state
    global _dmx
    global _last_update
    global _mapping

    # convert DMX to channel mapping
    for light in _mapping:
        try:
            for channel_id, val in light.dmx_to_state(new_dmx):
                _state[channel_id] = val
        except NotImplementedError:
            log.debug("dmx_to_state() not implemented in {}".format(light))

    _dmx = bytearray(new_dmx)
    _last_update = datetime.now()
    notify()


def subscribe(call_when_updated):
    _subscribers.append(call_when_updated)


def subscribe_dmx(call_when_updated):
    _dmx_subscribers.append(call_when_updated)


def notify():
    global _last_notify
    global _last_dmx_notify
    now = datetime.now()

    # Update the the outgoing channels every second.
    if (now - _last_notify).total_seconds() >= 1.0:
        for call_when_updated in _subscribers:
            asyncio.ensure_future(call_when_updated())
        for call_when_updated in _dmx_subscribers:
            asyncio.ensure_future(call_when_updated())
        return

    # Update DMX 25 times per second if the other channels did not update.
    if (now - _last_notify).total_seconds() >= 0.04:
        for call_when_updated in _dmx_subscribers:
            asyncio.ensure_future(call_when_updated())

        
def fixtures():
    global _mapping
    ret = []
    for id, light in enumerate(_mapping):
        one_light = {
            'fixture_id': "dmx-%d-%d" % (1, light.address + 1),
            'name': light.name,
            'pos_x': light.pos_x,
            'pos_y': light.pos_y,
            'elements': light.elements
        }
        ret.append(one_light)
    return ret


def as_list():
    global _state
    ret = []
    for key, value in _state.items():
        ret += [{'channel_id': key, 'value': value}]
    return ret


def as_dmx():
    global _dmx
    return _dmx


def as_dict():
    global _state
    return _state






