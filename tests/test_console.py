#!/usr/bin/python3
""" Modules for Console tests"""
import unittest
from models.base_model import BaseModel
from console import HBNBCommand
import sys
from io import StringIO
import io
import unittest.mock
import os


class TestConsole(unittest.TestCase):
    """ tests console """
    @classmethod
    def tearDown(self):
        """ removes json file """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def create(self):
        """ creates an instance of interpreter """
        return HBNBCommand()

    """
    def test_quit(self):
         test the quit command
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
         test the EOF command
        with unittest.mock.patch('sys.stdout',
        new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("EOF")
            self.assertEqual(mock_stdout.getvalue(), None)
    """

    def test_create_normal(self):
        """ test the create command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("create City")
            self.assertEqual(type(mock_stdout.getvalue()), str)

    def test_show(self):
        """ test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("create City")
            city_id = mock_stdout.getvalue()
            console.onecmd(f"show City {city_id}")
            self.assertIsInstance(mock_stdout.getvalue(), str)

    def test_show_error1(self):
        """ test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("show")
            self.assertEqual(mock_stdout.getvalue(),
                             "** class name missing **\n")

    def test_show_error2(self):
        """ test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("show City")
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")

    def test_show_error3(self):
        """ test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            city_id = mock_stdout.getvalue()
            console.onecmd(f"show Bla {city_id}")
            self.assertEqual(mock_stdout.getvalue(),
                             "** class doesn't exist **\n")

    def test_destroy_error1(self):
        """ test the destroy command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("destroy City")
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")

    def test_destroy_error2(self):
        """ test the destroy command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            city_id = mock_stdout.getvalue()
            console.onecmd(f"destroy Bla {city_id}")
            self.assertEqual(mock_stdout.getvalue(),
                             "** class doesn't exist **\n")

    def test_destroy_error3(self):
        """ test the destroy command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            city_id = mock_stdout.getvalue()
            console.onecmd(f"destroy {city_id}")
            self.assertEqual(mock_stdout.getvalue(),
                             "** class name missing **\n")

    def test_all(self):
        """ test the all command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd('create State name="France"')
            console.onecmd("all State")
            self.assertIn("France", mock_stdout.getvalue())

    def test_update_1(self):
        """ test the update command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("update User")
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")
