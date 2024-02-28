#!/usr/bin/python3
"""Module that tests the console"""
import unittest
from console import HBNBCommand
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
    def create_state(self):
        result = HBNBCommand.do_create("create_State")
        self.assertEqual(HBNBCommand.do_create(result, result.id))