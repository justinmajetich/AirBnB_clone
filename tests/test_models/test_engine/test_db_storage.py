#!/usr/bin/python3
""" Module for testing db storage"""
from console import HBNBCommand
import unittest
from models.state import State
from models.city import City
from models import storage
from os import environ
import MySQLdb
from unittest.mock import patch
from io import StringIO

db_url = {
    'user': environ.get('HBNB_MYSQL_USER'),
    'passwd': environ.get('HBNB_MYSQL_PWD'),
    'db': environ.get('HBNB_MYSQL_DB'),
    'host': environ.get('HBNB_MYSQL_HOST')
}


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db', "Testing FileStorage Engine")
class test_db_Storage(unittest.TestCase):
    """Test class for dbstorage"""

    def setUp(self):
        """ Set up test environment """
        self.conn = MySQLdb.connect(**db_url)
        self.cur = self.conn.cursor()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            self.cur.close()
            self.onn.close()
        except:
            pass

    def test_new(self):
        """ New object is correctly added to db """
        new = State(name="New york")
        new.save()
        self.assertIn(new, storage.all().values())
        new.delete()

    def test_all(self):
        """ __objects is properly returned """
        self.assertIsInstance(storage.all(), dict)
    
    def test_all_given_cls(self):
        """Tests new method if cls is entered"""
        new = State(name="Carlifonia")
        new.save()
        objects = storage.all(State)
        self.assertTrue(isinstance(objects, dict))
        self.assertIn(f'State.{new.id}', objects)
        self.assertIn(new, objects.values())
        new.delete()

    def test_city_storage(self):
        """ Tests creation of city  """
        self.cur.execute('SELECT count(*) FROM cities')
        length = self.cur.fetchone()[0]
        self.cur.close()
        self.conn.close()
        create_state = 'create State name="California" id="1c8508c9"'
        create_city = 'create City name="San_Francisco" state_id="1c8508c9"'
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd(create_state)
            HBNBCommand().onecmd(create_city)
        self.conn = MySQLdb.connect(**db_url)
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT count(*) FROM cities')
        length2 = self.cur.fetchone()[0]
        self.assertEqual(length2, length + 1)
        self.cur.execute(
            'SELECT name FROM cities WHERE name = "San Francisco";'
            )
        name = self.cur.fetchone()
        self.assertIn("San Francisco", name)

    def test_state_storage(self):
        """Tests storage of state"""
        self.cur.execute('SELECT count(*) FROM states')
        length = self.cur.fetchone()[0]
        self.cur.close()
        self.conn.close()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Carlifonia"')
        self.conn = MySQLdb.connect(**db_url)
        self.cur = self.conn.cursor()
        self.cur.execute('SELECT count(*) FROM states')
        length2 = self.cur.fetchone()[0]
        self.assertEqual(length2, length + 1)
        
    def test_delete(self):
        """Test if an object is deleted from DB"""
        new = State(name="South America")
        new.save()
        name = new.name
        sql_query = (
            'SELECT * FROM states'
            ' WHERE name = %s ORDER BY id ASC'
            )
        self.cur.execute(sql_query, (name,))
        state_name = self.cur.fetchone()[0]
        new.delete()
        self.cur.close()
        self.conn.close()
        self.conn = MySQLdb.connect(**db_url)
        self.cur = self.conn.cursor()
        
        # search after deletion
        self.cur.execute(sql_query, (name,))
        del_name = self.cur.fetchone()
        self.assertEqual(name, state_name)
        self.assertIsNone(del_name)
