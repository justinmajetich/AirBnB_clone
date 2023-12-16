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


if __name__ == '__main__':
    unittest.main()
