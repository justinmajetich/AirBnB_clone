#!/usr/bin/python3
"""Defines the unittests for models/engine/file_storage.py

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    """Unitests for testing instances of clase: FileStorage"""

    def test_FileStorage_no_arguments(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arguments(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_private_and_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_private_and_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_other_methods(unittest.TestCase):
    """Unitesting for remaining methods in class FileStorage"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "other")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("other", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_None(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base1 = BaseModel()
        usr = User()
        st = State()
        plc = Place()
        cty = City()
        am = Amenity()
        rev = Review()
        models.storage.new(base1)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(am)
        models.storage.new(rev)
        self.assertIn("BaseModel." + base1.id, models.storage.all().keys())
        self.assertIn(base1, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())

    def test_new_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 10)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        base1 = BaseModel()
        usr = User()
        st = State()
        plc = Place()
        cty = City()
        am = Amenity()
        rev = Review()
        models.storage.new(base1)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(am)
        models.storage.new(rev)
        models.storage.save()
        read_val = ""
        with open("file.json", "r") as file:
            read_val = file.read()
            self.assertIn("BaseModel." + base1.id, read_val)
            self.assertIn("User." + usr.id, read_val)
            self.assertIn("State." + st.id, read_val)
            self.assertIn("Place." + plc.id, read_val)
            self.assertIn("City." + cty.id, read_val)
            self.assertIn("Amenity." + am.id, read_val)
            self.assertIn("Review." + rev.id, read_val)

    def test_save_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base1 = BaseModel()
        usr = User()
        st = State()
        plc = Place()
        cty = City()
        am = Amenity()
        rev = Review()
        models.storage.new(base1)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(am)
        models.storage.new(rev)
        models.storage.save()
        models.storage.reload()
        obs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base1.id, obs)
        self.assertIn("User." + usr.id, obs)
        self.assertIn("State." + st.id, obs)
        self.assertIn("Place." + plc.id, obs)
        self.assertIn("City." + cty.id, obs)
        self.assertIn("Amenity." + am.id, obs)
        self.assertIn("Review." + rev.id, obs)
        
    def test_reload_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.reload([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
