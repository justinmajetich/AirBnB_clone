#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This test module defines tests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Unit tests for the HBNBCommand class
    """

    def tearDown(self):
        """
        Clean up the test environment after each test method is executed.
        """
        self.console = None

    def test_EOF(self):
        """
        Test the EOF command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd('EOF'))
            self.assertEqual(f.getvalue(), '\n')

    def test_do_create(self):
        """
        Test the create command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_do_show(self):
        """
        Test the show command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy(self):
        """
        Test the destroy command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BaseModel 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_all(self):
        """
        Test the all command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('all')
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_do_update(self):
        """
        Test the update command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(
                'update BaseModel 1234-5678-9012 name "John Doe"')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_help(self):
        """
        Test the help command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertIn('Documented commands', output)
            self.assertIn(
                'EOF  all  create  destroy  help  quit  show  update', output)

    def test_create_missing_class_name(self):
        """
        Test the create command with missing class name.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_missing_class_name(self):
        """
        Test the show command with missing class name.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_destroy_missing_class_name(self):
        """
        Test the destroy command with missing class name.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_update_missing_class_name(self):
        """
        Test the update command with missing class name.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update')
            output = f.getvalue().strip()
            self.assertEqual(output, '** class name missing **')

    def test_show_missing_instance_id(self):
        """
        Test the show command with missing instance id.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_destroy_missing_instance_id(self):
        """
        Test the destroy command with missing instance id.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_update_missing_instance_id(self):
        """
        Test the update command with missing instance id.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel')
            output = f.getvalue().strip()
            self.assertEqual(output, '** instance id missing **')

    def test_user_show_command(self):
        """
        Test the show command for User class.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_user_destroy_command(self):
        """
        Test the destroy command for User class.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_base_model_show_command(self):
        """
        Test the show command for BaseModel class.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show BaseModel 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_base_model_destroy_command(self):
        """
        Test the destroy command for BaseModel class.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy BaseModel 1234-5678-9012')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
