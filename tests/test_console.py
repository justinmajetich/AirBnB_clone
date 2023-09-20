#!/usr/bin/python3
""" To test the 'do_create' function using the 'unittest' module. """
import unittest
from unittest.mock import patch
from console import HBNBCommand


class test_docreate(unittest.TestCase):

    def setUp(self):
        # Create an instance of HBNBCommand for testing
        self.cmd = HBNBCommand()

    def tearDown(self):
        # Clean up any resources after each test
        pass

    @patch('builtins.print')  # Mock the print function for testing
    def test_create_object_no_parameters(self, mock_print):
        # Test case for create command with no parameters
        self.cmd.onecmd("create")
        mock_print.assert_called_with("** class name missing **")

    @patch('builtins.print')
    def test_create_object_invalid_class(self, mock_print):
        # Test case for create command with invalid class
        self.cmd.onecmd("create InvalidClass")
        mock_print.assert_called_with("** class doesn't exist **")

    @patch('builtins.print')
    def test_create_object_valid_parameters(self, mock_print):
        # Test case for create command with valid parameters
        self.cmd.onecmd('create BaseModel name="Test Object" value=42')
        # Replace with the actual ID
        mock_print.assert_called_with('SomeGeneratedID')

    @patch('builtins.print')
    def test_create_object_invalid_parameter_format(self, mock_print):
        # Test case for create command with invalid parameter format
        self.cmd.onecmd('create BaseModel invalid_format')
        mock_print.assert_called_with("** invalid parameter format **")


if __name__ == '__main__':
    unittest.main()
