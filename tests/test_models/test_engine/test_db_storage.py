#!/usr/bin/python3
"""
    Test module for the DB_Storage
"""

from datetime import datetime
import unittest
import MySQLdb
import os
from models.user import User


class TestDBStorage(unittest.TestCase):
    """
        This tests the Database storage engine
    """
    def test_new_and_save(self):
        """
            Test the creation of new users
        """
        db = MySQLdb.connect(user=os.getenv('HBNB_MYSQL_USER'),
                             host=os.getenv('HBNB_MYSQL_HOST'),
                             passwd=os.getenv('HBNB_MYSQL_PWD'),
                             port=3306,
                             db=os.getenv('HBNB_MYSQL_DB'))
        # now = datetime.now().isoformat()
        # updated_at = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        new_user = User(**{'first_name':'jack',
                           'last_name': 'bond',
                           'email':'jack@bond.com',
                           'password':12345,})
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
