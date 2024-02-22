#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        timefmt = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now().strftime(timefmt)
            else:
                 kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], timefmt)
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now().strftime(timefmt)
            else:
                 kwargs['created_at'] = datetime.strptime(kwargs['updated_at'], timefmt)
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = datetime.fromisoformat(self.created_at).isoformat()
        dictionary['updated_at'] = datetime.fromisoformat(self.created_at).isoformat()
        return dictionary
