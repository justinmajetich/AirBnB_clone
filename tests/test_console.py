#!/usr/bin/python3
''' Tests for console'''

import sys
import unittest
import pep8
from io import StringIO
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    ''' Testing the console'''

    """Check for Pep8 style conformance"""

    def test_pep8_console(self):
        """Pep8 for the console"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def setUp(self):
        """ setup """
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        """ tearDown """
        sys.stdout = self.backup

if __name__ == "__main__":
    unittest.main()
