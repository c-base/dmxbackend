# -*- coding: utf-8 -*-
import pytest
from dmxbackend.channel_mapping import DMXMapping
from dmxbackend.channel_mapping import RGBMapping

def test_dmx_mapping():
    d = DMXMapping('Superlight', 'An der Säule', 0)
    assert d.address == 0


class TestRGBMapping:
    TEST_MODEL = 'Varytec Floodpanel 150'
    TEST_NAME = 'RGB light'

    @pytest.fixture
    def mapping(self):
        return RGBMapping(self.TEST_MODEL, self.TEST_NAME, 0, 0)

    def test_rgb_mapping(self, mapping):
        assert mapping.pixel == 0
        assert mapping.address == 0
        assert mapping.model == self.TEST_MODEL
        assert mapping.name == self.TEST_NAME

    def test_map_pixel_to_channels(self, mapping):
        result = mapping.map_pixel_to_channels([(31, 32, 33, 255)])
        assert len(result) == 3

    def test_map_pixel_to_channels_empty(self, mapping):
        result = mapping.map_pixel_to_channels([(31, 32, 33, 0)])
        assert len(result) == 0