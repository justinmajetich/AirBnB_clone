#!/usr/bin/python3
"""
Not empty
"""
import datetime
import inspect
import json
from os.path import exists
from os import remove
import unittest
import pep8
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Unittest for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """test for pep8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/base_model.py', 'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 1)
        self.assertTrue(len(BaseModel.save.__doc__) >= 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 1)


class test_basemodel(unittest.TestCase):
    """
    Not empty
    """

    def __init__(self, *args, **kwargs):
        """
        Makes a new object with only name and value
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        There's no setup steps yet.
        What would we need outside of init?
        """

    def tearDown(self):
        """
        Not empty
        """
        if exists('file.json'):
            remove('file.json')

    def test_default(self):
        """
        Tests that the type of a new object matches the one called for
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Makes two new models, and ensures they are actually separate objects
        """
        i = self.value()
        new = BaseModel(**(i.to_dict()))
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Creates a new object, copies it,
        And checks for an expected type error
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Create a new object, and compare its contents to file.json"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r', encoding='utf-8') as file:
            j = json.load(file)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Compares output of string method with desired result
        """
        i = self.value()
        self.assertEqual(str(i), f'[{self.name}] ({i.id}) {i.__dict__}')

    def test_todict(self):
        """
        Creates a new object and compares its data with its dictionary
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Creates a new object with one set of keyword arguments as 'none'
        And tests for expected error
        """
        test_obj = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**test_obj)

    def test_kwargs_one(self):
        """
        Creates object with one keyword and tests for expected error
        """
        test_obj = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**test_obj)

    def test_id(self):
        """
        Checks that the id of an object is a string (and not uuid)
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        Creates a new object and checks that 'created_at' is a datetime object
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Creates a new object, checks for a datetime variable called updated_at,
        Copies it to a new object, overwrites itself,
        And checks that creation and update times do not match
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        new_2 = new.to_dict()
        new = BaseModel(**new_2)
        self.assertFalse(new.created_at == new.updated_at)
