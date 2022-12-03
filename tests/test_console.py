#!/usr/bin/python3
"""Unittest module of console.py
"""
import unittest
import sys
import os
import json
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_Console(unittest.TestCase):
    """Test of the console commands
    """

    def setUp(self):
        """Start console for each tests
        """
        self.cnsl = HBNBCommand()
        self.patcher = patch('sys.stdout', new=StringIO())
        self.f = self.patcher.start()

    def tearDown(self):
        """delete console and json file after each item"""
        del self.cnsl
        self.patcher.stop()
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_empty(self):
        """Test empty line input"""
        self.cnsl.onecmd("\n")
        self.assertEqual('', self.f.getvalue())

    def test_quit(self):
        """Test quit input"""
        self.cnsl.onecmd("quit")
        self.assertEqual('', self.f.getvalue())

    def test_EOF(self):
        """Test EOF input"""
        self.cnsl.onecmd("EOF")
        self.assertEqual('', self.f.getvalue())

    def test_create_BaseModel(self):
        """test create BaseModel cmd"
        """
        d = storage.all().copy()
        self.cnsl.onecmd("create BaseModel")
        d2 = storage.all()
        self.assertTrue(len(d) < len(d2))
        self.assertNotEqual('', self.f.getvalue())
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r') as f:
            self.assertTrue("BaseModel" in f.read())


if __name__ == '__main__':
    unittest.main()
