#!/usr/bin/python3
"""Test command line module.
"""
import unittest
from unittest.mock import patch
from os import getenv
import sys
from io import StringIO
from re import search
import os
import pep8
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestHBCommand(unittest.TestCase):
    """This class contains all modules that test all
        functionalities of the command line.
    """

    if getenv("HBNB_TYPE_STORAGE") != "db":

        def setUp(self):
            """Clean code after each test.
            """
            if os.path.isfile("file.json"):
                os.remove("file.json")
            FileStorage._FileStorage__objects = {}

        def test_style_base(self):
            """test pep8
            """
            style = pep8.StyleGuide()
            m = style.check_files(["console.py"])
            self.assertEqual(m.total_errors, 0, "fix pep8")

        def test_docstring(self):
            """Test doc strings.
            """
            self.assertIsNotNone(HBNBCommand.__doc__)
            self.assertIsNotNone(HBNBCommand.precmd.__doc__)
            self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
            self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
            self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
            self.assertIsNotNone(HBNBCommand.do_create.__doc__)
            self.assertIsNotNone(HBNBCommand.do_show.__doc__)
            self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
            self.assertIsNotNone(HBNBCommand.do_all.__doc__)
            self.assertIsNotNone(HBNBCommand.do_update.__doc__)
            self.assertIsNotNone(HBNBCommand.do_count.__doc__)

        def test_help(self):
            """Test help message.
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help")
            val = f.getvalue()
            msg = """\nDocumented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update\n\n"""
            self.assertEqual(val, msg)

        def test_quit(self):
            """Test quit command.
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help quit")
            val = f.getvalue()
            msg = "Exits the program with formatting\n\n"
            self.assertEqual(val, msg)

        def test_help_EOF(self):
            """Test EOF command.
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help EOF")
            val = f.getvalue()
            msg = "Exits the program without formatting\n\n"
            self.assertEqual(val, msg)

        def test_create(self):
            """Test create command.
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help create")
            val = f.getvalue()
            msg = "Creates a class of any type\n[Usage]: create <className>\n\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create")
            val = f.getvalue()
            msg = "** class name missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create HELL")
            val = f.getvalue()
            msg = "** class doesn't exist **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("create BaseModel")
            val = f.getvalue()
            trex = r"\w+[-]\w+[-]\w+[-]\w+[-]\w+\n"
            self.assertTrue(search(trex, val))

        def test_show(self):
            """Test show command.
            """
            new = BaseModel()
            new.save()
            nid = new.id

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help show")
            val = f.getvalue()
            msg = "Shows an individual instance of a class\n\
    [Usage]: show <className> <objectId>\n\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show")
            val = f.getvalue()
            msg = "** class name missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show A")
            val = f.getvalue()
            msg = "** class doesn't exist **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show User")
            val = f.getvalue()
            msg = "** instance id missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show User 2")
            val = f.getvalue()
            msg = "** no instance found **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show BaseModel {}".format(nid))
            val = f.getvalue()
            trex = r"\[BaseModel\] \(.*\) .*"
            self.assertTrue(search(trex, val))

        def test_destroy(self):
            """Test destroy command.
            """
            new = BaseModel()
            new.save()
            nid = new.id

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help destroy")
            val = f.getvalue()
            msg = "Destroys an individual instance of a class\n\
    [Usage]: destroy <className> <objectId>\n\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy")
            val = f.getvalue()
            msg = "** class name missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy A")
            val = f.getvalue()
            msg = "** class doesn't exist **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy User")
            val = f.getvalue()
            msg = "** instance id missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy User 2")
            val = f.getvalue()
            msg = "** no instance found **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy BaseModel {}".format(nid))
            val = f.getvalue()
            msg = ""
            self.assertEqual(val, msg)

        def test_help_all(self):
            """Test all command.
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help all")
            val = f.getvalue()
            msg = "Shows all objects, or all of a class\n\
    [Usage]: all <className>\n\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all")
            val = f.getvalue()
            msg = "[]\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all A")
            val = f.getvalue()
            msg = "** class doesn't exist **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all City")
            val = f.getvalue()
            msg = "[]\n"
            self.assertEqual(val, msg)

            new = BaseModel()
            new.save()
            nid = new.id

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("all BaseModel {}".format(nid))
            val = f.getvalue()
            trex = r"[\.*]"
            self.assertTrue(search(trex, val))

        def test_update(self):
            """Test update command.
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help update")
            val = f.getvalue()
            msg = "Updates an object with new information\n\
    Usage: update <className> <id> <attName> <attVal>\n\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update")
            val = f.getvalue()
            msg = "** class name missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update A")
            val = f.getvalue()
            msg = "** class doesn't exist **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update User")
            val = f.getvalue()
            msg = "** instance id missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update User 2")
            val = f.getvalue()
            msg = "** no instance found **\n"
            self.assertEqual(val, msg)

            new = BaseModel()
            new.save()
            nid = new.id

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update BaseModel {}".format(nid))
            val = f.getvalue()
            msg = "** attribute name missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update BaseModel {} a".format(nid))
            val = f.getvalue()
            msg = "** value missing **\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update BaseModel {} a 2".format(nid))
            val = f.getvalue()
            msg = ""
            self.assertEqual(val, msg)

        def test_count(self):
            """Test count command.
            """
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("help count")
            val = f.getvalue()
            msg = "Usage: count <class_name>\n"
            self.assertEqual(val, msg)

            new = BaseModel()
            new.save()

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("count BaseModel")
            val = f.getvalue()
            msg = "1\n"
            self.assertEqual(val, msg)

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("count User)")
            val = f.getvalue()
            msg = "0\n"
            self.assertEqual(val, msg)


if __name__ == "__main__":
    unittest.main()
