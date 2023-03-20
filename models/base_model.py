#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            date_fmt = '%Y-%m-%dT%H:%M:%S.%f'
            date_time = ['created_at', 'updated_at']

            if '__class__' in kwargs:
                del kwargs['__class__']

            # used for `reload` which is the only thing permitted to come
            # with `id` as an attribute
            if 'id' in kwargs:
                for key in kwargs:
                    if key in date_time:
                        kwargs[key] = datetime.strptime(kwargs[key], date_fmt)
                self.__dict__.update(kwargs)

            # this is used by `create` console command when key/value pairs
            # are passed as well
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                self.__dict__.update(kwargs)
                storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
