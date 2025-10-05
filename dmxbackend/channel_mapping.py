#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)


class DMXMapping(object):
    def __init__(self, model: str, name: str, address: int, universe: int=0):
        self.model = model
        self.name = name
        self.address = int(address)
        self.num_pixels = 1
        self.universe = int(universe)
        self.pos_x = 0
        self.pos_y = 0
        self.rot = 0
        self.groups = []
        self.hidden = False

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
            ret.append((self.universe, self.address + i, data_dict[id]))
        return ret

    def map_consecutive_dmx(self, dmx_data, first_address, channel_ids):
        ret = []
        for i, id in enumerate(channel_ids):
            ret.append((self.universe, id, dmx_data[first_address + i]))
        return ret

    def __str__(self):
        return '{}: {}'.format(self.name, self.address)


class RGBMapping(DMXMapping):
    def __init__(self, model:str, name:str, address:int, pixel:int, universe:int=0):
        """
        :param pixel: The pixel in the RGB
        :param channel: The DMX address of the first channel (red) - zero indexed
        """
        super().__init__(model, name, address, universe=universe)
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
    def __init__(self, model, name, address, pixel, universe=0):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, int(address)+1, pixel)


class GigabarMapping(RGBMapping):
    def __init__(self, model, name, address, pixel, universe=0):
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


class SonicPulseLEDBarMapping(RGBMapping):
    def __init__(self, model, name, address, pixel, universe=0):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, address, pixel, universe=universe)
        self.num_pixels = 1

    @property
    def channel_ids(self):
        channels = [
            self.light_id + '/rgb/r',
            self.light_id + '/rgb/g',
            self.light_id + '/rgb/b',
            self.light_id + '/white/whi',
        ]
        return channels

    @property
    def elements(self):
        return [
            {
                'name': 'rgb',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'r', 'channel_id': self.light_id + '/rgb/r'},
                    {'name': 'g', 'channel_id': self.light_id + '/rgb/g'},
                    {'name': 'b', 'channel_id': self.light_id + '/rgb/b'},
                ]
            },
            {
                'name': 'white',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'whi', 'channel_id': self.light_id + '/white/whi'},
                ],
            }
        ]

    def state_to_dmx(self, data_dict):
        channel_ids = self.channel_ids
        return self.map_consecutive_channels(data_dict, channel_ids)

    def dmx_to_state(self, dmx_data):
        channel_ids = self.channel_ids
        return self.map_consecutive_dmx(dmx_data, self.address, channel_ids)


class OctagonMapping(DMXMapping):
    def __init__(self, model, name, address, pixel, universe):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, address, universe=universe)
        self.pixel = pixel
        self.num_pixels = 4

    @property
    def channel_ids(self):
        return [
            self.light_id + '/coldwhite/cw',
            self.light_id + '/warmwhite/ww',
            self.light_id + '/amber/amb',
            self.light_id + '/dimmer/dim',
        ]

    @property
    def elements(self):
        ch = self.pixel * 3
        return [
            {
                'name': 'dimmer',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'dim', 'channel_id': self.light_id + '/dimmer/dim'},
                ],
            },
            {
                'name': 'coldwhite',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'cw', 'channel_id': self.light_id + '/coldwhite/cw'},
                ],
            },
            {
                'name': 'warmwhite',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'ww', 'channel_id': self.light_id + '/warmwhite/ww'},
                ],
            },
            {
                'name': 'amber',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'amb', 'channel_id': self.light_id + '/amber/amb'},
                ],
            },
        ]

    def state_to_dmx(self, data_dict):
        return self.map_consecutive_channels(data_dict, self.channel_ids)

    def dmx_to_state(self, dmx_data):
        return self.map_consecutive_dmx(dmx_data, self.address, self.channel_ids)


class DimmerPackMapping(DMXMapping):
    def __init__(self, model, name, address, pixel, universe=0):
        # the first 2 addresses in 26-channel mode are reserved for functions
        super().__init__(model, name, address, universe=universe)
        self.pixel = pixel
        self.num_pixels = 1

    @property
    def channel_ids(self):
        return [
            self.light_id + '/dimmerpack/dim1',
            self.light_id + '/dimmerpack/dim2',
            self.light_id + '/dimmerpack/dim3',
            self.light_id + '/dimmerpack/dim4',
        ]

    @property
    def elements(self):
        ch = self.pixel * 3
        return [{
            'name': 'dimmerpack',
            'pixel': self.pixel,
            'channels': [
                {'name': 'dim1', 'channel_id': self.light_id + '/dimmerpack/dim1'},
                {'name': 'dim2', 'channel_id': self.light_id + '/dimmerpack/dim2'},
                {'name': 'dim3', 'channel_id': self.light_id + '/dimmerpack/dim3'},
                {'name': 'dim4', 'channel_id': self.light_id + '/dimmerpack/dim4'}
            ],
        }]

    def state_to_dmx(self, data_dict):
        return self.map_consecutive_channels(data_dict, self.channel_ids)

    def dmx_to_state(self, dmx_data):
        return self.map_consecutive_dmx(dmx_data, self.address, self.channel_ids)


