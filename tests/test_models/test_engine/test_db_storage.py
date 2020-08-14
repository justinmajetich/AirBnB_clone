#!/usr/bin/python
"""Unittests for DBStorage class of AirBnb_Clone_v2"""
import unittest
import pep8
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import MySQLdb


class TestDBStorage(unittest.TestCase):
    """Test for DBSTorage file."""

    def setUp(self):
        """Set up method"""
        self.db_connection = MySQLdb.connect(host="localhost", port=3306,
                                             user="hbnb_dev", charset="utf8",
                                             passwd="hbnb_dev_pwd",
                                             db='hbnb_dev_db')

        self.cursor = self.db_connection.cursor()

    def tearDown(self):
        """Tear down method (db.close)."""
        self.cursor.close()
        self.db_connection.close()

    def test_pep8_DBStorage(self):
        """Test for pep8 style."""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "pep8 error")
