#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""


import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, id=None, created_at=None, updated_at=None):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(BaseModel.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__
        dictionary.update({'__class__': BaseModel.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
