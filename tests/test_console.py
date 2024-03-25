#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
from console import HBNBCommand
from models.__init__ import storage


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):

        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    @patch("sys.stdout", new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, function, *args):
        if callable(function):
            function(*args)
        else:
            raise TypeError("The 'function' argument must be callable.")
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.do_quit("")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        with self.assertRaises(SystemExit):
            self.console.do_EOF("")
        self.assertEqual(mock_stdout.getvalue(), "\n")

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.emptyline()
            self.assertEqual(mock_stdout.getvalue(), "")

    def test_precmd(self):
        test_line = "create BaseModel"
        expected_result = "create BaseModel"
        self.assertEqual(self.console.precmd(test_line), expected_result)

        test_line = "User.create()"
        expected_result = "create User"
        self.assertEqual(self.console.precmd(test_line), expected_result)

        test_line = "User.create() 123 {'name': 'John'}"
        expected_result = "create User 123 {'name': 'John'}"
        self.assertEqual(self.console.precmd(test_line), expected_result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        self.console.do_create("BaseModel")
        self.assertIn("created_at", storage.all()
                      ["BaseModel." +
                       mock_stdout.getvalue().strip()].to_dict())
        self.assertIn("updated_at", storage.all()
                      ["BaseModel." +
                       mock_stdout.getvalue().strip()].to_dict())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        self.console.do_show("BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(),
                         "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        self.console.do_destroy("BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(),
                         "** instance id missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        self.console.do_all("")
        self.assertEqual(mock_stdout.getvalue().strip(), "[]")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        self.console.do_count("BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "0")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        self.console.do_update("BaseModel")
        self.assertIn("** instance id missing **",
                      mock_stdout.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
