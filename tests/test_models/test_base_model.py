#!/usr/bin/python3
"""
module for testing base model class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the base model class"""
    def test_uuid(self):
        """Test the uuid of the base model"""
        base = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base.id, base2.id)

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
        self.assertEqual(base.id, base2.id)
        self.assertEqual(base.created_at, base2.created_at)
        self.assertEqual(base.updated_at, base2.updated_at)
        self.assertEqual(base.name, base2.name)
        self.assertEqual(base.number, base2.number)
        self.assertNotEqual(base, base2)
        self.assertEqual(type(base.created_at), type(base2.created_at))
        self.assertEqual(type(base.updated_at), type(base2.updated_at))
        self.assertEqual(type(base.name), type(base2.name))
        self.assertEqual(type(base.number), type(base2.number))
        self.assertEqual(base.__dict__, base2.__dict__)
        self.assertEqual(base.to_dict(), base2.to_dict())
        self.assertEqual(base.__str__(), base2.__str__())
        self.assertEqual(str(base), str(base2))

    def test_types(self):
        """Test the type of the base model"""
        base = BaseModel()
        self.assertEqual(type(base.id), str)
        self.assertEqual(type(base.created_at), type(base.updated_at))
