#!/usr/bin/python3
"""This module tests the City class"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City
from models.state import State


class TestCity(TestBaseModel):
    """Tests the City class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests the state_id attribute of the City class"""
        new = self.value()
        state = State()
        new.state_id = state.id
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Tests the name attribute of the City class"""
        new = self.value()
        new.name = "Accra"
        self.assertEqual(type(new.name), str)
