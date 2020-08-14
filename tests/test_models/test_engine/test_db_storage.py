#!/usr/bin/python3
""" Module for testing file storage"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8
from models.place import Place
import MySQLdb
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        """ Verify the documentation """
        self.assertTrue(len(DBStorage.__doc__) > 1)
        self.assertTrue(len(DBStorage.all.__doc__) > 1)
        self.assertTrue(len(DBStorage.new.__doc__) > 1)
        self.assertTrue(len(DBStorage.save.__doc__) > 1)
        self.assertTrue(len(DBStorage.reload.__doc__) > 1)
        self.assertTrue(len(DBStorage.delete.__doc__) > 1)
        self.assertTrue(len(DBStorage.close.__doc__) > 1)

    @classmethod
    def setUpClass(cls):
        cls.storage = DBStorage()
        cls.storage.reload()
        cls.state = State(name="California")
        cls.state.save()
        # creation of a City
        cls.city = City(state_id=cls.state.id, name="San Francisco")
        cls.city.save()
        # creation of a User
        cls.user = User(email="john@snow.com", password="johnpwd")
        cls.user.save()
        # creation of a place
        cls.place = Place(user_id=cls.user.id,
                          city_id=cls.city.id, name="House 1")
        cls.place.save()

        cls.place_2 = Place(user_id=cls.user.id,
                            city_id=cls.city.id, name="House 2")
        cls.place_2.save()

        cls.amenity_1 = Amenity(name="Wifi")
        cls.amenity_1.save()

        cls.amenity_2 = Amenity(name="Cable")
        cls.amenity_2.save()

        cls.amenity_3 = Amenity(name="Oven")
        cls.amenity_3.save()
        # link place_1 with 2 amenities
        cls.place.amenities.append(cls.amenity_1)
        cls.place.amenities.append(cls.amenity_2)

        # link place_2 with 3 amenities
        cls.place_2.amenities.append(cls.amenity_1)
        cls.place_2.amenities.append(cls.amenity_2)
        cls.place_2.amenities.append(cls.amenity_3)

        cls.storage.save()

    def setUp(self):
        """ check for the right type of datastorage otherwise skiptheTest """
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            self.skipTest("because is not using db_storage")
        self.connection()

    def tearDown(self):
        """ Close conections """
        self.db.close()
        self.storage.close()

    def connection(self):
        """ set the connection for the database MYSQL """
        my_user = os.getenv("HBNB_MYSQL_USER")
        my_passw = os.getenv("HBNB_MYSQL_PWD")
        my_host = os.getenv("HBNB_MYSQL_HOST")
        my_db = os.getenv("HBNB_MYSQL_DB")

        self.db = MySQLdb.connect(host=my_host, db=my_db, user=my_user,
                                  passwd=my_passw, port=3306)
        # creation of 2 Places
        self.cursor = self.db.cursor()

    def test_Place_id(self):
        """ Test when creating Places """
        self.cursor.execute(
            """SELECT id FROM places""")
        query = self.cursor.fetchall()
        lista = []
        for id in query:
            lista.append(id[0])
        self.assertIn(self.place.id, lista)

        self.cursor.close()

    def test_Place_attribute(self):
        """test Place adds an attribute when instanciating it"""

        self.cursor.execute(
            """SELECT name FROM places""")
        query = self.cursor.fetchall()
        lista = []
        for name in query:
            lista.append(name[0])
        self.assertIn(self.place.name, lista)
        self.cursor.close()

    def test_leng_queary(self):
        """Check the lenght of the query """

        self.cursor.execute(
            """SELECT id FROM places""")
        query = self.cursor.fetchall()
        self.assertEqual(2, len(query))
        self.cursor.close()

    def test_type(self):
        """test the type of the class """
        self.assertTrue(type(self.place), Place)

    def test_amenities(self):
        """ Test for the the amenitis of id of the"""
        list_amenities = self.place_2.amenities
        amenity_name = []
        for a in list_amenities:
            amenity_name.append(a.name)
        self.assertIn("Wifi", amenity_name)
        self.assertIn("Oven", amenity_name)
        self.assertIn("Cable", amenity_name)

    def test_attribute(self):
        """ Test for attributes """
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "close"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "new"))
