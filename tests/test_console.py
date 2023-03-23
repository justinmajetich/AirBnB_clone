#!/usr/bin/python3
"""task for changes to console"""

import unittest
import io
from console import HBNBCommand
import sys


class Test(unittest.TestCase):
    def test_create_instance(self):
        """create state"""
        output = io.StringIO()
        sys.stdout = output
        console = HBNBCommand()
        console.onecmd("create State id='123' name=test")
        sys.stdout = sys.__stdout__
        expected_output = output.getvalue()
        self.assertIn("test", expected_output)
