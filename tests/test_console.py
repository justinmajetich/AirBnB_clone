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
        len_before = len(self.objects)
        command = 'create State name="Kampala"'
        self.onecmd(command)
        len_after = len(self.objects)
        self.assertNotEqual(len_before, len_after)
        
        self.clear(stdout)
        command = 'create State myname = "California"'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        self.assertFalse(hasattr(self.objects[obj_id], 'myname'))


    def test_string_values_quotes(self, stdout):
        """
        "<value>" => starts with a double quote
        """
        command = 'create State myname="Lagos'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        self.assertFalse(hasattr(self.objects[obj_id], 'myname'))
    
    def test_string_values_underscore(self, stdout):
        """
        all underscores _ must be replace by spaces
        """
        command = 'create State name="Cape_Town"'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        attr = getattr(self.objects[obj_id], 'name', None)
        error_msg = "underscores not removed"
        self.assertEqual(attr, "Cape Town", msg=error_msg)
