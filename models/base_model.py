#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
import os
from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), unique=True, nullable=False,
                    primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__"""
        dic = self.__dict__.copy()
        dic['__class__'] = type(self).__name__
        dic['created_at'] = (self.created_at).isoformat()
        dic['updated_at'] = (self.updated_at).isoformat()

        if '_sa_instance_state' in dic.keys():
            del dic['_sa_instance_state']

        return dic

    def delete(self):
        """Deletes the current instance from the storage"""
        models.storage.delete(self)
