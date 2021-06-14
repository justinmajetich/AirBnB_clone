#!/usr/bin/python3
"""tests for the console"""

import unittest
import os
from io import StringIO
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from console import console

class test_console(unittest.TestCase):
    """"class to test the console"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db')
    def test_create(self):
        if os.path.exists(Filestorage()._Filestorage__file_path):
            os.remove(Filestorage()._Filestorage__file_path)








if __name__ == '__main__':
    unittest.main()