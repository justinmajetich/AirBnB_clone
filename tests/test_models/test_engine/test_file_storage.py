#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
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
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_show_all_objects(self):
        """ shows all objects in __objects """
        new = BaseModel()
        all_objects = new.all()
        self.assertEqual(all_objects, new._BaeModel_objects)

    def test_show_by_int_type(self):
        """ shows all integer type in __objects"""
        new = BaseModel()
        class int:
            pass
        int_objects = {1: int(), -1: int()}
        new._BaseMdel__objects = int_objects
        int_type_object = new.all(int)
        self.assertEqual(int_type_object, int_objects)

    def test_show_by_float_type(self):
        """ shows all float type in __objects """
        new = BaseModel()
        class float:
            pass
        float_objects = {105.3: float(), -105.3: float()}
        new._BaseModel__objects = float_objects
        float_type_object = new.all(float)
        self.assertEqual(float_type_object, float_objects)

    def test_show_by_int_type(self):
        """ shows all string type in __objects"""
        new = BaseModel()
        class str:
            pass
        str_objects = {"monwalker": str(), "Holbie": str()}
        new._BaseModel__objects = str_objects
        str_type_object = new.all(str)
        self.assertEqual(str_type_object, str_objects)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_delete_existing_object(self):
        self.assertEqual(len(self.new.__objects), 2)
        self.new.delete(self.obj1)
        self.assertEqual(len(self.new.__objects), 1)
        self.assertNotIn("{}.{}".format(type(self.obj1).__name__, self.obj1.id), self.new.__objects)

    def test_delete_non_existing_object(self):
        non_existing_object = object()
        self.new.delete(non_existing_object)
        self.assertEqual(len(self.new.__objects), 2)

     def test_delete_with_none_object(self):
         self.assertEqual(len(self.new.__objects), 2)
         self.new.delete(None)
         self.assertEqual(len(self.new.__objects), 2)
