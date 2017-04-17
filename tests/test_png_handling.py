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

