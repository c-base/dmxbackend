# -*- coding: utf-8 -*-
import asyncio
import logging

from .png_handling import get_single_line
from .png_handling import image_line_to_dmx
from . import channel_state

log = logging.getLogger(__name__)


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
            channel_state.update_dmx(dmx)
            
            await asyncio.sleep(frame_duration)
        log.debug("Animation done.")
