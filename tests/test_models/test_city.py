#!/usr/bin/python3
"""Module for testing city"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """City testing class"""

    def __init__(self, *args, **kwargs):
        """Initializing city tests"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """State ID tests"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """City name tests"""
        new = self.value()
        self.assertEqual(type(new.name), str)
