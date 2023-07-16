#!/usr/bin/python3
""" unittest for console.py """

import unittest
import console
from unittest.mock import create_autospec
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from io import StringIO
import sys


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up testing environment"""
        self.hbnb_command = console.HBNBCommand()

    def test_do_create_no_args(self):
        """Test do_create method with no arguments"""
        sys.stdout = StringIO()  # redirect output to a buffer
        self.hbnb_command.onecmd("create")
        self.assertEqual("** class name missing **\n", sys.stdout.getvalue())
        sys.stdout = sys.__stdout__  # reset redirection

    def test_do_create_invalid_class(self):
        """Test do_create method with invalid class"""
        sys.stdout = StringIO()  # redirect output to a buffer
        self.hbnb_command.onecmd("create InvalidClass")
        self.assertEqual("** class doesn't exist **\n", sys.stdout.getvalue())
        sys.stdout = sys.__stdout__  # reset redirection
    # Add more tests for each command...


if __name__ == '__main__':
    unittest.main()
