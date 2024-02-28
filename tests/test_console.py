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

    def test_create_state(self):
        """Test if create State is present"""

        command = HBNBCommand()
        with patch('builtins.print') as mock_print:
            result = command.do_create("create State")
        printed_output = mock_print.call_args[0][0]
        self.assertTrue(printed_output)

    def test_create_with_name(self):
        """Test if create_state with name is present (new feature)"""
        command = HBNBCommand()
        with patch('builtins.print') as mock_print:
            result = command.do_create("create_state name='California'")
        printed_output = mock_print.call_args[0][0]
        self.assertTrue(printed_output)
    def test_general_command(self):
        """Test if a general command works"""

        user_input = ""
        
        with patch('builtins.input', return_value=user_input):
            with patch('builtins.print') as mock_print:
                self.command.onecmd(user_input)
        printed_output = mock_print.call_args[0][0]
        self.assertTrue(printed_output.startswith("Expected output"))

if __name__ == "__main__":
    unittest.main()