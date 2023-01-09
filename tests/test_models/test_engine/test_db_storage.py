#!/usr/bin/python3
"""The file contains the database storagee class tests"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.basemodel import Basemodel
from models.city import City
from models.place import Place
from models.review import Review
from models.stat import State
from models.user import User
import json
import os
import pep8
import unittest

DBStorage = db_storage.DBStorage
classes = {"Amenity" : Amenity, "City" : City, "User" : User, "Place" : Place, "State" : State, "Review" : Review}


class TestDBStorageDocs(unittest.TestCase):
	"""tests the documentations of the DBStorage class"""
	@classmethod
	def setUpClass(cls):
	"""set up for the doc tests"""
	cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

	
	def test_pep8_conformance_db_storage(self):
	"""
	checks if the models db_storage.py conforms with the pep8 regulations
	"""
	pep8s = pep8.StyleGuide(quiet=True)
	result = pep8s.check_files(['models/engine/db_storage.py'])
	self.assertEqual(result.total_errors, 0, "Found code style errors(and warnings).")


	def test_pep8_conformance_test_db_storage(self):
	"""tests whether files test_models/test_db_storage.py/ conformss to pep8"""
	pep8s pep8.StyleGuide(quiet=True)
	result = pep8s.check_files(['tests/test_models/test_engine/\test_db_storage.py'])
	self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")


	def test_db_storage_module_docstring(self):
	"""Tests for the module docstring in sb_storgae.py"""
	self.assertIsNot(db_storage.__doc__, None, "db_storage.py needs a docstring")
	self.assertTrue(len(db_storage.__doc__) >= 1, "db_storage.py needs a doc string")


	def test_db_storgae_class_docstring(self):
	"""TEsts for class docstring"""
	self.assertIsNot(DBStorage.__doc__, None, "DBStorage class needs a docstring")
	self.assertTrue(len(DBStorgae.__doc__) >= 1, "DBStorage class needs a docstring")


	def test_dbs_func_docstrings(self):
	"""Checks the presence of doocstring in DBStorage methods"""
	for func in self.dbs.f:
		self.assertIsNot(func[1].__doc__, None, "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TEstcase):
	"""Test the file storage class"""
	@unittest.skipIf(models.storage_t != 'db', "not testing db storage")
	def test_all_returns_dict(self):
	self.assertIs(type(models.storgae.all())), dict)


	@unittest.skipIf(models.storage_t != 'db', "not testing db storage")
	def test_all_no_class(self):
	"""test returns all rows when no class is passed"""
	
	@unittest.skipIf(models.storage_t != 'db', "not testing db storage")
	def test_new(self):
	"""test that adds new objects to the database"""


	@unittest.skipIf(models.storage_t != 'db'. "not testing db storage")
	def test_save(self):
	"""test saves ojects to file.json properly"""
