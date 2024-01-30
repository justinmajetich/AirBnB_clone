#!/usr/bin/python3
"""
module that contains unittests for the Base class
"""
from models.base_model import BaseModel
import unittest
from unittest.mock import patch
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """
    unittest subclass that test the BaseModle class
    """

    def __init__(self, *args, **kwargs):
        """
        Initiate super class and setting some attrs
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Setup steps for the test cases
        """

    def tearDown(self):
        """
        Clean up steps after each test case
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    @patch("models.storage", **{"new.return_value": None})
    def test_default(self, storage):
        """
        test instanation of the BaseModel class
        """
        instance = self.value()
        self.assertEqual(type(instance), self.value)
        self.assertFalse(instance.created_at == instance.updated_at)
        self.assertTrue(storage.new.called)

    def test_kwargs(self):
        """
        create a BaseModel class by using kwargs
        """
        instance = self.value()
        copy = instance.to_dict()
        new = self.value(**copy)
        self.assertFalse(new is instance)
        self.assertDictEqual(new.to_dict(), instance.to_dict())

    def test_kwargs_int(self):
        """Test wrong keys on the kwargs dict initiaten """
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @patch("models.storage", **{"save.return_value": None})
    def test_save(self, storage):
        """ Testing save method
        """
        instance = self.value()
        updated_at = instance.updated_at
        instance.save()

        self.assertNotEqual(instance.updated_at, updated_at)
        self.assertTrue(storage.save.called)

    def test_str(self):
        """ Testing the __str__ method"""
        instance = self.value()
        str_inst = '[{}] ({}) {}'.format(self.name, instance.id,
                                         instance.__dict__)
        self.assertEqual(str(instance), str_inst)

    def test_todict(self):
        """Test the BaseModel.todic method """
        instance = self.value()
        n = instance.to_dict()
        self.assertDictEqual(instance.to_dict(), n)

    def test_kwargs_none(self):
        """Test the kwargs with None """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """
        Test invalide value of the kwargs dict
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """
        Test the BaseModel.id attribute type and uniqueness
        """
        new_1 = self.value()
        new_2 = self.value()
        self.assertEqual(type(new_1.id), str)
        self.assertNotEqual(new_1.id, new_2.id)

    def test_created_at(self):
        """
        Test BaseModel.created_at attribute
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Test BaseModel.updated_at attribute
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)

    def test_updated_creted_format(self):
        """
        Test BaseModel.updated_at and BaseModel.created_at format
        """
        import re

        new = self.value()
        update = new.to_dict()["updated_at"]
        create = new.to_dict()["created_at"]
        pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}")

        self.assertRegex(update, pattern)
        self.assertRegex(create, pattern)
