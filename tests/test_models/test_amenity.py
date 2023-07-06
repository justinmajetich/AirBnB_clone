#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.amenity = self.value()
        self.amenity.name = "Internet"

    def test_name(self):
        """ """
        self.assertEqual(type(self.amenity.name), str)
