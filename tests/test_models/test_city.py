"""City module tests"""
import unittest
import models
import os
from datetime import datetime
from models.city import City
import sqlalchemy.orm


class TestCityModel(unittest.TestCase):
    def test_init(self):
        self.assertEqual(City, type(City()))

    def test_state_id(self):
        Tulsa = City()
        self.assertEqual(sqlalchemy.orm.attributes.InstrumentedAttribute,
                         type(City.state_id))
        self.assertIn("state_id", dir(Tulsa))
        self.assertNotIn("state_id", Tulsa.__dict__)


if __name__ == "__main__":
    unittest.main()