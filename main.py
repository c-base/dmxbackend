#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""main.py

Usage:
  main.py <qxw_file> <positions_file> [--usb <usb_device>] [--mqtt <mqtt_server>] [--debug]

"""

import os
import sys
import logging
import asyncio
import configparser
import click
import serial_asyncio
from aiohttp import web

from dmxbackend.animation import animation_loop
from dmxbackend.enttex_usb_dmx import EnttecProtocol
from dmxbackend.server import setup_web_app
from dmxbackend.parse_qxw import find_fixtures, get_mapping_from_qxw
from dmxbackend.artnet_server import ArtNetServerProtocol
from dmxbackend import channel_state
from dmxbackend.mqtt import AsyncMQTT

log = logging.getLogger(__name__)


def prepare_mapping(qxw_filename, positions):
    fixtures = find_fixtures(qxw_filename)
    mapping = get_mapping_from_qxw(fixtures)
    for i, light in enumerate(mapping):
        try:
            light.pos_x = int(positions[light.name]['pos_x']) 
            light.pos_y = int(positions[light.name]['pos_y'])
            light.rot = int(positions[light.name].get('rot', 0))
            light.groups = [x.strip() for x in positions[light.name].get('groups', '').split(',') if x.isalnum()]
            light.hidden = bool(positions[light.name].get('hidden', False))
        except KeyError:
            pass
        except NameError:
            pass
        log.info(u'{}: (U: {}, DMX: {}) -> x={}, y={}'.format(light.name, light.universe, light.address,
                                                       light.pos_x, light.pos_y))
    return mapping


def run_main_loop(usb_device, second_usb_device, qxw_filename, pos_filename, mqtt_server, port, dev_mode):
    loop = asyncio.get_event_loop()
    positions = configparser.ConfigParser()
    positions.read(pos_filename)
    mapping = prepare_mapping(qxw_filename, positions)
    image_queue = asyncio.Queue()

    ## USB-Serial device
    enttec_protocol = None
    if usb_device is not None:
        # Baud rate is not needed with the Enttec device because DMX's baudrate is fixed.
        def enttec_protocal_factory():
            return EnttecProtocol(universe=0)
        usb_serial = serial_asyncio.create_serial_connection(loop, enttec_protocal_factory, usb_device, baudrate=250000)
        enttec_transport, enttec_protocol = loop.run_until_complete(usb_serial)

    if second_usb_device is not None:
        # Baud rate is not needed with the Enttec device because DMX's baudrate is fixed.
        def second_enttec_protocal_factory():
            return EnttecProtocol(universe=1)
        usb_serial = serial_asyncio.create_serial_connection(loop, second_enttec_protocal_factory, usb_device, baudrate=250000)
        enttec_transport, enttec_protocol = loop.run_until_complete(usb_serial)

    ## ArtNet device UDP
    udp_listen = loop.create_datagram_endpoint(ArtNetServerProtocol, local_addr=('0.0.0.0', 6454))
    artnet_transport, artnet_protocol = loop.run_until_complete(udp_listen)
    # tell the artnet protocol about the USB device
    artnet_protocol.enttec_protocol = enttec_protocol

    ## Animation play-back
    asyncio.ensure_future( animation_loop(loop, image_queue, 1/30, None, mapping) )

    ## Webserver
    app = setup_web_app(image_queue, mapping, dev_mode)
    channel_state.initialize_state(mapping)
    print(f"++++{channel_state._state}")
    if mqtt_server is not None:
        async_mqtt = AsyncMQTT()
        #asyncio.ensure_future(async_mqtt.every_semisecond(loop))
        asyncio.ensure_future(async_mqtt.mqtt_loop(loop, mqtt_server))

    try:
        web.run_app(app, loop=loop, port=port)
    except KeyboardInterrupt:
        pass

    artnet_transport.close()
    enttec_transport.close()
    loop.close()


@click.command()
@click.argument('qxw_file')
@click.argument('pos_file')
@click.option('--usb', default=None, help='USB device')
@click.option('--second-usb', default=None, help='second universe USB device')
@click.option('--mqtt', default=None, help='MQTT server')
@click.option('--port', default=80, help='Web server port')
@click.option('--devmode', default=False)
def main(qxw_file, pos_file, usb, second_usb, mqtt, port, devmode):
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    dev_mode_on = True
    if devmode is False:
        dev_mode_on = False

    run_main_loop(usb, second_usb, qxw_file, pos_file, mqtt, port, dev_mode_on)


if __name__ == '__main__':
    main()