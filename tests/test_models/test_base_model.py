#!/usr/bin/python3
""" Unittest for class BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Unittest for class base_model"""

    def __init__(self, *args, **kwargs):
        """ Tests initialization of model """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ test setUp """
        pass

    def tearDown(self):
        """ Test teardow method of test class"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ test default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """  Test type int of kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        model = BaseModel()
        string = str(model)
        self.assertIsInstance(string, str)
        self.assertTrue("[BaseModel]" in string)
        self.assertTrue(model.id in string)

    def test_save(self):
        model = BaseModel()
        before = model.updated_at
        model.save()
        after = model.updated_at
        self.assertLess(before, after)

    def test_to_dict(self):
        model = BaseModel()
        dictionary = model.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertTrue("id" in dictionary)
        self.assertTrue("created_at" in dictionary)
        self.assertTrue("updated_at" in dictionary)
        self.assertTrue("__class__" in dictionary)
        self.assertEqual(dictionary["id"], model.id)
        self.assertEqual(dictionary["created_at"], model.created_at.isoformat())
        self.assertEqual(dictionary["updated_at"], model.updated_at.isoformat())
        self.assertEqual(dictionary["__class__"], "BaseModel")

    def test_kwargs_none(self):
        """  test if no kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ test if only one kwarg"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ test id type """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test created attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """  test updated attribute"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    """ part test """
    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        now = datetime.utcnow()
        kwargs = {
            "id": "123",
            "created_at": now,
            "updated_at": now,
            "test": "test_value"
        }
        model = BaseModel(**kwargs)
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at, now)
        self.assertEqual(model.updated_at, now)
        self.assertEqual(model.test, "test_value")
