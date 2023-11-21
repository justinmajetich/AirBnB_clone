#!/usr/bin/python3
"""
Import necessary modules and files.
"""


from tests.test_models.test_base_model import test_basemodel
from models.states_name import states_name


class TestStateCreation(unittest.TestCase):
    """
    Test case for the state creation console command
    """
    def setUp(self):
        """
        Set up a MySQL connection and cursor before each test
        """
        self.conn = MySQLdb.connect(host="localhost", user="user", passwd="password", db="test_db")
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """
        Close the cursor and connection after each test
        """
        self.cursor.close()
        self.conn.close()

    def test_create_state_command(self):
        """
        Test the execution of the console command to create a state
        """
        initial_count = self.get_states_count()

        execute_console_command()

        final_count = self.get_states_count()

        self.assertEqual(final_count - initial_count, 1)

    def get_states_count(self):
        """
        Helper function to get the count of states in the database
        """
        self.cursor.execute("SELECT COUNT(*) FROM states")
        return self.cursor.fetchone()[0]

if __name__ == '__main__':
    unittest.main()
