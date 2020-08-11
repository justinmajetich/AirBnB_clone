#!/usr/bin/python3
"""Test module for console
    """
import unittest
from unittest.mock import patch
import sys
from io import StringIO
from re import search
import os
import pep8
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Test console: it will test the pep8 and docstring"""

    def test_base_pep8_conformance_console(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_pep8_conformance_consoletest(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./tests/test_console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_console_docstring(self):
        """test docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_docstring(self):
        """test command interpreter docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_help_EOF(self):
        """ Help command test """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            value = f.getvalue()
            msg = "Exits the program without formatting\n\n"
            self.assertEqual(value, msg)
