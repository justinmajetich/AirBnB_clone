#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import os
import unittest

new = Amenity(name='Toaster')


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        self.assertEqual(type(new.name), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") is None, "Using \
                     DBStorage")
    def test_place_amenities(self):
        """ """
        self.assertEqual(type(new.place_amenities), list)
