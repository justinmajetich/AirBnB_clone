#!/usr/bin/python3

"""Tests for the console output."""

import os
import pathlib as pl
from unittest.mock import patch
from io import StringIO
from unittest import TestCase

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models import storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from console import HBNBCommand
from models.engine.file_storage import FileStorage

class TestConsole(TestCase):
    """Console testcase."""

    @classmethod
    def setUpClass(cls):
        """SetUp class."""

        storage.new_object()
        storage.set_path('tests.json')

    @classmethod
    def tearDownClass(cls):
        """tear down class."""

        if pl.Path("tests.json").is_file():
            os.remove("tests.json")

    def setUp(self):
        """ setUp method for every tests."""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="NewYork"')
            self.obj_id = f.getvalue()

            HBNBCommand().onecmd('show State {}'.format(
                self.obj_id))
            self.obj_data = f.getvalue()

    def test_create(self):
        """Tests for do_create method."""

        # checking of object id is in storage
        all_objects = storage.all()

        self.assertIn(
            "State.{}".format(self.obj_id)
            .replace("\n", ""),
            all_objects)

        # checking it the id is in the console output
        self.assertRegex(self.obj_data, self.obj_id.replace("\n", ""))

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Edo State"')
            obj_id = f.getvalue().replace("\n", "")
            HBNBCommand().onecmd('show State {}'.format(obj_id))
            obj_data = f.getvalue()

        # checking if there is a name and it key value
        self.assertRegex(obj_data, "name")
        self.assertRegex(obj_data, "Edo State")

    def test_multiple_parameters(self):
        """testing for multiple name parameters."""

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create User name="Jojo" sprint=3' +
                                 ' state="Edo State"')
            user_id = f.getvalue().replace("\n", "")

            HBNBCommand().onecmd('show User {}'.format(user_id))
            user_data = f.getvalue().replace("\n", "")

            # check if user_id is in the console response
            self.assertRegex(user_data, user_id)

            # checking if object exist in the storage class
            all_objects = storage.all()
            self.assertIn("User.{}".format(user_id),
                          all_objects)
            user_object = all_objects['User.{}'.format(user_id)]

            self.assertIn("name", user_object.__dict__)
            self.assertIn("sprint", user_object.__dict__)
            self.assertIn("state", user_object.__dict__)

            self.assertIsInstance(getattr(user_object, 'name'), str)
            self.assertIsInstance(getattr(user_object, 'sprint'), int)
            self.assertIsInstance(getattr(user_object, 'state'), str)
            

class TestConsoleWithFileStorage(TestCase):

    @classmethod
    def setUpClass(cls):
        """setup class"""
        storage.new_object()
        storage.set_path("tests.json")
        
    @classmethod
    def tearDownClass(cls):
        """tear down class."""

        if pl.Path("tests.json").is_file():
            os.remove("tests.json")

    def test_storage(self):
        """Test is the storage object is the instance object."""
        
        all_objects = storage.all()

        self.assertEqual(len(all_objects), 0)

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Edo State"')
            HBNBCommand().onecmd('create State name="Lagos"')
            HBNBCommand().onecmd('create State name="Imo"')
            HBNBCommand().onecmd('create State name="Delta"')

        all_objects = storage.all()

        self.assertEqual(len(all_objects), 4)
