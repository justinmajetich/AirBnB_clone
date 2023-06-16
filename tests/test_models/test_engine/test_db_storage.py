#!/usr/bin/python3
"""
This script confirms that the DBStorage class performs as expected
It servers as the database storage
"""

import MySQLdb
import unittest
from os import getenv       # to fetch environmental variables

# Assist in identifying error in SQL commands
from tests.test_models.test_engine.helper_funcs import run

import os

TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")
if TYPE_STORAGE == "db":
    exit(0)


class test_db_storage(unittest.TestCase):
    """
    This class test the DBStorage class for database storage
    """

    print("\nIn test_db_storage\n")     # test

    def setUp(self):
        """
        Set up the environment for each test
        """
        print("\nIn setUp\n")       # test
        self.MY_ENV = getenv("HBNB_ENV")
        self.MY_HOST = getenv("HBNB_MYSQL_HOST")
        self.MY_PORT = 3306
        self.MY_USER = getenv("HBNB_MYSQL_USER")
        self.MY_PWD = getenv("HBNB_MYSQL_PWD")
        self.MY_DB = getenv("HBNB_MYSQL_DB")
        self.TYPE_STORAGE = getenv("HBNB_TYPE_STORAGE")

        # Skip all test if the type of storage being used is not "database"
        if self.TYPE_STORAGE != "db":
            exit(0)

        # Else set up a database connection
        self.db = MySQLdb.connect(
                host=self.MY_HOST,
                port=self.MY_PORT,
                user=self.MY_USER,
                passwd=self.MY_PWD,
                database=self.MY_DB)

        # Creae a cursor instance
        self.cur = self.db.cursor()

        # Clear all enteries in the tables
        run(self.cur.execute, """USE %s";
        SHOW TABLES;""", (str(self.MY_DB),))

        # Fetch all results
        rows = run(self.cur.fetchall())

        self.TABLES = list()
        if rows is not None:
            for row in rows:
                print("setup: row: {}".format(row))     # test
                self.TABLES.append(row)     # get tables
        else:
            print("NO TABLE FOUND IN DATABASE: {}".format(self.MY_DB))
            return

        # Trucate all the tables to ensure a fresh start
        for TABLE in self.TABLES:
            run(self.cur.execute, """TRUNCATE TABLE IF EXISTS %s;""",
                (str(TABLE),))

    def tearDown(self):
        """
        Do necessary clean up after each test
        """
        print("\nIn tearDown\n")        # test
        self.cur.close()    # Close cursor's connection
        self.db.close()     # Close database's connection
