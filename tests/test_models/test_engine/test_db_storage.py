#!/usr/bin/python3


import unittest
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models


class test_DBStorage(unittest.TestCase):

    def testAmenity(self):
        amenity = Amenity(name="Pool")
        if amenity.id in models.storage.all():
            self.assertTrue(amenity.name, "Pool")

    def testCity(self):
        city = City(name="Moca")
        if city.id in models.storage.all():
            self.assertTrue(city.name, "Moca")
