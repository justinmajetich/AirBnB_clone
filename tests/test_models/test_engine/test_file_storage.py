#!/usr/bin/python3
"""Module for testing file FileStorage"""
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        self.storage.delete(self.model)
        self.storage.save()

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(new_model.id), all_objects)

    def test_save(self):
        self.model.updated_at = self.model.created_at
        self.storage.save()
        loaded_model = self.storage.all(BaseModel)['BaseModel.{}'.format(self.model.id)]
        self.assertEqual(loaded_model.updated_at, self.model.created_at)

    def test_delete(self):
        self.storage.delete(self.model)
        all_objects = self.storage.all()
        self.assertNotIn('BaseModel.{}'.format(self.model.id), all_objects)

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        reloaded_model = self.storage.all(BaseModel)['BaseModel.{}'.format(self.model.id)]
        self.assertEqual(reloaded_model.updated_at, self.model.created_at)

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage._FileStorage__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage._FileStorage__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage._FileStorage__objects:
                del FileStorage._FileStorage__objects[key]
                self.save()  # Save the storage after deleting the object
        else:
            pass


if __name__ == '__main__':
    unittest.main()
