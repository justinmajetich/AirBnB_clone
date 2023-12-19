#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = kwargs.get('created_at', datetime.utcnow())
            self.updated_at = kwargs.get('updated_at', datetime.utcnow())
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
        dictionary = {
                key: value.isoformat() if isinstance(value, datetime) else value
                for key, value in self.__dict__.items()
        }
        dictionary['__class__'] = type(self).__name__
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Deletes instance from storage"""
        from models import storage
        storage.delete(self)
