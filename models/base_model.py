#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            if key != '__class__':
                setattr(self, key, value)

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
        """Creates a dictionary representation of an instance"""
        dict_repr = self.__dict__.copy()
        dict_repr['created_at'] = dict_repr['created_at'].isoformat()
        dict_repr['updated_at'] = dict_repr['updated_at'].isoformat()
        dict_repr['__class__'] = self.__class__.__name__

        if '_sa_instance_state' in dict_repr:
            del dict_repr['_sa_instance_state']

        return dict_repr

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
