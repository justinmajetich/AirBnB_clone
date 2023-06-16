#!/usr/bin/python3
""" Module for testing file FileStorage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.storage = self.storage  # Set the storage attribute
        self.model.save()

    def tearDown(self):
        self.storage.delete(self.model)
        self.storage.save()

    # def test_all(self):
    #     all_objects = self.storage.all()
    #     self.assertIsInstance(all_objects, dict)
    #     self.assertIn('BaseModel.{}'.format(self.model.id), all_objects)

    # def test_all_with_cls(self):
    #     all_objects = self.storage.all(BaseModel)
    #     self.assertIsInstance(all_objects, dict)
    #     self.assertIn('BaseModel.{}'.format(self.model.id), all_objects)

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

    # def test_reload(self):
    #     self.storage.save()
    #     loaded_model = self.storage.all(BaseModel)['BaseModel.{}'.format(self.model.id)]
    #     self.assertEqual(loaded_model.updated_at, self.model.created_at)
    #     self.storage.reload()
    #     reloaded_model = self.storage.all(BaseModel)['BaseModel.{}'.format(self.model.id)]
    #     self.assertEqual(reloaded_model.updated_at, self.model.created_at)

    def delete(self, obj=None):
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in obj.storage.all():
                del obj.storage.all()[key]
                obj.storage.save()  # Save the storage after deleting the object
        else:
            pass



if __name__ == '__main__':
    unittest.main()
