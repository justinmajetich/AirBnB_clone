#!/usr/bin/python3
""" Test amenity """

import unittest
import models
from models.amenity import Amenity
from models.base_model import BaseModel


class amenity_tests(unittest.TestCase):
    """ Test for amenity file """

    def test_amenity(self):
        """ Test the subclass amenity """
        inst = Amenity()
        self.assertIsInstance(inst, BaseModel)
        self.assertTrue(hasattr(inst, "id"))
        self.assertTrue(hasattr(inst, "created_at"))
        self.assertTrue(hasattr(inst, "updated_at"))

    def test_amenityname(self):
        """ Test if the name exists """
        instance = Amenity()
        self.assertTrue(hasattr(instance, "name"))
        self.assertEqual(instance.name, "")
