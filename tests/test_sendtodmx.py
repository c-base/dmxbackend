from dmxbackend import sendtodmx

import pytest
from dmxbackend.sendtodmx import ArtNetError
from dmxbackend.sendtodmx import ArtNet

def test_artneterror_message():
    TEST_TEXT = 'something is wrong'
    e = ArtNetError(TEST_TEXT)
    assert e.message == TEST_TEXT


def test_artnet():
    a = ArtNet(broadcast='127.0.0.1')