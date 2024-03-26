#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """This class defines the test cases for FileStorage class"""
    def setUp(self):
        """Set up the test environment for FileStorage"""
        self.file_storage = FileStorage()
        self.file_storage.reload()

    def test_all(self):
        """Test all method of FileStorage"""
        model = BaseModel()
        l1 = self.file_storage.all()
        self.file_storage.new(model)
        l2 = self.file_storage.all()
        self.assertNotEqual(l1, l2)
        self.file_storage.reload()
        l3 = self.file_storage.all()
        self.assertEqual(l1, l3)

    def test_new(self):
        """Test new method of FileStorage"""
        model = BaseModel()
        self.file_storage.new(model)
        obj = self.file_storage.all()[
            model.__class__.__name__ + '.' + model.id]
        self.assertEqual(model.to_dict(), obj.to_dict())

    def test_save(self):
        """Test save method of FileStorage"""
        model = BaseModel()
        self.file_storage.new(model)
        self.file_storage.save()
        obj_dict = model.to_dict()
        obj_dict['id'] = model.id
        obj_dict['created_at'] = model.created_at.isoformat()
        obj_dict['updated_at'] = model.updated_at.isoformat()
        with open(FileStorage.__file_path, 'r') as f:
            obj_dict_read = json.load(f)
        self.assertEqual(obj_dict, obj_dict_read)

    def test_reload(self):
        """Test reload method of FileStorage"""
        model = BaseModel()
        self.file_storage.new(model)
        self.file_storage.save()
        self.file_storage.reload()
        obj_dict = model.to_dict()
        obj_dict['id'] = model.id
        obj_dict['created_at'] = model.created_at.isoformat()
        obj_dict['updated_at'] = model.updated_at.isoformat()
        obj_read = self.file_storage.all()[
            model.__class__.__name__ + '.' + model.id]
        self.assertEqual(obj_dict, obj_read.to_dict())

    def test_delete(self):
        """Test delete method of FileStorage"""
        model = BaseModel()
        self.file_storage.new(model)
        self.file_storage.save()
        self.assertRaises(KeyError, self.file_storage.delete, 1234)
        self.file_storage.delete(model)
        self.assertNotIn(model.__class__.__name__ + '.' + model.id,
                         self.file_storage.all())


if __name__ == '__main__':
    unittest.main()