#!/usr/bin/python3
"""
This module defines test class for the City model
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    Define test for the City model
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class instance
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Ensure that the `state_id` attribute of the class is a string
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        Ensure that the `name` attribute of the class is a string
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
