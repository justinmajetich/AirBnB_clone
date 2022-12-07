#!/usr/bin/python3
"""Defines all classes/attributes common to other classes. \
It is the base model of the current model."""

import uuid
from datetime import datetime, date, time
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME


Base = declarative_base()


class BaseModel:
    """Defines all fields and methods common to other classes"""

    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializing BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Prints: [<class name>] (<self.id>) <self.__dict__>"""
        tmp = '[{}] ({}) {}'
        return tmp.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance"""
        new_dictionary = self.__dict__.copy()
        try:
            new_dictionary.pop('_sa_instance_state')
        except KeyError:
            pass
        finally:
            new_dictionary.update({'__class__': str(type(self).__name__)})
            new_dictionary["created_at"] = self.created_at.isoformat()
            new_dictionary["updated_at"] = self.updated_at.isoformat()
        return new_dictionary

    def delete(self):
        models.storage.delete(self)
