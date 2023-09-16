#!/usr/bin/python3
"""Console test cases"""

import unittest
import os
from unittest.mock import patch
from io import StringIO
import json
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class TestConsole(unittest.TestCase):
    """Console class test cases."""

    @classmethod
    def setUpClass(my_class):
        """Test cases Setup"""
        my_class.cmd = HBNBCommand()

    @classmethod
    def teardown(my_class):
        """Tear down the Setup"""
        del my_class.cmd

    def tearDown(self):
        """Remove temp files (file.json)"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_console_docstrings(self):
        """checking the method's docstring."""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_Console_prompt_empty_line(self):
        """Check empty line."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue())

    def test_quit(self):
        """test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd('create User email="hoal@.com" password="1234"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.onecmd("all User")


class ConsoleShowTest(unittest.TestCase):
    """Test show command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_show_no_class(self):
        """Test show no class"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show")
            self.assertEqual("** class name missing **", op.getvalue().strip())

    def test_Console_show_no_existing_class(self):
        """Test show class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show Cake")
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_no_id(self):
        """Test show class no id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show BaseModel")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_no_existing_id(self):
        """Test show class no existing id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("show BaseModel no-id-123")
            expected = "** no instance found **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_show_instance(self):
        """Test show class id"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(_id)]
            command = "show BaseModel {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(_id)]
            command = "show User {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(_id)]
            command = "show Amenity {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(_id)]
            command = "show City {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(_id)]
            command = "show Place {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(_id)]
            command = "show Review {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(_id)]
            command = "show State {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())


class ConsoleDestroyTest(unittest.TestCase):
    """Test destroy command"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "_file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("_file.json", "file.json")
        except IOError:
            pass

    def test_Console_destroy_no_class(self):
        """Test destroy no class"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("** class name missing **", op.getvalue().strip())

    def test_Console_destroy_no_existing_class(self):
        """Test destroy class doesn't exist"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy Cake")
            expected = "** class doesn't exist **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_destroy_no_id(self):
        """Test destroy class no id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy BaseModel")
            expected = "** instance id missing **"
            self.assertEqual(expected, op.getvalue().strip())

    def test_Console_destroy_no_existing_id(self):
        """Test destroy class no existing id"""
        with patch("sys.stdout", new=StringIO()) as op:
            HBNBCommand().onecmd("destroy BaseModel no-id-123")
            self.assertEqual("** no instance found **", op.getvalue().strip())

    def test_Console_destroy_instance(self):
        """destroy class id"""
        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy BaseModel {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show BaseModel {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create User"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy User {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show User {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy Amenity {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Amenity {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create City"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy City {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show City {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy Place {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Place {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy Review {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show Review {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as op:
            _id = ""
            self.assertFalse(HBNBCommand().onecmd("create State"))
            _id = op.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as op:
            command = "destroy State {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("", op.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as op:
            command = "show State {}".format(_id)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual("** no instance found **", op.getvalue().strip())

