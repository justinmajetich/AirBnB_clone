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
        self.cur = self.conn.cursor()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            self.cur.close()
            self.conn.close()
        except Exception:
            pass
    
    def test_all_given_cls(self):
        """"""
        new = State(name="Carlifonia")
        new.save()
        objects = storage.all(State)
        self.assertTrue(isinstance(objects, dict))
        self.assertIn(f'State.{new.id}', objects)
        self.assertIn(new, objects.values())
        storage.delete(new)
