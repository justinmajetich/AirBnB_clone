#!/usr/bin/python3
''' Tests for console'''

import sys
import unittest
from io import StringIO
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    ''' Testing the console'''

    """Check for Pep8 style conformance"""

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
