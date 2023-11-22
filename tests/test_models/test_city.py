#!/usr/bin/python3
""" """
import unittest
from models.city import City


class test_City(unittest.TestCase):
    """ """

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

    def test_invalid_param(self):
        """test that an invalid parameter is not considered"""
        new = self.value({"invalid_param": "value"})
        self.assertNotIn("invalid_param", new.to_dict())
