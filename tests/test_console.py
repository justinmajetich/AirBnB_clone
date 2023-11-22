#!/usr/bin/python3
"""
Unittests for console.py
"""


import unittest
import os
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand



class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_output(self, expected_output, mock_stdout):
        HBNBCommand().onecmd(expected_output)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    # Test methods for quitting the console
    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.assert_output("quit")

    def test_help_quit(self):
        self.assert_output("help quit")

    # Test methods for handling EOF
    def test_EOF(self):
        with self.assertRaises(SystemExit):
            self.assert_output("EOF")

    def test_help_EOF(self):
        self.assert_output("help EOF")

    # Add similar test methods for other commands (do_create, do_show, etc.)

    # Test methods for the 'create' command
    def test_create_no_args(self):
        self.assert_output("create")

    def test_create_invalid_class(self):
        self.assert_output("create InvalidClass")

    def test_create_valid_class(self):
        self.assert_output("create BaseModel")

    def test_create_with_params(self):
        self.assert_output('create BaseModel key="value"')

    # Test methods for the 'show' command
    def test_show(self):
        self.assert_output('show BaseModel')

    # Test methods for the 'destroy' command
    def test_destroy(self):
        self.assert_output('destroy BaseModel')

    # Test methods for the 'all' command
    def test_all(self):
        self.assert_output('all')

    def test_all_with_class(self):
        self.assert_output('all BaseModel')

    # Test methods for the 'count' command
    def test_count(self):
        self.assert_output('count BaseModel')

    # Test methods for the 'update' command
    def test_update(self):
        self.assert_output('update BaseModel')

    def test_update_with_params(self):
        self.assert_output('update BaseModel 1234 key="value"')

    # Add other test methods as needed

if __name__ == '__main__':
    unittest.main()

