import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO
from models.__init__ import storage
from models.state import State


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

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_without_args(self, mock_stdout):
        # Redirect stdout to capture print output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Execute the console command
            self.hbnb_command_instance.do_all("")

        # Get the captured output
        result = mock_stdout.getvalue().strip()

        # If there are no instances in storage, the output should be an empty list
        if not storage.all():
            self.assertEqual(result, '[]')
        else:
            # Check if the output contains the string representation of all objects
            for model_class in HBNBCommand.classes.values():
                self.assertIn(str(model_class()), result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_with_valid_class(self, mock_stdout):
        # Redirect stdout to capture print output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Execute the console command
            self.hbnb_command_instance.do_all("all State")

        # Get the captured output
        result = mock_stdout.getvalue().strip()

        # Check if the output contains the string representation of all State objects
        for obj_id, obj in storage.all(State).items():
            self.assertIn(str(obj), result)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_with_invalid_class(self, mock_stdout):
        # Redirect stdout to capture print output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Execute the console command
            self.hbnb_command_instance.do_all("all InvalidClass")

        # Get the captured output
        result = mock_stdout.getvalue().strip()

        # Check if the output contains the error message
        self.assertIn("** class doesn't exist **", result)



if __name__ == '__main__':
    unittest.main()
