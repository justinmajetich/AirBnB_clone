# test_console_commands.py

import unittest
from unittest.mock import patch
from io import StringIO
import MySQLdb

class TestConsoleCommands(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_connection = MySQLdb.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="test_airbnb"
        )

        with cls.db_connection.cursor() as cursor:
            with open('setup_test_database.sql', 'r') as setup_file:
                setup_queries = setup_file.read()
                cursor.execute(setup_queries)

    def test_create_state_command(self):
        initial_count = self.get_state_records_count()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            your_console_instance.do_create("State name='California'")

        updated_count = self.get_state_records_count()

        self.assertEqual(updated_count, initial_count + 1)

    def get_state_records_count(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM states;")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

if __name__ == '__main__':
    unittest.main()
