#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class test_console(unittest.TestCase):
    """ Class to test the file storage method """
    @patch('builtins.print')
    def test_do_create_int(self, mock_print):
        try:
            HBNBCommand.do_create(self, "Place number_rooms=four")
        except ValueError:
            self.assertNotIsInstance(int, type(HBNBCommand.number_rooms))

    @patch('builtins.print')
    def test_do_create_float(self, mock_print):
        try:
            HBNBCommand.do_create(self, "Place latitude=thirty")
        except ValueError:
            self.assertNotIsInstance(float, type(HBNBCommand.latitude))


if __name__ == '__main__':
    unittest.main()
