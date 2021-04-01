#!/usr/bin/python3
""" Module for testing database storage"""

import unittest
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models import storage
import datetime
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class test_dbStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        os.environ['HBNB_MYSQL_USER'] = "hbnb_test"
        os.environ['HBNB_MYSQL_PWD'] = "hbnb_test_pwd"
        os.environ['HBNB_MYSQL_HOST'] = "localhost"
        os.environ['HBNB_MYSQL_DB'] = "hbnb_test_db"
        os.environ['HBNB_TYPE_STORAGE'] = "db"

        self.storage = DBStorage()
        self.storage.reload()

        storage = self.storage

    def tearDown(self):
        os.environ['HBNB_TYPE_STORAGE'] = "apple"

    def test_storage(self):
        """ docstring"""
        self.assertIsInstance(self.storage, DBStorage)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != "db", "FileStorage")
    def test_city(self):
        """ Testing cities in the database """
        bark = State(**{'name': 'Michigan'})
        bark.save()
        meow = City(**{'state_id': bark.id})
        meow.save()
        storage.save()
        self.assertIn("City." + meow.id, storage.all())

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
