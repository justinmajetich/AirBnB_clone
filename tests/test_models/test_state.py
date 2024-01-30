#!/usr/bin/python3
"""Test module for the State class using unittest module
"""
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class test_state(TestBaseModel):
    """subClass of unittest to test State class """

    def __init__(self, *args, **kwargs):
        """ Init the state test class and its super"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test the State name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
