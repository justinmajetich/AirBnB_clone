#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import os
import sys
from console import HBNBCommand
from models.__init__ import storage
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import pep8


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):

        self.console = HBNBCommand()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_emptyline(self):
        """Test empty line input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue())

    def test_EOF(self):
        """Test that EOF quits."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
