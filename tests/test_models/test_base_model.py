#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test the kwargs of the base model"""
        i = self.value()
        i.name = "My first model"
        i.number = 89
        i_dict = i.to_dict()
        i2 = self.value(**i_dict)
        self.assertEqual(i.id, i2.id)
        self.assertEqual(i.created_at, i2.created_at)
        self.assertEqual(i.updated_at, i2.updated_at)
        self.assertEqual(i.name, i2.name)
        self.assertEqual(i.number, i2.number)
        self.assertNotEqual(i, i2)
        self.assertEqual(type(i.created_at), type(i2.created_at))
        self.assertEqual(type(i.updated_at), type(i2.updated_at))
        self.assertEqual(type(i.name), type(i2.name))
        self.assertEqual(type(i.number), type(i2.number))
        self.assertEqual(i.__dict__, i2.__dict__)
        self.assertEqual(i.to_dict(), i2.to_dict())
        self.assertEqual(i.__str__(), i2.__str__())
        self.assertEqual(str(i), str(i2))

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

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
