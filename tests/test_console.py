#!/usr/bin/python3
"""tests for the console"""

import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from os import getenv


class test_console(unittest.TestCase):
    """"class to test the console"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "FileStorage")
    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual("[[User]", f.getvalue()[:7])

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DBStorage")
    def test_create_db(self):
        """Test create command inpout DB"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create State name="California!"')
            s = f.getvalue()
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[[State]", f.getvalue()[:8])
        with patch('sys.stdout', new=StringIO()) as foo:
            s = "destroy State " + s
            self.consol.onecmd(s)


if __name__ == '__main__':
    unittest.main()
