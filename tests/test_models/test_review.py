#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8
from models.review import Review
import models
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.engine.db_storage import DBStorage
import MySQLdb


class test_review(unittest.TestCase):
    """ """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        self.assertTrue(len(Review.__init__.__doc__) > 1)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "Review"
            self.value = Review

        def test_place_id(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.place_id), str)

        def test_user_id(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.user_id), str)

        def test_text(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.text), str)


class test_Review_db_storage(unittest.TestCase):
    """ test for checking deb_storage """

    @classmethod
    def setUpClass(cls):
        if os.getenv("HBNB_TYPE_STORAGE") == "db":

            # create storage DB
            cls.storage = DBStorage()
            cls.storage.reload()

            # creation of a State
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

            cls.review = Review(
                place_id=cls.place.id,
                user_id=cls.user.id,
                text="Amazing_place,_huge_kitchen")
            cls.review.save()

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

    def test_review_id(self):
        """ Test when creating Places """
        self.cursor.execute(
            """SELECT id FROM reviews""")
        query = self.cursor.fetchall()
        lista = []
        for id in query:
            lista.append(id[0])
        self.assertIn(self.review.id, lista)

        self.cursor.close()

    def test_review_attribute(self):
        """test Preview attribute"""

        self.assertEqual(self.review.text, "Amazing_place,_huge_kitchen")
        self.cursor.close()

    def test_lenght_query(self):
        """Check the lenght of the query """

        self.cursor.execute(
            """SELECT * FROM reviews""")
        query = self.cursor.fetchall()
        self.assertEqual(1, len(query))
        self.cursor.close()

    def test_type(self):
        """test the type of the class """
        self.assertTrue(type(self.place), Place)

    def test_review_user_id(self):
        """ Test for the the user_id of review class"""
        self.cursor.execute(
            """SELECT user_id FROM reviews""")
        query = self.cursor.fetchall()
        lista = []
        for user_id in query:
            lista.append(user_id[0])
        self.assertIn(self.review.user_id, lista)
        self.cursor.close()
        self.review.user_id


if __name__ == "__main__":
    unittest.main()
