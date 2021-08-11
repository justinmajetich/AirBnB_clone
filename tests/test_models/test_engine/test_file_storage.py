#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from unittest.case import skipIf
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

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

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        for obj in storage.all(BaseModel).values():
            temp = obj
            self.assertTrue(temp is obj)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
            self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_key_format(self):
        """ Key is properly formatted """
        new = Amenity()
        _id = new.to_dict()['id']
        for key in storage.all('Amenity').keys():
            temp = key
            self.assertEqual(temp, 'Amenity' + '.' + _id)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        print(type(storage))
        self.assertEqual(type(storage), FileStorage)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testSpecificAll(self):
        self.__testSpecificAll("Amenity", "User")
        self.__testSpecificAll("City", "User")
        self.__testSpecificAll("Place", "User")
        self.__testSpecificAll("Review", "User")
        self.__testSpecificAll("State", "User")
        self.__testSpecificAll("User", "Amenity")

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def testObjectDeletion(self):
        for prmClassName in self.__classes:
            self.__testOjectDeletion(prmClassName)

    def __testSpecificAll(self, prmClassName, prmOtherClassName):
        """ __objects only for specific class returned """
        from models.engine.file_storage import FileStorage

        fs = FileStorage()
        instance = eval(prmClassName)()
        other = eval(prmOtherClassName)()
        fs.new(instance)
        fs.new(other)
        keyInstance = self.__keyFromInstance(instance)
        keyOther = self.__keyFromInstance(other)
        self.assertIn(keyInstance, fs.all(type(instance)))
        self.assertNotIn(keyOther, fs.all(type(instance)))
        del fs.all()[keyInstance]
        del fs.all()[keyOther]

    def __testOjectDeletion(self, prmClassName):
        """ object from __objects is deleted """
        from models.engine.file_storage import FileStorage

        fs = FileStorage()
        len = self.__rowLenFromDict(fs.all(eval(prmClassName)))
        instance = eval(prmClassName)()
        fs.new(instance)
        newLen = self.__rowLenFromDict(fs.all(eval(prmClassName)))
        self.assertEqual(newLen, len + 1)
        fs.delete(instance)
        newLen = self.__rowLenFromDict(fs.all(eval(prmClassName)))
        self.assertEqual(newLen, len)

    def __keyFromInstance(self, prmInstance):
        return "{}.{}".format(prmInstance.__class__.__name__, prmInstance.id)

    def __rowLenFromDict(self, prmDict):
        return len(prmDict.keys())
