#!/usr/bin/python3
""" Unittest test cases for 'models.place' """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest


class test_Place(test_basemodel):
    """ Test the instantiation of the Place class. """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.model = Place

    def test_instance_exists(self):
        """ """
        self.assertIsNotNone(self.model)

    def test_class_attributes(self):
        """ """
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_class_attributes_type(self):
        """ """
        self.assertIsInstance(getattr(Place, 'name'), str)
        self.assertIsInstance(getattr(Place, 'city_id'), str)
        self.assertIsInstance(getattr(Place, 'user_id'), str)
        self.assertIsInstance(getattr(Place, 'description'), str)
        self.assertIsInstance(getattr(Place, 'number_rooms'), int)
        self.assertIsInstance(getattr(Place, 'number_bathrooms'), int)
        self.assertIsInstance(getattr(Place, 'max_guest'), int)
        self.assertIsInstance(getattr(Place, 'price_by_night'), int)
        self.assertIsInstance(getattr(Place, 'latitude'), float)
        self.assertIsInstance(getattr(Place, 'longitude'), float)
        self.assertIsInstance(getattr(Place, 'amenity_ids'), list)


if __name__ == '__main__':
    unittest.main()
