# -*- coding; utf-8 -*-
from PIL import Image


class DMXMapping(object):
    def __init__(self, name, address):
        self.name = name
        self.address = int(address)
        self.num_pixels = 1

    def map_pixel_to_channels(self, line):
        """

        :param line:
        :return: A tuple of (DMX address, value)
        """
        raise NotImplementedError()

    def __str__(self):
        return '{}: {03d}'.format(self.name, self.address)


class RGBMapping(DMXMapping):
    def __init__(self, name, address, pixel):
        """
        :param pixel: The pixel in the RGB
        :param channel: The DMX address of the first channel (red) - zero indexed
        """
        super().__init__(name, address)
        self.pixel = pixel

    def map_pixel_to_channels(self, line):
        mapped = []
        current_addr = self.address
        for i in range(self.num_pixels):
            pixel_val = line[self.pixel + i]
            # alpha channel
            if pixel_val[3] < 255:
                pass
            else:
                mapped += [
                    (current_addr    , pixel_val[0]),
                    (current_addr + 1, pixel_val[1]),
                    (current_addr + 2, pixel_val[2]),
                ]
            current_addr += 3
        return mapped


class GigabarMapping(RGBMapping):
    def __init__(self, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(name, int(address)+2, pixel)
        self.num_pixels = 8


def image_line_to_dmx(line, mapping_list, dmx_packet_old=None):
    dmx_packet = bytearray(512)
    for mapping in mapping_list:
        for dmx_addr, color_intensity in mapping.map_pixel_to_channels(line):
            dmx_packet[dmx_addr] = color_intensity
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


