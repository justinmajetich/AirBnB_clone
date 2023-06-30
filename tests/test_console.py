#!/usr/bin/python3
"""Test for console"""
import unittest

from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models


class ConsoleTestCase(unittest.TestCase):
    """Test for console"""

    def setUp(self):
        self.console = HBNBCommand()
        self.stdout = StringIO()
        self.storage = models.storage

    def tearDown(self):
        del self.stdout
        del self.storage

    def test_create(self):
        """test create basic"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        # print(state_id)
        # print(len(state_id))
        self.assertTrue(len(state_id) == 36)

    def test_create_save(self):
        """test create save"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California')
        state_id = self.stdout.getvalue()[:-1]
        self.assertIsNotNone(
            self.storage.all()["State.{}".format(state_id)])

    def test_create_non_existing_class(self):
        """test non-existing class"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create MyModel')
        self.assertEqual("** class doesn't exist **\n",
                         self.stdout.getvalue())

    def test_all(self):
        """test all"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('all State')
        output = self.stdout.getvalue()[:-1]
        self.assertIn("State", output)
        self.assertIn("California", output)

    def test_update(self):
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
        """test destroy"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('destroy State {}'.format(state_id))
        # with patch('sys.stdout', self.stdout):
        #     self.console.onecmd('show State {}'.format(state_id))
        # self.assertEqual("** no instance found **\n",
        #                  self.stdout.getvalue())

    def test_show(self):
        """test show"""
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('create State name="California"')
        state_id = self.stdout.getvalue()[:-1]
        with patch('sys.stdout', self.stdout):
            self.console.onecmd('show State {}'.format(state_id))
        output = self.stdout.getvalue()[:-1]
        self.assertIn("California", output)
