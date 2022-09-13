#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


time = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Defines the BaseModel class for all hbnb models

    Attributes:
      id(sqlalchemy String) NOT NULL PK: BaseModel id
      created_at(sqlalchemy Datetime) NOT NULL: Datetime at creation
      updated_at(sqlalchemy Datetime) NOT NULL: Datetime at updation
    """
    if models.storage_type == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
            for key,value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, time)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            new_dict.pop("_sa_instance_state", None)
        return new_dict
#        my_dict = self.__dict__.copy()
#        my_dict["__class__"] = str(type(self).__name__)
#        my_dict["created_at"] = self.created_at.isoformat()
#        my_dict["updated_at"] = self.updated_at.isoformat()
#        my_dict.pop("_sa_instance_state", None)
#        return my_dict

    def delete(self):
        """deletes the current instance from the storage"""
        models.storage.delete(self)
