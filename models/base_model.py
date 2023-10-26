#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
    Defines the BaseModel class for all models
    """
    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the Database"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            if kwargs.get('__class__', None):
                del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                self.__dict__.update({key: value})

    def save(self):
        """Saves the current state of the model into the database"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """Delete the model from the database"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert the model to a dictionary representation"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def __str__(self):
        """
        It returns a string representation of the dictionary
        with the given name and value as a string
        """
        attributes = {}
        attributes.update(self.__dict__)
        attributes.pop('_sa_instance_state', None)
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, attributes)
