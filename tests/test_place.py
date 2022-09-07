#!/usr/bin/python3
"""unitest for testing Place class """
import models
from os import getenv
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from sqlalchemy.exc import OperationalError


class test_Place(test_basemodel):
    """Unittests for testing the place class"""

    def __init__(self, *args, **kwargs):
        """ inicialization values """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.state = State(name="California")
        self.city = City(name="San_Jose", state_id=self.state.id)
        self.user = User(name="Chepe", email="cheperramito@yahoo.com")
        self.place = Place(
            user_id=self.user.id, city_id=self.city.id, name="Laurita",
            number_rooms=3, number_bathrooms=2, max_guest=4,
            price_by_night=100)

    def test_city_id(self):
        """ test city id """
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(self.city.id, self.place.city_id)

    def test_user_id(self):
        """ test user id """
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(self.user.id, self.place.user_id)

    def test_name(self):
        """ test name """
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.name), str)

    def test_description(self):
        """ test description"""
        self.assertEqual(self.place.description, None)

    def test_number_rooms(self):
        """ test number of rooms"""
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(self.place.number_rooms, 3)

    def test_number_bathrooms(self):
        """ check number of bathrooms """
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(self.place.number_bathrooms, 2)

    def test_max_guest(self):
        """test the max of guest """
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(self.place.max_guest, 4)

    def test_price_by_night(self):
        """ test cost or price by night """
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(self.place.price_by_night, 100)

    def test_latitude(self):
        """test amenity latitude"""
        self.assertEqual(self.place.latitude, None)

    def test_longitude(self):
        """test amenity longitude"""
        self.assertEqual(self.place.longitude, None)

    def test_amenity_ids(self):
        """ test amenity ids"""
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertEqual(self.place.amenity_ids, [])

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_without_mandatory_arguments(self):
        """ """
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_is_subclass(self):
        """Check that Place is a subclass of Basemodel"""
        place = self.value()
        self.assertTrue(isinstance(place, Place))
