#!/usr/bin/python3
"""This are the tests for console"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import os
import json

import console
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class TestDoCreate(unittest.TestCase):
    """class test Do create method"""

    @classmethod
    def setUp(cls):
        """setting up for tests"""
        cls.consolle = HBNBCommand()
        cls.mock_stdout = StringIO()

    @classmethod
    def tearDown(cls):
        """tear down method"""
        del cls.console

    def tearDown(self):
        """remove file jsone"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_create_with_bad_input(self):
        message = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            self.consolle.onecmd("create")
            self.assertEqual(message, f.getvalue())

    def test_create_no_class(self):
        message = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as f:
            self.consolle.onecmd("create dog")
            self.assertEqual(message, f.getvalue())


if __name__ == "__main__":
    unittest.main()
