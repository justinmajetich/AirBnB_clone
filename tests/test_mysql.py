#!/usr/bin/python3
""""Module for testing MySQLdb"""
import unittest
import mysql.connector
import os

HBNB_MYSQL_USER = os.environ('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = os.environ('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = os.environ('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = os.environ('HBNB_MYSQL_DB')


class TestMySQL(unittest.TestCase):
    """The MySQLdb test class"""

    def setUp(self):
        """Set up for the tests"""
        self.connection = mysql.connector.connect(
            user=HBNB_MYSQL_USER,
            password=HBNB_MYSQL_PWD,
            host=HBNB_MYSQL_HOST,
            database=HBNB_MYSQL_DB
        )

    def tearDown(self):
        """Tear down for the tests"""
        self.connection.close()

    def test_connection(self):
        """Test the connection"""
        self.assertTrue(self.connection.is_connected())

    def test_cursor(self):
        """Test the cursor"""
        cursor = self.connection.cursor()
        self.assertTrue(cursor)

    def test_select(self):
        """Test the select"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM states")
        result = cursor.fetchall()
        self.assertTrue(result)

    def test_insert(self):
        """Test the insert"""
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.connection.commit()
        cursor.execute("SELECT * FROM states WHERE name='California'")
        result = cursor.fetchall()
        self.assertTrue(result)

    def test_delete(self):
        """Test the delete"""
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.connection.commit()
        cursor.execute("DELETE FROM states WHERE name='California'")
        self.connection.commit()
        cursor.execute("SELECT * FROM states WHERE name='California'")
        result = cursor.fetchall()
        self.assertFalse(result)

    def test_update(self):
        """Test the update"""
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.connection.commit()
        cursor.execute("""UPDATE states SET name='New York'
                       WHERE name='California'""")
        self.connection.commit()
        cursor.execute("SELECT * FROM states WHERE name='New York'")
        result = cursor.fetchall()
        self.assertTrue(result)

    def test_select_all(self):
        """Test the select all"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM states")
        result = cursor.fetchall()
        self.assertTrue(result)

    def test_add_record(self):
        """Get the number of records before adding"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM states")
        result = cursor.fetchone()[0]
        # Add a record
        cursor.execute("""INSERT INTO states (name)
                       VALUES ('California') ('Arizona')""")
        self.connection.commit()
        # Get the number of records after adding
        cursor.execute("SELECT COUNT(*) FROM states")
        result2 = cursor.fetchone()[0]
        # Compare the two
        self.assertEqual(result2, result + 1)
