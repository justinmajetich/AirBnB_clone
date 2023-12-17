import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestCreateFunction(unittest.TestCase):
    def setUp(self):
        self.hbnb_command_instance = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_base_model(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create BaseModel")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    def test_create_user(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create User email=\"user@\
                                                 example.com\" password=\"\
                                                 secure_password\"")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    def test_create_state(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create State\
                                                 name=\"California\"")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    def test_create_city(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create City state_id=123\
                                                 name=\"San Francisco\"")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    def test_create_place(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create Place city_id=456\
                                                 user_id=789 name=\"Modern\
                                                 Loft price_per_night=150.5")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    def test_create_amenity(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create Amenity\
                                                 name=\"Wi-Fi\"")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    def test_create_review(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create Review place_id=101\
                                                 user_id=202 text=\"Lovely\
                                                 stay!\"")
        self.assertEqual(str(context.exception), "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
