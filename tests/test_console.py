#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys


""" This module the test cases for different
for the console that we built already"""


class TestConsole(unittest.TestCase):
    """This class contains several testcases of
    the console features and other associated features"""

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_create(self):
        """Method to test the create function..."""
        with patch('sys.stdout', new=StringIO()) as f:
            test_cmd_line = "create   "
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class name missing **\n"
            actual = f.getvalue()
            self.assertEqual(expected, actual)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "create #BaseModel"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class doesn't exist **\n"
            actual = f.getvalue()
            self.assertEqual(expected, actual)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "create '  '"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class doesn't exist **\n"
            actual = f.getvalue()
            self.assertEqual(expected, actual)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "create BaseModel"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected_len = 28
            actual_len = len(f.getvalue())
            self.assertGreaterEqual(actual, expected)
            f.seek(0)
            f.truncate(0)
            """         test_cmd_line = "BaseModel.create()"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected_len = 28
            actual_len = len(f.getvalue())
            self.assertGreaterEqual("None", expected)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "BaseModel.create(\"12345\")"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class doesn't exist **\n"
            actual = f.getvalue()
            self.assertGreaterEqual(actual, expected)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "BaseModel.create(\"\")"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class name missingi **\n"
            actual = f.getvalue()
            self.assertGreaterEqual(actual, expected)
            f.seek(0)
            f.truncate(0)"""

    def test_show_normal(self):
        """Method to test show"""
        with patch('sys.stdout', new=StringIO()) as f:
            test_cmd_line = "create BaseModel"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            known_id = f.getvalue()
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "show Base"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class doesn't exist **\n"
            actual = f.getvalue()
            self.assertEqual(expected, actual)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "show "
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class name missing **\n"
            actual = f.getvalue()
            self.assertEqual(expected, actual)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "show BaseModel {}".format(known_id)
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            regex = known_id.strip()
            actual = f.getvalue()
            self.assertRegex(actual, regex)
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "show BaseModel"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** instance id missing **\n"
            actual = f.getvalue()
            self.assertEqual(expected, actual)
            f.seek(0)
            f.truncate(0)
            """Show for known_id inside quotes
            The result here is instance id not found, which
            is debatable as a behaviour of the console"""
            test_cmd_line = "show BaseModel \"{}\"".format(known_id)
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            regex = known_id.strip()
            actual = f.getvalue()
            self.assertNotRegex(actual, regex)
            f.seek(0)
            f.truncate(0)
            """Show for known_id where w/o quotes but with jargon
            after the id"""
            test_cmd_line = "show BaseModel {} xyzfoobar".format(known_id)
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** no instance found **\n"
            actual = f.getvalue()
            self.assertEqual(actual, expected)
            f.seek(0)
            f.truncate(0)

    def test_show_alt_syntax(self):
        with patch("sys.stdout", new=StringIO()):
            pass
