#!/usr/bin/python3
"""Test place class"""
import pycodestyle
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlaceDoc(unittest.TestCase):
    """check Place documentation"""
    def test_class_documentation(self):
        self.assertTrue(len(Place.__doc__) > 0)


class TestPlacePycode(unittest.TestCase):
    """check pycodestyle"""
    def test_pycodestyle(self):
        """tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        self.assertEqual(
            style.check_files(['models/place.py']).total_errors,
            0, "PEP 8 style issues found"
        )


class test_Place(test_basemodel):
    """Test place class"""

    def __init__(self, *args, **kwargs):
        """test place constructor"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test city id in place"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test user id in place"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test name in place"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test description in place"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test number of rooms in place"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test bathrooms in place"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test max guest in place"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test price in place"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude in place"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test longitude in place"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test amenity id in place"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)


    def test_place_inheritance(self):
        """test attributes of place class"""
        self.assertTrue(issubclass(self.value, BaseModel)

if __name__ == "__main__":
    unittest.main()
