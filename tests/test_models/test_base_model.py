#!/usr/bin/python3
"""This module tests the BaseModel class"""

import os
import unittest
import datetime
import json
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_default(self):
        """Tests for the BaseModel class"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Tests for the BaseModel class"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test update with integer keyword argument"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            _ = BaseModel(**copy)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "file")
    def test_save(self):
        """Testing save"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open("file.json", "r", encoding="utf-8") as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Tests the string representation of the BaseModel class"""
        i = self.value()
        dictionary = i.get_dict_without_sa_instance()
        self.assertEqual(
            str(i), f"[{self.name}] ({i.id}) {dictionary}"
        )

    def test_to_dict(self):
        """Tests the `to_dict` method of the BaseModel class"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test update with None keyword argument"""
        n = {None: None}
        with self.assertRaises(TypeError):
            _ = self.value(**n)

    def test_kwargs_one(self):
        """Tests instantiating with one keyword argument"""
        n = {"name": "test"}
        instance = self.value(**n)

        self.assertIn("name", instance.__dict__)
        self.assertIn("test", instance.__dict__.values())

    def test_id(self):
        """Tests the id of the BaseModel class"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "file")
    def test_created_at(self):
        """Tests the `created_at` attribute of the BaseModel class"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "file")
    def test_updated_at(self):
        """Tests the `updated_at` attribute of the BaseModel class"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        new.save()
        self.assertFalse(new.created_at == new.updated_at)
