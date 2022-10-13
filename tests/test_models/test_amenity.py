#!/usr/bin/python3
""" Testing Amenity Class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test Cases for Amenity"""

    def __init__(self, *args, **kwargs):
        """ Test instantiation """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_is_a_public_str(self):
        """ Testing name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
