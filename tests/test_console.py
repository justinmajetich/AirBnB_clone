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
import models


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

    @unittest.skipIf(type(models.storage) is DBStorage, "Testing DBStorage")
    def test_create(self):
        """Test create command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            bm = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create User")
            us = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create State")
            st = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Place")
            pl = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create City")
            ct = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Review")
            rv = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            am = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertIn(us, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all State")
            self.assertIn(st, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertIn(pl, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all City")
            self.assertIn(ct, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all Review")
            self.assertIn(rv, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("all Amenity")
            self.assertIn(am, f.getvalue())


if __name__ == "__main__":
    unittest.main()
