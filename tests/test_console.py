#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from os import getenv


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "Not a database")
class test_HBNBCommand(unittest.TestCase):
    """Tests the HBNBCommand class in console.py"""

    @patch('sys.stdout')
    def test_do_create(self, obj):
        """Tests do_create method"""
