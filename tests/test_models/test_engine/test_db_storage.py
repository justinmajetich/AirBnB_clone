#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import storage
import MySQLdb
import os


class test_DBStorage(unittest.TestCase):
    """ Class to test the file storage method """
