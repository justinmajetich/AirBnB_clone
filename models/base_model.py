#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)


    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def __repr__(self):
        """Call __str__ and returns a string representation of the instance"""
        return self.__str__

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Deletes an object"""
        models.storage.delete(self)
