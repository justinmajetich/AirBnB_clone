#!/usr/bin/python3
"""Test for console"""
import unittest

from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models


class HBNBCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_prompt(self):
        self.assertEqual('(hbnb) ', self.console.prompt)

    def test_preloop(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.preloop()
            self.assertEqual('(hbnb)\n', mock_stdout.getvalue())

    def test_precmd(self):
        line = self.console.precmd('show BaseModel 123')
        self.assertEqual('show BaseModel 123', line)

        line = self.console.precmd('BaseModel.show(123)')
        self.assertEqual('show BaseModel 123', line)

    def test_postcmd(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            stop = self.console.postcmd(stop=True, line='')
            self.assertEqual('(hbnb) ', mock_stdout.getvalue())
            self.assertTrue(stop)

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.console.do_quit('')

    def test_do_EOF(self):
        with self.assertRaises(SystemExit):
            self.console.do_EOF('')

    def test_emptyline(self):
        pass  # Emptyline method does nothing, no need to test

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.do_create('BaseModel')
            self.assertIn('\n', mock_stdout.getvalue())

            self.console.do_create('InvalidClass')
            self.assertIn("** class doesn't exist **\n", mock_stdout.getvalue())

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.do_show('BaseModel 123')
            self.assertIn("** instance id missing **\n", mock_stdout.getvalue())

            self.console.do_show('InvalidClass')
            self.assertIn("** class doesn't exist **\n", mock_stdout.getvalue())

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.do_destroy('BaseModel 123')
            self.assertIn("** instance id missing **\n", mock_stdout.getvalue())

            self.console.do_destroy('InvalidClass')
            self.assertIn("** class doesn't exist **\n", mock_stdout.getvalue())

    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.do_all('')
            self.assertIn('[', mock_stdout.getvalue())

            self.console.do_all('InvalidClass')
            self.assertIn("** class doesn't exist **\n", mock_stdout.getvalue())

    def test_do_count(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.do_count('BaseModel')
            self.assertIn('0\n', mock_stdout.getvalue())

            self.console.do_count('InvalidClass')
            self.assertIn('0\n', mock_stdout.getvalue())

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.do_update('BaseModel 123')
            self.assertIn("** attribute name missing **\n", mock_stdout.getvalue())

            self.console.do_update('InvalidClass')
            self.assertIn("** class doesn't exist **\n", mock_stdout.getvalue())
