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


if __name__ == '__main__':
    unittest.main()
