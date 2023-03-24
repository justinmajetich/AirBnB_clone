#!/usr/bin/python3
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User
from io import StringIO


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Sets up the HBNBCommand instance to be used in the tests"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Cleans up the HBNBCommand instance after the tests"""
        del self.console

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            # Executes the create command with User as argument
            self.console.onecmd('create User')
            new_id = f.getvalue().strip()
            objs = storage.all(User).values()
            # Search the User object with the new_id in the objects dictionary
            obj = [obj for obj in objs if obj.id == new_id]
            # Asserts User object was created and add to the objects dictionary
            self.assertEqual(len(obj), 1)
            self.assertEqual(obj[0].id, new_id)
            self.assertEqual(obj[0].__class__.__name__, 'User')
