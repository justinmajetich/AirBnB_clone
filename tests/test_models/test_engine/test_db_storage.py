#!/usr/bin/python3
"""test for file storage"""
import unittest
from models.engine import db_storage
from models.engine.db_storage import DBStorage


class TestConsole(unittest.TestCase):
    """ Test class for DBStorage """

    def test_documentation(self):
        """ Test docstrings documentation"""

        self.assertTrue(db_storage.__doc__)
        self.assertTrue(db_storage.DBStorage.__doc__)

    def test_methods_doc(self):
        """ Test all docstrings of each method"""

        for all_methods in dir(DBStorage):
            self.assertTrue(all_methods.__doc__)


if __name__ == '__main__':
    unittest.main()