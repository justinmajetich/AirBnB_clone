#!/usr/bin/python3
""" Unittest for class State"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Unittest of State class """

    def __init__(self, *args, **kwargs):
        """ test of initialisation """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test of type name attribute """
        new = self.value()
        self.assertEqual(type(new.name), str)
