#!/usr/bin/python3
"""
    Unittest for console.py
"""
import unittest
from console import HBNBCommand
from models import storage
from unittest.mock import patch
from io import StringIO
import os
import sys
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class TestConsole(unittest.TestCase):
    """Unittest for console.py"""

    @classmethod
    def setUp(cls):
        """Set up method"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDown(cls):
        """Tear down method"""
        del cls.console

    def tearDown(self):
        """Tear down method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual("", f.getvalue())


if __name__ == '__main__':
    unittest.main()