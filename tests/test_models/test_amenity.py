#!/usr/bin/python3
""" Module to test amenity """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


@unittest.skip("For now")
class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
