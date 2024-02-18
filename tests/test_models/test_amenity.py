#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity
from os import getenv

class test_Amenity(TestBaseModel):
    """ """
    if getenv("HBNB_TYPE_STORAGE") != "db":
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "Amenity"
            self.value = Amenity

        def test_name2(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.name), str)
