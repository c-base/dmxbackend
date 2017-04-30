# -*- coding; utf-8 -*-
import logging

log = logging.getLogger(__name__)

def image_line_to_dmx(line, mapping_list, dmx_packet_old=None):
    dmx_packet = bytearray(512)
    for mapping in mapping_list:
        try:
            for dmx_addr, color_intensity in mapping.map_pixel_to_channels(line):
                dmx_packet[dmx_addr] = color_intensity
        except NotImplementedError:
            log.warn('Not implemented pixel to channels')
    return dmx_packet


async def get_single_line(image, line_number):
    """
    Returns a single, one-pixel high line from the image
    :param image:
    :param line_number: Which one?
    :return:
    """
    width, height = image.size
    line = []
    for x in range(width):
        line.append(image.getpixel((x, line_number)))
    return line


