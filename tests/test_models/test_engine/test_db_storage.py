#!/usr/bin/python3

"""
Module for testing db_storage
"""

from console import HBNBCommand
from models.state import State
from models.city import City
from models import storage
from unittest.mock import patch
from io import StringIO
from os import environ
import unittest
import MySQLdb

evars = {
    'env' = environ.get('HBNB_ENV'),
    'user' = environ.get('HBNB_MYSQL_USER'),
    'pass' = environ.get('HBNB_MYSQL_PWD'),
    'host' = environ.get('HBNB_MYSQL_HOST'),
    'dbName' = environ.get('HBNB_MYSQL_DB')m
    'storageType' = environ.get('HBNB_TYPE_STORAGE')
}


@unittest.skipIf(storageType != 'db', "DB_STORAGE")
class test_db_storage(unittest.TestCase):
    """Unit test class for db_storage"

    def
