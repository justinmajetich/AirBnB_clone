#!/usr/bin/python3
"""Unit tests for the Place class."""

# Importing necessary modules
from tests.test_models.test_base_model import test_basemodel
from models.place import Place

class TestPlaceAttributes(test_basemodel):
    """Test cases for the attributes of the Place class."""
    
    def __init__(self, *args, **kwargs):
        """Initialize test cases."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id_type(self):
        """Test if the 'city_id' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id_type(self):
        """Test if the 'user_id' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name_type(self):
        """Test if the 'name' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description_type(self):
        """Test if the 'description' attribute is of type string."""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms_type(self):
        """Test if the 'number_rooms' attribute is of type integer."""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms_type(self):
        """Test if the 'number_bathrooms' attribute is of type integer."""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest_type(self):
        """Test if the 'max_guest' attribute is of type integer."""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night_type(self):
        """Test if the 'price_by_night' attribute is of type integer."""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude_type(self):
        """Test if the 'latitude' attribute is of type float."""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude_type(self):
        """Test if the 'longitude' attribute is of type float."""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids_type(self):
        """Test if the 'amenity_ids' attribute is of type list."""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
