#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Test for the class State"""

    def __init__(self, *args, **kwargs):
        """ Initialization of the test State"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """A test to check for the name of the state """
        new = self.value()
        self.assertEqual(type(new.name), str)
