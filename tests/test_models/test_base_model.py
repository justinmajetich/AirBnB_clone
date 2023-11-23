#!/usr/bin/python3
"""
module for testing base model class
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test the base model class"""
    def test_uuid(self):
        """Test the uuid of the base model"""
        base = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base.id, base2.id)

    def test_default(self):
        """Test the type fo the base model"""
        base = BaseModel()
        self.assertEqual(type(base), BaseModel)

    def test_save(self):
        """Test the save method of the base model"""
        base = BaseModel()
        base.save()
        self.assertNotEqual(base.created_at, base.updated_at)
        with open("file.json", "r", encoding="utf-8") as f:
            self.assertIn(base.id, f.read())

    def test_to_dict(self):
        """Test the to_dict method of the base model"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict["__class__"], "BaseModel")
        self.assertEqual(type(base_dict["created_at"]), str)
        self.assertEqual(type(base_dict["updated_at"]), str)

    def test_str(self):
        """Test the __str__ method of the base model"""
        base = BaseModel()
        base_str = base.__str__()
        self.assertEqual(base_str, "[BaseModel] ({}) {}"
                         .format(base.id, base.__dict__))
        self.assertEqual(type(base_str), str)

    def test_kwargs(self):
        """Test the kwargs of the base model"""
        base = BaseModel()
        base.name = "My first model"
        base.number = 89
        base_dict = base.to_dict()
        base2 = BaseModel(**base_dict)
        self.assertFalse(base is base2)

    def test_kwargs_types(self):
        """Test the kwargs types of the base model"""
        with self.assertRaises(TypeError):
            BaseModel(**{None: None})
        with self.assertRaises(TypeError):
            BaseModel(**{1: 2})

    def test_types(self):
        """Test the type of the base model"""
        base = BaseModel()
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertEqual(type(base.updated_at), datetime.datetime)
