#!/usr/bin/python3
"""unittests for base_model"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    '''Test cases for the test base model class'''

    @classmethod
    def setUp(self):
        # This method is called before each test method
        try:
            os.rename("file.json", "temp.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}
        self.storage = FileStorage()
        self.model = BaseModel()

    @classmethod
    def tearDown(self):
        # This method is called after each test method
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except IOError:
            pass
        del self.storage
        del self.model

    def test_init(self):
        self.assertEqual(type(self.model.id), str)
        self.assertEqual(type(self.model.created_at), datetime.datetime)
        self.assertEqual(type(self.model.updated_at), datetime.datetime)
        self.assertIsInstance(self.model, BaseModel)

    def test_str(self):
        '''testing str representation'''
        model_str = self.model.__str__()
        self.assertTrue(self.model.id in model_str)
        self.assertTrue("created_at" in model_str)
        self.assertTrue("updated_at" in model_str)

    @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "DBStorage")
    def test_save(self):
        '''Testing save method'''
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(type(model_dict), dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict.get("_sa_instance_state", None), None)

    @unittest.skipIf(os.getenv("HBNB_ENV") is not None, "DBStorage")
    def test_delete(self):
        '''Testing the delete method'''
        self.model.delete()
        self.assertNotIn(self.model, FileStorage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()

'''class test_basemodel(unittest.TestCase):
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
        except:
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

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

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
        self.assertFalse(new.created_at == new.updated_at)'''
