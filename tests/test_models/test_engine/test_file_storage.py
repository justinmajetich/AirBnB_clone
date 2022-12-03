#!/usr/bin/python3
""" Unittest for file_storage
"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class Test_FileStorage(unittest.TestCase):
    """Test different attributes and methods of FileStorage instances
    """

    def setUp(self):
        """set up of the FileStorage instance
        """
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass
        FileStorage.reload(storage)

    def test___file_path(self):
        """test of __file_path value equal to "file.json"
        """
        self.assertEqual(type(self.file_path), str)

    def test__objects(self):
        """test of __objects value equal to []
        """
        self.assertEqual(type(self.objects), dict)

    def test_all(self):
        """test of __objects value equal to storage.all()
        """
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """test of new() adding new object to __objects
        """
        all_objs = storage.all().copy()
        base = BaseModel()
        all_objs2 = storage.all().copy()
        self.assertNotEqual(all_objs, all_objs2)

    def test_save(self):
        """test save() creates a file
        """
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """test reload recreates all objects from "file.json"
        """
        st = FileStorage()
        stcopy = st.all().copy()
        print(stcopy)
        FileStorage.reload(storage)

    if __name__ == "__main__":
        unittest.main()
