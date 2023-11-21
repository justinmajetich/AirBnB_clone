#!/usr/bin/python3
"""
Test script contains test classes for Amenity model
"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """
    Test class for Amenity model
    """

    def __init__(self, *args, **kwargs):
        """
        constructor for test class
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test 'name' attribute of Amenity model
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
