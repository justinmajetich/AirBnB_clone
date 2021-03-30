#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from os import getenv


class test_dbstorage(unittest.TestCase):
    """this will test nothing"""

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', reason="m")
    def test001(self):
        """Test 001 db storage"""
        self.skipTest("TTest001 Skipped")
