#!/usr/bin/python3
"""
unittest model for testing the Aminty class
"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class test_Amenity(TestBaseModel):
    """
    A unnittest subclass to test the Amenity class
    """

    def __init__(self, *args, **kwargs):
        """
        Init method for the class
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Test the name attribute of the Amenity
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
