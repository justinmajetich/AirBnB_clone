#!/usr/bin/python3
""" Test file storage """
import pep8
import os
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


class TestFileStorage(unittest.TestCase):
    """ Test cases for file storage """

    @classmethod
    def Class1(cls):
        """ Instanciando la clase """
        cls.user = User()
        cls.user.first_name = "Santiago"
        cls.user.last_name = "Mic"
        cls.user.email = "3890@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def delete(cls):
        """ Delete the instance """
        del cls.user

    def Deletejson(self):
        """ Delete the json file created """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FS(self):
        """ Pep8 style """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_allFS(self):
        """ Test the method all """
        storage = FileStorage()
        objects = storage.all()
        self.assertIsNotNone(objects)
        self.assertEqual(type(objects), dict)
        self.assertIs(objects, storage._FileStorage__objects)

    def test_newFS(self):
        """ Test the creation """
        storage = FileStorage()
        objects = storage.all()
        user = User()
        user.id = 5678902
        user.name = "Santiago"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(objects[key])

    def test_FS_reload(self):
        """ Tests the reload """
        with open("file.json", 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        with open("file.json", 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
