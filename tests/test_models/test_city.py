#!/usr/bin/python3
""" Unittest for class City """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ Unittest for City class"""

    def __init__(self, *args, **kwargs):
        """ test initiation of class City"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test type of state_id attribute """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test type of name attribute """
        new = self.value()
        self.assertEqual(type(new.name), str)
