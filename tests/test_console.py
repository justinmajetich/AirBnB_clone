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

    def test_true(self):
        """True test"""
        self.assertTrue(True)
