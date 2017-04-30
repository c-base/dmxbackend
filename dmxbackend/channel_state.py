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
    _dmx = new_dmx

    # convert DMX to channel mapping
    # convert channels to DMX
    for light in _mapping:
        try:
            for channel_id, val in light.state_to_dmx(_state):
                log.debug('channel_id: %s, val: %d' % (channel_id, val))
                _state[channel_id] = val
        except NotImplementedError:
            log.debug("dmx_to_state() not implemented in {}".format(light))


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


def as_dmx():
    global _dmx
    return _dmx


def as_dict():
    global _state
    return _state






