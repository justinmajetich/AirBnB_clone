import unittest
import MySQLdb
import os
from console import HBNBCommand


class TestCreateCommand(unittest.TestCase):
    """Test case for create command in the console."""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment."""
        cls.db = MySQLdb.connect(
            host=os.getenv("HBNB_MYSQL_HOST"),
            user=os.getenv("HBNB_MYSQL_USER"),
            passwd=os.getenv("HBNB_MYSQL_PWD"),
            db=os.getenv("HBNB_MYSQL_DB")
        )

        """Create a cursor object to execute SQL queries"""
        cls.cursor = cls.db.cursor()

        """Count the initial number of records in the 'states' table"""
        cls.initial_count = cls.get_states_count()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test environment."""
        cls.db.close()

    def test_create_state(self):
        """Test create command for adding a new state."""
        HBNBCommand().onecmd('create State name="California"')

    """Count the number of records in the 'states' table after the command"""
    final_count = self.get_states_count()

    """Calculate the difference in counts"""
    count_diff = final_count - self.initial_count

    """Assert that the difference is 1"""
    self.assertEqual(count_diff, 1)

    @staticmethod
    def get_states_count():
        """Get current num of records in the 'states' table"""
    query = "SELECT COUNT(*) FROM states"
    TestCreateCommand.cursor.execute(query)

    """Fetch the count from the query result"""
    count = TestCreateCommand.cursor.fetchone()[0]

    return count


if __name__ == '__main__':
    unittest.main()
