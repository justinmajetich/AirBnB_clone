#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from models.city import City
import os


class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """
    def test_all(self):
        """ test all() function """
        new = City()
        storage.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_methods(self):
        """ test presence of methods """
        self.assertTrue(hasattr(storage, 'all'))
        self.assertTrue(hasattr(storage, 'new'))
        self.assertTrue(hasattr(storage, 'save'))
        self.assertTrue(hasattr(storage, 'delete'))
        self.assertTrue(hasattr(storage, 'reload'))

if __name__ == "__main__":
    unittest.main()
