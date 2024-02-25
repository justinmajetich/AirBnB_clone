#!/usr/bin/python3
"""Test module for the HBNBCommand class in console.py."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test the do_create method."""
        # Test create command with valid input
        with patch('builtins.input', side_effect=['create BaseModel', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # Check if ID is generated

        # Test create command with invalid class name
        with patch('builtins.input', side_effect=['create NotAClass', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

        # Test create command with invalid attribute value
        with patch('builtins.input', side_effect=['create BaseModel name=Test', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # Check if ID is generated

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """Test the do_show method."""
        # Create a BaseModel instance
        obj = BaseModel()
        obj.save()
        obj_id = obj.id

        # Test show command with valid input
        with patch('builtins.input', side_effect=['show BaseModel {}'.format(obj_id), 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertTrue(obj_id in output)

        # Test show command with invalid class name
        with patch('builtins.input', side_effect=['show NotAClass {}'.format(obj_id), 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

        # Test show command with invalid instance id
        with patch('builtins.input', side_effect=['show BaseModel invalid_id', 'quit']):
            HBNBCommand().cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    # Add more test methods to cover other functionality of HBNBCommand


if __name__ == "__main__":
    unittest.main()
