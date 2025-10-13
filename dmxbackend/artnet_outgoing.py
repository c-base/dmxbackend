# -*- coding: utf-8 -*-
import asyncio
import logging

from dmxbackend import channel_state
from dmxbackend.artnet import *

log = logging.getLogger(__name__)


class ArtNetOutgoingProtocol(asyncio.Protocol):

    def __init__(self):
        super().__init__()
        self.sequence = 0
        self.enttec_protocol = None

    def connection_made(self, transport):
        self.transport = transport
        channel_state.subscribe_dmx(self.notify_dmx)

    def datagram_received(self, data, addr):
        # do nothing
        pass

    async def notify_dmx(self):
        """
        Called by the channel state when DMX values have changed in any of the
        allowed universes.
        """
        for universe in channel_state.UNIVERSES:
            dmx = channel_state.as_dmx(universe)
            self.sequence = (self.sequence + 1) % 256
            message = encode_artnet_packet(dmx, universe=universe, sequence=self.sequence)
            self.transport.sendto(message)
