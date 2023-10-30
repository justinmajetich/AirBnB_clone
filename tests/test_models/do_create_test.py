#!/usr/bin/python3
"""
Unittests for create command in HBNB console
"""

import unittest
from console import HBNBCommand
from io import StringIO
import sys

class TestConsoleCreateParams(unittest.TestCase):
    """Test create command with parameters."""

    def setUp(self):
        self.console = HBNBCommand()
        self.orig_stdout = sys.stdout
        self.orig_stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()

    def tearDown(self):
        sys.stdout = self.orig_stdout
        sys.stderr = self.orig_stderr

    def test_create_state_with_name(self):
        self.console.onecmd('create State name="California"')
        output = sys.stdout.getvalue()
        self.assertTrue(len(output) == 36)
        
    def test_create_state_with_invalid_params(self):
        self.console.onecmd('create State invalid_param="test"')
        output = sys.stdout.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_create_place_with_params(self):
        self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        output = sys.stdout.getvalue()
        self.assertTrue(len(output) == 36)

    def test_create_place_with_invalid_params(self):
        self.console.onecmd('create Place invalid_param="test"')
        output = sys.stdout.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_create_no_class_name(self):
        self.console.onecmd('create')
        output = sys.stdout.getvalue()
        self.assertEqual(output, "** class name missing **\n")

if __name__ == '__main__':
    unittest.main()
