#!/usr/bin/python3
""" test for state class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest

class test_state(unittest.TestCase,test_basemodel):
    """test state class """

    def __init__(self, *args, **kwargs):
        """ initialize the state class for testing """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test for name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
