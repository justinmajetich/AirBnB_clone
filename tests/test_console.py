#!/usr/bin/python3
"""
This module defines test cases for the console class
"""
import unittest
from unittest.mock import patch
import MySQLdb
import os
from console import HBNBCommand

# Check if MySQL is available for testing
MYSQL_AVAILABLE = all(os.getenv(var) is not None for var in ['HBNB_MYSQL_HOST',
                      'HBNB_MYSQL_USER', 'HBNB_MYSQL_PWD', 'HBNB_MYSQL_DB'])


@unittest.skipIf(not MYSQL_AVAILABLE, "MySQL not available for testing")
class TestDoCreateWithMySQL(unittest.TestCase):

    def setUp(self):
        # Set up an instance of your command interpreter
        self.console = HBNBCommand()

    def _get_record_count(self):
        # Helper method to get the number of records in the 'states' table
        with MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
        ) as cursor:
            cursor.execute("SELECT COUNT(*) FROM states")
            return cursor.fetchone()[0]

    def test_create_state_command_changes_database(self):
        # Get the initial number of records in the 'states' table
        initial_count = self.do_count()

        # Execute the console command
        with patch('builtins.print') as mock_print:
            self.console.do_create("State name=\"California\"")

        # Get the number of records after executing the command
        final_count = self.do_count()

        # Check if the difference is +1
        self.assertEqual(final_count, initial_count + 1)

class TestDoCreate(unittest.TestCase):

    def setUp(self):
        # Set up an instance of your command interpreter
        self.command_interpreter = YourCommandInterpreter()

    def test_valid_string_parameter(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("MyClass name=\"Test Object\"")
            mock_print.assert_called_with(mock_print.new_instance.id)

    def test_valid_float_parameter(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("AnotherClass value=3.14")
            mock_print.assert_called_with(mock_print.new_instance.id)

    def test_valid_integer_parameter(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("ThirdClass count=42")
            mock_print.assert_called_with(mock_print.new_instance.id)

    def test_valid_multiple_parameters(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("YetAnotherClass name=\"Multiple Params\" count=10 value=2.5")
            mock_print.assert_called_with(mock_print.new_instance.id)

    def test_invalid_class_name(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("NonExistentClass name=\"Invalid Class\"")
            mock_print.assert_called_with("** class doesn't exist **")

    def test_invalid_parameter_format(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("MyClass invalid_param")
            mock_print.assert_called_with("Error: Invalid parameter format for invalid_param. Skipping.")

    def test_string_parameter_with_escaped_quotes(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("AnotherClass name=\"Test with escaped quotes: \\\"\"")
            mock_print.assert_called_with(mock_print.new_instance.id)

    def test_float_parameter_with_incorrect_format(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("AnotherClass value=3.14.2")
            mock_print.assert_called_with("Error: Invalid float value for parameter value=3.14.2. Skipping.")

    def test_empty_input(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("")
            mock_print.assert_called_with("** class name missing **")

    def test_valid_input_with_underscores(self):
        with patch('builtins.print') as mock_print:
            self.command_interpreter.do_create("MyClass name=\"String_With_Underscores\"")
            mock_print.assert_called_with(mock_print.new_instance.id)


if __name__ == '__main__':
    unittest.main()
