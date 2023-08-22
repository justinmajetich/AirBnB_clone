#!/usr/bin/python3
""" Module used to test  the base model """

import os
import json
import unittest
import datetime
from models.base_model import BaseModel
from uuid import UUID


class test_basemodel(unittest.TestCase):
    """ Test class for base model """

    def __init__(self, *args, **kwargs):
        """ Constructor for test_basemodel class """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def setUp(self):
        """ """
        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertRaises(KeyError)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)


if __name__ == "__main__":
    unittest.main()
