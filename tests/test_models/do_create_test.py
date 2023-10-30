#!/usr/bin/python3
"""
Unittests for create command in HBNB console
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_string(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel name="My House"')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # The output should be a UUID

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_float(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel price=123.45')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # The output should be a UUID

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_valid_integer(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel age=25')
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # The output should be a UUID

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_attribute(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel invalid_attr=123')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** attribute doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_float_value(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel price=invalid_float')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** invalid float value **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_parameter_format(self, mock_stdout):
        HBNBCommand().onecmd('create BaseModel name=InvalidName"')
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** invalid parameter format **")
