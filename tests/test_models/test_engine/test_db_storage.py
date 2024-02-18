#!/usr/bin/python3
""" Module for testing database storage"""


import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.user import User
import os
from os import getenv


class test_databaseStorage(unittest.TestCase):
    def test_all(self):
        """ __objects is properly returned """
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)
