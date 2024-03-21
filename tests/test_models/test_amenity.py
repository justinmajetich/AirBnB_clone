#!/usr/bin/python3
"""This module tests the Amenity class"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Tests the Amenity class"""

    data = {
        "__class__": "Amenity",
        "created_at": "2024-03-19T19:12:06.548029",
        "id": "0d279dc7-4fdb-4969-962d-c902e73ffadf",
        "name": "Wifi",
        "updated_at": "2024-03-19T19:12:06.548249",
    }

    def test_amenity_name(self):
        """Tests the name attribute of the Amenity class"""
        new = Amenity(**self.data)
        self.assertEqual(type(new.name), str)
