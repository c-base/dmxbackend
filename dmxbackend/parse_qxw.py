# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from .channel_mapping import (
    RGBMapping,
    StairVilleMapping,
    GigabarMapping,
    OctagonMapping,
    DimmerMapping,
)

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
    address = retrieve(fixture, 'Address')[0].text
    channels = retrieve(fixture, 'Channels')[0].text

    if model == 'LED PAR56':
        if manufacturer == 'Stairville':
            return [StairVilleMapping(model, name, address, first_pixel)]
        elif manufacturer == 'Eurolite':
            return [RGBMapping(model, name, address, first_pixel)]
    elif model == 'LED Flood Panel 150':
        return [RGBMapping(model, name, address, first_pixel)]
    elif model == 'Gigabar II':
        return [GigabarMapping(model, name, address, first_pixel)]
    elif model == 'Generic' and int(channels) == 4 and 'octacon' in name.lower():
        # Model is called "Octacon" in the QXW file
        my_model = 'Octagon'
        return [OctagonMapping(my_model, name, address, first_pixel)]
    elif model == 'Generic' and int(channels) == 4 and 'dimmer' in name.lower():
        my_model = 'Dimmer 4 CH'
        return [DimmerMapping(my_model, name, address, first_pixel)]
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