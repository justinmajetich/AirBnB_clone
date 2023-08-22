#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from io import StringIO
import console
from models.engine.file_storage import FileStorage
import os
from os import getenv
from console import HBNBCommand
import json
import tests


class TestConsole(unittest.TestCase):
    """File to test AirBnB's project cases"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_create(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual(
                "[\"[User", f.getvalue()[:7])

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_create_v2(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show State {}".format(id))
            self.assertEqual(
                "[State]", f.getvalue()[:7])
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create Place latitude=7.89')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create Place max_guest=5')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)

    def test_create_v2_params(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="ilovetim@google.com"\
                               password="timisboss"\
                               first_name="Farrukh"')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show User {}".format(id))
            print(f.getvalue())

    def test_show(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel abcd-123")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_all(self):
        """ """
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_update(self):
        """Test update command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update sldkfjsl")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update User " + id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())

    def test_z_all(self):
        """Test alternate all command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("asdfsdfsd.all()")
            self.assertEqual(
                "", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("State.all()")
            self.assertEqual("", f.getvalue())

    def test_z_count(self):
        """Test count command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("asdfsdfsd.count()")
            self.assertEqual(
                "", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("State.count()")
            self.assertEqual("", f.getvalue())

    def test_z_show(self):
        """Test alternate show command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("safdsa.show()")
            self.assertEqual(
                "", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("BaseModel.show(abcd-123)")
            self.assertEqual(
                "", f.getvalue())

    def test_z_destroy(self):
        """Test alternate destroy command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("Galaxy.destroy()")
            self.assertEqual(
                "", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.destroy(12345)")
            self.assertEqual(
                "", f.getvalue())

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_update_error(self):
        """Test alternate update command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("sldkfjsl.update()")
            self.assertEqual(
                "", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(12345)")
            self.assertEqual(
                "", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + id + ")")
            self.assertEqual(
                "", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("User.update(" + id + ", name)")
            self.assertEqual(
                "", f.getvalue())


if __name__ == "__main__":
    unittest.main()
