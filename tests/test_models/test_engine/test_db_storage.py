#!/usr/bin/python3
"""
Test validation the class TestDBStorage
"""
import unittest
import os
import tempfile
from models import storage
from models.engine.db_storage import DBStorage
from models.state import State


class TestDBStorage(unittest.TestCase):
    """Test Case """

    @classmethod
    def setUpClass(cls):
        """setting up a test environment for the class"""
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        os.environ['HBNB_TYPE_STORAGE'] = 'db'
        cls.storage = DBStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        """
        configures a database to be used as a data storage medium
        """
        os.close(cls.db_fd)
        os.unlink(cls.db_path)

    def setUp(self):
        """
        removes all objects in the base
        """
        self.storage._DBStorage__session.remove()

    def test_obj_list_empty(self):
        """
        checks that the __objects dictionary of the
        FileStorage class instance is initially empty
        """
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload(self):
        """
        checks if reload() of the FileStorage class works
        correctly when the object storage file does not exist
        """
        self.assertEqual(self.storage.reload(), None)

    def test_type_objects(self):
        """
        confirm that the __objects attribute of an instance
        of a class that uses a dictionary data storage system
        (storage.all()) is of type dictionary.
        """
        self.assertEqual(type(self.storage.all()), dict)

    def test_store(self):
        """checks that the object has been correctly saved in the database"""
        new = State(name="Florida")
        new.save()
        _id = new.to_dict()['id']
        self.assertIn(new.__class__.__name__ + '.' + _id,
                      self.storage.all(type(new)).keys())

    def test_storage_var_created(self):
        """verifies that an object of class"""

        self.assertEqual(type(self.storage), DBStorage)

        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)


if __name__ == "__main__":
    unittest.main()
