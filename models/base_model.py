#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

time_fmt = "%Y-%m-%dT%H:%M:%S.%f" #extended date time format for precise timestamps

if models.storage == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A basemodel All other classes will inherit from to get common values"""
    if models.storage == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow())
        updated_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """initialize basemodel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at)is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time_fmt)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time_fmt)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else: #if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        """Returns a string representation of the BaseModel"""
        return '[{:s}] ({:s}) {}'.format(self.__class__.name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """return dictionary containing all keys/values of instances"""
        new_dict =self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time_fmt)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time_fmt)
        new_dict["__class__"] = self.__class__.__name__
        if "__sa__instance_state" in new_dict:
            del new_dict["__sa__instance_state"]
        return new_dict
    
    def delete(self):
        """deletes current instance"""
        models.storage.delete(self)
