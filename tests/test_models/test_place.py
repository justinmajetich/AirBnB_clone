#!/usr/bin/python3
"""
    test place
"""
from models.place import Place
from models.city import City
from models.user import User
from models.base_model import BaseModel
import unittest


class test_Place(unittest.TestCase):
    """
        test for Place class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy_city = Place()
        cls.dummy_city.city_id = City().id
        cls.dummy_city.user_id = User().id
        cls.dummy_city.name = "test"
        cls.dummy_city.description = "testing"
        cls.dummy_city.number_rooms = 1
        cls.dummy_city.number_bathrooms = 1
        cls.dummy_city.max_guest = 1
        cls.dummy_city.price_by_night = 1
        cls.dummy_city.latitude = 1.0
        cls.dummy_city.longitude = 1.0
        cls.dummy_city.amenity_ids = []

    @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy_city

    def test_inheritance(self):
        """
            test proper inheritance
        """
        self.assertIsInstance(self.dummy_city, BaseModel)
        self.assertTrue(hasattr(self.dummy_city, "id"))
        self.assertTrue(hasattr(self.dummy_city, "created_at"))
        self.assertTrue(hasattr(self.dummy_city, "updated_at"))

    def test_attrs(self):
        """
            test attributes
        """
        self.assertTrue(hasattr(self.dummy_city, "city_id"))
        self.assertTrue(hasattr(self.dummy_city, "user_id"))
        self.assertTrue(hasattr(self.dummy_city, "name"))
        self.assertTrue(hasattr(self.dummy_city, "description"))
        self.assertTrue(hasattr(self.dummy_city, "number_rooms"))
        self.assertTrue(hasattr(self.dummy_city, "number_bathrooms"))
        self.assertTrue(hasattr(self.dummy_city, "max_guest"))
        self.assertTrue(hasattr(self.dummy_city, "price_by_night"))
        self.assertTrue(hasattr(self.dummy_city, "latitude"))
        self.assertTrue(hasattr(self.dummy_city, "longitude"))
        self.assertTrue(hasattr(self.dummy_city, "amenity_ids"))

if __name__ == "__main__":
    unittest.main()
