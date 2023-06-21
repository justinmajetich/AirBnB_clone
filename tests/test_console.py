#!/usr/bin/python3
"""This module contains test suites for testing
   the behaviour of the console.
"""
from console import HBNBCommand
from io import StringIO
from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from unittest import mock, TestCase


class TestConsole_create(TestCase):
    """Unittests for testing the create method."""

    def test_create_no_class(self):
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = "** class name missing **\n"
            self.assertEqual(output, f.getvalue())

    def test_create_wrong_class(self):
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = "** class doesn't exist **\n"
            self.assertEqual(output, f.getvalue())

    def test_create_with_correct_class(self):
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip('\n')
            self.assertIn(f"Amenity.{output}", storage.all().keys())

    def test_create_kwargs(self):
        """Testing the create method with
           keyword arguments

           Usage: create <class> <param 1> <param 2> <param 3>
           parameter syntax: <name>=<value>
           value syntax:
                string: "<>" -> string must be enclosed in double quoutes.
                        Underscores in strings must be replaced with spaces.
                        Double quotes in strings must be escaped.
                float: <unit>.<decimal> -> floats contain a dot.
                integer: <number>
            Any parameter that does not fit these requirement must be skipped.
            e.g name = value, name= value, name =value will get skipped.
        """
        with self.subTest('testing with proper kwargs'):
            with mock.patch('sys.stdout', new=StringIO()) as f:
                line = 'create City name="California" state_id=1'
                HBNBCommand().onecmd(line)
                output = f.getvalue().strip('\n')
                obj_dict = storage.all()[f"City.{output}"].__dict__
                self.assertIn('name', obj_dict.keys())
                self.assertIn('state_id', obj_dict.keys())
                self.assertIn('California', obj_dict.values())
                self.assertIn(1, obj_dict.values())

        with self.subTest('invalid kwargs get skipped'):
            with mock.patch('sys.stdout', new=StringIO()) as f:
                line = 'create Place city_id= "0001" \
                    max_guest = 10 name ="Pheonix"'
                HBNBCommand().onecmd(line)
                output = f.getvalue().strip('\n')
                obj_dict = storage.all()[f"Place.{output}"].__dict__
                self.assertNotIn('city_id', obj_dict.keys())
                self.assertNotIn('max_guest', obj_dict.keys())
                self.assertNotIn('name', obj_dict.keys())

        with self.subTest('Underscores become Spaces'):
            with mock.patch('sys.stdout', new=StringIO()) as f:
                line = 'create Place name="My_Little_House"'
                HBNBCommand().onecmd(line)
                output = f.getvalue().strip('\n')
                obj_dict = storage.all()[f"Place.{output}"].__dict__
                self.assertNotIn('My_Little_House', obj_dict.values())
                self.assertIn('My Little House', obj_dict.values())
