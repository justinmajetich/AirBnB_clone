#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""


import uuid
from datetime import datetime

import sqlalchemy
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

import models

Base = declarative_base()

time = "%Y-%m-%dT%H:%M:%S.%f"
now = datetime.now()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = now
            self.updated_at = now

        else:
            for k, v in kwargs.items():
                if v is not self.__class__.__name__:
                    self.__dict__[k] = v
            if kwargs.get("created_at", None) and\
                    isinstance(self.created_at, str):
                self.created_at = datetime.strptime(kwargs["created_at"], time)

            else:
                self.created_at = datetime.utcnow()

            if kwargs.get("updated_at", None) and\
                    isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)

            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = now
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = self.__dict__.copy()
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime(
                time
            )

        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime(
                time
            )

        my_dict["__class__"] = self.__class__.__name__

        if "_sa_instance_state" in my_dict:
            del my_dict["_sa_instance_state"]

        return (my_dict)

    def delete(self):
        """deletes the current instance from the storage
        """
        models.storage.delete(self)
