#!/usr/bin/python3
"""Test module for BaseModel"""

import unittest
import datetime
import json
import os
from uuid import UUID
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for BaseModel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test instantiation with no arguments"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instantiation with **kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test instantiation with **kwargs containing an int"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """Test __str__ method"""
        i = self.value()
        expected_str = '[{}] ({}) {}'.format(self.name, i.id, i.__dict__)
        self.assertEqual(str(i), expected_str)

    def test_todict(self):
        """Test to_dict method"""
        i = self.value()
        self.assertEqual(i.to_dict(), i.to_dict())

    def test_kwargs_none(self):
        """Test instantiation with **kwargs containing None"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test instantiation with **kwargs containing only one arg"""
        n = {'name': 'test'}
        new = self.value(**n)
        self.assertTrue(isinstance(new, BaseModel))

    def test_id(self):
        """Test id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

if __name__ == "__main__":
    unittest.main()
