#!/usr/bin/python3
""" Module for testing db storage"""
from console import HBNBCommand
import unittest
from models.state import State
from models.city import City
from models import storage
from os import environ
import MySQLdb


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "Testing Filestorage now!")
class test_db_Storage(unittest.TestCase):
    """Test class for dbstorage"""

    def setUp(self):
        """ Set up test environment """
        self.conn = MySQLdb.connect(
            user=environ.get('HBNB_MYSQL_USER'),
            passwd=environ.get('HBNB_MYSQL_PWD'),
            db=environ.get('HBNB_MYSQL_DB'),
            host=environ.get('HBNB_MYSQL_HOST')
            )
        self.cursor = self.db_connection.cursor()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            self.cursor.close()
            self.conn.close()
        except Exception:
            pass
