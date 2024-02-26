#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            if kwargs.get('__class__', None):
                for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    if key != "__class__":
                        setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        d = self.__dict__.copy()
        d.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, d)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = str(type(self).__name__)
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        dict_rep.pop("_sa_instance_state", None)
        return dict_rep

    def delete(self):
        """Deletes the current instance from the storage."""
        models.storage.delete(self)
