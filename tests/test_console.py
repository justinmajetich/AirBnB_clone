#!/usr/bin/python3
"""
test module for testing the console one-line program commands
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import models
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """test Console class"""
    def setUp(self):
        """setup"""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.console = HBNBCommand()
        models.storage._FileStorage__objects.clear()

    def tearDown(self):
        """teardown"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.console

    def test_EOF(self):
        """test the end-of-file condition"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertEqual("\n", f.getvalue())  # no output

    def test_quit(self):
        """test the quit command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_help(self):
        """test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):",
                          f.getvalue())

    def test_create(self):
        """test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertEqual(36, len(f.getvalue().strip()))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertEqual(36, len(f.getvalue().strip()))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.assertEqual(36, len(f.getvalue().strip()))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.assertEqual(36, len(f.getvalue().strip()))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.assertEqual(36, len(f.getvalue().strip()))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.assertEqual(36, len(f.getvalue().strip()))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.assertEqual(36, len(f.getvalue().strip()))

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State name='California' id='tester'")
            self.assertEqual(6, len(f.getvalue().strip()))
            self.assertEqual('tester\n', f.getvalue())
            self.console.onecmd("show State tester")
            self.assertEqual('tester', f.getvalue()[0:6])

    def test_show(self):
        """test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Amenity")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(key))
            self.assertIn(key, f.getvalue())

    def test_emptyline(self):
        """test the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual("", f.getvalue())

    def test_destroy(self):
        """test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy State")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy City")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Amenity")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Place")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Review")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(key))
            self.assertEqual("", f.getvalue())

    def test_all(self):
        """test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all City")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Amenity")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Review")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertIn(key, f.getvalue())

    def test_update(self):
        """test the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update State")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update City")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Amenity")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Place")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Review")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('update BaseModel {} name "Betty"'
                                .format(key))
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(key))
            self.assertIn("Betty", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                                'update BaseModel ' + key + ' email '
                                + '"betty@holberton.com"')
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(key))
            self.assertIn("betty@holberton.com", f.getvalue())

    def test_count(self):
        """test the count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            self.assertEqual("0\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count User")
            self.assertEqual("0\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count State")
            self.assertEqual("0\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count City")
            self.assertEqual("0\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count Amenity")
            self.assertEqual("0\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count Place")
            self.assertEqual("0\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count Review")
            self.assertEqual("0\n", f.getvalue())

        self.console.onecmd("create User")
        self.console.onecmd("create City")
        self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count User")
            self.assertEqual("2\n", f.getvalue())

    def test_all_dot_commands(self):
        """test the all dot commands"""
        uid = None
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            uid = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.show()")
            self.console.onecmd(processed_line)
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.show("{}")'.format(uid))
            self.console.onecmd(processed_line)
            self.assertIn(uid, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.count()")
            self.console.onecmd(processed_line)
            self.assertEqual("1\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.update()")
            self.console.onecmd(processed_line)
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.update("{}"'.format(uid)
                                                 + ', "name", "Betty")')
            self.console.onecmd(processed_line)
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.show("{}")'.format(uid))
            self.console.onecmd(processed_line)
            self.assertIn("Betty", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.update("' + uid +
                                                 '", { "name": "Holberton", '
                                                 + '"email": "b@hbtn.com" })')
            self.console.onecmd(processed_line)
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.show("{}")'.format(uid))
            self.console.onecmd(processed_line)
            output = f.getvalue()
            self.assertIn("Holberton", output)
            self.assertIn("b@hbtn.com", output)

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.destroy()")
            self.console.onecmd(processed_line)
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.destroy("{}")'
                                                 .format(uid))
            self.console.onecmd(processed_line)
            self.assertEqual("", f.getvalue())
