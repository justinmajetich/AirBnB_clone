#!/usr/bin/python3
"""Defines unittests for console.py.
"""
import os
import sys
import unittest
import models
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class ConsoleTestCase(unittest.TestCase):
    """Class to test the HBNBCommand console"""
    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        self.stdout = StringIO()
        self.storage = models.storage

    def tearDown(self):
        """Tear down the test environment"""
        del self.stdout
        del self.storage

    def test_create(self):
        """Test the 'create' command"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State')
        state_id = self.stdout.getvalue()[:-1]
        self.assertTrue(len(state_id) == 36)

    def test_create_save(self):
        """Test the 'create' command and data saving"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        self.assertIsNotNone(
            self.storage.all()["State.{}".format(state_id)])

    def test_create_non_existing_class(self):
        """Test the 'create' command with a non-existing class"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create MyModel')
        self.assertEqual("** class doesn't exist **\n",
                         self.stdout.getvalue())

    def test_all(self):
        """Test the 'all' command"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('all State')
        output = self.stdout.getvalue()[:-1]
        self.assertIn("State", output)
        self.assertIn("California", output)

    def test_update(self):
        """Test the 'update' command"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd(
                'update State {} name="New California"'.format(state_id))
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('show State {}'.format(state_id))
        output = self.stdout.getvalue()[:-1]
        self.assertIn("California", output)

    def test_destroy(self):
        """Test the 'destroy' command"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('destroy State {}'.format(state_id))

    def test_show(self):
        """Test the 'show' command"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('show State {}'.format(state_id))
        output = self.stdout.getvalue()[:-1]
        self.assertIn("California", output)
