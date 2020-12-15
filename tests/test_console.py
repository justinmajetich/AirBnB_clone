#!/usr/bin/python3
"""Test for file console.
"""
import unittest
from console import HBNBCommand
from io import StringIO
import os
import sys
import console
from models.base_model import BaseModel
from unittest.mock import patch
from models import storage


class testHBNBCommand(unittest.TestCase):
    def test_docstrings_console(self):
        """check for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        value = f.getvalue()
        self.assertEqual(value, "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create hbnb")
        value = f.getvalue()
        self.assertEqual(value, "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel name=\"Arizona\"")
        value = f.getvalue().strip()

    def test_prueba(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel name=\"Arizona\"")
        self.assertTrue('"Arizona"' in storage.all().values())
