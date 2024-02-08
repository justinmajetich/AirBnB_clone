#!/usr/bin/python3
'''Test for the DBStorage'''
import unittest
import os
from models.engine.db_storage import DBStorage


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "Test is not supported ")
class test_DB_Storage(unittest.TestCase):
    '''tests '''
    def test_moduleDocs(self):
        '''
        Docs
        '''
        self.assertGreater(len(DBStorage.__doc__), 0)


if __name__ == '__main__':
    unittest.main()
