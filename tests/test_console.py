#!/usr/bin/python3
"""Task for changes to console"""
import unittest
import io
from console import HBNBCommand
import sys


class Test(unittest.TestCase):
    def test_create_instance(self):
        """Create state"""
        output = io.StringIO()
        sys.stdout = output
        console = HBNBCommand()
        console.onecmd("create User email=\"test\" password=\"2104\" id=\"2\"")
        sys.stdout = sys.__stdout__
        expected_output = output.getvalue()
        self.assertIn('2', expected_output)
