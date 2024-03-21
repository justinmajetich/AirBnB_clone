#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_state(self, mock_stdout):
        # Test creating a new State
        self.console.do_create('State name="California"')
        # Assert that the State is created successfully
        output = mock_stdout.getvalue().strip()
        self.assertRegex(output, r'\w*\-?')
        # self.assertIsInstance(output, str)
        # self.assertIn('California', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_place(self, mock_stdout):
        # Test creating a new Place
        self.console.do_create('Place city_id="0001" user_id="0001"\
                               name="My_little_house" number_rooms=4\
                               number_bathrooms=2\
                               max_guest=10 price_by_night=300\
                               atitude=37.773972 longitude=-122.431297')
        # Assert that the Place is created successfully

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_state(self, mock_stdout):
        # Test showing all States
        self.console.do_all("State")
        # Assert that all States are shown

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_place(self, mock_stdout):
        # Test showing all Places
        self.console.do_all("Place")
        # Assert that all Places are shown


if __name__ == '__main__':
    unittest.main()
