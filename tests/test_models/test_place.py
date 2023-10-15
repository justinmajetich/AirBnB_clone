#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pep8


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_description(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new), self.value)
    
    def test_pep8_conformance_place(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "Found style errors")

    def test_class(self):
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father(self):
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))
