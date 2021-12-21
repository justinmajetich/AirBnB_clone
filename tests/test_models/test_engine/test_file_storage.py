#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os

# import pep8
import pycodestyle
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.engine import file_storage
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from datetime import datetime
import json


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

""" OWN TESTS """

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "Amenity": Amenity, "Place": Place, "City": City, "Review": Review}


class Test_Base(unittest.TestCase):
    """Base class tests"""

    def test_1(self):
        """  Test Dictionary """
        model = BaseModel()
        model.save()
        new_object = storage.all()
        self.assertEqual(dict, type(new_object))

    def test_pep8(self):
        """Test PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_docstrings_filestorage(unittest.TestCase):

    def test_Documentation(self):
        """Test if module file_storage has documentation
        """
        self.assertTrue(len(models.engine.file_storage.__doc__) > 0)
        self.assertIsNotNone(file_storage.__doc__,
                             "file_storage.py need docstrings")

    def test_type_field(self):
        """Test type of field
        """
        object = FileStorage()
        self.assertIsInstance(object, FileStorage)
        self.assertIsInstance(object.all(), dict)
        self.assertIsInstance(object._FileStorage__file_path, str)
        self.assertIsInstance(object._FileStorage__objects, dict)

    def test_all(self):
        """Test all method
        """
        object = BaseModel()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIsInstance(storage.all(), dict)
        key_object = f"{object.__class__.__name__}.{object.id}"
        self.assertEqual(all_objs[key_object], object)

    def test_save(self):
        """Test for save method
        """
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass

        my_model = BaseModel()
        my_model.save()

        dummy_dict = my_model.to_dict()
        dummy_key = f"{my_model.__class__.__name__}.{my_model.id}"

        self.assertTrue(os.path.isfile(path + "/" + file_name_expected))
        with open(file_name_expected, mode="r") as file:
            output = file.read()
        dict_json = eval(output)
        keys = dict_json.keys()
        self.assertIn(dummy_key, keys)
        self.assertEqual(dummy_dict, dict_json[dummy_key])
        os.remove(path + "/" + file_name_expected)

    def testing_save(self):
        """Testing serializes method"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    def test_reload(self):
        """Test Reload Method
        """
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass
        update = "2017-09-28T21:08:06.151750"
        create = "2017-09-28T21:08:06.151711"
        json_string = {"BaseModel.e79e744a": {"__class__": "BaseModel",
                                              "id": "e79e744a",
                                              "updated_at": update,
                                              "created_at": create,
                                              "name": "My_First_Model",
                                              "my_number": 89}
                       }
        expected_dictionary = {"BaseModel.e79e744a":
                               {"__class__": "BaseModel", "id": "e79e744a",
                                "updated_at": "2017-09-28T21:08:06.151750",
                                "created_at": "2017-09-28T21:08:06.151711",
                                "name": "My_First_Model", "my_number": 89}}
        with open('file.json', mode="w") as file:
            json.dump(json_string, file)

        storage.reload()
        dictionary_reload = storage.all()
        key_expected = "BaseModel.e79e744a"
        self.assertIn(key_expected, dictionary_reload.keys())
        self.assertEqual(
            dictionary_reload[key_expected].name,
            expected_dictionary[key_expected]["name"])
        os.remove(path + "/" + file_name_expected)
