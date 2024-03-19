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
        self.n = {'Name': 'test'}
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

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

    def test_kwargs_types(self):
        """Test if types remain the same as attribute
            types when using kwargs"""
        # Define a BaseModel instance with known attribute types
        base_model = BaseModel()
        attribute_types_before = {key: type(getattr(base_model, key))
                                  for key in base_model.__dict__.keys()}

        # Create a BaseModel instance with kwargs
        base_model = BaseModel(id='test_id', __class__='BaseModel',
                               created_at='2024-01-01T00:00:00.000000',
                               updated_at='2024-01-01T00:00:00.000000')
        attribute_types_after = {key: type(getattr(base_model, key))
                                 for key in base_model.__dict__.keys()}

        # Compare attribute types before and after setting attributes
        self.assertEqual(attribute_types_before, attribute_types_after)

    def test_empty_kwargs(self):
        """Test if kwargs is empty"""
        base_model = BaseModel()
        self.assertEqual(len(base_model.to_dict()), 4)

    # def test_kwargs_with_none_value(self):
    #     """Test if kwargs has a value of None for both key and value"""
    #     base_model = BaseModel(id=None, created_at=None, updated_at=None)
    #     expected_dict = {'id': None, 'created_at': None, 'updated_at': None}
    #     self.assertEqual(base_model.__dict__, expected_dict)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    @unittest.skip("Skipping test because dictionary is passed")
    def test_kwargs_one(self):
        """ """
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
        self.assertFalse(new.created_at == new.updated_at)
