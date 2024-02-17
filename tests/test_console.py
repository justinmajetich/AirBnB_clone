#!/usr/bin/python3
"""Test Cases for the console. NOT WORKING"""

import json
import unittest
import os
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestDoCreate(unittest.TestCase):
    """Test cases for do_create module"""

    def setUp(self):
        """set up module"""

        self.command = HBNBCommand()

    def tearDown(self):
        """Tear down"""

        HBNBCommand.classes = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_do_create_with_attributes(self):
        """Test do_create method with attributes"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.command.onecmd("create State name='California'")
            created_id = mock_stdout.getvalue().strip()

        # Verify that the object is created and stored in the dictionary
        self.assertTrue(created_id)

        # Verify that the object is saved in the file
        with open("file.json", "r") as file:
            data = json.load(file)
            self.assertIn(created_id, data["State"])

        # Clean up the file after the test
        # os.remove("file.json")
