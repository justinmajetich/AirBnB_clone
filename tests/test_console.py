#!/usr/bin/python3
"""Module for testing ``HBNBCommand`` class
"""
import os
import sys
import unittest
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models import storage
from tests import reset_stream


class TestHBNBCommand(unittest.TestCase):
    """Class for Testing ``HBNBCommand`` class
    """
    def test_FileStorage_create(self):
        with patch("sys.stdout", new=StringIO()) as output:
            cmd = HBNBCommand()
            cmd.onecmd('State.count()')
            total_states = output.getvalue().strip()
#            reset_stream(output)
            cmd.onecmd('create State name="California"')
            reset_stream(output)
            cmd.onecmd('State.count()')
            self.assertEqual(total_states, output.getvalue().strip())
