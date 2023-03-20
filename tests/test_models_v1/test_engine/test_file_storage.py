#!/usr/bin/env python3
"""A unit test module for testing
``model/engine/file_storage.py`` module."""

import unittest
from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """This class tests some basic features of
    ``FileStorage`` class."""

    def test_all_method(self):
        """Simple test for if ``all()`` returns a dictionary"""
        self.assertEqual(type(storage.all()), dict)

    def test_new_method(self):
        """The class BaseModel uses the method ``storage.new(self, obj)``
        from ``FileStorage`` class on creation of new class instance,
        makes it a suitable option for this test"""
        base1 = BaseModel()
        fetch_all = str(storage.all())  # str() freezes the dict [1]
        base2 = BaseModel()
        self.assertNotEqual(fetch_all, str(storage.all()))  # [1]

    def test_save(self):
        """
        Tests ``save`` method of the
        FileStorage class.
        """
        storage = FileStorage()
        storage.reload()
        initial_file = str(storage.all())  # [1]
        base1 = BaseModel()
        storage.save()
        storage.reload()
        new_file = str(storage.all())  # [1]
        self.assertNotEqual(initial_file, new_file)

    def test_reload(self):
        """
        Tests ``reload`` method of the
        FileStorage class.
        """
        storage = FileStorage()
        storage.reload()
        initial_file = str(storage.all())  # [1]
        base1 = BaseModel()
        base1.save()
        storage.reload()
        new_file = str(storage.all())  # [1]
        self.assertNotEqual(initial_file, new_file)
