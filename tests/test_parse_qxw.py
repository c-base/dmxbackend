# -*- coding: utf-8 -*-
import os
import pytest
import xml.etree.ElementTree as ET

from dmxbackend.parse_qxw import get_mapping_from_qxw
from dmxbackend.parse_qxw import find_fixtures
from dmxbackend.parse_qxw import retrieve
from dmxbackend.parse_qxw import XML_NAMESPACE

@pytest.fixture
def qxw_file():
    fname = os.path.join(os.path.dirname(__file__), 'mainhall_2017_010.qxw')
    return open(fname, mode='r')


def test_find_fixtures(qxw_file):
    result = find_fixtures(qxw_file)
    assert len(result) == 23
    assert result[0].tag == '{http://www.qlcplus.org/Workspace}Fixture'


def test_get_mapping_from_qxw(qxw_file):
    fixtures = find_fixtures(qxw_file)
    result = get_mapping_from_qxw(fixtures)
    assert len(result) == 11
    assert result[0].pixel == 0
    assert result[1].pixel == 1


def test_retreive(qxw_file):
    tree = ET.parse(qxw_file)
    root = tree.getroot()
    eng = retrieve(root, 'Engine')[0]
    assert eng.tag == XML_NAMESPACE + 'Engine'


