#!/usr/bin/python3
""" Unittests for state class """
import unittest
from models.state import State
from tests.test_models.test_base_model import test_basemodel


class test_state(test_basemodel):
    """ Test class for state"""

    def __init__(self, *args, **kwargs):
        """ Test State instantiation"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test name type"""
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
