#!/usr/bin/python3
"""Console unittest
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage
import inspect
from unittest.mock import patch, create_autospec
from io import StringIO
from console import HBNBCommand
import uuid
from time import sleep
import sys


class Test_console(unittest.TestCase):
    """Test cases for the console.py file
    """
    clis = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
    storage = FileStorage()

    def setUp(self):
        """set environment to start testing"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """set enviroment when testing is finished"""
        # Empty objects in engine
        FileStorage._FileStorage__objects = {}
        # Remove file.json if exists
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_create(self):
        """Test for create command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            command = "create State name=\"California\""
            HBNBCommand().onecmd(command)
            _id = f.getvalue().strip()
            key = "State" + "." + _id
            self.assertTrue(key in storage.all().keys())
