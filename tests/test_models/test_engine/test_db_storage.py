#!/usr/bin/python3
"""
Test for DataBase Storage
"""
from os import getenv
import unittest
import pep8
import os
import MySQLdb
import sqlalchemy
from models.engine.db_storage import DBStorage


class TestDB(unittest.TestCase):
    """
    Unittest for database storage
    """

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Test only for DBstorage")
    def setUp(self):
        """set up for test"""
        if os.getenv("HBNB_TYPE_STORAGE") == 'db':
            self.db = MySQLdb.connect(os.getenv("HBNB_MYSQL_HOST"),
                                      os.getenv("HBNB_MYSQL_USER"),
                                      os.getenv("HBNB_MYSQL_PWD"),
                                      os.getenv("HBNB_MYSQL_DB"))
            self.cursor = self.db.cursor()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Test only for DBstorage")
    def tearDown(self):
        """teardown"""
        if os.getenv("HBNB_TYPE_STORAGE") == 'db':
            self.db.close()

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Test only for DBstorage")
    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db',
                     "Test only for DBstorage")
    def test_attributes_DBStorage(self):
        """Test the methods"""
        self.assertTrue(hasattr(DBStorage, '_DBStorage__engine'))
        self.assertTrue(hasattr(DBStorage, '_DBStorage__session'))
        self.assertTrue(hasattr(DBStorage, 'new'))
        self.assertTrue(hasattr(DBStorage, 'save'))
        self.assertTrue(hasattr(DBStorage, 'all'))
        self.assertTrue(hasattr(DBStorage, 'delete'))
        self.assertTrue(hasattr(DBStorage, 'reload'))

if __name__ == "__main__":
    unittest.main()
