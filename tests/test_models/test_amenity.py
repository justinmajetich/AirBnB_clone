#!/usr/bin/python3
"""tests for amenity class"""
import unittest
import pycodestyle
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenityDoc(unittest.TestCase):
    """check Amenity documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(Amenity.__doc__) > 0)


class TestAmenityPycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/amenity.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class test_Amenity(test_basemodel):
    """tests for amenity class"""

    def __init__(self, *args, **kwargs):
        """test constructor for amenity"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """test name for amenity"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_class(self):
        """Tests if correct class"""
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_inheritance(self):
        """tests if inheriting from BaseModel correctly"""
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel))


if __name__ == "__main__":
    unittest.main()
