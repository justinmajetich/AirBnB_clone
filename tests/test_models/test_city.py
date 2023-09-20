#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest


class test_City(unittest.TestCase,test_basemodel):
    """ Test city class"""

    def __init__(self, *args, **kwargs):
        """ Instance of city class """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test state_id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test city name """
        new = self.value()
        self.assertEqual(type(new.name), str)
