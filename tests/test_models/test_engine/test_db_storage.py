#!/usr/bin/python3
import unittest
import pep8
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
import models
import os


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db", "Test_DB")
class TestDBstorage(unittest.TestCase):
    """Unittest on mysqlDB"""

    def test_pep8(self):
        """Test pep8 styling"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstr(self):
        """Test Docstrings"""
        self.assertIsNone(DBStorage.__doc__)
        self.assertIsNone(DBStorage.__init__.__doc__)
        self.assertIsNone(DBStorage.all.__doc__)
        self.assertIsNone(DBStorage.new.__doc__)
        self.assertIsNone(DBStorage.save.__doc__)
        self.assertIsNone(DBStorage.delete.__doc__)
        self.assertIsNone(DBStorage.reload.__doc__)

if __name__ == "__main__":
    unittest.main()
