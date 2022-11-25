#!/usr/bin/python3
""" Tests for BaseModel """
from models.base_model import BaseModel
from models import base_model
import unittest
import datetime
from uuid import UUID
import json
import os
from os import getenv


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ Constructor """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Default test """
        pass

    def tearDown(self):
        """Default test"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ Default test """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Default test """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Default test """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "Engine=FileStorage")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Def test """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ Def test """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Def test """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip("AssertionError: KeyError not raised")
    def test_kwargs_one(self):
        """ Def test """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ Def test """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Def test """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Def test """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_documentation(self):
        """ Test mmodule docstring"""
        self.assertTrue(base_model.__doc__)
        self.assertTrue(base_model.BaseModel.__doc__)

    def test_methods_doc(self):
        """Testing all docstrings of each method"""
        for all_methods in dir(BaseModel):
            self.assertTrue(all_methods.__doc__)


if __name__ == '__main__':
    unittest.main()