import unittest
import subprocess
import MySQLdb
from unittest import skipIf
from io import StringIO
from contextlib import redirect_stdout
from models.base_model import BaseModel
from console import HBNBCommand
from models import storage
from os import getenv
import sys


class TestHBNBCommand(unittest.TestCase):

    @classmethod
    def clean_up_states_table(cls):
        # Disable foreign key checks
        cls.cursor.execute("SET foreign_key_checks = 0")

        # Clean up existing data in the 'states' table
        cls.cursor.execute("DELETE FROM states")

        # Re-enable foreign key checks
        cls.cursor.execute("SET foreign_key_checks = 1")

        # Commit changes to the database
        cls.db.commit()

    @classmethod
    def setUpClass(cls):
        cls.db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='hbnb_dev',
            passwd='hbnb_dev_pwd',
            db='hbnb_dev_db'
        )
        cls.cursor = cls.db.cursor()
        cls.clean_up_states_table()

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def setUp(self):
        self.output_buffer = StringIO()

    def tearDown(self):
        self.output_buffer.close()

    def execute_console_command(self, command):
        with StringIO() as buffer, redirect_stdout(buffer):
            try:
                HBNBCommand().onecmd(command)
                return buffer.getvalue().strip()
            except Exception as e:
                return str(e)

    def get_states_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

    def test_count_with_mysql(self):
        self.clean_up_states_table()
        command = 'create State name="Arizona"'
        self.execute_console_command(command)
        command = 'count State'
        output = self.execute_console_command(command)
        self.assertEqual(int(output), "1", "Incorrect count for 'count' command")

    def test_create_with_mysql(self):
        # Count the number of records before creating a new one
        initial_count = self.get_states_count()

        # Execute the create command
        command = 'create State name="California"'
        self.run_console_command(command)

        # Count the number of records after creating a new one
        new_count = self.get_states_count()

        # Print debug information
        print(f"Initial count: {initial_count}")
        print(f"New count: {new_count}")

        # Assert that the new count is equal to the initial count plus 1
        self.assertEqual(new_count, initial_count + 1, "Record not added to the 'states' table")

    def test_destroy_with_mysql(self):
        # Count the number of records before destroying one
        initial_count = self.get_states_count()

        # Execute the destroy command
        command = 'destroy State 1'
        self.run_console_command(command)

        # Count the number of records after destroying one
        new_count = self.get_states_count()

        # Print debug information
        print(f"Initial count: {initial_count}")
        print(f"New count: {new_count}")

        # Assert that the new count is equal to the initial count minus 1
        self.assertEqual(new_count, initial_count - 1, "Record not deleted from the 'states' table")

    def run_console_command(self, command):
        # Helper method to run a command in the HBNB console and print the output
        print(f"Running command: {command}")
        with redirect_stdout(self.output_buffer):
            HBNBCommand().onecmd(command)

        # Print the console output
        output = self.output_buffer.getvalue()
        print(f"Command output:\n{output}")

    def test_show_with_mysql(self):
        self.clean_up_states_table()
        command = 'create State name="New York"'
        self.execute_console_command(command)
        command = 'show State 1'
        output = self.execute_console_command(command)
        self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
