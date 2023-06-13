#!/usr/bin/python3
"""Consle module"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand


class HBNBCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_quit('')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create('BaseModel')
            output = fake_out.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_show('BaseModel 12345')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_destroy('BaseModel 12345')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all('')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_count('BaseModel')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '0')

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_update('BaseModel 12345 name "test name"')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    # Add more test methods for other commands...


if __name__ == '__main__':
    unittest.main()
