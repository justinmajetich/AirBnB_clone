#!/usr/bin/python3
"""module with unittests for db_storage"""
from models import storage
from datetime import datetime
from models.user import User
import unittest
import MySQLdb
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 'db_storage test not supported')
class TestDBStorage(unittest.TestCase):
    """Class that tests DBStorage engine"""
    def test_new_and_save(self):
        """Function that tests new and save methods"""
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        new_user = User(**{'first_name': 'Hannibal',
                           'last_name': 'Mejbri',
                           'email': 'hm@utd.com',
                           'password': 13})
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchall()
        cur.close()
        db.close()
        new_user.save()
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        cur = db.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)
        cur.close()
        db.close()

    def test_new(self):
        """ Function that tests new objects """
        new = User(
            email='hm@utd.com',
            password='13',
            first_name='Hannibal',
            last_name='Mejbri'
        )
        self.assertFalse(new in storage.all().values())
        new.save()
        self.assertTrue(new in storage.all().values())
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('hm@utd.com', result)
        self.assertIn('13', result)
        self.assertIn('Hannibal', result)
        self.assertIn('Mejbri', result)
        cursor.close()
        dbc.close()

    def test_delete(self):
        """Test for delete method"""
        new = User(
            email='hm@utd.com',
            password='13',
            first_name='Hannibal',
            last_name='Mejbri'
        )
        obj_key = 'User.{}'.format(new.id)
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        new.save()
        self.assertTrue(new in storage.all().values())
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('hm@utd.com', result)
        self.assertIn('13', result)
        self.assertIn('Hannibal', result)
        self.assertIn('Mejbri', result)
        self.assertIn(obj_key, storage.all(User).keys())
        new.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())
        cursor.close()
        dbc.close()

    def test_reload(self):
        """Test for reload method"""
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
            [
                'some-guy',
                str(datetime.now()),
                str(datetime.now()),
                'hm@utd.com',
                '13',
                'Hannibal',
                'Mejbri',
            ]
        )
        self.assertNotIn('User.some-guy', storage.all())
        dbc.commit()
        storage.reload()
        self.assertIn('User.some-guy', storage.all())
        cursor.close()
        dbc.close()

    def test_save(self):
        """Test for save method"""
        new = User(
            email='hm@utd.com',
            password='13',
            first_name='Hannibal',
            last_name='Mejbri'
        )
        dbc = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = dbc.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        cursor.execute('SELECT COUNT(*) FROM users;')
        old_cnt = cursor.fetchone()[0]
        self.assertTrue(result is None)
        self.assertFalse(new in storage.all().values())
        new.save()
        dbc1 = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor1 = dbc1.cursor()
        cursor1.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor1.fetchone()
        cursor1.execute('SELECT COUNT(*) FROM users;')
        new_cnt = cursor1.fetchone()[0]
        self.assertFalse(result is None)
        self.assertEqual(old_cnt + 1, new_cnt)
        self.assertTrue(new in storage.all().values())
        cursor1.close()
        dbc1.close()
        cursor.close()
        dbc.close()