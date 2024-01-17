#!/usr/bin/python3
"""
testing module for city
"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    test class for city
    """

    def __init__(self, *args, **kwargs):
        """
        __init__
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        test_state_id
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        test_name
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
