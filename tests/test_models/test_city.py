#!/usr/bin/python3
"""Test module for City Class"""
import unittest
import pep8
import inspect
from unittest.mock import patch
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel
from models import storage
from sqlalchemy import String, Column
import os


class TestCityDocumentationAndStyle(unittest.TestCase):
    """
    Tests for the City class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_funcs = inspect.getmembers(
                City, predicate=inspect.isfunction
                )

    def test_pep8_conformance_City(self):
        """
        Test that models/city.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_City(self):
        """
        Test that tests/test_models/test_city.py
        conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["tests/test_models/test_city.py"]
        )
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_city_class_docstring(self):
        """
        Test for the City class docstring
        """
        self.assertIsNot(
                City.__doc__,
                None,
                "City class needs a docstring"
                )
        self.assertTrue(
            len(City.__doc__) >= 1, "City class needs a docstring"
        )

    def test_city_func_docstrings(self):
        """
        Tests for the presence of docstrings in City methods
        """
        for func in self.city_funcs:
            self.assertIsNot(
                func[1].__doc__,
                None,
                "{:s} method needs a docstring".format(func[0])
                )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0]),
                )


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
