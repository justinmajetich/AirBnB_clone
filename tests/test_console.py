#!/usr/bin/python3
"""tests for the console"""

import unittest
import os
import sys
import sqlalchemy
from io import StringIO
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from console import HBNBCommand
from unittest.mock import patch
import MySQLdb
from models import storage
from models.state import State


class test_console(unittest.TestCase):
    """"class to test the console"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_create(self):
        if os.path.exists(FileStorage()._FileStorage__file_path):
            os.remove(FileStorage()._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as molehill:
            HBNBCommand().onecmd("create State name=\"shalala\"") 
            state_id = molehill.getvalue()[:1]
        with open(FileStorage()._FileStorage__file_path, 'r') as mountain:
            # check if State exists in FileStorage after collecting state id    
            self.assertIn(state_id, mountain.read())
    #     with patch('set.stdout', new=StringIO()) as target:
    #         HBNBCommand().onecmd("create City name=\"sendit\"")
    #         city_id = target.getvalue()
    #     with open

    # @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DBStorage")
    # def test_create_db(self):
    #     # test all
    #     # create cursor
    #     self.assertTrue(type("this is a string"), str)

if __name__ == '__main__':
    unittest.main()
