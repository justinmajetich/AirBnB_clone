#!/usr/bin/python3
"""Module that tests the console"""
import unittest
from unittest.mock import patch
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
        """Test if create State is present"""

        command = HBNBCommand()
        with patch('builtins.print') as mock_print:
            result = command.do_create("create_State")
        printed_output = mock_print.call_args[0][0]
        self.assertTrue(printed_output)

if __name__ == "__main__":
    unittest.main()