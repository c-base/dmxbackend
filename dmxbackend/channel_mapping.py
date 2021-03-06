#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

class DMXMapping(object):
    def __init__(self, model, name, address):
        self.model = model
        self.name = name
        self.address = int(address)
        self.num_pixels = 1
        self.universe = 0
        self.pos_x = 0
        self.pos_y = 0

    def map_pixel_to_channels(self, line):
        """
        :param line:
        :return: A tuple of (DMX address, value)
        """
        raise NotImplementedError()

    def state_to_dmx(self, data):
        raise NotImplementedError()

    def dmx_to_state(self, dmx_data):
        raise NotImplementedError()

    @property
    def light_id(self):
        return 'dmx-%d-%d' % (self.universe + 1, self.address + 1)

    @property
    def elements(self):
        return []

    @property
    def channel_ids(self):
        return []

    def map_consecutive_channels(self, data_dict, channel_ids):
        ret = []
        for i, id in enumerate(channel_ids):
            ret.append((self.address + i, data_dict[id]))
        return ret

    def map_consecutive_dmx(self, dmx_data, first_address, channel_ids):
        ret = []
        for i, id in enumerate(channel_ids):
            ret.append((id, dmx_data[first_address + i]))
        return ret

    def __str__(self):
        return '{}: {}'.format(self.name, self.address)


class RGBMapping(DMXMapping):
    def __init__(self, model:str, name:str, address:int, pixel:int):
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
            try:
                pixel_val = line[self.pixel + i]
            except IndexError:
                log.warn('Not enough pixels: pixel {}'.format(self.pixel + i))
                continue
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

    def state_to_dmx(self, data_dict):
        channel_ids = [self.light_id + '/rgb/r', self.light_id + '/rgb/g', self.light_id + '/rgb/b']
        return self.map_consecutive_channels(data_dict, channel_ids)

    def dmx_to_state(self, dmx_data):
        channel_ids = [self.light_id + '/rgb/r', self.light_id + '/rgb/g', self.light_id + '/rgb/b']
        return self.map_consecutive_dmx(dmx_data, self.address, channel_ids)

    @property
    def channel_ids(self):
        return [
            self.light_id + '/rgb/r',
            self.light_id + '/rgb/g',
            self.light_id + '/rgb/b'
        ]

    @property
    def elements(self):
        ch = self.pixel * 3
        return [{
            'name': 'rgb',
            'pixel': self.pixel,
            'channels': [
                {'name': 'r', 'channel_id': self.light_id + '/rgb/r'},
                {'name': 'g', 'channel_id': self.light_id + '/rgb/g'},
                {'name': 'b', 'channel_id': self.light_id + '/rgb/b'}
            ]
        }]


class StairVilleMapping(RGBMapping):
    """
    The older StairVille models have a different channel layout.
    Channel 1 is mode, Channels 2-4 are RGB.
    """
    def __init__(self, model, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, int(address)+1, pixel)


class GigabarMapping(RGBMapping):
    def __init__(self, model, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, int(address)+2, pixel)
        self.num_pixels = 8

    @property
    def channel_ids(self):
        channels = []
        for i in range(self.num_pixels):
            part_name = 'rgb%d' % (i + 1)
            channels += [
                self.light_id + '/' + part_name + '/r',
                self.light_id + '/' + part_name + '/g',
                self.light_id + '/' + part_name + '/b',
            ]
        return channels

    @property
    def elements(self):
        parts = []
        for i in range(self.num_pixels):
            current_pixel = self.pixel + i
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

    def state_to_dmx(self, data_dict):
        channel_ids = self.channel_ids
        return self.map_consecutive_channels(data_dict, channel_ids)

    def dmx_to_state(self, dmx_data):
        channel_ids = self.channel_ids
        return self.map_consecutive_dmx(dmx_data, self.address, channel_ids)


class OctagonMapping(DMXMapping):
    def __init__(self, model, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, address)
        self.pixel = pixel
        self.num_pixels = 4

    @property
    def channel_ids(self):
        return [
            self.light_id + '/white/cw',
            self.light_id + '/white/ww',
            self.light_id + '/white/a',
            self.light_id + '/white/dim',
        ]

    @property
    def elements(self):
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

    def state_to_dmx(self, data_dict):
        channel_ids = [
            self.light_id + '/white/cw',
            self.light_id + '/white/ww',
            self.light_id + '/white/a',
            self.light_id + '/white/dim'
        ]
        return self.map_consecutive_channels(data_dict, channel_ids)

    def dmx_to_state(self, dmx_data):
        channel_ids = [
            self.light_id + '/white/cw',
            self.light_id + '/white/ww',
            self.light_id + '/white/a',
            self.light_id + '/white/dim'
        ]
        return self.map_consecutive_dmx(dmx_data, self.address, channel_ids)


class DimmerMapping(DMXMapping):
    def __init__(self, model, name, address, pixel):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, address)
        self.pixel = pixel
        self.num_pixels = 4

    @property
    def channel_ids(self):
        return [
            self.light_id + '/dimmer/dim1',
            self.light_id + '/dimmer/dim2',
            self.light_id + '/dimmer/dim3',
            self.light_id + '/dimmer/dim4',
        ]

    @property
    def elements(self):
        ch = self.pixel * 3
        return [{
            'name': 'dimmer',
            'pixel': self.pixel,
            'channels': [
                {'name': 'dim1', 'channel_id': self.light_id + '/dimmer/dim1'},
                {'name': 'dim2', 'channel_id': self.light_id + '/dimmer/dim2'},
                {'name': 'dim3', 'channel_id': self.light_id + '/dimmer/dim3'},
                {'name': 'dim4', 'channel_id': self.light_id + '/dimmer/dim4'}
            ],
        }]

    def state_to_dmx(self, data_dict):
        channel_ids = [
            self.light_id + '/dimmer/dim1',
            self.light_id + '/dimmer/dim2',
            self.light_id + '/dimmer/dim3',
            self.light_id + '/dimmer/dim4'
        ]
        return self.map_consecutive_channels(data_dict, channel_ids)

    def dmx_to_state(self, dmx_data):
        channel_ids = [
            self.light_id + '/dimmer/dim1',
            self.light_id + '/dimmer/dim2',
            self.light_id + '/dimmer/dim3',
            self.light_id + '/dimmer/dim4',
        ]
        return self.map_consecutive_dmx(dmx_data, self.address, channel_ids)

