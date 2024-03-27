#!/usr/bin/python3
""" Unittests for City class"""
import unittest
from models.city import City
from tests.test_models.test_base_model import test_basemodel


class test_City(test_basemodel):
    """ Test class for city"""

    def __init__(self, *args, **kwargs):
        """ Test class instantiation """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test state id type"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ Test name type """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
