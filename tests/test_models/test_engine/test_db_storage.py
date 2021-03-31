#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models import storage
import datetime
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        os.environ['HBNB_MYSQL_USER'] = "hbnb_test"
        os.environ['HBNB_MYSQL_PWD'] = "hbnb_test_pwd"
        os.environ['HBNB_MYSQL_HOST'] = "localhost"
        os.environ['HBNB_MYSQL_DB'] = "hbnb_test_db"
        os.environ['HBNB_TYPE_STORAGE'] = "db"
        self.storage = DBStorage()
        self.storage.reload()

        storage = self.storage

    def tearDown(self):
        os.environ['HBNB_TYPE_STORAGE'] = "apple"

    def test_storage(self):
        """ docstring"""
        self.assertIsInstance(self.storage, DBStorage)

    def test_city(self):
        """ Testing cities in the database """
        bark = State(**{'id': '4f33f621-7fdd-436a-8e9e-933c5f363724',
                        'name': 'Mishagain',
                        'created_at': datetime.datetime(2021, 3, 31, 2,
                                                        46, 58, 325269),
                        'updated_at': datetime.datetime(2021, 3, 31, 2,
                                                        46, 58, 325285)})
        bark.save()
        meow = City(**{'id': '68dd7376-b89f-47ee-ac09-96f6211f9e8d',
                       'name': 'Lansing',
                       'state_id': '4f33f621-7fdd-436a-8e9e-933c5f363724',
                       'updated_at': datetime.datetime(2021, 3, 31, 2,
                                                       15, 14, 882874),
                       'created_at': datetime.datetime(2021, 3, 31, 2,
                                                       15, 14, 882858)})
        meow.save()
        storage.save()
        self.assertIn("City." + meow.id, storage.all())

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    '''
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel new """
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

    @unittest.skip("FileStorage")
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

    @unittest.skip("FileStorage")
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

    @unittest.skip("All")
    def test_delete(self):
        """ Delete FileStorage object """
        self.assertEqual(len(storage.all()), 0)
        new = BaseModel()
        self.assertEqual(len(storage.all()), 1)
        storage.delete(new)
        self.assertEqual(len(storage.all()), 0)

    @unittest.skip("All")
    def test_delete_none(self):
        """ Delete "None" FileStorage object """
        self.assertEqual(len(storage.all()), 0)
        new = BaseModel()
        self.assertEqual(len(storage.all()), 1)
        storage.delete()
        self.assertEqual(len(storage.all()), 1)'''
