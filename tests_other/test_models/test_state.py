#!/usr/bin/python3
"""
test module for testing city models
"""

import unittest
import inspect
import pycodestyle
import json
import os
import datetime
from models.base_model import BaseModel
from models import state
State = state.State


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel class """

    def setUp(self):
        """ general test setup, will create a temp baseModel """
        self.temp_b = State()
        self.temp_b1 = State()

    def tearDown(self):
        """ general tear down, will delete the temp baseModel """
        self.temp_b = None
        self.temp_b1 = None

    def test_type_creation(self):
        """ will test the correct type of creation """
        self.assertEqual(type(self.temp_b), State)
        self.assertEqual(type(self.temp_b1), State)

    def test_uuid(self):
        """test UUID for BaseModel """
        self.assertNotEqual(self.temp_b.id, self.temp_b1.id)
        self.assertRegex(self.temp_b.id,
                         '^[0-9a-f]{8}-[0-9a-f]{4}'
                         '-[0-9a-f]{4}-[0-9a-f]{4}'
                         '-[0-9a-f]{12}$')
        self.assertRegex(self.temp_b1.id,
                         '^[0-9a-f]{8}-[0-9a-f]{4}'
                         '-[0-9a-f]{4}-[0-9a-f]{4}'
                         '-[0-9a-f]{12}$')

    def test_default_values(self):
        """ will test the ability to update """
        self.assertEqual(self.temp_b.name, "")

    def test_str_method(self):
        """ will test the __str__ method to ensure it is working """
        returned_string = str(self.temp_b)
        test_string = f"[State] ({self.temp_b.id}) {self.temp_b.__dict__}"
        self.assertEqual(returned_string, test_string)

    def test_to_dict(self):
        """tests the to_dict method to ensure it is working """
        temp_b_dict = self.temp_b.to_dict()
        self.assertEqual(str, type(temp_b_dict['created_at']))
        self.assertEqual(temp_b_dict['created_at'],
                         self.temp_b.created_at.isoformat())
        self.assertEqual(temp_b_dict['__class__'],
                         self.temp_b.__class__.__name__)
        self.assertEqual(temp_b_dict['id'], self.temp_b.id)

    def test_updated_time(self):
        """test that updated time gets updated"""
        time1 = self.temp_b.updated_at
        self.temp_b.save()
        time2 = self.temp_b.updated_at
        self.assertNotEqual(time1, time2)
        self.assertEqual(type(time1), datetime.datetime)
