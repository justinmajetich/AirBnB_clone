#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
import uuid
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True,
                nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

    def __init__(self, *args, **kwargs) -> None:
        """Initialization of BaseModel Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    date = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                    exec("self.{} = {}".format(key, repr(date)))
                elif key != "__class__":
                    exec("self.{} = {}".format(key, repr(value)))

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        return models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Docs"""
        models.storage.delete(self)
