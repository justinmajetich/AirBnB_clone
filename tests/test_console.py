#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand testing setup.

        Temporarily rename any existing file.json.
        Reset FileStorage objects dictionary.
        Create an instance of the command interpreter.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand testing teardown.

        Restore original file.json.
        Delete the test HBNBCommand instance.
        """
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_docstrings(self):
        """Check for docstrings."""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test empty line input."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("\n")
            self.assertEqual("", captured_output.getvalue())

    def test_quit(self):
        """Test quit command input."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("quit")
            self.assertEqual("", captured_output.getvalue())

    def test_EOF(self):
        """Test that EOF quits."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.assertTrue(self.HBNB.onecmd("EOF"))

    def test_create_errors(self):
        """Test create command errors."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create(self):
        """Test create command."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create BaseModel")
            bm = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create User")
            us = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create State")
            st = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create Place")
            pl = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create City")
            ct = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create Review")
            rv = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("create Amenity")
            am = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bm, captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all User")
            self.assertIn(us, captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all State")
            self.assertIn(st, captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all Place")
            self.assertIn(pl, captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all City")
            self.assertIn(ct, captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all Review")
            self.assertIn(rv, captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all Amenity")
            self.assertIn(am, captured_output.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_create_kwargs(self):
        """Test create command with kwargs."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            call = ('create Place city_id="0001" name="My_house" '
                    'number_rooms=4 latitude=37.77 longitude=a')
            self.HBNB.onecmd(call)
            pl = captured_output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all Place")
            output = captured_output.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': 'My house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'latitude': 37.77", output)
            self.assertNotIn("'longitude'", output)

    def test_show(self):
        """Test show command."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                "** no instance found **\n", captured_output.getvalue())

    def test_destroy(self):
        """Test destroy command input."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", captured_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", captured_output.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_all(self):
        """Test all command input."""
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all State")
            self.assertEqual("[]\n", captured_output.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_update(self):
        """Test update command input."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("update sldkfjsl")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("update User 12345")
            self.assertEqual(
                "** no instance found **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("all User")
            obj = captured_output.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", captured_output.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_z_all(self):
        """Test alternate all command."""
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("asdfsdfsd.all()")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch("sys.stdout", new=StringIO()) as captured_output:
            self.HBNB.onecmd("State.all()")
            self.assertEqual("[]\n", captured_output.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_z_count(self):
        """Test count command inpout"""
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("asdfsdfsd.count()")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("State.count()")
            self.assertEqual("0\n", captured_output.getvalue())

    def test_z_show(self):
        """Test alternate show command inpout"""
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("safdsa.show()")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("BaseModel.show(abcd-123)")
            self.assertEqual(
                "** no instance found **\n", captured_output.getvalue())

    def test_destroy(self):
        """Test alternate destroy command inpout"""
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("Galaxy.destroy()")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("User.destroy(12345)")
            self.assertEqual(
                "** no instance found **\n", captured_output.getvalue())

    @unittest.skipIf(type(models.storage) == DBStorage, "Testing DBStorage")
    def test_update(self):
        """Test alternate destroy command inpout"""
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("sldkfjsl.update()")
            self.assertEqual(
                "** class doesn't exist **\n", captured_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("User.update(12345)")
            self.assertEqual(
                "** no instance found **\n", captured_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("all User")
            obj = captured_output.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("User.update(" + my_id + ")")
            self.assertEqual(
                "** attribute name missing **\n", captured_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as captured_output:
            self.HBNB.onecmd("User.update(" + my_id + ", name)")
            self.assertEqual(
                "** value missing **\n", captured_output.getvalue())


if __name__ == "__main__":
    unittest.main()