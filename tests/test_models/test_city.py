#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Tests for the class City"""

    def __init__(self, *args, **kwargs):
        """ Initialization of the test City"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test to check for the state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Test to check for the City name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
