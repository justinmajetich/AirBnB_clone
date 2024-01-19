import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel

class TestCreateCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_create_with_valid_parameters(self):
        with patch('builtins.input', side_effect=['create BaseModel name="My House" age=25']):
            self.console.cmdloop()

        output = self.mock_stdout.getvalue().strip()
        expected_output = "My House"
        self.assertIn(expected_output, output)

        # Optionally, you can also check if the object was actually created
        created_object = BaseModel().new_instance()
        self.assertEqual(created_object.name, expected_output)

    def test_create_with_invalid_syntax(self):
        with patch('builtins.input', side_effect=['create BaseModel invalid_syntax']):
            self.console.cmdloop()

        output = self.mock_stdout.getvalue().strip()
        expected_output = "** invalid parameter syntax **"
        self.assertIn(expected_output, output)

        # Optionally, check that no object was created
        self.assertEqual(len(BaseModel().new_instance()), 0)

    # Add more test cases as needed for different scenarios

if __name__ == '__main__':
    unittest.main()
