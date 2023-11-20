#!/usr/bin/python3
"""
define a module testing db
"""

import unittest
import datetime
from uuid import UUID
import json
import os
import MySQLdb


class test_database(unittest.TestCase):
    """Representation of class db"""

    def test_create_db_table_insert(self):
        try:
            db = MySQLdb.connect(host='localhost', user='root', passwd='')
            cur = db.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS testingdb;")
            cur.execute("USE testingdb;")
            cur.execute("CREATE TABLE IF NOT EXISTS users \
                    (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(32));")
            cur.execute("SELECT COUNT(*) FROM users")
            total_rows_b = cur.fetchone()
            cur.execute("INSERT INTO users (name) VALUES ('alx')")
            db.commit()
            cur.execute("SELECT COUNT(*) FROM users")
            total_rows_a = cur.fetchone()
            cur.execute("SELECT name FROM users WHERE id = 1")
            result = cur.fetchone()
            cur.close()
            db.close()
            self.assertEqual(result[0], 'alx', "check for name inserted")
            self.assertTrue(total_rows_b[0] < total_rows_a[0], "record add")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
