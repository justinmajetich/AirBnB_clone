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
            self.assertRegex(actual, "BaseModel")
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
        with patch("sys.stdout", new=StringIO()) as f:
            """Unknown Class David"""
            test_cmd_line = "David.show()"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** class doesn't exist **\n"
            actual = f.getvalue()
            self.assertEqual(actual, expected)
            f.seek(0)
            f.truncate(0)
            """instance id missing"""
            test_cmd_line = "User.show()"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** instance id missing **\n"
            actual = f.getvalue()
            self.assertEqual(actual, expected)
            f.seek(0)
            f.truncate(0)
            """Non-exisitng user id"""
            test_cmd_line = "User.show(non-exis-ting-user-id)"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "** no instance found **\n"
            actual = f.getvalue()
            self.assertEqual(actual, expected)
            f.seek(0)
            f.truncate(0)
            """existing id with and without quotes"""
            test_cmd_line = "create User"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            known_id = f.getvalue()
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "User.show({})".format(known_id)
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = r"^[User]\s+({}).+$".format(known_id.strip())
            actual = f.getvalue()
            self.assertRegex(actual, known_id.strip())
            self.assertRegex(actual, "User")
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "User.show(\"{}\")".format(known_id)
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            expected = "[User] ({})".format(known_id)
            actual = f.getvalue()
            self.assertRegex(actual, known_id.strip())
            self.assertRegex(actual, "User")
            f.seek(0)
            f.truncate(0)

    def test_all_norms(self):
        """Method to test for all """
        with patch("sys.stdout", new=StringIO()) as f:
            """Create User, Place and BaseModel for testing"""
            test_cmd_line = "create User"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            test_cmd_line = "create BaseModel"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            test_cmd_line = "create Place"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            f.seek(0)
            f.truncate(0)
            """Check for behaviour of all"""
            test_cmd_line = "all"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            result_string = f.getvalue()
            self.assertRegex(result_string, "BaseModel")
            self.assertRegex(result_string, "User")
            self.assertRegex(result_string, "Place")
            f.seek(0)
            f.truncate(0)
            """Check beaviour of all when a given class is used"""
            test_cmd_line = "all User"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            result_string = f.getvalue()
            self.assertNotRegex(result_string, "BaseModel")
            self.assertRegex(result_string, "User")
            self.assertNotRegex(result_string, "Place")
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "all Place"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            result_string = f.getvalue()
            self.assertNotRegex(result_string, "BaseModel")
            self.assertNotRegex(result_string, "User")
            self.assertRegex(result_string, "Place")
            f.seek(0)
            f.truncate(0)
            test_cmd_line = "all Place"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            result_string = f.getvalue()
            self.assertNotRegex(result_string, "BaseModel")
            self.assertNotRegex(result_string, "User")
            self.assertRegex(result_string, "Place")
            f.seek(0)
            f.truncate(0)
            """When an invalid class is passed"""
            test_cmd_line = "all David"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            result_string = f.getvalue()
            self.assertNotRegex(result_string, "BaseModel")
            self.assertNotRegex(result_string, "User")
            self.assertNotRegex(result_string, "Place")
            self.assertEqual(result_string, "** class doesn't exist **\n")
            f.seek(0)
            f.truncate(0)
            """What will be the behaviour when
            multiple valid classes are passed"""
            test_cmd_line = "all Place User"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            result_string = f.getvalue()
            self.assertNotRegex(result_string, "BaseModel")
            self.assertNotRegex(result_string, "User")
            self.assertRegex(result_string, "Place")
            f.seek(0)
            f.truncate(0)

    def test_all_norms(self):
        """Method to test for all """
        with patch("sys.stdout", new=StringIO()) as f:
            test_cmd_line = "create User"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            test_cmd_line = "create BaseModel"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            test_cmd_line = "create Place"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            f.seek(0)
            f.truncate(0)
            """Debatable behaviour of User.all(Place)"""
            test_cmd_line = "User.all(Place)"
            test_cmd_line = HBNBCommand().precmd(test_cmd_line)
            HBNBCommand().onecmd(test_cmd_line)
            self.assertRegex(f.getvalue().strip(), "User")
            f.seek(0)
            f.truncate(0)
