#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-


class DMXMapping(object):
    def __init__(self, model, name, address):
        self.model = model
        self.name = name
        self.address = int(address)
        self.num_pixels = 1
        self.universe = 0

    def map_pixel_to_channels(self, line):
        """

        :param line:
        :return: A tuple of (DMX address, value)
        """
        raise NotImplementedError()

    @property
    def light_id(self):
        return 'dmx-%d-%d' % (self.universe + 1, self.address + 1)

    @property
    def channels(self):
        return []

    def __str__(self):
        return '{}: {03d}'.format(self.name, self.address)


class RGBMapping(DMXMapping):
    def __init__(self, model, name, address, pixel):
        """
        :param pixel: The pixel in the RGB
        :param channel: The DMX address of the first channel (red) - zero indexed
        """
        super().__init__(model, name, address)
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
                {'name': 'r', 'channel_id': self.light_id + '/rgb/r'},
                {'name': 'g', 'channel_id': self.light_id + '/rgb/g'},
                {'name': 'b', 'channel_id': self.light_id + '/rgb/b'}
            ],
        }]


class GigabarMapping(RGBMapping):
    def __init__(self, model, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, int(address)+2, pixel)
        self.num_pixels = 8

    @property
    def channels(self):
        parts = []
        for i in range(self.num_pixels):
            current_pixel = self.pixel + i
            ch = current_pixel * 3
            part_name = 'rgb%d' % (i + 1)
            parts += [{
                'name': part_name,
                'pixel': current_pixel,
                'channels': [
                    {'name': 'r', 'channel_id': self.light_id + '/' + part_name + '/r'},
                    {'name': 'g', 'channel_id': self.light_id + '/' + part_name + '/g'},
                    {'name': 'b', 'channel_id': self.light_id + '/' + part_name + '/b'}
                ],
            }]
        return parts


class OctagonMapping(DMXMapping):
    def __init__(self, model, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, address)
        self.pixel = pixel
        self.num_pixels = 4

    @property
    def channels(self):
        ch = self.pixel * 3
        return [{
            'name': 'white',
            'pixel': self.pixel,
            'channels': [
                {'name': 'cw',  'channel_id': self.light_id + '/white/cw'},
                {'name': 'ww',  'channel_id': self.light_id + '/white/ww'},
                {'name': 'a',   'channel_id': self.light_id + '/white/a'},
                {'name': 'dim', 'channel_id': self.light_id + '/white/dim'}
            ],
        }]