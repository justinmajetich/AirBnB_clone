#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME
import os

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # Class attributes
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DATETIME, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DATETIME, default=datetime.utcnow(), nullable=False)


    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            # kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
            #                                         '%Y-%m-%dT%H:%M:%S.%f')
            # kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
            #                                         '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                if key != '__class__':
                    setattr(self, key, value)
            if os.getenv("HBNB_TYPE_STORAGE") == "db":
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())


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
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del(dictionary['_sa_instance_state'])
        return dictionary

    def delete(self):
        """Deletes current instance from db"""
        from models import storage
        storage.delete(self)

