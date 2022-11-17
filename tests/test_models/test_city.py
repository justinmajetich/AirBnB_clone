#!/usr/bin/python3
"""Test module for city class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8
import unittest
import models.city


class test_City(test_basemodel):
    """Tests for functionality of city class"""

    def __init__(self, *args, **kwargs):
        """Tests proper instantiation of city clas"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests proper creation of state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """Tests proper creation of city name"""
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in city class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.city.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(City.__doc__), 1)


class TestCityPep8(unittest.TestCase):
    """Tests Amenity Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests to ensure tests/test_models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_city.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
