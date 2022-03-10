#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import os
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.now,
                            nullable=False)
        updated_at = Column(DateTime, default=datetime.now,
                            nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if id not in kwargs:
            self.id = str(uuid.uuid4())

        if 'created_at' not in kwargs:
            self.created_at = datetime.now()

        else:
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")

        if 'updated_at' not in kwargs:
            self.updated_at = datetime.now()

        else:
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'created_at':
                self.created_at = value
            elif key == 'updated_at':
                self.updated_at = value
            else:
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary
