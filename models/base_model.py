#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    # skip this attribute
                    continue
                if key == "created_at" or key == "updated_at":
                    # convert value from string to datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                # set attribute of object using key & value
                setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary = {}
        for key, value in self.__dict__.items():
            if key != "_sa_instance_state":
                dictionary[key] = value
        return '[{}] ({}) {}'.format(cls, self.id, dictionary)

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__': self.__class__.__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        key = "_sa_instance_state"
        if key in dictionary:
            del dictionary[key]

        return dictionary

    def delete(self):
        """Delete current instance from storage"""
        models.storage.delete(self)
