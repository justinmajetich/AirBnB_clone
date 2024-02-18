#!/usr/bin/python3
""" Module for testing the console """
import unittest
import os
from models import storage
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class testConsole(unittest.TestCase):
    """Test the console commands"""

    def setUp(self):
        """Set up test environment """
        self.objs = storage.all().copy()

    def tearDown(self):
        """Remove file storage"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def testCreateUser(self):
        """Create user"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
        id = output.getvalue().replace('\n', '')
        self.assertNotEqual(self.objs, storage.all())
        self.assertIn(f"User.{id}", storage.all())
        self.assertEqual(len(storage.all()), len(self.objs) + 1)

    def testCreateState(self):
        """Create state"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create State name="Texas"')
        id = output.getvalue().replace('\n', '')
        state_dict = storage.all()[f"State.{id}"].to_dict()
        self.assertNotEqual(self.objs, storage.all())
        self.assertEqual(len(storage.all()), len(self.objs) + 1)
        self.assertIn(f"State.{id}", storage.all())
        self.assertIn('name', state_dict.keys())
        self.assertEqual(state_dict['name'], "Texas")
        self.assertIs(type(state_dict['name']), str)

    def testCreatePlace(self):
        """Create a place"""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create Place name="my_home" number_rooms=3')
        id = output.getvalue().replace('\n', '')
        place_dict = storage.all()[f"Place.{id}"].to_dict()
        self.assertNotEqual(self.objs, storage.all())
        self.assertEqual(len(storage.all()), len(self.objs) + 1)
        self.assertIn(f"Place.{id}", storage.all())
        self.assertIn('name', place_dict.keys())
        self.assertIn('number_rooms', place_dict.keys())
        self.assertEqual(place_dict['name'], "my home")
        self.assertEqual(place_dict['number_rooms'], 3)
        self.assertIs(type(place_dict['name']), str)
        self.assertIs(type(place_dict['number_rooms']), int)
