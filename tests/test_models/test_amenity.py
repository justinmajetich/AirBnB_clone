#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test Case"""

    def __init__(self, *args, **kwargs):
        """attribute initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """checks if the name attribute is of type str"""
        new = self.value()
        self.assertEqual(type(new.name), str)
