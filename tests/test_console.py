#!/usr/bin/python3
"""Unittest module for console.py"""

import unittest
from unittest.mock import patch
import io
import os
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test cases for the console module"""

    def setUp(self):
        """Sets up test environment"""
        self.console = HBNBCommand()
        self.file_storage = storage
        self.default_prompt = '(hbnb) '

    def tearDown(self):
        """Cleans up test environment"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_create_with_params(self):
        # Test creating a new User instance with parameters
        command = 'create User email="test@test.com" password="pass123"'
        self.assertFalse('test@test.com' in self.file_storage.all().values())
        self.console.onecmd(command)
        self.assertTrue('test@test.com' in self.file_storage.all().values())

        # Test creating a new Place instance with parameters
        command = 'create Place name="My house" city_id="123" price=1000.50'
        self.assertFalse('My house' in self.file_storage.all().values())
        self.console.onecmd(command)
        self.assertTrue('My house' in self.file_storage.all().values())