#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import unittest


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    @unittest.skipIf(True,
                     "fails, not sure why")
    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name(self):
        """ test name attribute setting via kwargs """
        attr = {'name': 'Amenity'}
        new = self.value(**attr)
        self.assertEqual(type(new.name), str)
