#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        self.fs = FileStorage()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_all_empty(self):
        """ Test if __objects is initially empty """
        all_objs = self.fs.all()
        self.assertEqual(len(all_objs), 0)

    def test_new(self):
        """ Test if new object is correctly added to __objects """
        new_obj = BaseModel()
        new_obj_key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.fs.new(new_obj)
        all_objs = self.fs.all()
        self.assertTrue(new_obj_key in all_objs)

    def test_save(self):
        """ Test if file is saved correctly """
        new_obj = BaseModel()
        new_obj_key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.fs.new(new_obj)
        self.fs.save()
        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            data = f.read()
            self.assertTrue(new_obj_key in data)

    def test_reload(self):
        """ Test if file is loaded correctly """
        new_obj = BaseModel()
        new_obj_key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.fs.new(new_obj)
        self.fs.save()
        self.fs.reload()
        all_objs = self.fs.all()
        self.assertTrue(new_obj_key in all_objs)

    def test_delete(self):
        """ Test if object is deleted correctly """
        new_obj = BaseModel()
        new_obj_key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.fs.new(new_obj)
        self.fs.save()
        self.fs.delete(new_obj)
        all_objs = self.fs.all()
        self.assertFalse(new_obj_key in all_objs)

    def test_all_filter(self):
        """ Test if objects are filtered correctly """
        new_obj = BaseModel()
        self.fs.new(new_obj)
        new_obj2 = BaseModel()
        self.fs.new(new_obj2)
        new_obj3 = BaseModel()
        self.fs.new(new_obj3)
        self.fs.save()
        all_objs = self.fs.all(BaseModel)
        self.assertEqual(len(all_objs), 3)

    def test_delete_no_obj(self):
        """ Test if delete method does nothing if obj is None """
        self.fs.delete(None)
        self.assertEqual(len(self.fs.all()), 0)

if __name__ == '__main__':
    unittest.main()
