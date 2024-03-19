import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down test environment"""
        del self.base_model
        storage.delete(self.base_model)

    def test_attributes(self):
        """Test instance attributes"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id(self):
        """Test id attribute"""
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict method"""
        base_dict = self.base_model.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn('id', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)

    def test_save(self):
        """Test save method"""
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_delete(self):
        """Test delete method"""
        self.base_model.save()
        self.assertIn(self.base_model, storage.all().values())
        self.base_model.delete()
        self.assertNotIn(self.base_model, storage.all().values())


if __name__ == '__main__':
    unittest.main()
