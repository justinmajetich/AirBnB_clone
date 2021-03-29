#!/usr/bin/python3
"""testing the console"""
from console import HBNBCommand
from io import StringIO
import unittest
import datetime
from uuid import UUID
import json
import os


class test_console(unittest.TestCase):
    """test_console"""

    def test_create(self):
        '''test_create'''
        error = "** class name missing **"
        with unittest.mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(error, f.getvalue().strip())
