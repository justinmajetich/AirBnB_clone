#!/usr/bin/python3
"""Module to test state functionality """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
from unittest.mock import patch
from models.state import State
from models.state import City
from models.base_model import BaseModel
from models import storage
from sqlalchemy import String, Column
import os
import pep8
import inspect


class TestStateDocumentationAndStyle(unittest.TestCase):
    """
    Tests for the State class documentation and style.
    """

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_funcs = inspect.getmembers(
                State, predicate=inspect.isfunction
                )

    def test_pep8_conformance_State(self):
        """
        Test that models/state.py conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_State(self):
        """
        Test that tests/test_models/test_state.py
        conforms to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["tests/test_models/test_state.py"]
        )
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_state_class_docstring(self):
        """
        Test for the State class docstring
        """
        self.assertIsNot(
                State.__doc__,
                None,
                "State class needs a docstring"
                )
        self.assertTrue(
            len(State.__doc__) >= 1, "State class needs a docstring"
        )

    def test_state_func_docstrings(self):
        """
        Tests for the presence of docstrings in State methods
        """
        for func in self.state_funcs:
            self.assertIsNot(
                func[1].__doc__,
                None,
                "{:s} method needs a docstring".format(func[0])
                )
            self.assertTrue(
                len(func[1].__doc__) >= 1,
                "{:s} method needs a docstring".format(func[0]),
                )


class test_state(test_basemodel):
    """Test the functionality of State class"""

    def setUp(self):
        """Set up for the tests"""
        self.state = State()

    def tearDown(self):
        """Tearing down after the test"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def __init__(self, *args, **kwargs):
        """Initilizing the tests"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == "db",
                     "To be tested in the FileStorage Mode only")
    def test_name3(self):
        """Test creation of a state"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_init(self):
        """Test the initialization"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test the attributes of State class"""
        self.assertTrue(hasattr(self.state, "name"))

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "skip if storage type is not db"
            )
    def test_db_columns(self):
        """Test the columns in the database"""
        self.assertIsInstance(State.name.property.columns[0], Column)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "skip if storage type is not db"
            )
    def test_db_column_types(self):
        """Test the column types in the database"""
        self.assertIsInstance(State.name.property.columns[0].type, String)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "skip if storage type is not db"
            )
    def test_db_column_constraints(self):
        """Test the column constraints in the database"""
        self.assertTrue(State.name.property.columns[0].nullable is False)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') != 'db',
            "skip if storage type is not db"
            )
    def test_relationships(self):
        """Test the relationships in the database"""
        self.assertTrue(hasattr(State, "cities"))

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_cities(self):
        """Test the cities property"""
        all_cities = self.state.cities
        self.assertIsInstance(all_cities, list)
        if all_cities:
            self.assertIsInstance(all_cities[0], City)

    @unittest.skipIf(
            os.getenv('HBNB_TYPE_STORAGE') == 'db',
            "skip if storage type is db"
            )
    def test_cities(self):
        """Test the cities property"""
        city = City()
        city.state_id = self.state.id
        city.save()

        cities = self.state.cities

        self.assertTrue(len(cities) > 0)

        for city in cities:
            self.assertIsInstance(city, City)

        for city in cities:
            self.assertEqual(city.state_id, self.state.id)


if __name__ == '__main__':
    unittest.main()
