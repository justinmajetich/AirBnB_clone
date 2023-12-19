import MySQLdb
import unittest

# Your DB credentials
DB_USER = 'hbnb_test'
DB_PASSWORD = 'hbnb_test_pwd'
DB_HOST = 'localhost'
DB_NAME = 'hbnb_test_db'

class TestMySQL(unittest.TestCase):
    def setUp(self):
        # Connect to MySQL
        self.db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
        self.cursor = self.db.cursor()

        # Create a table for testing if it doesn't exist
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"
        )
        self.db.commit()

    def tearDown(self):
        self.cursor.execute("DROP TABLE states")
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        # Create a new state
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.db.commit()

        # Get the count of records after the state creation
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Assert that the count increased by 1
        self.assertEqual(new_count, 1)

    def test_all_method(self):
        # Insert a few states for testing
        self.cursor.executemany("INSERT INTO states (name) VALUES (%s)", [("California",), ("New York",)])
        self.db.commit()

        # Get all records from states table using 'all' method
        self.cursor.execute("SELECT * FROM states")
        states = self.cursor.fetchall()

        # Assert that the 'all' method retrieves the same number of records
        self.assertEqual(len(states), 2)

    def test_new_method(self):
        # Insert a new state object
        self.cursor.execute("INSERT INTO states (name) VALUES ('Texas')")
        self.db.commit()

        # Get the count of records after the state creation
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Simulating a 'new' method by inserting directly into the database
        self.cursor.execute("INSERT INTO states (name) VALUES ('Florida')")
        self.db.commit()

        # Get the count of records after a new object was 'added'
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Assert that the count increased by 1
        self.assertEqual(new_count, initial_count + 1)

    def test_save_method(self):
        # Insert a new state object
        self.cursor.execute("INSERT INTO states (name) VALUES ('Washington')")
        self.db.commit()

        # Get the count of records after the state creation
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Modifying a record and simulating 'save'
        self.cursor.execute("UPDATE states SET name = 'Oregon' WHERE name = 'Washington'")
        self.db.commit()

        # Get the count of records after modification (simulating 'save')
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Assert that the count remained the same
        self.assertEqual(new_count, initial_count)

    def test_delete_method(self):
        # Insert a new state object
        self.cursor.execute("INSERT INTO states (name) VALUES ('Alaska')")
        self.db.commit()

        # Get the count of records after the state creation
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Delete a record and simulate 'delete' method
        self.cursor.execute("DELETE FROM states WHERE name = 'Alaska'")
        self.db.commit()

        # Get the count of records after deletion (simulating 'delete')
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Assert that the count decreased by 1
        self.assertEqual(new_count, initial_count - 1)

if __name__ == '__main__':
    unittest.main()
