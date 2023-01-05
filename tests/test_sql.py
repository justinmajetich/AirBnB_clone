#!/usr/bin/python3
""" TEST FOR MySQL """
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
    """SQL database unittest"""
    conn = None
    cur = None

    def connection(self):
        """connect to MySQLdb"""
        storage = DBStorage()
        storage.relaod()
        self.conn = MySQLdb.connect(getenv('HBNB_MYSQL_HOST'),
                                    getenv('HBNB+MYSQL_USER'),
                                    getenv('HBNB_MYSQL_PWD'),
                                    getenv('HBNB_MYSQL_DB'))
        self.cr = self.conn.cursor()

    def diconnection(self):
        """ Disconect form the db"""
        self.cur.close()
        self.conn.close()
        self.conn = None
        self.cur = None

    def test_create_state(self):
        """Test create state entry"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State nam="California"')
        self.cur.execute("SELECT COUNT(*) FROM states")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()

    def test_create_city(self):
        """ Test create city entry"""
        self.connection()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id = f.getvalue()[:-1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id}"
                                        name="SAN_Francisco"''')
        self.cur.execute("SELECT COUNT(*) FROM cities")
        res = self.cur.fetchone()[0]
        self.assertEqual(res, 1)
        self.disconnection()


if __name__ == '__main__':
    unittest.main()
