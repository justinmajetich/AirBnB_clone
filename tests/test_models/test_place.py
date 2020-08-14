#!/usr/bin/python3
""" """
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

print("\n ###################  ##### INICIO TESTS ######## ###### ######\n")


class test_Place_file_storage(unittest.TestCase):
    """ """

    def setUp(self):
        """ check for the right type of datastorage otherwise skiptheTest """
        if os.getenv("HBNB_TYPE_STORAGE") != "FileStorage":
            raise unittest.SkipTest("because is not using Filstorage")
            # self.skipTest("f------oo")

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        self.assertTrue(len(Place.__init__.__doc__) > 1)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


class test_Place_db_storage(unittest.TestCase):
    """ test for checking deb_storage """

    print("\n **************** START test db ****************\n")

    @classmethod
    def setUpClass(cls):
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
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

            cls.amenity_1 = Amenity(name="Wifi")
            cls.amenity_1.save()

            cls.amenity_2 = Amenity(name="Cable")
            cls.amenity_2.save()

            cls.amenity_3 = Amenity(name="Oven")
            cls.amenity_3.save()

            cls.storage = DBStorage()
            cls.storage.reload()
            cls.storage.save()

    def setUp(self):
        """ check for the right type of datastorage otherwise skiptheTest """
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            self.skipTest("because is not using db_storage")
        self.connection()

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

    def test_type(self):
        """test the type of the class """
        self.assertTrue(type(self.place), Place)


if __name__ == "__main__":
    unittest.main()
