#!/usr/bin/python3
"""unitest for testing BaseModel class """
from models.base_model import Base, BaseModel
import unittest
import datetime
from uuid import UUID
import json
from os import getenv
import os


class test_basemodel(unittest.TestCase):
    """ Unittests for testing the basemodel class"""

    def __init__(self, *args, **kwargs):
        """ inicialization values """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Set Up """
        pass

    def tearDown(self):
        """ Tear Down """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Test default values of instance """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test creation of an instance with dictionary"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Test method dictionary and update method """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """Check str format """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test to_dict method """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test dictionary with none arguments"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Test dictionary with arguments"""
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertEqual(type(new), self.value)

    def test_id(self):
        """ Test id of the instante"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test creation of the instance"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test update method """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
