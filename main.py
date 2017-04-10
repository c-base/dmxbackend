#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import asyncio
from aiohttp import web
from dmxbackend.server import setup_web_app
from dmxbackend.parse_qxw import find_fixtures
from dmxbackend.parse_qxw import get_mapping_from_qxw
from dmxbackend.png_handling import get_single_line
from dmxbackend.png_handling import image_line_to_dmx

from dmxbackend.sendtodmx import ArtNet
# app.router.add_get('/{name}', handle)
t = [
    bytearray(b'\xff\x00\x00'),
    bytearray(b'\x00\xff\x00'),
    bytearray(b'\x00\x00\xff'),
]

async def animation_loop(loop, queue, frame_duration, artnet, mapping):
    print("Queue ready to process images ...")
    dmx_packet = bytearray(512)
    while True:
        print("Waiting for next image from queue ...")
        image = await queue.get()
        print("Got image from queue.")
        width, height = image.size
        length = height * frame_duration
        print("Animation playing ({} seconds) ...".format(length))
        for line_number in range(height):
            line = await get_single_line(image, line_number)
            dmx = image_line_to_dmx(line, mapping, dmx_packet)
            # dmx = t[line_number % len(t)]
            # dmx = dmx[:36]
            #for i,chunk in enumerate([dmx[i:i + 32] for i in range(0, len(dmx), 32)]):
            #    print(' '.join(['%3d' % int(x) for x in range(i*32+1, (i+1)*32+1)]))
            #    print(' '.join(['%3d' % int(x) for x in chunk]))
            print(dmx)
            if line_number > -1:
                artnet = ArtNet(broadcast='10.0.1.133')
                artnet.send_dmx(dmx)
                await asyncio.sleep(0.01)

            artnet = ArtNet(broadcast='10.0.1.133')
            artnet.send_dmx(dmx)
            await asyncio.sleep(frame_duration)
        print("Animation done.")
    return True


def prepare_mapping():
    with open('tests/mainhall_2017_010.qxw', mode='r') as qxw_file:
        fixtures = find_fixtures(qxw_file)
    mapping = get_mapping_from_qxw(fixtures)
    return mapping


loop = asyncio.get_event_loop()
image_queue = asyncio.Queue()
mapping = prepare_mapping()
#artnet = None# ArtNet(broadcast='10.0.1.133')
# artnet = ArtNet(broadcast='127.0.0.1')
asyncio.ensure_future( animation_loop(loop, image_queue, 1/30, None, mapping) )
app = setup_web_app(image_queue)
web.run_app(app, loop=loop)
