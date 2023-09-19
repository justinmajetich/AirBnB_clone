#!/usr/bin/python3
""" Test for console.py """
import unittest
from console import HBNBCommand
from models import storage


class TestCreateWithParameters(unittest.TestCase):
    """ Test for do_create method from console.py """

    def test_create_string_parameter(self):
        """ Test creating an object with a string parameter """
        cmd = HBNBCommand()
        cmd.do_create("City name=\"New_York\"")
        obj_id = cmd.last_response.strip()
        obj = storage.get("City", obj_id)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.name, "New York")

    def test_create_float_parameter(self):
        """ Test creating an object with a float parameter """
        cmd = HBNBCommand()
        cmd.do_create("Place price=199.99")
        obj_id = cmd.last_response.strip()
        obj = storage.get("Place", obj_id)
        self.assertIsNotNone(obj)
        self.assertAlmostEqual(obj.price, 199.99, delta=0.01)

    def test_create_integer_parameter(self):
        """ Test creating an object with an integer parameter """
        cmd = HBNBCommand()
        cmd.do_create("User age=30")
        obj_id = cmd.last_response.strip()
        obj = storage.get("User", obj_id)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.age, 30)

    def test_create_invalid_parameter(self):
        """ Test creating an object with an invalid parameter """
        cmd = HBNBCommand()
        cmd.do_create("Place invalid_param=abc")
        obj_id = cmd.last_response.strip()
        obj = storage.get("Place", obj_id)
        self.assertIsNotNone(obj)
        self.assertNotIn("invalid_param", obj.to_dict())


if __name__ == '__main__':
    unittest.main()
