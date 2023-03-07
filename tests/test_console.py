#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.state import State
from os import getenv


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'Only applies to database storage')
class TestConsoleDB(unittest.TestCase):
    """Tests for the console when using database storage"""

    @classmethod
    def setUpClass(cls):
        """Set up for tests"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Tear down for tests"""
        del cls.console

    def tearDown(self):
        """Tear down"""
        storage.delete_all()

    def test_create(self):
        """Tests the create command with DB storage"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California"')
            state_id = f.getvalue().strip()

        self.assertTrue(state_id)

        state = storage.get("State", state_id)
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "California")