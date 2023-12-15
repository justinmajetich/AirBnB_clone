#!/usr/bin/python3
""" Module for testing mysql storage"""
import unittest
from models.base_model import BaseModel
import MySQLdb
import os


class test_dbStorage(unittest.TestCase):
    """ Class to test the mysql storage method """

    def setUp(self):
        """ Set up test environment """
        host = os.environ.get("HBNB_MYSQL_HOST")
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        test_db = os.environ.get("HBNB_MYSQL_DB")

        self.db = MySQLdb.connect(host=host, user=user, passwd=password, db=test_db)
        self.cursor = self.db.cursor()

    def tearDown(self):
        """ Close the database connection after the test """
        self.db.close()

