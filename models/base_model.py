#!/usr/bin/python3

"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
import sqlalchemy
from sqlalchemy import String, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from . import storage_type

if storage_type == 'db':
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """
    A base class for all hbnb models
    """
    if storage_type == 'db':
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime,
                            default=datetime.now(),
                            nullable=False)
        updated_at = Column(DateTime,
                            default=datetime.now(),
                            nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def addAttribute(self, **kwargs):
        """method to add attribute
            to an object
        """
        self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get("_sa_instance_state", None) is not None:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """
        deleting an obj from
        storage
        """
        storage.delete(self)
