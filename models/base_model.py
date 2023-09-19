#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from models import which_storage


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(
            DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for c in kwargs:
                if c in ["created_at", "updated_at"]:
                    setattr(self, c, kwargs[c])
                elif c != "__class__":
                    setattr(self, c, kwargs[c])
            if which_storage == "db":
                if not hasattr(kwargs, "id"):
                    setattr(self, "id", str(uuid.uuid4()))
                if not hasattr(kwargs, "created_at"):
                    setattr(self, "created_at", datetime.now())
                if not hasattr(kwargs, "updated_at"):
                    setattr(self, "updated_at", datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        modification = {}
        keys_to_delete = []

        for key, value in dictionary.items():
            if isinstance(value, datetime):
                modification[key] = value.isoformat()

            if key == "_sa_instance_state":
                keys_to_delete.append(key)

        for key in keys_to_delete:
            del dictionary[key]

        dictionary.update(modification)

        return dictionary

    def delete(self):
        """delete instances from storage"""

        storage.delete(self)
