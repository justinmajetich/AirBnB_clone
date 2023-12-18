import unittest
import mysql.connector
import os
from unittest.mock import patch
from console import HBNBCommand


class TestCreateFunction(unittest.TestCase):
    def setUp(self):
        self.hbnb_command_instance = HBNBCommand()

        # Check if environment variables are set for MySQL testing
        self.mysql_testing = os.getenv("HBNB_TYPE_STORAGE") == "db"

        if self.mysql_testing:
            # Set up a connection to the test database
            self.db_connection = mysql.connector.connect(
                host=os.getenv("HBNB_MYSQL_HOST"),
                user=os.getenv("HBNB_MYSQL_USER"),
                password=os.getenv("HBNB_MYSQL_PWD"),
                database=os.getenv("HBNB_MYSQL_DB")
            )
            self.db_cursor = self.db_connection.cursor()

    def tearDown(self):
        # Clean up resources after each test
        if self.mysql_testing:
            self.db_cursor.close()
            self.db_connection.close()

    @unittest.skipIf(not os.getenv("HBNB_TYPE_STORAGE") == "db", "MySQL testing is not enabled.")
    def test_create_base_model(self):
        # Get the initial count of records in the base_models table
        initial_count = self.get_base_models_count()

        # Execute the console command
        with self.assertRaises(HBNBCommand.CommandError):
            self.hbnb_command_instance.do_create("create BaseModel")

        # Get the count of records after executing the command
        final_count = self.get_base_models_count()

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    @unittest.skipIf(not os.getenv("HBNB_TYPE_STORAGE") == "db", "MySQL testing is not enabled.")
    def test_create_user(self):
        # Get the initial count of records in the users table
        initial_count = self.get_users_count()

        # Execute the console command
        with self.assertRaises(HBNBCommand.CommandError):
            self.hbnb_command_instance.do_create("create User email=\"user@example.com\" password=\"secure_password\"")

        # Get the count of records after executing the command
        final_count = self.get_users_count()

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    @unittest.skipIf(not os.getenv("HBNB_TYPE_STORAGE") == "db", "MySQL testing is not enabled.")
    def test_create_state(self):
        # Get the initial count of records in the states table
        initial_count = self.get_states_count()

        # Execute the console command
        with self.assertRaises(HBNBCommand.CommandError):
            self.hbnb_command_instance.do_create("create State name=\"California\"")

        # Get the count of records after executing the command
        final_count = self.get_states_count()

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    @unittest.skipIf(not os.getenv("HBNB_TYPE_STORAGE") == "db", "MySQL testing is not enabled.")
    def test_create_city(self):
        # Get the initial count of records in the cities table
        initial_count = self.get_cities_count()

        # Execute the console command
        with self.assertRaises(HBNBCommand.CommandError):
            self.hbnb_command_instance.do_create("create City state_id=123 name=\"San Francisco\"")

        # Get the count of records after executing the command
        final_count = self.get_cities_count()

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    @unittest.skipIf(not os.getenv("HBNB_TYPE_STORAGE") == "db", "MySQL testing is not enabled.")
    def test_create_place(self):
        # Get the initial count of records in the places table
        initial_count = self.get_places_count()

        # Execute the console command
        with self.assertRaises(HBNBCommand.CommandError):
            self.hbnb_command_instance.do_create("create Place city_id=456 user_id=789 name=\"Modern Loft\" price_per_night=150.5")

        # Get the count of records after executing the command
        final_count = self.get_places_count()

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    @unittest.skipIf(not os.getenv("HBNB_TYPE_STORAGE") == "db", "MySQL testing is not enabled.")
    def test_create_amenity(self):
        # Get the initial count of records in the amenities table
        initial_count = self.get_amenities_count()

        # Execute the console command
        with self.assertRaises(HBNBCommand.CommandError):
            self.hbnb_command_instance.do_create("create Amenity name=\"Wi-Fi\"")

        # Get the count of records after executing the command
        final_count = self.get_amenities_count()

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)

    @unittest.skipIf(not os.getenv("HBNB_TYPE_STORAGE") == "db", "MySQL testing is not enabled.")
    def test_create_review(self):
        # Get the initial count of records in the reviews table
        initial_count = self.get_reviews_count()

        # Execute the console command
        with self.assertRaises(HBNBCommand.CommandError):
            self.hbnb_command_instance.do_create("create Review place_id=101 user_id=202 text=\"Lovely stay!\"")

        # Get the count of records after executing the command
        final_count = self.get_reviews_count()

        # Check if the difference is +1
        self.assertEqual(final_count - initial_count, 1)
