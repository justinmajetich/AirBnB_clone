#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.user import User
import os
from os import getenv


class test_databaseStorage(unittest.TestCase):
    def test_all(self):
        """ Test that all objects are returned """
        storage = DBStorage()
        user = User(email="test@example.com", password="password")
        user.save()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn(user.id, all_objects.keys())
        self.assertIsInstance(all_objects[user.id], User)
