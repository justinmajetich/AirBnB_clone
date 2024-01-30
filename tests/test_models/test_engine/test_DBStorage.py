#!/usr/bin/python3
"""
Module to test the Storage management system of the the Database DBStorage.py
"""
import unittest
from unittest.mock import patch
import os
from models.base_model import BaseModel, storage, Base
from models.palce import Place
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db" or
                 os.getenv("HBNB_ENV") != "test",
                 "Not test environment for DataBase")
class TestDBS(unittest.TestCase):
    """
    A TestCase subclass that test the functionalty of DBStorage model using
    Unittest module
    """
    @classmethod
    def setUpClass(cls):
        """ Setup the environment and requirements for the class
        """
        import MySQLdb

        TestDBS.tables = ["users", "plases", "states", "cities",
                  "amenities", "reviews"]
        # create a connection to the database for testing and setup purpose
        TestDBS.db = MySQLdb.connect(
            host=os.getenv("HBNB_MYSQL_HOST"),
            port=3306,
            user=os.getenv("HBNB_MYSQL_USER"),
            passwd=os.getenv("HBNB_MYSQL_PWD"),
            database=os.getenv("HBNB_MYSQL_DB")
            )
        TestDBS.cur = db.cursor()  # create a cursor to execute the statments

    def setUp(self):
        """ Setup the test environment
        """
        self.engine = storage._DBStorage__engine
        self.session = storage._DBStorage__session


    def tearDown(self):
        """ Clean after each test case
        """
        self.session.deleted  # mark all the bindding objects as deleted
        self.session.commit()  # commit the session into the database

        query = "DROP TABLE IF EXISTS %s"

        for table in TestDBS.tables:
            TestDBS.cur.execute(query, table)

    def test_all(self):
        """ Test DBStorage.all(self) with empty database
        """
        objects = storage.all()

        self.assertTrue(type(objects) is dict)
        self.assertTrue(len(objects) == 0)
