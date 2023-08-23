#!/usr/bin/python3
"""
unittest for the console
"""
import unittest
import pep8
import os
import json
import console
import tests
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestForConsole(unittest.TestCase):
    """
    Unittest for the console
    """

    @classmethod
    def setUpClass(cls):
        """
        setup for test
        """
        cls.console_instance = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """
        tear it down after the test
        """
        cls.console_instance = None

    def test_pep8_console(self):
        """
        checks that the console code complies with PEP 8
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "PEP8 style fix")

    def test_emptyline(self):
        """
        Test if the emptyline method works as expected
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.emptyline()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")

    def test_all(self):
        """
        Test if the do_all method works as expected
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.do_all("")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_do_create_string_param(self):
        """
        Test object creation with string parameter
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.do_create("User name=\"John_Doe\"")
            output = mock_stdout.getvalue().strip()
            self.assertIn("User", output)
            self.assertIn("name", output)
            self.assertIn("John Doe", output)


if __name__ == '__main__':
    unittest.main()
