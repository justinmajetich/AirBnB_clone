#!/usr/bin/python3
"""Module that tests the console"""
import unittest
from models.base_model import BaseModel
from models import storage
import os

class test_console(unittest.TestCase):
    """Class to test the console"""
    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Default test"""
        i = self.value()
        self.assertEqual(type(i), self.value)
