#!/usr/bin/python3
"""testing for the City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """testing for the City"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
