#!/usr/bin/python3
"""
HHNB Console unit tests

"""
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

from models.base_model import BaseModel
from datetime import datetime
from models.user import User
import unittest
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State
from models.amenity import Amenity
from models import storage
import re


class TestHBNBCommand(unittest.TestCase):
    """
    Tests for HBNBCommand line tool
    """
    classes = ["BaseModel", "User", "Place", "Review", "Amenity",
               "City", "State"]

    def test_help(self):
        """
        test help function by checking return value of
            help all
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual("return all", f.getvalue().lower().strip())

    def test_quit(self):
        """
        test command quit which return True causing the to exit the prompt
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """
        test the command EOF to HBNBCommand line whith
        return True
        """
        with patch("sys.stdout",  new=StringIO) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create(self):
        """Test Creation of objects """

        with patch("sys.stdout", new=StringIO()) as f:
            classes = self.classes
            for className in classes:
                cmd_ = "create {}".format(className)
                self.assertFalse(HBNBCommand().onecmd(cmd_))

    def test_all(self):
        """
            test all
        """

        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            HBNBCommand().onecmd("create User")
            self.assertFalse(HBNBCommand().onecmd('all'))
            self.assertNotEqual("[]", f.getvalue().strip)

    def test_Count(self):
        """
        test count.
            Not well implemented yet due to parse of cmd output

            check count of instances of a class type and then compare
            with count after creation of a new element.
        """
        with patch("sys.stdout", new=StringIO()) as f:
            for className in self.classes:
                HBNBCommand().onecmd("{}.count()".format(className))
                initial = f.getvalue().strip()
                HBNBCommand().onecmd("create {}".format(className))
                fx = f.getvalue()
                HBNBCommand().onecmd("{}.count()".format(className))
                final = f.getvalue().strip()
                self.assertNotEqual(final, initial)
