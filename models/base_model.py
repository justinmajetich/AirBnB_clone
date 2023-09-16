#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Datetime
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = Column(Integer, primary_key=True, nullable=False)
            self.created_at = Column(Datetime, default=datetime.utcnow(),
                                     nullable=False)
            self.updated_at = Column(Datetime, default=datetime.utcnow(),
                                     nullable=False)
        else:
            for key, value in kwargs.items():
                if not hasattr(self, key):
                    setattr(self, key, value)
            kwargs['updated_at'] = Column(Datetime, default=datetime.utcnow(),
                                          nullable=False)
            kwargs['created_at'] = Column(Datetime, default=datetime.utcnow(),
                                          nullable=False)

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
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        for key, value in dictionary.items():
            if key == '_sa_instance_state':
                del dictionary[key]
        return dictionary
