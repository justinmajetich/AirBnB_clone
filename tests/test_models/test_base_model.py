#!/usr/bin/python3
"""Module for testing the base model"""
from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class test_basemodel(unittest.TestCase):
    """Class to test the base model"""
    def __init__(self, *args, **kwargs):
        """Initializing tests"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Default test"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """a"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """a"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

#    def test_save(self):
#        """Testing save"""
#        i = self.value()
#        key = self.name + "." + i.id
#        with open('file.json', 'r') as f:
#            j = json.load(f)
#            self.assertEqual(j[key], i.to_dict())
#        i.save()

    def test_str(self):
        """a"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test equality property"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Check for no key word argument"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

#    def test_kwargs_one(self):
#        """Check one key word argument"""
#        n = {'Name': 'test'}
#        with self.assertRaises(KeyError):
#            new = self.value(**n)

    def test_id(self):
        """a"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """a"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """a"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertTrue(new.created_at, new.updated_at)
