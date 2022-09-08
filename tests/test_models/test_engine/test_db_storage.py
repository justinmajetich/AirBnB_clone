#!/usr/bin/python3
""" Test DBstorage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.state import State


class test_dbstorage(unittest.TestCase):
    """ Class to test the DBstorage method """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Cannot storage if db is active")
    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.all().keys():
            del_list.append(key)
        for key in del_list:
            storage._DBStorage__session.delete(storage.all()[key])
            storage._DBStorage__session.commit()

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_store(self):
        """ Test if an object is store in the database """
        new = State(name="Florida")
        new.save()
        _id = new.to_dict()['id']
        self.assertIn(new.__class__.__name__ + '.' + _id,
                        storage.all(type(new)).keys())

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)
