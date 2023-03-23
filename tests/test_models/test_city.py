#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test Case"""

    def __init__(self, *args, **kwargs):
        """attribute initialization"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """check if the type of the state_id attribute is a string."""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """check if the type is a string"""
        new = self.value()
        self.assertEqual(type(new.name), str)
