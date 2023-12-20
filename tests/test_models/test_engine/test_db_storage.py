#!/usr/bin/python3
""" Module for testing mysql storage"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import MySQLdb
import os


class test_dbStorage(unittest.TestCase):
    """ Class to test the mysql storage method """

    def setUp(self):
        """ Set up test environment """
        host = os.environ.get("HBNB_MYSQL_HOST")
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        test_db = os.environ.get("HBNB_MYSQL_DB")

        self.db = MySQLdb.connect(
            host=host, user=user, passwd=password, db=test_db)
        self.cursor = self.db.cursor()

    def tearDown(self):
        """ Close the database connection after the test """
        self.db.close()

    def test_database_created(self):
        """ Test if the database <hbnb_test_db> was successfuly created
        """
        self.cursor.execute("show databases")
        databases = self.cursor.fetchall()
        test_db = os.environ.get("HBNB_MYSQL_DB")
        self.assertIn((test_db,), databases)

    def test_table_created(self):
        """Test to make sure  table is present from the start"""
        table_count = self.cursor.execute("show tables")
        self.assertNotEqual(table_count, 0)

    def test_exact_number_of_tables(self):
        """Test if the exact number of tables expected(7) are created"""
        table_count = self.cursor.execute("show tables")
        self.assertEqual(table_count, 7)

    # Testing  existence of right tables
    def test_for_existence_of_users_table(self):
        """Test if the users table exist"""
        self.cursor.execute("SHOW TABLES")
        self.assertIn(('users',), self.cursor.fetchall())

    def test_for_existence_of_amenities_table(self):
        """Test if the users table exist"""
        self.cursor.execute("SHOW TABLES")
        self.assertIn(('amenities',), self.cursor.fetchall())

    def test_for_existence_of_cities_table(self):
        """Test if the users table exist"""
        self.cursor.execute("SHOW TABLES")
        self.assertIn(('cities',), self.cursor.fetchall())

    def test_for_existence_of_place_amenity_table(self):
        """Test if the users table exist"""
        self.cursor.execute("SHOW TABLES")
        self.assertIn(('place_amenity',), self.cursor.fetchall())

    def test_for_existence_of_places_table(self):
        """Test if the users table exist"""
        self.cursor.execute("SHOW TABLES")
        self.assertIn(('places',), self.cursor.fetchall())

    def test_for_existence_of_reviews_table(self):
        """Test if the users table exist"""
        self.cursor.execute("SHOW TABLES")
        self.assertIn(('reviews',), self.cursor.fetchall())

    def test_for_existence_of_states_table(self):
        """Test if the users table exist"""
        self.cursor.execute("SHOW TABLES")
        self.assertIn(('states',), self.cursor.fetchall())

    # Testing various funcitonalities of db_storage class
    def test_save(self):
        """Test if save function actually saves in db"""
        pass

    def test_delete(self):
        """Test if delete function actually deletes from db"""
        pass

    def test_reload(self):
        """Test if reload function actually reloads most recent
        data in db"""
        pass

    def test_new(self):
        """Test if new function actually creates new record in db"""
        pass

    def test_all(self):
        """Test if all function actually returns all records of a
        table in db"""
        pass
