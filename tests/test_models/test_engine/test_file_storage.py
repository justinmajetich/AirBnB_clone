#!/usr/bin/python3
"""
This module defines tests for the FileStorage class
"""

import unittest
from models.base_model import BaseModel
from models import storage
import os

TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")
if TYPE_STORAGE == "db":
    exit(0)


class test_fileStorage(unittest.TestCase):
    """
    Class to test the file storage method
    """

    def setUp(self):
        """
        Set up test environment
        """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """
        Remove storage file at end of tests
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_obj_list_empty(self):
        """
        Ensure that __objects is initially empty
        """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """
        Ensure that new object is correctly added to __objects
        """
        new = BaseModel()
        for obj in storage.all().values():
            with self.subTest(obj=obj):
                self.assertTrue(obj is new)

    def test_all(self):
        """
        Ensure that the dictionary __objects is properly returned
        """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_all_cls(self):
        """
        Ensure that FileStorage can return specific classes
        using the all method
        """
        from models.state import State
        from models.city import City

        base_1 = BaseModel()
        base_2 = City()
        state_1 = State()
        state_2 = State()

        cls = State     # class to test
        for key, value in storage.all(cls).items():
            with self.subTest(key=key, value=value):
                self.assertIsInstance(value, cls)

    def test_base_model_instantiation(self):
        """
        Ensure that file is not created on BaseModel save
        """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """
        Ensure that data is saved to file
        """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """
        Verify FileStorage save method works
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """
        Ensure storage file is successfully loaded to __objects
        """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            with self.subTest(obj=obj):
                self.assertEqual(
                        new.to_dict()["id"],
                        obj.to_dict()["id"])

    def test_reload_empty(self):
        """
        Ensure that data is not loaded from an empty file
        """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """
        Ensure nothing happens if file does not exist
        """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """
        Ensure BaseModel save method calls storage save
        """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """
        Confirm __file_path is string
        """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """
        Confirm __objects is a dict
        """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """
        Ensure that identification Key is properly formatted
        """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            with self.subTest(key=key):
                self.assertEqual(key, "BaseModel" + '.' + _id)

    def test_storage_var_created(self):
        """
        Ensure FileStorage object storage created
        """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    def test_delete(self):
        """
        Ensure that the delete method works properly:
        * Should delete object if the key exists
        * Should raise a `KeyError` exception if object does not exist
        """
        # Ensure that the newly created instance is in storage
        new = BaseModel()
        new.save()
        self.assertIn(new, storage.all().values())

        """
        cls = type(new).__name__.split('.')[-1]
        key = cls + '.' + new.id
        """
        storage.delete(new)     # delete the object from storage

        # Ensure an error is raised if you try to delete a non-existing
        # object
        try:
            storage.delete(new)
        except Exception as e:
            self.fail("Exception raised on trying to delete an object that\
is not in storage.\n{}".format(e))
