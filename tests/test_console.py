#!/usr/bin/python3
"""Unittest for console"""

import os
from unittest.mock import patch
import sys
from io import StringIO
from console import HBNBCommand
import unittest
import pep8


class TestConsole(unittest.TestCase):
    """Test the console"""

    def test_pep8(self):
        """Test for pep8 style"""
        pep8_style = pep8.StyleGuide(quiet=True)
        res = pep8_style.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0, "errors found in console")

    def test_docstring(self):
        """Test for docstring"""
        set.assertIsNotNone(HBNBCommand.__doc__)

    def test_do_EOF(self):
        """Test for EOF method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.HBNB.onecmd('EOF'))

    def test_do_create(self):
        """Test for create method """
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create ext")
            self.assertEqual("\n** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create mis")
            self.assertEqual("\n** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            base = f.getvalue().strip()
            self.assertIn(base, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            state = f.getvalue().strip()
            self.assertIn(state, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            user = f.getvalue().strip()
            self.assertIn(user, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            city = f.getvalue().strip()
            self.assertIn(city, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            place = f.getvalue().strip()
            self.assertIn(place, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            amenity = f.getvalue().strip()
            self.assertIn(amenity, f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("create Review")
            review = f.getvalue().strip()
            self.assertIn(review, f.getvalue())

    def test_do_all(self):
        """Test for all method """
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("all")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_do_show(self):
        """Test for show method """
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("show")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_do_update(self):
        """Test for update method """
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("update")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")

    def test_do_destroy(self):
        """Test for destroy method """
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("destroy")
            self.assertEqual(f.getvalue(), "\n** class doesn't exist **\n")


if __name__ == "__main__":
    unittest.main()