class CameoRootPAR6Mapping(DMXMapping):
    def __init__(self, model, name, address, pixel, universe=0):
        super().__init__(model, name, address, universe=universe)
        self.pixel = pixel
        self.num_pixels = 1

    @property
    def channel_ids(self):
        return [
            self.light_id + '/dimmer/dim',
            self.light_id + '/strobe/str',
            self.light_id + '/rgb/r',
            self.light_id + '/rgb/g',
            self.light_id + '/rgb/b',
            self.light_id + '/white/whi',
            self.light_id + '/amber/amb',
            self.light_id + '/uv/uv'
        ]

    @property
    def elements(self):
        return [
            {
                'name': 'rgb',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'r', 'channel_id': self.light_id + '/rgb/r'},
                    {'name': 'g', 'channel_id': self.light_id + '/rgb/g'},
                    {'name': 'b', 'channel_id': self.light_id + '/rgb/b'}
                ],
            },
            {
                'name': 'dimmer',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'dim', 'channel_id': self.light_id + '/dimmer/dim'},
                ],
            },
            {
                'name': 'strobe',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'str', 'channel_id': self.light_id + '/strobe/str'},
                ],
            },
            {
                'name': 'white',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'whi', 'channel_id': self.light_id + '/white/whi'},
                ],
            },
            {
                'name': 'amber',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'amb', 'channel_id': self.light_id + '/amber/amb'},
                ],
            },
            {
                'name': 'uv',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'uv', 'channel_id': self.light_id + '/uv/uv'},
                ],
            },
            ]

    def state_to_dmx(self, data_dict):
        return self.map_consecutive_channels(data_dict, self.channel_ids)

    def dmx_to_state(self, dmx_data):
        return self.map_consecutive_dmx(dmx_data, self.address, self.channel_ids)


class RevueLED120Mapping(DMXMapping):
    def __init__(self, model, name, address, pixel, universe=0):
        super().__init__(model, name, address, universe=universe)
        self.pixel = pixel
        self.num_pixels = 1

    @property
    def channel_ids(self):
        return [
            self.light_id + '/rgb/r',
            self.light_id + '/rgb/g',
            self.light_id + '/rgb/b',
            self.light_id + '/warmwhite/ww',
            self.light_id + '/dimmer/dim',
            self.light_id + '/strobe/str',
            self.light_id + '/auto/prg',
        ]

    @property
    def elements(self):
        return [
            {
                'name': 'rgb',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'r', 'channel_id': self.light_id + '/rgb/r'},
                    {'name': 'g', 'channel_id': self.light_id + '/rgb/g'},
                    {'name': 'b', 'channel_id': self.light_id + '/rgb/b'}
                ],
            },
            {
                'name': 'warmwhite',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'ww', 'channel_id': self.light_id + '/warmwhite/ww'},
                ],
            },
            {
                'name': 'dimmer',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'dim', 'channel_id': self.light_id + '/dimmer/dim'},
                ],
            },
            {
                'name': 'strobe',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'str', 'channel_id': self.light_id + '/strobe/str'},
                ],
            },
            {
                'name': 'auto',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'prg', 'channel_id': self.light_id + '/auto/prg'},
                ],
            },
        ]

    def state_to_dmx(self, data_dict):
        return self.map_consecutive_channels(data_dict, self.channel_ids)

    def dmx_to_state(self, dmx_data):
        return self.map_consecutive_dmx(dmx_data, self.address, self.channel_ids)


class CompactPar7Q4Mapping(DMXMapping):
    def __init__(self, model, name, address, pixel, universe=0):
        super().__init__(model, name, address, universe=universe)
        self.pixel = pixel
        self.num_pixels = 1

    @property
    def channel_ids(self):
        return [
            self.light_id + '/dimmer/dim',
            self.light_id + '/strobe/str',
            self.light_id + '/rgb/r',
            self.light_id + '/rgb/g',
            self.light_id + '/rgb/b',
            self.light_id + '/white/whi',
        ]

    @property
    def elements(self):
        return [
            {
                'name': 'dimmer',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'dim', 'channel_id': self.light_id + '/dimmer/dim'},
                ],
            },
            {
                'name': 'strobe',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'str', 'channel_id': self.light_id + '/strobe/str'},
                ],
            },
            {
                'name': 'rgb',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'r', 'channel_id': self.light_id + '/rgb/r'},
                    {'name': 'g', 'channel_id': self.light_id + '/rgb/g'},
                    {'name': 'b', 'channel_id': self.light_id + '/rgb/b'}
                ],
            },
            {
                'name': 'white',
                'pixel': self.pixel,
                'channels': [
                    {'name': 'whi', 'channel_id': self.light_id + '/white/whi'},
                ],
            },
        ]

    def state_to_dmx(self, data_dict):
        return self.map_consecutive_channels(data_dict, self.channel_ids)

    def dmx_to_state(self, dmx_data):
        return self.map_consecutive_dmx(dmx_data, self.address, self.channel_ids)