#!/usr/bin/python3
import unittest
from unittest.mock import patch
from console import HBNBCommand  # Import your class here

class TestDoCreateMethod(unittest.TestCase):

    def setUp(self):
        # Set up any necessary resources or configurations
        self.instance = HBNBCommand()
        self.cmd = HBNBCommand()

    def tearDown(self):
        # Clean up after the test
        pass

    @patch('builtins.print')  # Mock the print function to capture output
    @patch('models.engine.file_storage.FileStorage')  # Mock FileStorage
    def test_do_create_with_no_args(self, mock_storage, mock_print):
        self.cmd.onecmd("create")
        mock_print.assert_called_with("** class name missing **")
        mock_storage.assert_not_called()

    @patch('builtins.print')
    @patch('models.engine.file_storage.FileStorage')
    def test_do_create_with_unknown_class(self, mock_storage, mock_print):
        self.cmd.onecmd("create UnknownClass")
        mock_print.assert_called_with("** class doesn't exist **")
        mock_storage.assert_not_called()

    @patch('builtins.print')
    @patch('models.engine.file_storage.FileStorage')
    def test_do_create_with_valid_class_no_args(self, mock_storage, mock_print):
        with patch.object(self.cmd.classes['User'], '__init__', return_value=None):
            self.cmd.onecmd("create User")
        mock_storage.assert_called_once()
        mock_print.assert_called_with(self.instance.id)

    @patch('builtins.print')
    @patch('models.engine.file_storage.FileStorage')
    def test_do_create_with_valid_class_and_args(self, mock_storage, mock_print):
        with patch.object(self.cmd.classes['User'], '__init__', return_value=None):
            self.cmd.onecmd("create User attribute1=value1 attribute2=value2")
        mock_storage.assert_called_once()
        mock_print.assert_called_with(self.instance.id)

    def test_parse_params_with_valid_args(self):
        args_list = ["attribute1=value1", "attribute2=value2"]
        result = self.cmd.parse_params(args_list)
        expected_result = {'attribute1': 'value1', 'attribute2': 'value2'}
        self.assertEqual(result, expected_result)

    def test_parse_params_with_invalid_args(self):
        args_list = ["invalid_param", "attribute1=value1", "attribute2=value2"]
        result = self.cmd.parse_params(args_list)
        expected_result = {'attribute1': 'value1', 'attribute2': 'value2'}
        self.assertEqual(result, expected_result)

    def test_parse_params_with_malformed_args(self):
        args_list = ["attribute1value1", "attribute2=value2"]
        result = self.cmd.parse_params(args_list)
        expected_result = {'attribute2': 'value2'}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()