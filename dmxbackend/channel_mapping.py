#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-


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

    @property
    def channels(self):
        return []

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

    @property
    def channels(self):
        ch = self.pixel * 3
        return [{
            'name': 'rgb',
            'pixel': self.pixel,
            'channels': [
                {'name': 'r', 'offset':  ch + 0},
                {'name': 'g', 'offset':  ch + 1},
                {'name': 'b', 'offset':  ch + 2}],
        }]




class GigabarMapping(RGBMapping):
    def __init__(self, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(name, int(address)+2, pixel)
        self.num_pixels = 8

    @property
    def channels(self):
        parts = []
        for i in range(self.num_pixels):
            current_pixel = self.pixel + i
            ch = current_pixel * 3
            parts += [{
                'name': 'rgb%d' % (i + 1),
                'pixel': current_pixel,
                'channels': [
                    {'name': 'r', 'offset': ch + 0},
                    {'name': 'g', 'offset': ch + 1},
                    {'name': 'b', 'offset': ch + 2}],
            }]
        return parts