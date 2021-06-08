#!/usr/bin/python3

"""
Unittesting for console in interactive and non-interacitve
"""

import unittest
import os
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import models
from models.state import State
from models.city import City
import MySQLdb
from models.engine.db_storage import user, passwd, host, database
from models.engine.file_storage import FileStorage
fs = models.storage


class test_console(unittest.TestCase):
    """Console unit tests"""

    def test_create_state_fs(self):
        if type(fs) != FileStorage:
            with self.assertRaises(Exception):
                open(fs.__FileStorage__file_path, 'r')
        else:
            if os.path.exists(fs._FileStorage__file_path):
                os.remove(fs.FileStorage__file_path)
            with patch('sys.stdout', new=StringIO()) as boy:
                HBNBCommand().onecmd("create State name=\"Hawaii\"")
                state_id = boy.getvalue()[:-1]
            with open(fs._FileStorage__file_path, 'r') as guy:
                self.assertIn(state_id, guy.read())



    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "Using DBStorage")
    def test_create_state_db(self):
        db = MySQLdb.connect(host, user, passwd, database)
        cursor = db.cursor()
        s = State(name="California")
        s.save()
        c = City(state_id=s.id, name="San Francisco")
        c.save()
        cursor.execute("SELECT cities.id FROM cities INNER JOIN states ON \
                       cities.state_id = states.id WHERE BINARY states.name \
                       = 'California'")
        end = cursor.fetchall()
        self.assertEqual(end[0][0], c.id)
