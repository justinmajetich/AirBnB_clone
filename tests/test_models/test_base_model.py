#!/usr/bin/python3
""" Unittest for class BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
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
