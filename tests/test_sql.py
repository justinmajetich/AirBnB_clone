#!/usr/bin/pyhthon3
"""Module for the test of MySQL"""
import MySQLdb
import unittest
from unittest.mock import patch
import io
from console import HBNBCommand
from os import getenv
from models.engine.db_storage import DBStorage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "Not DBStorage")
class TestMySQL(unittest.TestCase):
    """Test for the SQL database"""
    conn = None
    cur = None

    def connection(self):
        """Connect to MySQLdb"""
        storage = DBStorage()
        storage.reload()
        self.conn = MySQLdb.connect(getenv('HBNB_MYSQL_HOST'),
                                    getenv('HBNB_MYSQL_USER'),
                                    getenv('HBNB_MYSQL_PWD'),
                                    getenv('HBNB_MYSQL_DB'))
        self.cur = self.conn.cursor()

    def disconnection(self):
        """Disconnect from MySQLdb"""
        self.cur.close()
        self.conn.close()
        self.conn = None
        self.cur = None

    def test_create_state(self):
        """Test create of a State"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        self.cur.execute("SELECT COUNT(*) FROM states")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_city(self):
        """Test create of a City"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id}"
                                 name="San_Francisco"''')
        self.cur.execute("SELECT COUNT(*) FROM cities")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()


if __name__ == '__main__':
    unittest.main()
