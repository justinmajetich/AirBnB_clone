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
        def test_state_id_db(self):
            """"""
            db = MySQLdb.connect(
                host="localhost", user="hbnb_dev", passwd="hbnb_dev_pwd", db="hbnb_dev_db")
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM states")
            result_before = cursor.fetchone()[0]
            subprocess.call(['echo', 'create State name=\"California\"',
                            '|', 'HBNB_MYSQL_USER=hbnb_dev', 'HBNB_MYSQL_PWD=hbnb_dev_pwd',
                             'HBNB_MYSQL_HOST=localhost', 'HBNB_MYSQL_DB=hbnb_dev_db',
                             'HBNB_TYPE_STORAGE=db', './console.py'])
            cursor.execute("SELECT COUNT(*) FROM states")
            result_after = cursor.fetchone()[0]
            count = result_after - result_before
            self.assertEqual(result_after - result_before, count)
