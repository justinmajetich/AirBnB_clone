#!/usr/bin/python3
"""test for amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ test class for amenity """

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test """
        new = self.value(name="kjgjkjh")
        self.assertEqual(type(new.name), str)