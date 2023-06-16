import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test the FileStorage class"""

    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}  # Clear the __objects attribute

    def tearDown(self):
        """Remove FileStorage file at the end of tests"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_setUp(self):
        """Test the setUp method of FileStorage"""
        # Check if __objects attribute is not empty before setUp
        self.storage._FileStorage__objects = {'obj1': 'value1', 'obj2': 'value2'}
        self.assertNotEqual(len(self.storage._FileStorage__objects), 0)

        # Call reload method to reset __objects attribute
        self.storage.reload()

        # Check if __objects attribute is an empty dictionary after calling reload
        self.assertEqual(len(self.storage._FileStorage__objects), 0)

    def test_obj_list_empty(self):
        """__objects is initially empty"""
        self.assertEqual(len(self.storage.all()), 0)

    def test_new(self):
        """New object is correctly added to __objects"""
        new = BaseModel()
        new.save()
        temp = None
        for obj in self.storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """__objects is properly returned"""
        new = BaseModel()
        new.save()
        temp = self.storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """File is not created on BaseModel save"""
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """Data is saved to file"""
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """FileStorage save method"""
        new = BaseModel()
        self.storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """FileStorage file is successfully loaded to __objects"""
        new = BaseModel()
        new.save()
        self.storage.save()
        self.storage.reload()
        for obj in self.storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """Load from an empty file"""
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            self.storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing happens if file does not exist"""
        self.assertEqual(self.storage.reload(), None)

    def test_base_model_save(self):
        """BaseModel save method calls FileStorage save"""
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """Confirm __file_path is string"""
        self.assertEqual(type(self.storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """Confirm __objects is a dict"""
        self.assertEqual(type(self.storage.all()), dict)

    def test_key_format(self):
        """Key is properly formatted"""
        new = BaseModel()
        new.save()
        _id = new.to_dict()['id']
        for key in self.storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_FileStorage_var_created(self):
        """FileStorage object FileStorage created"""
        self.assertEqual(type(self.storage), FileStorage)


if __name__ == '__main__':
    unittest.main()
