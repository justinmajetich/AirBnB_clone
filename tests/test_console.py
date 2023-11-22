#!/usr/bin/python3
"""This is a test module for the HBNBCommand class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
from time import sleep
import os
import json
from io import StringIO
from unittest.mock import patch
import sqlalchemy
import MySQLdb


class TestHBNBCommand(unittest.TestCase):
    """This is a test class for the HBNBCommand class"""

    @classmethod
    def setUp(self):
        """renames the file.json file to avoid overwriting it"""
        try:
            os.rename("file.json", "tmp")
        except Exception as e:
            pass

    def tearDown(self):
        """renames tmp back to file.json to restore it"""

        try:
            os.remove("file.json")
            pass
        except Exception as e:
            pass
        try:
            os.rename("tmp", "file.json")
        except Exception as e:
            pass

    @unittest.skipIf(type(storage) != FileStorage, "Test only\
                    applicable to FileStorage")
    def test_create_no_kwargs(self):
        """Tests create command with no args"""

        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create User')
            new_user = f.getvalue().strip()
            self.assertIn(f'User.{new_user}', storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create BaseModel')
            new_bm = f.getvalue().strip()
            self.assertIn(f'BaseModel.{new_bm}', storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create City')
            new_city = f.getvalue().strip()
            self.assertIn(f'City.{new_city}', storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create Place')
            new_place = f.getvalue().strip()
            self.assertIn(f'Place.{new_place}', storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create Review')
            new_review = f.getvalue().strip()
            self.assertIn(f'Review.{new_review}', storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create State')
            new_state = f.getvalue().strip()
            self.assertIn(f'State.{new_state}', storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create Amenity')
            new_amenity = f.getvalue().strip()
            self.assertIn(f'Amenity.{new_amenity}', storage.all().keys())

    @unittest.skipIf(type(storage) != FileStorage, "Test\
                    only applicable to FileStorage")
    def test_create_kwargs(self):
        """Tests create command with no args"""

        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd('create Place city_id="0001"\
                                        user_id="0001" name="My_little_house"\
                                        number_rooms=4\
                                        number_bathrooms=2 max_guest=10\
                                        price_by_night=300 latitude=37.773972\
                                        longitude=-122.431297')
            new_place = f.getvalue().strip()
            self.assertIn(f'Place.{new_place}', storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as f:
            obj = HBNBCommand().onecmd("all Place")
            user_output = f.getvalue().replace('\\', '')
            self.assertIn(new_place, user_output)
            self.assertIn("'price_by_night': 300", user_output)
            self.assertIn("'longitude': -122.431297", user_output)
            self.assertNotIn("'number_rooms': 4", user_output)
            self.assertIn("'user_id': '0001'", user_output)
