#!/usr/bin/python3
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """test empty line from console"""

    @classmethod
    def setUp(self):
        """setup for json file"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        """teardown json file"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_prompt(self):
        """ test prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """ test empty line"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertEqual("", out.getvalue().strip())

    def test_all(self):
        """ test all function"""
        string = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("all Model"))
            self.assertEqual(string, out.getvalue().strip())

    def test_help_quit(self):
        """ test quit from help function"""
        string = "Exits the program with formatting"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(string, out.getvalue().strip())

    def test_help_EOF(self):
        """ test EOF from help"""
        string = "Exits the program without formatting"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(string, out.getvalue().strip())

    def test_show(self):
        """ test show from console"""
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(string, out.getvalue().strip())

    def test_update(self):
        """ test update from console"""
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(string, out.getvalue().strip())

    def test_destroy(self):
        """ test destroy from console"""
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(string, out.getvalue().strip())

    def test_create(self):
        """test create from console"""
        string = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(string, out.getvalue().strip())

    def test_all_with_period(self):
        """test all with dot notation"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
