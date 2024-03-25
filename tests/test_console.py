#!/usr/bin/python3

"""
File: test_console.py
Author: Teddy Deberdt
Date: 2024-03-25
Description:

"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestDoCreate(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_missing_class_name(self, mock_stdout):
        """Test `do_create` when no class name is given, expecting a specific error message."""
        HBNBCommand().do_create('')
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_class_does_not_exist(self, mock_stdout):
        """Test `do_create` with an invalid class name, expecting an error message for non-existent class."""
        HBNBCommand().do_create('NonExistentClass')
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_attribute_format_error(self, mock_stdout):
        """Test `do_create` with a malformed attribute string, checking for an attribute format error message."""
        HBNBCommand().do_create('User email="user@example.com" Password')
        self.assertIn(
            "** attribute format error **: Password (expected key=value)", mock_stdout.getvalue())
        # Using `assertIn` to allow for partial match, given that the entire error message may vary.

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_valid_attributes(self, mock_stdout):
        """
        Test for `do_create` with valid class name and attributes.
        """
        HBNBCommand().do_create('Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        # Here you should assert that the new object was correctly created and stored.
        # This might require mocking the storage system or checking the output.
        self.assertIn('76b65327-9e94-4632-b688-aaa22ab8a124',
                      mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
