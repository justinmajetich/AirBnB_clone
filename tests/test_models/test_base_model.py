#!/usr/bin/python3
"""
Test module containing unit tests for BaseModel class
"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Test case for BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for test case
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Setup method to prepare resources before each test
        """
        pass

    def tearDown(self):
        """
        Tear down method to clean up resources after each test
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """
        Test case for creating an instance of Base model
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """
        Test case for creating an instance of BaseModel using kwargs
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        Test case for creating instance with non-string key in kwargs
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """
        Testing casee for saving instance of BaseModel
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Test case for string representation of Basemodel
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        Testcase for converting an instance to a dictionary
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Testcase for creating an instance with None in kwargs
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        Testcase for creating an instance with a single key in kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        Testcase for checking the type of id attribute
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """
        Test case for checking type of created_at atribute
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test case for checking type and values of updated_at attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
