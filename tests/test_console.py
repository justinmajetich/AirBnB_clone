#!/usr/bin/python3

"""Tests for Console functions"""

import unittest
from unittest.mock import patch
import pep8
import os
from io import StringIO
import json
import tests
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """This class is use to test console funtions"""

    @classmethod
    def setUpClass(cls):
        """Test Setup"""
        cls.console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """Test tear down"""
        del cls.console

    def tearDown(self):
        """Delete temporary files file.json """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """Test if console.py complies with the pep8"""
        style = pep8.StyleGuide(quiet=True)
        res = style.check_files(["console.py"])
        self.assertEqual(res.total_errors, 0, 'Fix Pep8')

    def test_docstring(self):
        """Test if all functions and classes are documented in console.py"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.preloop.__doc__)
        self.assertIsNotNone(HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.help_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.help_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.help_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.help_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.help_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.help_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.help_update.__doc__)

    def test_emptyline(self):
        """Test emptyline"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test Create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create abcdefgh")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="Arizona"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all State')
            self.assertEqual('["[State]', f.getvalue()[:9])

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all abcdefgh")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all City")
            self.assertEqual("[]\n", f.getvalue())

    def test_z_all(self):
        """Test all command when call on class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("abcdefgh.all()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City.all()")
            self.assertEqual("[]\n", f.getvalue())

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show abcdef")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel abcdef")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_z_show(self):
        """Test show command when call on class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("abcdef.show()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show()")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.show(abcdef)")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Alx")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Place")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User Yan")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_z_destroy(self):
        """Test destroy when calling on a class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.destroy()")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place.destroy()")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.destroy(12345)")
            self.assertEqual("** no instance found **\n", f.getvalue())

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update abcdefgh")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update State")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User email='yan@email.com'" +
                                " password='pd' first_name='ya'" +
                                " last_name='ti'")
            self.console.onecmd("all User")
            obj = f.getvalue()
        user_id = obj[obj.find('(') + 1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User " + user_id)
            self.assertEqual("** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User " + user_id + " Name")
            self.assertEqual("** value missing **\n", f.getvalue())

    def test_z_update(self):
        """Test update command when calling with a class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("abcdefg.update()")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State.update()")
            self.assertEqual("** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.update(12345)")
            self.assertEqual("** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            obj = f.getvalue()
        user_id = obj[obj.find('(') + 1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.update(" + user_id + ")")
            self.assertEqual("** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.update({}, name)".format(user_id))
            self.assertEqual("** value missing **\n", f.getvalue())

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count abcdefg")
            self.assertEqual("0\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count State")
            self.assertEqual("0\n", f.getvalue())


if __name__ == '__main__':
    unittest.main()
