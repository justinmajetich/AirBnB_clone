#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.engine.file_storage import FileStorage
from models.user import User


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
        except Exception:
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

    def test_delete_method(self):
        """deltes of from storage"""
        new = BaseModel()
        object_key = "{}.{}".format(type(new).__name__, new.id)
        storage.delete(new)
        self.assertNotIn(object_key, storage.all())

    def test_all_with_class(self):
        """all method returns objects of the given class"""
        new1 = BaseModel()
        new2 = BaseModel()
        outcome = storage.all(BaseModel)
        self.assertIn(new1, outcome.values())
        self.assertIn(new2, outcome.values())

    def test_delete_with_bad_objects(self):
        """deleting bad objects"""
        new = BaseModel()
        bad_obj = BaseModel()
        storage.delete(bad_obj)

    def test_delete_with_many_obj(self):
        """deleting manay objects"""

        new1 = BaseModel()
        new2 = BaseModel()

        object_one = "{}.{}".format(type(new1).__name__, new1.id)
        object_two = "{}.{}".format(type(new2).__name__, new2.id)

        self.assertIn(object_one, storage.all())
        self.assertIn(object_two, storage.all())

        storage.delete(new1)
        self.assertNotIn(object_one, storage.all())
        self.assertIn(object_two, storage.all())

    def test_all_emty_class(self):
        """all method should return empty dict"""
        class NonExistentClass:
            pass
        bad_class = NonExistentClass()
        outcome = storage.all(bad_class)
        self.assertEqual(len(outcome), 0)

    def test_all_many_class_objects(self):
        """return only objects of the requested class"""
        new1 = BaseModel()
        new2 = BaseModel()
        new3 = User()

        outcome1 = storage.all(BaseModel)
        outcome2 = storage.all(User)

        self.assertIn(new1, outcome1.values())
        self.assertIn(new2, outcome1.values())
        self.assertIn(new3, outcome2.values())


if __name__ == "__main__":
    unittest.main()
