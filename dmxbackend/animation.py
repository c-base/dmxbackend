# -*- coding: utf-8 -*-
import asyncio
import logging

from .png_handling import get_single_line
from .png_handling import image_line_to_dmx
from .sendtodmx import ArtNet

log = logging.getLogger(__file__)


async def animation_loop(loop, queue, frame_duration, artnet, mapping):
    log.info("Animation queue ready to process images ...")
    dmx_packet = bytearray(512)
    while True:
        log.debug("Waiting for next image from queue ...")
        image = await queue.get()
        log.debug("Got image from queue.")
        width, height = image.size
        length = height * frame_duration
        log.info("Animation playing ({} seconds) ...".format(length))
        for line_number in range(height):
            line = await get_single_line(image, line_number)
            dmx = image_line_to_dmx(line, mapping, dmx_packet)
            # dmx = dmx[:36]
            # for i,chunk in enumerate([dmx[i:i + 32] for i in range(0, len(dmx), 32)]):
            #    print(' '.join(['%3d' % int(x) for x in range(i*32+1, (i+1)*32+1)]))
            #    print(' '.join(['%3d' % int(x) for x in chunk]))
            log.debug(line_number, '|'.join('{:02x}'.format(x) for x in dmx))
            #if line_number > -1:
            #    artnet = ArtNet(broadcast='10.0.1.133')
            #    artnet.send_dmx(dmx)
            #    await asyncio.sleep(0.01)

            artnet = ArtNet(broadcast='10.0.1.134') #'10.0.1.133')
            artnet.send_dmx(dmx)
            await asyncio.sleep(frame_duration)
        log.debug("Animation done.")
