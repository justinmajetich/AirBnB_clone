#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from os import getenv
import models


type_storage = getenv('HBNB_TYPE_STORAGE')


class test_dbstorage(unittest.TestCase):
    """this will test nothing"""

    @unittest.skipIf(type_storage != 'db', reason="m")
    def test001(self):
        """Test 001 db storage"""
        self.skipTest("TTest001 Skipped")

    @unittest.skipIf(type_storage != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(type_storage != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(type_storage != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(type_storage != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
