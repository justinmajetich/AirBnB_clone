#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Tests for the class Amenity"""

    def __init__(self, *args, **kwargs):
        """ Initialization of the class Amenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test for the Amenity name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
