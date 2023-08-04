#!/usr/bin/python3
"""
Test validation test city
"""
from models.base_model import BaseModel
from models.city import City
from models.state import State
import unittest
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test case city"""

    def test_City_inheritance(self):
        """
        tests that the City class Inherits from BaseModel
        """
        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())
