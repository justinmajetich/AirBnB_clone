import unittest
from models.state import State
from models.city import City
from models.base_model import BaseModel
from os import environ


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Set up test environment"""
        self.state = State()

    def tearDown(self):
        """Tear down test environment"""
        del self.state

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.state, BaseModel)
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'cities'))

    def test_name_type(self):
        """Test name attribute type"""
        self.assertIsInstance(self.state.name, str)

    def test_cities_relationship_db_storage(self):
        """Test cities relationship for DBStorage"""
        if environ.get('HBNB_TYPE_STORAGE') == 'db':
            city = City(state_id=self.state.id)
            city.save()
            self.assertIn(city, self.state.cities)
            city.delete()
        else:
            self.skipTest("Test is only applicable for DBStorage")

    def test_cities_getter_file_storage(self):
        """Test cities getter for FileStorage"""
        if environ.get('HBNB_TYPE_STORAGE') != 'db':
            city = City(state_id=self.state.id)
            city.save()
            self.assertIn(city, self.state.cities)
        else:
            self.skipTest("Test is only applicable for FileStorage")


if __name__ == '__main__':
    unittest.main()
