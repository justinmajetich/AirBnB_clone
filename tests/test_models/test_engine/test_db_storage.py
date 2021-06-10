#!/usr/bin/python3

"""
Module for testing db_storage
"""

from console import HBNBCommand
from models.state import State
from models.city import City
from models import storage
from unittest.mock import patch
from io import StringIO
from os import environ
import unittest
import MySQLdb

evars = {
    'env': environ.get('HBNB_ENV'),
    'user': environ.get('HBNB_MYSQL_USER'),
    'pass': environ.get('HBNB_MYSQL_PWD'),
    'host': environ.get('HBNB_MYSQL_HOST'),
    'dbName': environ.get('HBNB_MYSQL_DB'),
    'storageType': environ.get('HBNB_TYPE_STORAGE')
}


@unittest.skipIf('storageType' != 'db', "DB_STORAGE")
class test_db_storage(unittest.TestCase):
    """Unit test class for db_storage"""

    def test_create_state(self):
        """ Tests state creation """
        with patch('sys.stdout', new=StringIO()) as boy:
            HBNBCommand().onecmd("create State name='ChaveraLand'")
            state = boy.getvalue()
            state = state[:-1]
        with patch('sys.stdout', new=StringIO()) as guy:
            HBNBCommand().onecmd("show State ()".format(state))
            state_all = guy.getvalue()
        self.assertIn(state, state_all)

        def test_storing_city(self):
            """ Tests if creating a city stores it in cities """
            with patch('sys.stdout', new=StringIO()) as boy:
                HBNBCommand().onecmd("create State name='ChaveraLand'")
                state = boy.getvalue()
                state = state[:-1]
            with patch('sys.stdout', new=StringIO()) as guy:
                HBNBCommand().onecmd("create City name='lilgoober' state_id={}"
                                     .format(state))
                city = guy.getvalue()
                city = city[:-1]
            with patch('sys.stdout', new=StringIO()) as man:
                HBNBCommand().onecmd("show City {}".format(city))
                cities = man.getvalue()
            self.assertIn(city, cities)

if __name__ == '__main__':
    unittest.main()
