#!/usr/bin/python3
"""BaseModel class"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import os


Base = declarative_base()


class BaseModel:
    """Base class for other classes used."""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """__init__ method for BaseModel class"""
        if kwargs:
            for name, value in kwargs.items():
                if name != '__class__':
                    if name == 'created_at' or name == 'updated_at':
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, name, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
                setattr(self, 'created_at', datetime.utcnow())
                self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Return string of BaseModel class"""
        base_dict = dict(self.__dict__)
        base_dict.pop('_sa_instance_state', None)
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, base_dict))

    def __repr__(self):
        """Return string of BaseModel class"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """save with new."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return dict of BaseModel class. """
        cp_dct = dict(self.__dict__)
        cp_dct['__class__'] = type(self).__name__
        cp_dct['updated_at'] = cp_dct['updated_at'].isoformat()
        cp_dct['created_at'] = cp_dct['created_at'].isoformat()
        cp_dct.pop('_sa_instance_state', None)
        return (cp_dct)

    def delete(self):
        """deletes the current storage"""
        models.storage.delete(self)
