#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import unittest
from models.base_model import BaseModel
from models import storage


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def test_save_method(self):
        """Test the save method"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_storage_engine(self):
        """Test the storage engine type"""
        model = BaseModel()
        if storage.get_engine_type() == "db":
            # Adjust this based on your actual method for retrieving records count
            initial_records_count = storage.get_records_count()
            model.save()
            updated_records_count = storage.get_records_count()
            self.assertEqual(updated_records_count, initial_records_count + 1)
        else:
            self.skipTest("Skipping DB-specific test for file storage")

if __name__ == '__main__':
    unittest.main()
    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
