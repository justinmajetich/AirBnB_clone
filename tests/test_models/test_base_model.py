#!/usr/bin/python3
"""
Test for BaseModel class
"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Definition of tests for the class
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the class
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Set up the method for each test
        """
        pass

    def tearDown(self):
        """
        Tear down method for each test
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """
        Ensure default instance creation works
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Ensure keyword arguments can be used to create instance of the class
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Ensure that integers can't be passed as keywords
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        Ensure that the save method in the class works properly
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Ensure that the class instances are well represented in string format
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        Ensure that instances of the class can be returned as a dictionary
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Ensure that `None` type can't be used as a keyword argument
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        """
        print("new.created_at: {}\t|\tnew.updated_at {}".format(
            new.created_at, new.updated_at))
        """
        self.assertFalse(new.created_at == new.updated_at)
