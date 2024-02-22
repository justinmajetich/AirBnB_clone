#!/usr/bin/python3
"""Test module for City Class"""
import unittest
from unittest.mock import patch
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
from models import storage
from sqlalchemy import String, Column
import os


class test_City(unittest.TestCase):
    """Test the functionality of City class"""

    def setUp(self):
        """Set up for the tests"""
        self.city = City()

    def tearDown(self):
        """Tearing down after the test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.city, City)

    def __init__(self, *args, **kwargs):
        """Instantiating the tests"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_name(self):
        """Test the attr name of City class"""
        self.assertTrue(hasattr(self.city, "name"))

    def test_state_id(self):
        """Test the attr state_id of City class"""
        self.assertTrue(hasattr(self.city, "state_id"))

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "skip if storage type is not db"
            )
    def test_db_columns(self):
        """Test the columns in the database"""
        self.assertIsInstance(City.name.property.columns[0], Column)
        self.assertIsInstance(City.state_id.property.columns[0], Column)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "skip if storage type is not db"
            )
    def test_db_column_types(self):
        """Test the column types in the database"""
        self.assertIsInstance(City.name.property.columns[0].type, String)
        self.assertIsInstance(City.state_id.property.columns[0].type, String)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "skip if storage type is not db"
            )
    def test_db_column_constraints(self):
        """Test the column constraints in the database"""
        self.assertTrue(City.name.property.columns[0].nullable is False)
        self.assertTrue(City.state_id.property.columns[0].nullable is False)


if __name__ == '__main__':
    unittest.main()
