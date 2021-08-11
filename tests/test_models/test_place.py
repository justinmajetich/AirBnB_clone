#!/usr/bin/python3
""" """
from unittest.case import skipIf
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_city_id(self):
        """ """
        new = self.value()
        new.city_id = "Toto"
        self.assertIn("'city_id': '{}'".format(new.city_id), str(new))
        # self.assertEqual(type(new.city_id), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_user_id(self):
        """ """
        new = self.value()
        new.user_id = "Toto"
        self.assertIn("'user_id': '{}'".format(new.user_id), str(new))
        # self.assertEqual(type(new.user_id), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_name(self):
        """ """
        new = self.value()
        new.name = "toto"
        self.assertIn("'name': '{}'".format(new.name), str(new))
        # self.assertEqual(type(new.name), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_description(self):
        """ """
        new = self.value()
        new.description = "description"
        self.assertIn("'description': '{}'".format(new.description), str(new))
        # self.assertEqual(type(new.description), str)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_number_rooms(self):
        """ """
        new = self.value()
        new.number_rooms = 2
        self.assertIn("'number_rooms': {:d}".format(
            new.number_rooms), str(new))
        # self.assertEqual(type(new.number_rooms), int)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_number_bathrooms(self):
        """ """
        new = self.value()
        new.number_bathrooms = 5
        self.assertIn("'number_bathrooms': {:d}".format(
            new.number_bathrooms), str(new))
        # self.assertEqual(type(new.number_bathrooms), int)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_max_guest(self):
        """ """
        new = self.value()
        new.max_guest = 6
        self.assertIn("'max_guest': {:d}".format(new.max_guest), str(new))
        # self.assertEqual(type(new.max_guest), int)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_price_by_night(self):
        """ """
        new = self.value()
        new.price_by_night = 120
        self.assertIn("'price_by_night': {:d}".format(
            new.price_by_night), str(new))
        # self.assertEqual(type(new.price_by_night), int)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_latitude(self):
        """ """
        new = self.value()
        new.latitude = 21.54
        self.assertIn("'latitude': {:.2f}".format(new.latitude), str(new))
        # self.assertEqual(type(new.latitude), float)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_longitude(self):
        """ """
        new = self.value()
        new.longitude = 18.14
        self.assertIn("'longitude': {:.2f}".format(new.longitude), str(new))
        # self.assertEqual(type(new.latitude), float)

    @skipIf(
        os.environ.get('HBNB_TYPE_STORAGE') != 'file',
        "File storage tests only"
    )
    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
