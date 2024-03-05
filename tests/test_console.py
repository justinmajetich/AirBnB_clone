#!/usr/bin/python3
"""Test module for console.py."""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage
from tests import test_file, BaseTest
from unittest.mock import patch
from io import StringIO


@patch('sys.stdout', new_callable=StringIO)
class TestConsoleDoCreate(BaseTest):
    """Test the do_create method."""

    def test_param_syntax(self, stdout):
        """
        Param syntax: <key name>=<value>
        """
        command = 'create State name="California"'
        self.onecmd(command)
        self.assertNotEqual(len(stdout.getvalue()), 0)
        
        command = 'create State name = "California"'
        self.onecmd(command)
        self.assertEqual(len(stdout.getvalue()), 0)

