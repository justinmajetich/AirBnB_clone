#!/usr/bin/python3
"""Test module for amenity class"""
import unittest
import models.amenity
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class test_Amenity(test_basemodel):
    """Test functionality of Amenity class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


class TestAmenityDoc(unittest.TestCase):
    """Tests for documentation in amenity class"""

    def test_module_doc(self):
        """Checks for module doc"""
        self.assertGreaterEqual(len(models.amenity.__doc__), 1)

    def test_class_doc(self):
        """Checks for class doc"""
        self.assertGreaterEqual(len(Amenity.__doc__), 1)


class TestAmenityPep8(unittest.TestCase):
    """Tests Amenity Class for pep8 compliance"""

    def test_pep8_compliance(self):
        """Tests to ensure models/amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance(self):
        """Tests that tests/test_models/test_amenity.py is pep8 compliant"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
