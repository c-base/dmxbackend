#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""main.py

Usage:
  main.py <usb_device> <qxw_file>
  
"""

import os
import sys
import logging
import asyncio
from aiohttp import web
from serial.aio import create_serial_connection
from docopt import docopt

from dmxbackend.animation import animation_loop
from dmxbackend.enttex_usb_dmx import EnttecProtocol
from dmxbackend.server import setup_web_app
from dmxbackend.parse_qxw import find_fixtures
from dmxbackend.parse_qxw import get_mapping_from_qxw
from dmxbackend.artnet_server import ArtNetServerProtocol

log = logging.getLogger(__file__)


def prepare_mapping(qxw_filename):
    fixtures = find_fixtures(qxw_filename)
    mapping = get_mapping_from_qxw(fixtures)
    for i, light in enumerate(mapping):
        log.info('%d, %s, %d' % (i, light.name, light.address))
    return mapping


def run_main_loop(usb_device, qxw_filename):
    loop = asyncio.get_event_loop()
    mapping = prepare_mapping(qxw_filename)
    image_queue = asyncio.Queue()

    ## USB-Serial device
    # Baud rate is not needed with the Enttec device because DMX's baudrate is fixed.
    usb_serial = create_serial_connection(loop, EnttecProtocol, usb_device)
    enttec_transport, enttec_protocol = loop.run_until_complete(usb_serial)

    ## ArtNet device UDP
    udp_listen = loop.create_datagram_endpoint(ArtNetServerProtocol, local_addr=('0.0.0.0', 6454))
    artnet_transport, artnet_protocol = loop.run_until_complete(udp_listen)
    artnet_protocol.enttec_protocol = enttec_protocol

    ## Animation play-back
    asyncio.ensure_future( animation_loop(loop, image_queue, 1/30, None, mapping) )

    ## Webserver
    app = setup_web_app(image_queue, mapping)

    try:
        web.run_app(app, loop=loop)
    except KeyboardInterrupt:
        pass

    artnet_transport.close()
    enttec_transport.close()
    loop.close()


if __name__ == '__main__':
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    arguments = docopt(__doc__, version='main.py 1.0')
    run_main_loop(arguments['<usb_device>'], arguments['<qxw_file>'])


