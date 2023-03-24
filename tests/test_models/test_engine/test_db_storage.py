#!/usr/bin/python3
""" Module for testing db_storage"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import os


class test_db_storage(unittest.TestCase):
    """ Class to test the db_storage method """
    def setUp(self):
        """Set up the test environment"""
        os.environ['HBNB_MYSQL_USER'] = 'test_user'
        os.environ['HBNB_MYSQL_PWD'] = 'test_pwd'
        os.environ['HBNB_MYSQL_HOST'] = 'localhost'
        os.environ['HBNB_MYSQL_DB'] = 'test_db'
        self.storage = DBStorage()

    def test_all_without_cls(self):
        """Test the all method without a class"""
        with patch.object(self.storage, '_DBStorage__session') as mock_session:
            mock_session.return_value.query.return_value.all.return_value = []
            self.assertEqual(self.storage.all(), {})
    
    def test_all_with_cls(self):
        """Test the all method with a class"""
        with patch.object(self.storage, '_DBStorage__session') as mock_session:
            mock_session.return_value.query.return_value.all.return_value = []
            self.assertEqual(self.storage.all(User), {})


if __name__ == '__main__':
    unittest.main()
