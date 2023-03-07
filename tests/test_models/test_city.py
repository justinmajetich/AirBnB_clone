#!/usr/bin/python3
"""Module containing tests for City class."""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class TestCity(test_basemodel):
    """Defines tests for City class."""

    def __init__(self, *args, **kwargs):
        """Initializes TestCity class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def setUp(self):
        """Sets up objects required for tests."""
        pass

    def tearDown(self):
        """Cleans up after each test."""
        pass

    def test_default(self):
        """Tests default City object."""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_str(self):
        """Tests City string representation."""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))