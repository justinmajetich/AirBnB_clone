#!/usr/bin/python3
""" Test module for amenity class """
import unittest
import models.amenity
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pep8
from models import storage
from models.engine.file_storage import FileStorage


class test_Amenity(test_basemodel):
    """ """

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
    """ test for documentation in amenity class"""

    def test_module_doc(self):
        """ checks for module doc"""
        self.assertGreaterEqual(len(models.amenity.__doc__), 1)

    def test_class_doc(self):
        """ checks for class doc"""
        self.assertGreaterEqual(len(Amenity.__doc__), 1)
    

class TestAmenityPep8(unittest.TestCase):
    """ test amenity class for pep8 complinace"""

    def test_pep8_compliance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")