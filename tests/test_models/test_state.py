#!/usr/bin/python3
""" File for unit testing on the state class"""
import models
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State

class TestState(test_basemodel):
    """ Unit testing for state class """

    def setUp(self):
        """ Initialization for state instance """
        super().setUp()
        self.name = "State"
        self.value = State
        self.state = State(name="Oklahoma")

    def test_name(self):
        """ Testing name for state instance """
        self.assertEqual(type(self.state.name), str)
        self.assertEqual(self.state.name, "Oklahoma")

if __name__ == "__main__":
    unittest.main()