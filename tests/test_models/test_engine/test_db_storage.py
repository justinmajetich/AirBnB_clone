#!/usr/bin/python3
''' module for file_storage tests '''
import unittest
import MySQLdb
from models.user import User
from models import storage
from datetime import datetime
import os
from test_models import storage_type


@unittest.skipIf(storage_type != "db", "File storage is not supported")
class TestDBStorage(unittest.TestCase):
    """Test database storage engine"""

    def test_new_and_save(self):
        """Test new and save methods"""
        connection = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                                     host=os.getenv('HBNB_MYSQL_HOST'),
                                     passwd=os.getenv('HBNB_MYSQL_PWD'),
                                     port=3306,
                                     db=os.getenv('HBNB_MYSQL_DB'))
        new_user = User(**{'first_name': 'Chee',
                           'last_name': 'Vee',
                           'email': 'donotfail@gmail.com',
                           'password': 12345})
        cur = connection.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        old_count = cur.fetchall()
        cur.close()
        connection.close()
        new_user.save()
        connection = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                                     host=os.getenv('HBNB_MYSQL_HOST'),
                                     passwd=os.getenv('HBNB_MYSQL_PWD'),
                                     port=3306,
                                     db=os.getenv('HBNB_MYSQL_DB'))
        cur = connection.cursor()
        cur.execute('SELECT COUNT(*) FROM users')
        new_count = cur.fetchall()
        self.assertEqual(new_count[0][0], old_count[0][0] + 1)

        cur.close()
        connection.close()

    def test_new(self):
        """Test that new objects are created and added successfully"""
        new = User(
            email='donotfail@good.com',
            password='word',
            first_name='Nothing',
            last_name='Wrong'
        )
        self.assertFalse(new in storage.all().values())
        new.save()
        self.assertTrue(new in storage.all().values())
        connection = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('donotfail@good.com', result)
        self.assertIn('word', result)
        self.assertIn('Nothing', result)
        self.assertIn('Wrong', result)

        cursor.close()
        connection.close()

    def test_delete(self):
        """Test delete removes an object"""
        new = User(
            email='donotfail@gmail.com',
            password='oneone',
            first_name='Our',
            last_name='World'
        )
        obj_key = 'User.{}'.format(new.id)
        connection = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        new.save()
        self.assertTrue(new in storage.all().values())
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn('donotfail@gmail.com', result)
        self.assertIn('oneone', result)
        self.assertIn('Our', result)
        self.assertIn('World', result)
        self.assertIn(obj_key, storage.all(User).keys())
        new.delete()
        self.assertNotIn(obj_key, storage.all(User).keys())
        cursor.close()
        connection.close()

    def test_reload(self):
        """Test the database is reloaded correctly"""
        connection = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = connection.cursor()
        cursor.execute('DELETE from users where id="123456-do-not-fail"')
        cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s);',
            [
                '123456-do-not-fail',
                str(datetime.now()),
                str(datetime.now()),
                'donotfail@good.com',
                'one',
                'Nothing',
                'Wrong',
            ]
        )
        connection.commit()
        storage.reload()
        self.assertIn('User.123456-do-not-fail', storage.all(User))

        cursor.close()
        connection.close()

    def test_save(self):
        """Test object is saved to the database"""
        new = User(
            email='donotfail@gmail.com',
            password='okeke',
            first_name='Ovy',
            last_name='Evbodi'
        )
        connection = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor.fetchone()
        cursor.execute('SELECT COUNT(*) FROM users')
        old_cnt = cursor.fetchone()[0]
        self.assertTrue(result is None)
        self.assertFalse(new in storage.all().values())
        new.save()
        connection1 = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )
        cursor1 = connection1.cursor()
        cursor1.execute('SELECT * FROM users WHERE id="{}"'.format(new.id))
        result = cursor1.fetchone()
        cursor1.execute('SELECT COUNT(*) FROM users')
        new_cnt = cursor1.fetchone()[0]
        self.assertFalse(result is None)
        self.assertEqual(old_cnt + 1, new_cnt)
        self.assertTrue(new in storage.all().values())
        cursor1.close()
        connection1.close()

        cursor.close()
        connection.close()
