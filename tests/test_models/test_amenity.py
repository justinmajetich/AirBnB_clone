#!/usr/bin/python3
"""tests for amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """tests for amenity class"""

    def __init__(self, *args, **kwargs):
        """test constructor for amenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test name for amenity"""
        new = self.value()
        self.assertEqual(type(new.name), str)
