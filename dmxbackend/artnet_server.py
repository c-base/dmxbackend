# -*- coding: utf-8 -*-
import asyncio
import logging

from dmxbackend import channel_state
from dmxbackend.artnet import *

log = logging.getLogger(__name__)



class ArtNetServerProtocol(asyncio.Protocol):

    def __init__(self):
        super().__init__()
        self.enttec_protocol = None

    def connection_made(self, transport):
        self.transport = transport

    

    def datagram_received(self, data, addr):
        try:
            artnet_packet = decode_artnet_packet(data)
            log.debug("rcv u%s" % artnet_packet.universe)
        except ArtNetPollReceived:
            log.debug("Art-Net poll (opcode 0x2000) received.")
            return

        
        universe = artnet_packet.universe
        dmx = artnet_packet.dmx

        channel_state.update_dmx(dmx, universe)
        #if self.enttec_protocol is not None:
        #    self.enttec_protocol.send_dmx(dmx)

        #log.info('Sequence %d, %d bytes from %s' % (artnet_packet.sequence, len(dmx), addr))
        #log.debug(str(dmx))
        #for i,chunk in enumerate([dmx[i:i + 32] for i in range(0, len(dmx), 32)]):
        #    log.debug(' '.join(['%3d' % int(x) for x in range(i*32+1, (i+1)*32+1)]))
        #    log.debug(' '.join(['%3d' % int(x) for x in chunk]))

        #print('Send %r to %s' % (message, addr))
        #self.transport.sendto(data, addr)
