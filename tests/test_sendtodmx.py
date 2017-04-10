# -*- coding; utf-8 -*-
import pytest
from unittest.mock import MagicMock, Mock

from dmxbackend.sendtodmx import ArtNetError
from dmxbackend.sendtodmx import ArtNet


def test_artneterror_message():
    """
    Just check that the ArtNetError is there and can carry a message.
    """
    TEST_TEXT = 'something is wrong'
    e = ArtNetError(TEST_TEXT)
    assert e.message == TEST_TEXT


class TestArtNet(object):

    @pytest.fixture
    def artnet(self):
        return ArtNet(broadcast='127.0.0.1')

    def test_build_dmx_header(self, artnet):
        header = artnet.build_dmx_header()
        assert len(header) == 18

    def test_send(self, artnet):
        packet = b' ' * 530
        _udp = Mock()
        _udp.sendto = Mock()
        _udp.sendto.return_value = 530
        artnet._udp = _udp
        result = artnet.send(packet)
        assert result == True

    def test_send_dmx(self, artnet):
        dmx = b' ' * 512
        _udp = Mock()
        _udp.sendto = Mock()
        _udp.sendto.return_value = 530
        artnet._udp = _udp
        result = artnet.send_dmx(dmx)
        assert result == True