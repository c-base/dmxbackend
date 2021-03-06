# -*- coding: utf-8 -*-
import pytest

from dmxbackend.channel_mapping import RGBMapping
from dmxbackend.channel_state import (
    as_dict,
    initialize_state,
    update_channels,
)


@pytest.fixture
def mapping():
    return [RGBMapping('RGB light', 'right', 0, 0)]


def test_uninitialized_state():
    assert as_dict() == None


def test_initialize_state(mapping):
    initialize_state(mapping)
    assert as_dict()['dmx-1-1/rgb/r'] == 0x00


def test_update_state(mapping):
    initialize_state(mapping)
    update_channels([{'channel_id': 'dmx-1-1/rgb/r', 'value': 0xff}])
    assert as_dict()['dmx-1-1/rgb/r'] == 0xff