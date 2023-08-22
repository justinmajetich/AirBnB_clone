#!/usr/bin/python3
"""Unit test for the db storage class"""
import unittest
import os
import pycodestyle
from models.engine import db_storage
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """Tests the DBStorage class"""

    def setUp(self):
        """Set up the test environment"""
        db_host = "hbnb_test_host"
        db_name = "hbnb_test_db"
        db_user = "hbnb_test"
        db_passwd = "hbnb_test_pwd"

    def test_pycodestyle(self):
        """Check db_storage and test_db_storage conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([
            "models/engine/db_storage.py",
            "tests/test_models/test_engine/test_db_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_permissions(self):
        """Check if the file has the necessary permissions to be executed"""
        file = "models/engine/db_storage.py"
        self.assertTrue(os.access(file, os.F_OK))
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(db_storage.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(DBStorage.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(DBStorage):
            self.assertTrue(len(method.__doc__) > 0)
