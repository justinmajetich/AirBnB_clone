#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.engine.db_storage import DBStorage
from os import getenv
import MySQLdb
import pep8
import sys

if getenv("HBNB_TYPE_STORAGE") == "db":
    db = MySQLdb.connect(
        host=getenv("HBNB_MYSQL_HOST"),
        passwd=getenv("HBNB_MYSQL_PWD"), user=getenv("HBNB_MYSQL_USER"),
        db=getenv("HBNB_MYSQL_DB"))
    cursor_objects = db.cursor()


class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        def test_base_pep8(self):
            """Test for pep8"""
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(['./models/engine/db_storage.py'])
            self.assertEqual(result.total_errors, 0)

        def test_docstring(self):
            """ Test doc strings """
            self.assertIsNotNone(DBStorage.__doc__)
            self.assertIsNotNone(DBStorage.__init__.__doc__)
            self.assertIsNotNone(DBStorage.all.__doc__)
            self.assertIsNotNone(DBStorage.new.__doc__)
            self.assertIsNotNone(DBStorage.save.__doc__)
            self.assertIsNotNone(DBStorage.delete.__doc__)
            self.assertIsNotNone(DBStorage.reload.__doc__)

        def test_create(self):
            """ Test create a class """
            storage = DBStorage()
            storage.reload()
            initial_count = len(storage.all(State))
            initial_db = cursor_objects.execute(
                """SELECT COUNT(id) FROM states;""")

            self.assertTrue(initial_count == 0)

            new_state = State(name="Antioquia")
            storage.reload()
            new_state.save()
            storage.save()

            final_count = len(storage.all(State))
            final_db = cursor_objects.execute(
                """SELECT COUNT(id) FROM states;""")

            self.assertEqual(final_count, final_db)

            self.assertEqual(initial_count + 1, final_db)
