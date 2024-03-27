#!/usr/bin/python3
""" Unittests for amenity class """
import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel


class test_Amenity(test_basemodel):
    """ Test class amenity"""

    def __init__(self, *args, **kwargs):
        """ Test the amenity instantiation"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test name value"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
