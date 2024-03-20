import unittest
from models.city import City
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def tearDown(self):
        """Tear down test environment"""
        del self.city

    def test_inheritance(self):
        """Test inheritance"""
        self.assertIsInstance(self.city, BaseModel)
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))

    def test_name_type(self):
        """Test name attribute type"""
        self.assertIsInstance(self.city.name, str)

    def test_state_id_type(self):
        """Test state_id attribute type"""
        self.assertIsInstance(self.city.state_id, str)

    def test_relationship(self):
        """Test relationship"""
        self.assertIn('State.cities', City.__table__.foreign_keys)

    def test_table_name(self):
        """Test table name"""
        self.assertEqual(City.__tablename__, 'cities')

    def test_nullable(self):
        """Test nullable constraints"""
        name_column = City.__table__.columns['name']
        state_id_column = City.__table__.columns['state_id']
        self.assertFalse(name_column.nullable)
        self.assertFalse(state_id_column.nullable)


if __name__ == '__main__':
    unittest.main()
