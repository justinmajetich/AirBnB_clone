#!/usr/bin/python3
"""
module for testing file storage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test the file storage class"""
    def setUp(self):
        """Set up the test"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.storage = FileStorage()
        self.storage._FileStorage__objects.clear()

    def tearDown(self):
        """Tear down the test"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.storage

    def test_file_storage(self):
        """Test the file storage class"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        """Test the all method of the file storage class"""
        base = BaseModel()
        self.storage.new(base)
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_new_one(self):
        """Test the new method of the file storage class with one object"""
        base = BaseModel()
        self.storage.new(base)
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_new_two(self):
        """Test the new method of the file storage class with two objects"""
        base = BaseModel()
        base2 = BaseModel()
        self.storage.new(base)
        self.storage.new(base2)
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)

    def test_save(self):
        """Test the save method of the file storage class"""
        base = BaseModel()
        self.storage.new(base)
        self.storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            file_contents = f.read()
            self.assertTrue(len(file_contents) > 0)
            self.assertIn('"BaseModel.' + base.id + '"', file_contents)

    def test_reload(self):
        """Test the reload method of the file storage class"""
        self.assertEqual(self.storage.all(), {})
        base = BaseModel()
        base2 = BaseModel()
        self.storage.new(base)
        self.storage.new(base2)
        storage_objects = self.storage.all()
        self.storage.save()
        del self.storage
        self.storage = FileStorage()
        self.storage.reload()
        for k, _ in storage_objects.items():
            self.assertTrue(k in self.storage.all())

    def test_reload_models(self):
        """Test the reload method of the file storage class for models"""
        self.assertEqual(self.storage.all(), {})
        user = User()
        state = State()
        city = City()
        place = Place()
        amenity = Amenity()
        review = Review()
        self.storage.new(user)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(place)
        self.storage.new(amenity)
        self.storage.new(review)
        storage_objects = self.storage.all()
        self.storage.save()
        del self.storage
        self.storage = FileStorage()
        self.storage.reload()
        for k, _ in storage_objects.items():
            self.assertTrue(k in self.storage.all())
