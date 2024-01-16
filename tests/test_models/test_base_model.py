#!/usr/bin/python3
"""module for the test_basemodel class """
import datetime
import json
import os
import unittest
from uuid import UUID

from models.base_model import BaseModel


class test_basemodel(unittest.TestCase):
    """tests for the BaseModel"""

    def __init__(self, *args, **kwargs):
        """initializes the test_basemodel class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """setUp method for tests"""
        pass

    def tearDown(self):
        """tearDown method for tests"""
        try:
            os.remove('file.json')
        except Exception as err:
            print(f"An error occured from tearDown: {err}")

    def test_default(self):
        """tests for default values"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """tests for kwargs method"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """tests for kwargs as integer key-value"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing the save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """tests the format print to stdout"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """tests for to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """tests for kwargs being none for key-value"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """tests for one key-value pair"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """test for id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test for created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """test for updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
