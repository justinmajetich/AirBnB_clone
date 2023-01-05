#!/usr/bin/python3
""" Test module for the Database storage"""

import unittest
import pycodestyle
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """ Clas TestDBStorage for testing the database storage"""
    
    def testPycodeStyle(self):
        """Test for pycodestyle compliancy in DBStorage"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring_DBStorage(self):
        """Test for docstring in DBStorage"""
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)


if __name__ == "__main__":
    unittest.main()
