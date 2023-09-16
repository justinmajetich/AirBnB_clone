#!/usr/bin/python3
"""file_storage test cases"""

import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class StorageTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_FileStorage_private_attribute_file_path(self):
        """Test the data type of the private attribute"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_models_storage_initialized(self):
        """check if storage is initialized"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_all_not_empty(self):
        """check that all is not empty after saving"""
        obj = BaseModel()
        obj.save()
        all_obj = models.storage.all()
        self.assertTrue(all_obj)

    def test_FileStorage_new_no_arg(self):
        """check new() with an argument"""
        with self.assertRaises(TypeError):
            models.storage.new()

    def test_FileStorage_new_two_args(self):
        """check new() with two arguments"""
        obj = BaseModel()
        with self.assertRaises(TypeError):
            models.storage.new(obj, obj)

    def test_FileStorage_new_keys_exist_in_all(self):
        """check new() adds elements to the objects dictionary"""
        _basemodel = BaseModel()
        _amenity = Amenity()
        _city = City()
        _place = Place()
        _review = Review()
        _state = State()
        _user = User()
        _basemodel.save()
        _amenity.save()
        _city.save()
        _place.save()
        _review.save()
        _state.save()
        _user.save()

        self.assertIn("BaseModel."
                      + _basemodel.id, models.storage.all().keys())
        self.assertIn("Amenity." + _amenity.id, models.storage.all().keys())
        self.assertIn("City." + _city.id, models.storage.all().keys())
        self.assertIn("Place." + _place.id, models.storage.all().keys())
        self.assertIn("Review." + _review.id, models.storage.all().keys())
        self.assertIn("User." + _user.id, models.storage.all().keys())

    def test_FileStorage_save_with_arg(self):
        """check save() with an argument"""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_FileStorage_save_keys_exist_in_file(self):
        """check that save() writes the instances in the file"""
        _basemodel = BaseModel()
        _amenity = Amenity()
        _city = City()
        _place = Place()
        _review = Review()
        _state = State()
        _user = User()

        _basemodel.save()
        _amenity.save()
        _city.save()
        _place.save()
        _review.save()
        _state.save()
        _user.save()
        with open("file.json", "r") as file:
            file_content = file.read()

        self.assertIn("BaseModel." + _basemodel.id, file_content)
        self.assertIn("Amenity." + _amenity.id, file_content)
        self.assertIn("City." + _city.id, file_content)
        self.assertIn("Place." + _place.id, file_content)
        self.assertIn("Review." + _review.id, file_content)
        self.assertIn("User." + _user.id, file_content)

    def test_FileStorage_reload_with_arg(self):
        """check reload() with an argument"""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_FileStorage_reload_loads_data(self):
        """check reload() loads data"""
        _basemodel = BaseModel()
        _amenity = Amenity()
        _city = City()
        _place = Place()
        _review = Review()
        _state = State()
        _user = User()

        _basemodel.save()
        _amenity.save()
        _city.save()
        _place.save()
        _review.save()
        _state.save()
        _user.save()
        models.storage.reload()
        content = FileStorage._FileStorage__objects

        self.assertIn("BaseModel." + _basemodel.id, content)
        self.assertIn("Amenity." + _amenity.id, content)
        self.assertIn("City." + _city.id, content)
        self.assertIn("Place." + _place.id, content)
        self.assertIn("Review." + _review.id, content)
        self.assertIn("User." + _user.id, content)
