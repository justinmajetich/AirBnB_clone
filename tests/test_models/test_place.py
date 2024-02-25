# test_Place.py
import unittest
from models.place import Place
from unittest.mock import patch
import sys
import io

class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def setUp(self):
        """Set up test environment"""
        self.place = Place()

    def tearDown(self):
        """Tear down test environment"""
        del self.place

    def test_city_id(self):
        """Test city_id attribute"""
        self.assertEqual(type(self.place.city_id), str)

    def test_user_id(self):
        """Test user_id attribute"""
        self.assertEqual(type(self.place.user_id), str)

    def test_name(self):
        """Test name attribute"""
        self.assertEqual(type(self.place.name), str)

    def test_description(self):
        """Test description attribute"""
        self.assertEqual(type(self.place.description), str)

    def test_number_rooms(self):
        """Test number_rooms attribute"""
        self.assertEqual(type(self.place.number_rooms), int)

    def test_number_bathrooms(self):
        """Test number_bathrooms attribute"""
        self.assertEqual(type(self.place.number_bathrooms), int)

    def test_max_guest(self):
        """Test max_guest attribute"""
        self.assertEqual(type(self.place.max_guest), int)

    def test_price_by_night(self):
        """Test price_by_night attribute"""
        self.assertEqual(type(self.place.price_by_night), int)

    def test_latitude(self):
        """Test latitude attribute"""
        self.assertEqual(type(self.place.latitude), float)

    def test_longitude(self):
        """Test longitude attribute"""
        self.assertEqual(type(self.place.longitude), float)

    def test_amenity_ids(self):
        """Test amenity_ids attribute"""
        self.assertEqual(type(self.place.amenity_ids), list)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_create(self, mock_stdout):
        """Test create command in console"""
        cmd = 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="House" description="des" number_rooms=4 number_bathrooms=2 max_guest=6 price_by_night=100 latitude=1.3 longitude=2.3'
        with patch('sys.stdin', io.StringIO(cmd)):
            from console import HBNBCommand
            HBNBCommand().onecmd('Place.all()')
            self.assertTrue(mock_stdout.getvalue().strip().startswith('[Place]'))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_create_with_missing_params(self, mock_stdout):
        """Test create command in console with missing params"""
        cmd = 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b"'
        with patch('sys.stdin', io.StringIO(cmd)):
            from console import HBNBCommand
            HBNBCommand().onecmd('Place.all()')
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_create_invalid_city_id(self, mock_stdout):
        """Test create command in console with invalid city_id"""
        cmd = 'create Place city_id="invalid_id" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="House"'
        with patch('sys.stdin', io.StringIO(cmd)):
            from console import HBNBCommand
            HBNBCommand().onecmd('Place.all()')
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_create_invalid_user_id(self, mock_stdout):
        """Test create command in console with invalid user_id"""
        cmd = 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="invalid_id" name="House"'
        with patch('sys.stdin', io.StringIO(cmd)):
            from console import HBNBCommand
            HBNBCommand().onecmd('Place.all()')
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_console_create_without_params(self, mock_stdout):
        """Test create command in console without params"""
        cmd = 'create Place'
        with patch('sys.stdin', io.StringIO(cmd)):
            from console import HBNBCommand
            HBNBCommand().onecmd('Place.all()')
            self.assertEqual(mock_stdout.getvalue().strip(), "")

if __name__ == '__main__':
    unittest.main()
