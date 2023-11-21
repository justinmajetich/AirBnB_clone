#!/usr/bin/python3
"""
module contains unit tests for the Place class
"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    Test case for the Place class
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the test case
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test case for checking the type of the city_id attribute in Place
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Test case for checking the type of the user_id attribute
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Test case for checking the type of the name attribute
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Test case for checking the type of the description attribute
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Test case for checking the type of the number_rooms attribute
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Test case for checking the type of the number_bathrooms attribute
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Test case for checking the type of the max_guest attribute
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Test case for checking the type of the price_by_night attribute
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Test case for checking the type of the latitude attribute
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Test case for checking the type of the longitude attribute
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Test case for checking the type of the amenity_ids attribute
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
