#!/usr/bin/python3
""" Unittest for the console """
import unittest
from unittest.mock import patch
import os
from io import StringIO

import console
from models import storage


class TestConsole(unittest.TestCase):
    """ Testing the console """

    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.cmd = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove 'file.json'"""
        try:
            os.remove("file.json")
        except:
            pass

    # Check existence of Docs in console module
    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(console.__doc__) >= 1)

    # Check existence of Docs in test_console module
    def test_docstrings_in_test_console(self):
        """Test docstrings exist in test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    def test_create(self):
        """ Test create command """
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create")
            self.assertEqual(output.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd("create undefinedClass")
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create Place name="Nzaha_T" longitude=-122.431297 latitude="WRONG_TYPE"')
        for obj in storage.all().values():
            self.assertEqual(obj.name, "Nzaha_T")
            self.assertEqual(obj.longitude, -122.431297)
            self.assertEqual(obj.latitude, 0.0)
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create City')
        self.assertEqual(len(storage.all()), 2)


if __name__ == '__main__':
    unittest.main()
