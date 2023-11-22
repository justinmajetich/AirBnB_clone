#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
import os


class test_dbStorage(unittest.TestCase):
    """Class to test the database storage method """

    def setUp(self):
        """ """
        os.environ["HBNB_ENV"] = "test"
        os.environ["HBNB_MYSQL_USER"] = "hbnb_test"
        os.environ["HBNB_MYSQL_PWD"] = "hbnb_test_pwd"
        os.environ["HBNB_MYSQL_HOST"] = "localhost"
        os.environ["HBNB_MYSQL_DB"] = "hbnb_test_db"
        os.environ["HBNB_TYPE_STORAGE"] = "db"

    def tearDown(self):
        """ """
        pass

    def test_all(self):
        """ """
        new = State()
        new.name = "California"
        new.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
