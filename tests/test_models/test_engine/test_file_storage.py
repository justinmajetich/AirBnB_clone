#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import pep8
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @classmethod
    def setUpClass(cls):
        """test set up"""
        cls.user = User()
        cls.user.first_name = "Yan"
        cls.user.last_name = "Tiom"
        cls.user.email = "yan@email.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """test Tear down"""
        del cls.user

    def tearDown(self):
        """Remove storage file at end of tests"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_pep8(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0, "fix pep8")

    def test_new(self):
        """test new method"""
        storage = FileStorage()
        user = User()
        user.id = "12345-abcd"
        user.name = "Yanin"
        storage.new(user)
        obj = storage.all()
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_all(self):
        """Test if __objects is properly returned """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_reload(self):
        """tests reload method"""
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
