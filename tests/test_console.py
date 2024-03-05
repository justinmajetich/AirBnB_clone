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


@unittest.skipUnless(os.getenv('HBNB_TYPE_STORAGE') == 'file',
                     "requires FileStorage type")
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

    def test_value_string_quotes(self, stdout):
        """
        "<value>" => starts with a double quote
        """
        command = 'create State myname="Lagos'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        self.assertFalse(hasattr(self.objects[obj_id], 'myname'))

    def test_value_tring_values_underscore(self, stdout):
        """
        all underscores _ must be replace by spaces
        """
        command = 'create State name="Cape_Town"'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        attr = getattr(self.objects[obj_id], 'name', None)
        error_msg = "underscores not removed"
        self.assertEqual(attr, "Cape Town", msg=error_msg)

    # TODO: validate 'double quote inside the value escaped with \'

    def test_value_float(self, stdout):
        """
        Float: <unit>.<decimal> => contains a dot
        """
        command = 'create State name="Kampala" latitude=23.78138'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        attr = getattr(self.objects[obj_id], 'latitude', None)
        error_msg = "float not converted"
        self.assertEqual(attr, 23.78138, msg=error_msg)

    def test_value_float_with_non_digit(self, stdout):
        """
        value has '.' but contains non digit
        """
        command = 'create State name="Kampala" latitude=23.4abc'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        error_msg = "attribute should not be added"
        self.assertFalse(hasattr(self.objects[obj_id], 'latitude'),
                         msg=error_msg)

    def test_value_integer(self, stdout):
        """
        Integer: <number> => default case
        """
        command = 'create State name="Kampala" population=23000'
        self.onecmd(command)
        obj_id = "State." + stdout.getvalue().replace('\n', '')
        attr = getattr(self.objects[obj_id], 'population', None)
        error_msg = "interger conversion failed"
        self.assertEqual(attr, 23000, msg=error_msg)

    def test_value_unrecognized(self, stdout):
        """ unrecognized values """
        command = 'create State name="Normal"'
        self.onecmd(command)
        obj_id_0 = "State." + stdout.getvalue().replace('\n', '')
        command = 'create State name="Abnormal" cant_recognize_me'
        self.clear(stdout)
        self.onecmd(command)
        obj_id_1 = "State." + stdout.getvalue().replace('\n', '')
        len0 = len(self.objects[obj_id_0].__dict__)
        len1 = len(self.objects[obj_id_1].__dict__)
        error_msg = "lengths of these 2 objects must be equal"
        self.assertEqual(len0, len1, msg=error_msg)
