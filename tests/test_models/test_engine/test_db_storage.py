#!/usr/bin/python3
""" Module for testing file storage"""
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from models.__init__ import storage
from unittest.mock import patch
from io import StringIO
import console
import unittest
import pep8
import sys
from os import getenv
import MySQLdb
import models
import unittest


class TestDBStorage(unittest.TestCase):
    """ Class to functionaly of Console. """
    def setUp(self):
        """Setting Up """
        self.console_o = DBStorage()

    def tearDown(self):
        """Cleaning up after each test. """
        pass

if __name__ == "__main__":
    unittest.main()
