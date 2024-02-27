#!/usr/bin/python3
""" test module for city class"""
from contextlib import AbstractContextManager
from typing import Any
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8
import unittest
import models.city


class test_City(test_basemodel):
    """ test for functionality of city class"""

    def __init__(self, *args, **kwargs):
        """ test for proper instantiation of city class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test for proper creation of state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test proper creation of city name """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestAmenityDoc(unittest.TestCase):
    """test for documentation in city class"""

    def test_module_doc(self):
        """checks for module doc"""
        self.assertGreaterEqual(len(models.city.__doc__), 1)
    
    def test_class_doc(self):
        """checks for class doc"""
        self.assertGreaterEqual(len(City.__doc__), 1)

class TestCityPep8(unittest.TestCase):
    """Test Amenity class for pep8 compliance"""

    def test_pep8_complinance(self):
        """test to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0,
                           "Found code style errors (and warnings).")
        
    def test_pep8_complinace(self):
        """test to ensure tests/test_models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_city.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")