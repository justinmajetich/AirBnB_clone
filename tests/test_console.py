#!/usr/bin/python3
""" Unittests for console """
from models import storage
from console import HBNBCommand
import console
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestConsole(TestCase):
    """test cases for console"""
    def test_docstring(self):
        """xhecking docstring"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

    def test_do_create(self):
        """ test do create"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            state_count = int(f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BadClassName")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

        HBNBCommand().onecmd("create State name=\"California\"")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "{}\n".format(state_count + 1))

        HBNBCommand().onecmd("create State name=\"Nevada\"")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count State")
            self.assertEqual(f.getvalue(), "{}\n".format(state_count + 2))
