#!/usr/bin/python3
''' Tests for console'''

import sys
import unittest
import os
import models
from unittest.mock import create_autospec
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.state import State
import console

class test_console(unittest.TestCase):
    ''' Testing the console'''

    @classmethod
    def setUpClass(test_cls):
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass
        test_cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(test_cls):
        try:
            os.rename("tmp_file", "file.json")
        except IOError:
            pass
        del test_cls.HBNB
        if type(models.storage) is DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        """ setup """
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all BaseMOdel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Amenity")
            new_amenity = test.getvalue().strip()

@unittest.skipIf(type(models.storage) is DBStorage, "Testing DBstorage")
class TestHBNBCommand(unittest.TestCase):
    """Unittesting the HBNB command interpreter"""
    @classmethod
    def setUpClass(test_cls):
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass
        test_cls.HBNB = HBNBCommand()

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'test DB mode')
class TestHBNBComDB(unittest.TestCase):
    """testing DB Storage"""

    @classmethod
    def setUpClass(cls):
        cls.cli = HBNBCommand()

    def setUp(self):
        pass

    def test_storage(self):
        self.assertIsInstance(console.storage, DBStorage)
        obj = State()
        obj.name = "California"
        obj.save()
        self.assertEqual(type(obj), State)

    def test_crt_dbs(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd("create State name='California'")
            ca = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.cli.onecmd("all State")
            self.assertIn(ca, f.getvalue())

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create BaseMOdel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Amenity")
            new_amenity = test.getvalue().strip()

if __name__ == '__main__':
    unittest.main()