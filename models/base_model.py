#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from email.policy import default
from sqlite3 import Date
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if getenv("HBNB_TYPE_STORAGE") == "db":
            if not kwargs:
                from models import storage
                self.id = str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()
                storage.new(self)
            else:
                for key, value in kwargs.items():
                    if key == "created_at" or "apdated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%S.%f")
                    if key != "__class__":
                        setattr(self, key, value)
        else:
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
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = (str(type(self).__name__))
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """Delete current instance"""
        from models import storage
        storage.delete(self)
        storage.save()
