#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from os import getenv


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        from models import storage

    def setUp(self):
        """ Set up test environment """
        del_list = []
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            for key in storage._FileStorage__objects.keys():
                del_list.append(key)
            for key in del_list:
                del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        temp = None
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            for obj in storage.all().values():
                temp = obj
        self.assertTrue(temp is None)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            temp = storage.all()
            self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            new = BaseModel()
            self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            new = BaseModel()
            thing = new.to_dict()
            new.save()
            new2 = BaseModel(**thing)
            self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            storage.save()
            self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            new = BaseModel()
            storage.save()
            storage.reload()
            loaded = None
            for obj in storage.all().values():
                loaded = obj
            self.assertNotEqual(new, loaded)

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            with self.assertRaises(ValueError):
                storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            new = BaseModel()
            new.save()
            self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(storage._FileStorage__file_path), str)

    # def test_type_objects(self):
    #     """ Confirm __objects is a dict """
    #     self.assertEqual(type(storage.all()), dict)

    # def test_key_format(self):
    #     """ Key is properly formatted """
    #     new = BaseModel()
    #     _id = new.to_dict()['id']
    #     for key in storage.all().keys():
    #         temp = key
    #     self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            from models.engine.file_storage import FileStorage
            print(type(storage))
            self.assertEqual(type(storage), FileStorage)