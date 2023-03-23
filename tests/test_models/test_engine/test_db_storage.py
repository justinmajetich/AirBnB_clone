#!/usr/bin/python3
""" Module for testing the DBStorage class """
import unittest
import pep8
from models import storage
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    """ Test the DBStorage class """

    @classmethod
    def setUpClass(self):
        """ Set up for the tests """
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def teardown(self):
        """ At the end of the test this will tear it down """
        del self.storage

    def test_pep8_conformance_db_storage(self):
        """ Test that models/engine/db_storage.py conforms to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """ Test that tests/test_models/test_engine/test_db_storage.py
        conforms to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_engine/test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attributes(self):
        """ Test that DBStorage have the attributes """
        self.assertTrue('engine' in self.storage.__dir__())
        self.assertTrue('session' in self.storage.__dir__())

    def test_all(self):
        """ Test all method """
        new = BaseModel()
        new.save()
        obj = storage.all()
        self.assertIn(new, obj.values())

    def test_new(self):
        """ Test new method """
        new = BaseModel()
        new.save()
        obj = storage.all()
        self.assertIn(new, obj.values())

    def test_save(self):
        """ Test save method """
        new = BaseModel()
        new.save()
        obj = storage.all()
        self.assertIn(new, obj.values())

    def test_delete(self):
        """ Test delete method """
        new = BaseModel()
        new.save()
        obj = storage.all()
        self.assertIn(new, obj.values())
        storage.delete(new)
        obj = storage.all()
        self.assertNotIn(new, obj.values())

    def test_reload(self):
        """ Test reload method """
        new = BaseModel()
        new.save()
        obj = storage.all()
        self.assertIn(new, obj.values())
        storage.delete(new)
        obj = storage.all()
        self.assertNotIn(new, obj.values())
        storage.reload()
        obj = storage.all()
        self.assertIn(new, obj.values)
