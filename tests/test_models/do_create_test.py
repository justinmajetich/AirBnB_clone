#!/usr/bin/python3
"""
Unittests for create command in HBNB console
"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys

# Append parent directory to the sys.path
sys.path.append('..')

from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    """Tests the create command in the HBNB console"""

    @classmethod
    def setUpClass(cls):
        """Set up the environment before running tests"""
        cls.mock_stdout = StringIO()
        cls.mock_stdin = StringIO()
        cls.command = HBNBCommand(stdout=cls.mock_stdout, stdin=cls.mock_stdin)

    def test_create_no_parameters(self):
        """Test create command with no parameters"""
        with patch('sys.stdout', new=self.mock_stdout):
            self.command.onecmd("create")
        output = self.mock_stdout.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_create_unknown_class(self):
        """Test create command with an unknown class"""
        with patch('sys.stdout', new=self.mock_stdout):
            self.command.onecmd("create SomeClass")
        output = self.mock_stdout.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_create_string_parameter(self):
        """Test create command with string parameters"""
        with patch('sys.stdout', new=self.mock_stdout):
            self.command.onecmd('create BaseModel name="My_little_house"')
        output = self.mock_stdout.getvalue()
        self.assertTrue(len(output.strip()) == 36)  # Length of UUID

    def test_create_integer_parameter(self):
        """Test create command with integer parameters"""
        with patch('sys.stdout', new=self.mock_stdout):
            self.command.onecmd('create BaseModel number_rooms=4 max_guest=10')
        output = self.mock_stdout.getvalue()
        self.assertTrue(len(output.strip()) == 36)  # Length of UUID

    def test_create_float_parameter(self):
        """Test create command with float parameters"""
        with patch('sys.stdout', new=self.mock_stdout):
            self.command.onecmd('create BaseModel price_by_night=300.50 latitude=37.77')
        output = self.mock_stdout.getvalue()
        self.assertTrue(len(output.strip()) == 36)  # Length of UUID

    def test_create_multiple_parameters(self):
        """Test create command with multiple parameters"""
        with patch('sys.stdout', new=self.mock_stdout):
            self.command.onecmd('create BaseModel name="My_little_house" number_rooms=4 max_guest=10')
        output = self.mock_stdout.getvalue()
        self.assertTrue(len(output.strip()) == 36)  # Length of UUID

    @classmethod
    def tearDownClass(cls):
        """Clean up after running tests"""
        cls.mock_stdout.close()
        cls.mock_stdin.close()

if __name__ == '__main__':
    unittest.main()