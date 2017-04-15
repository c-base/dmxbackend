# -*- coding; utf-8 -*-
import os
import pytest
import asyncio
from PIL import Image
from dmxbackend.channel_mapping import DMXMapping
from dmxbackend.channel_mapping import RGBMapping
from dmxbackend.png_handling import image_line_to_dmx
from dmxbackend.png_handling import get_single_line


@pytest.fixture
def image():
    im = Image.open(os.path.join(os.path.dirname(__file__), 'tropical.png'), 'r')
    p = im.convert('RGBA')
    return p


def test_dmx_mapping():
    d = DMXMapping('Superlight', 0)
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


def test_image_line_to_dmx(image):
    mapping = [RGBMapping('RGB light', 0, 0)]
    result = asyncio.ensure_future(image_line_to_dmx(image, 0, mapping))
    assert result[0] == 0
    assert len(result) == 512


def test_get_single_line(image):
    result = get_single_line(image, 0)
    # Image is 172 by 178
    assert len(result) == 172
    # The resulting pixel should have 4 elements
    assert len(result[0]) == 4
    # alpha channel is 255
    assert result[0][3] == 255

