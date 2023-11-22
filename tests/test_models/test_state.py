#!/usr/bin/python3
""" """
import unittest
from models.state import State


class test_state(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_invalid_param(self):
        """test that an invalid parameter is not considered"""
        new = self.value({"invalid_param": "value"})
        self.assertNotIn("invalid_param", new.to_dict())
