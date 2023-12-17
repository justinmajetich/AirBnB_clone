import unittest
from unittest.mock import patch
from console import HBNBCommand
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
            self.hbnb_command_instance.do_create("create User email=\"user@example.com\" password=\"secure_password\"")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    def test_create_state(self):
        with self.assertRaises(HBNBCommand.CommandError) as context:
            self.hbnb_command_instance.do_create("create State name=\"California\"")
        self.assertEqual(str(context.exception), "** class doesn't exist **")

    # Update other tests similarly...

if __name__ == '__main__':
    unittest.main()
