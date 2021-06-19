#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import sys
from console import HBNBcommand
from io import StringIO
from unittest.mock import patch
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "DBstorage")
class test_dbstorage(unittest.TestCase):
    """test class for dbstorage"""

    def test_all(self):
        """test db all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBcommand().onecmd("create State name='Empty'")
            state = f.getvalue()
            state = state[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBcommand.onecmd("show State {}".format(state))
            full_state = f.getvalue()
        self.assertIn(state, full_state)

if __name__ == "__main__"
    unittest.main()