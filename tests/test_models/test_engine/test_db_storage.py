#!/usr/bin/python3
""" Module for testing dbtorage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_dbStorage(unittest.TestCase):
    """ Class to test the db storage method """

    def test_all(self):
        """Function to test the all method"""
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
