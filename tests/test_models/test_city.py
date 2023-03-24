#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import TestBaseModel
from models.city import City
import MySQLdb
import subprocess
from os import getenv


class test_City(TestBaseModel):
    """ """

    if getenv("HBNB_TYPE_STORAGE") != "db":
        def __init__(self, *args, **kwargs):
            """ """
            super().__init__(*args, **kwargs)
            self.name = "City"
            self.value = City

        def test_state_id(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.state_id), str)

        def test_name(self):
            """ """
            new = self.value()
            self.assertEqual(type(new.name), str)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        def setUp(self):
            """Set up test environment"""
            self.db = MySQLdb.connect(
                host=getenv("HBNB_MYSQL_HOST"),
                user=getenv("HBNB_MYSQL_USER"),
                password=getenv("HBNB_MYSQL_PWD"),
                database=getenv("HBNB_MYSQL_DB")
            )

        def tearDown(self):
            """Tear down test environment"""
            self.db.close()

        def test_create_state_command(self):
            """Test if the create State command adds a new record to the states table"""
            # Get the number of current records in the table states
            cursor = self.db.cursor()
            cursor.execute("SELECT COUNT(*) FROM states")
            count_before = cursor.fetchone()[0]

            # Execute the console command
            command = f'HBNB_MYSQL_USER={getenv("HBNB_MYSQL_USER")} ' \
                    f'HBNB_MYSQL_PWD={getenv("HBNB_MYSQL_PWD")} ' \
                    f'HBNB_MYSQL_HOST={getenv("HBNB_MYSQL_HOST")} ' \
                    f'HBNB_MYSQL_DB={getenv("HBNB_MYSQL_DB")} ' \
                    f'HBNB_TYPE_STORAGE=db ' \
                    f'echo "create State name=\\"California\\"" | ./console.py'
            subprocess.run(command, shell=True)

            # Get the number of current records in the table states again
            cursor.execute("SELECT COUNT(*) FROM states")
            count_after = cursor.fetchone()[0]

            # Assert that the difference is +1
            self.assertEqual(count_after, count_before + 1)
