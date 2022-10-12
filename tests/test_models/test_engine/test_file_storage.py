#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import os


def setUpModule(self):
    """ Set up test environment """
    del_list = []
    for key in storage._FileStorage__objects.keys():
        del_list.append(key)
    for key in del_list:
        del storage._FileStorage__objects[key]


def tearDownModule(self):
    """ Remove storage file at end of tests """
    try:
        os.remove('file.json')
    except BaseException:
        pass


class TestFileStorage_All(unittest.TestCase):
    """ Test the instantiation of the storage object. """

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        # print(type(storage))
        self.assertIsInstance(storage, FileStorage)


class TestFileStorage_All(unittest.TestCase):
    """ Class to define test cases for public instance method 'all()' """

    def test_output_type(self):
        """ Confirm __objects is a dict """
        self.assertIsNotNone(storage.all())
        self.assertIsInstance(storage.all(), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

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

    def test_without_args(self):
        self.assertIsInstance(storage.all(), dict)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            storage.all(1)


class TestFileStorage_New(unittest.TestCase):
    """ Class to define test cases for public instance method 'new(obj)' """

    def test_without_args(self):
        with self.assertRaises(TypeError):
            storage.new()

    def test_with_args_str(self):
        with self.assertRaises(AttributeError):
            storage.new("id")

    def test_with_args_positive_integer(self):
        with self.assertRaises(AttributeError):
            storage.new(1)

    def test_with_args_negative_integer(self):
        with self.assertRaises(AttributeError):
            storage.new(-1)

    def test_with_args_float(self):
        with self.assertRaises(AttributeError):
            storage.new(1.99999)

    def test_with_args_bool_true(self):
        with self.assertRaises(AttributeError):
            storage.new(True)

    def test_with_args_bool_false(self):
        with self.assertRaises(AttributeError):
            storage.new(False)

    def test_with_args_complex(self):
        with self.assertRaises(AttributeError):
            storage.new(complex(1))

    def test_with_args_invalid_dict(self):
        with self.assertRaises(AttributeError):
            storage.new({"id": 1, "name": 2})

    def test_with_args_list(self):
        with self.assertRaises(AttributeError):
            storage.new([12, 24, 36])

    def test_with_args_tuple(self):
        with self.assertRaises(AttributeError):
            storage.new((12, 24, 36))

    def test_with_args_set(self):
        with self.assertRaises(AttributeError):
            storage.new({'id', '__class__', 36})

    def test_with_args_frozenset(self):
        with self.assertRaises(AttributeError):
            storage.new(frozenset({'id', '__class__', 36}))

    def test_with_args_range(self):
        with self.assertRaises(AttributeError):
            storage.new(range(5))

    def test_with_args_bytes(self):
        with self.assertRaises(AttributeError):
            storage.new(b'id')

    def test_with_args_bytearray(self):
        with self.assertRaises(AttributeError):
            storage.new(bytearray(b'id'))

    def test_with_args_memoryview(self):
        with self.assertRaises(AttributeError):
            storage.new(memoryview(b'id'))

    def test_with_args_inf(self):
        with self.assertRaises(AttributeError):
            storage.new(float('Inf'))

    def test_with_args_negative_inf(self):
        with self.assertRaises(AttributeError):
            storage.new(float('-Inf'))

    def test_with_args_NaN(self):
        with self.assertRaises(AttributeError):
            storage.new(float('NaN'))

    def test_with_more_args(self):
        with self.assertRaises(TypeError):
            storage.new("id", "__class__")


class TestFileStorage_Save(unittest.TestCase):
    """ Class to define test cases for public instance method 'save()' """

    def test_output_type(self):
        self.assertIsNone(storage.save())

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_without_args(self):
        self.assertIsNone(storage.save())

    def test_with_args(self):
        with self.assertRaises(TypeError):
            storage.save("id")


class TestFileStorage_Reload(unittest.TestCase):
    """ Class to define test cases for public instance method 'reload()' """

    def test_output_type(self):
        self.assertIsNone(storage.reload())

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

    def test_without_args(self):
        self.assertIsNone(storage.reload())

    def test_with_args(self):
        with self.assertRaises(TypeError):
            storage.reload("id")


if __name__ == '__main__':
    unittest.main()
