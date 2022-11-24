#!/usr/bin/python3
"""test for state"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test"""
        new = self.value(name="Alabama")
        self.assertEqual(type(new.name), str)
