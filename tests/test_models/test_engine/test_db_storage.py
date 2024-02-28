#!/usr/bin/python3
"""Module for testing file storage"""
import unittest
from models import storage
from models.engine.db_storage import DatabaseStorage
import os

class test_DatabaseStorageClass(unittest.TestCase):
    """Database storage class tests"""
    def setUp(self):
        """Set up test fixtures, if any."""
        self.storage = DatabaseStorage
