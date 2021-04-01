#!/usr/bin/python3
""" Module to test console """

import unittest
from io import StringIO
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from console import HBNBCommand
from models import FileStorage
from models.user import User
import os
import models


class TestConsoleClass(unittest.TestCase):

    """ Class that contains unittests for the console """

    u = (
        " Updates an instance based on the class name and id by adding\n"
        "        or updating attribute (save the change into the JSON file)\n"
        "        format: [classname, instid, attr, value]\n"
    )

    def test_has_attr(self):
        """ Method to test if attr exist """
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_show"))
        self.assertTrue(hasattr(HBNBCommand, "do_all"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        self.assertTrue(hasattr(HBNBCommand, "do_help"))

    def test_quit(self):
        """ Method to test quit """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """ Method to test EOF """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help_documentation(self):
        """ Mehtod to test help """
        h = (
            "\nDocumented commands (type help <topic>):\n"
            "========================================\n"
            "Amenity    City  Place   State  all     destroy  quit  update\n"
            "BaseModel  EOF   Review  User   create  help     show\n\n"
        )

        dHelp = (
            " Deletes an instance based on the class\n"
            "        name and id (save the change into the JSON file) \n"
        )

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertRegex(f.getvalue(), "Exits the console")

        with patch('sys.stdout', new=StringIO()) as f:

            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertAlmostEqual(f.getvalue(), h)

        with patch('sys.stdout', new=StringIO()) as f:
            showHelp = (" Prints the string representation of an\n"
                        "        instance based on the class name and id \n")
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertAlmostEqual(f.getvalue(), showHelp)

        with patch('sys.stdout', new=StringIO()) as f:
            ctHelp = (" Creates a new instance of BaseModel, saves\n"
                      "        it (to the JSON file) and prints the id \n")
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertAlmostEqual(f.getvalue(), ctHelp)

        with patch('sys.stdout', new=StringIO()) as f:

            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertAlmostEqual(f.getvalue(), dHelp)

        with patch('sys.stdout', new=StringIO()) as f:
            aHelp = (
                " Prints all string representation of\n"
                "        all instances based or not on the class name \n")
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertAlmostEqual(f.getvalue(), aHelp)

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertAlmostEqual(f.getvalue(), self.u)

    def test_create_inst(self):
        """ Method to test if create command executes propertly """

        if os.path.isfile("file.json"):
            os.remove("file.json")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create myCat"))
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertTrue(os.path.isfile)

    def test_show(self):
        """ Method to test show method  """

        meow = User()
        meowID = meow.id

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show myCat"))
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(
                HBNBCommand().onecmd("show User {}".format(meowID)))
            self.assertEqual("{}\n".format(str(meow)), f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("show User 432432342"))
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """ Method to test destroy method """

        meow = User()
        meowID = meow.id

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy myCat"))
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(
                HBNBCommand().onecmd("destroy BaseModel 4645631634"))
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User {}"
                                                  .format(meowID)))
            self.assertEqual("", f.getvalue())

    def test_all(self):
        """ Method to test all method """

        if os.path.exists("file.json"):
            os.remove("file.json")
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIs(list, type(f.getvalue()))
        """
