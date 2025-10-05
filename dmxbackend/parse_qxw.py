# -*- coding: utf-8 -*-
import logging
import xml.etree.ElementTree as ET
from .channel_mapping import (
    RGBMapping,
    StairVilleMapping,
    GigabarMapping,
    OctagonMapping,
    DimmerPackMapping,
    CameoRootPAR6Mapping,
    SonicPulseLEDBarMapping,
    RevueLED120Mapping,
    CompactPar7Q4Mapping,
    CompactPar18MKIIMapping,
    CB100LedColorMapping,
    LEDFloodPanel7x3WMapping,
    MirrorBallMotorMapping,
    TSL250ScanMapping,
)

log = logging.getLogger(__name__)

FIXTURE_XPATH = './' \
                '{http://www.qlcplus.org/Workspace}Engine/' \
                '{http://www.qlcplus.org/Workspace}Fixture'

# XML namespace
XML_NAMESPACE = '{http://www.qlcplus.org/Workspace}'


def retrieve(element, sub_element_name, ns=XML_NAMESPACE):
    full_name = ns + sub_element_name
    result = element.findall(full_name)
    return result


def find_fixtures(qxw_filename):
    """
    Get the DMX fixtures from the .qxw file
    """
    tree = ET.parse(qxw_filename)
    root = tree.getroot()
    fixtures = root.findall(FIXTURE_XPATH)
    return fixtures


def map_fixture(fixture, first_pixel):
    """
    Maps fixture tag from QXW file to to DMXMapping.
    :param fixture: The fixture that we need a mapping for.
    :return: List of DMXMapping instances.
    """
    name = retrieve(fixture, 'Name')[0].text
    manufacturer = retrieve(fixture, 'Manufacturer')[0].text
    model = retrieve(fixture, 'Model')[0].text
    universe = int(retrieve(fixture, 'Universe')[0].text)
    address = retrieve(fixture, 'Address')[0].text
    channels = retrieve(fixture, 'Channels')[0].text

    log.debug("Parsed univ %s, addr %s, name: %s" % (universe, address, name))
    if model == 'LED PAR56':
        if manufacturer == 'Stairville':
            return [StairVilleMapping(model, name, address, first_pixel, universe=universe)]
        elif manufacturer == 'Eurolite':
            return [RGBMapping(model, name, address, first_pixel, universe=universe)]
    elif model == 'LED PAR 36 COB RGBW 12W':
        return [SonicPulseLEDBarMapping(model, name, address, first_pixel, universe=universe)]
    elif model == 'LED Flood Panel 150':
        return [RGBMapping(model, name, address, first_pixel, universe=universe)]
    elif model == 'Gigabar II':
        return [GigabarMapping(model, name, address, first_pixel, univers=universe)]
    elif model == 'Octagon Theater 20x6W CW/WW/A' and int(channels) == 4 and 'octacon' in name.lower():
        # Model is called "Octacon" in the QXW file
        my_model = 'Octagon'
        return [OctagonMapping(my_model, name, address, first_pixel, universe=universe)]
    elif model == 'Generic' and int(channels) == 4 and 'dimmer' in name.lower():
        my_model = 'Dimmer 4 CH'
        return [DimmerPackMapping(my_model, name, address, first_pixel, universe=universe)]
    elif model == 'Generic RGB' and int(channels) == 3:
        my_model = 'RGB 3 CH'
        return [RGBMapping(my_model, name, address, first_pixel, universe=universe)]
    elif model == 'Root PAR 6' and int(channels) == 8:
        my_model = 'Root PAR 6'
        return [CameoRootPAR6Mapping(my_model, name, address, first_pixel, universe=universe)]
    elif model.strip() == 'RevueLED 120 COB' and int(channels) == 7:
        my_model = 'RevueLED 120 COB'
        return [RevueLED120Mapping(my_model, name, address, first_pixel, universe=universe)]
    elif model.strip() == 'Compact Par 7 Q4' and int(channels) == 6:
        my_model = 'Compact Par 7 Q4'
        return [CompactPar7Q4Mapping(my_model, name, address, first_pixel, universe=universe)]
    elif model.strip() == 'CB-100 LED Color' and int(channels) == 4:
        my_model = 'CB100 Led Color'
        return [CB100LedColorMapping(my_model, name, address, first_pixel, universe=universe)]
    elif model.strip() == 'LED Flood Panel 7x3W' and int(channels) == 4:
        my_model = 'LED Flood Panel 7x3W'
        return [LEDFloodPanel7x3WMapping(my_model, name, address, first_pixel, universe=universe)]
    elif model.strip() == 'MBM40D Mirror Ball Motor DMX':
        my_model = 'MBM40D Mirror Ball Motor DMX'
        return [MirrorBallMotorMapping(my_model, name, address, first_pixel, universe=universe)]
    elif model.strip() == 'LED TSL-250 Scan COB' and int(channels) == 10:
        my_model = 'LED TSL-250 Scan COB'
        return [TSL250ScanMapping(my_model, name, address, first_pixel, universe=universe)]
    elif model.strip() == 'Compact Par 18 MKII' and int(channels) == 6:
        my_model = 'Compact Par 18 MKII'
        return [CompactPar18MKIIMapping(my_model, name, address, first_pixel, universe=universe)]
    else:
        return []


def get_mapping_from_qxw(fixtures):
    """
    Map the fixture to DMXMapping instances.
    """
    final_mappings = []
    current_pixel = 0

    # We want the mappings be sorted by the address of the first DMX channel.
    # This simple accessor function is to be used with sorted(key=...).
    def address_of(fixture):
        return int(retrieve(fixture, 'Address')[0].text)

    # sort fixtures by their first DMX channel address
    for fixture in sorted(fixtures, key=address_of):
        mapped = map_fixture(fixture, current_pixel)
        for mapping in mapped:
            current_pixel = current_pixel + mapping.num_pixels
        final_mappings += mapped

    return final_mappings