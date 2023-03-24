#!/usr/bin/python3

"""
This module defines a base class for all models in our hbnb clone
"""
from uuid import uuid4
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    A base class for all hbnb models
    """
    def __init__(self, *args, **kwargs):
        """new instance"""
        if kwargs.__len__() > 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.fromisoformat(v)
                    setattr(self, k, v)
                    continue
                if k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates updated_at with current time when instance is changed
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        return new_dict
