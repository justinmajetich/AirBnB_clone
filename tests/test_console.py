#!/usr/bin/python3
"""test_base_model
"""
import unittest
import os
import pep8
import sys
from io import StringIO
from unittest.mock import patch
from models.__init__ import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from console import HBNBCommand
# from models.engine.db_storage import DBStorage


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)

    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_conformance_base(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base_test(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_1_file_HBNBCommand_exist(self):
        """ Check if methods exists """
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        self.assertTrue(hasattr(HBNBCommand, "postcmd"))
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_show"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertTrue(hasattr(HBNBCommand, "do_all"))
        self.assertTrue(hasattr(HBNBCommand, "precmd"))
        self.assertTrue(hasattr(HBNBCommand, "default"))

    def test_2_file_HBNBCommand_documentation(self):
        """ Check the documentation """
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    # @unittest.skipIf(condition == DBStorage, "For DBStorage")
    def test_3_check_for_the_entry_point(self):
        """ Check the program console.py that contains the entry point of the
        command interpreter: (quit), (EOF) y (help)"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")

    def test_4_check_for_command(self):
        """ Check if command interpreter (console.py) have these commands:
        (create), (show), (destroy), (all), (update)"""

        update = "update BaseModel fce4d085-ebc6-4472-ae0e-82e2a0db7e5a" + \
            "first_name \"Betty\""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(update)

    def test_5_check_for_commands_2(self):
        """ Check if command interpreter (console.py) have these commands:
        (create), (show), (destroy), (all), (update)"""

        update = "update User fce4d085-ebc6-4472-ae0e-82e2a0db7e5a" + \
            "first_name \"Betty\""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(update)

    def test_6_all(self):
        """check the command class.all classes,
        for showing all instances of just that class """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Reivew.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")

    def test_7_count(self):
        """check the command for class.count and
        it counts how many instances there are of that type"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Reivew.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")

    def test_8_show(self):
        """ check for command class.show, which shows only
        the instance and its dictionary """

        User = "User.show(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\")"
        Place = "Place.show(\"fce4d085-ebc6-4472-ae0e-82e2a0db7e5a\")"
        State = "State.show(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\")"
        City = "City.show(\"323f3340-1246-48e5-a47d-64d0e74349be\")"
        Amenity = "Amenity.show(\"7a6d7852-9368-4138-889b-8b3086a51885\")"
        Reivew = "Reivew.show(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\")"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

    def test_9_destroy(self):
        """ check for command class.destroy("id").
        Destroys that specific instance """

        User = "User.destroy(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\")"
        Place = "Place.destroy(\"fce4d085-ebc6-4472-ae0e-82e2a0db7e5a\")"
        State = "State.destroy(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\")"
        City = "City.destroy(\"323f3340-1246-48e5-a47d-64d0e74349be\")"
        Amenity = "Amenity.destroy(\"7a6d7852-9368-4138-889b-8b3086a51885\")"
        Reivew = "Reivew.destroy(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\")"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

    def test_10_update_simple(self):
        """ check for command <class name>.update("id", "name", "my name")
        It updates the arguments of that specific instance """

        User = "User.update(\"38f22813-2753-4d42-b37c-57a17f1e4f88\", " + \
            "\"first_name\", \"Erika\")"
        Place = "Place.update(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\", " + \
            "\"first_name\", \"Osorio\")"
        State = "State.update(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\", " + \
            "\"first_name\", \"Edison\")"
        City = "City.update(\"7a6d7852-9368-4138-889b-8b3086a51885\", " + \
            "\"first_name\", \"Esteban\")"
        Amenity = "Amenity.update(\"fce4d085-ebc6-4472-ae0e-82e2a0db\", " + \
            "\"first_name\", \"Isaza\")"
        Reivew = "Reivew .update(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\"," + \
            "\"first_name\", \"John\")"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

    def test_11_update_from_dictionary(self):
        """  to update an instance based on his ID with a dictionary:
        <class name>.update(<"id">, <dictionary representation>)"""

        User = "User.update(\"38f22813-2753-4d42-b37c-57a17f1e4f88\", " + \
            "{'first_name': \"Erika\", \"age\": 9})"
        Place = "Place.update(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\", " + \
            "{'first_name': \"Osorio\", \"age\": 29})"
        State = "State.update(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\", " + \
            "{'first_name': \"Esteban\", \"age\": 59})"
        City = "City.update(\"7a6d7852-9368-4138-889b-8b3086a51885\", " + \
            "{'first_name': \"Lopez\", \"age\": 86})"
        Amenity = "Amenity.update(\"fce4d085-ebc6-4472-ae0e-82e2a0db\", " + \
            "{'first_name': \"Castañeda\", \"age\": 34})"
        Reivew = "Reivew .update(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\"," + \
            "{'first_name': \"Andres\", \"age\": 80})"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

    def test_12_check_error_create(self):
        California = "create State name=\"California\""
        Arizona = "create State name=\"Arizona\""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(California)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Arizona)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        command = "create Place city_id=\"1111\" name=\"Arizona\"\
                    number_rooms=2 latitude=22.22 longitude=122"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(command)
            var = f.getvalue().strip()
            # print(var)
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            value = f.getvalue()
            self.assertIn(var, value)
            self.assertIn("'name': 'Arizona'", value)
            self.assertIn("'latitude': 22.22", value)
            self.assertIn("'number_rooms': 2", value)
            self.assertIn("'city_id': '1111'", value)
            self.assertNotIn("'longitude: 122'", value)
