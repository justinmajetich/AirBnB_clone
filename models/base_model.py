#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import os
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()
storage_type = os.getenv("HBNB_TYPE_STORAGE")


class BaseModel:
    """
    A base class for all hbnb models which creates the common
    attributes between all other classes.
    Attributes:
      id (int)
      created_at (datetime)
      updated_at (datetime)
    """
    id = Column(
            String(50),
            primary_key=True,
            unique=True,
            nullable=False
            )
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        now = datetime.now()
        if "created_at" not in kwargs:
            self.created_at = now
        if "updated_at" not in kwargs:
            self.updated_at = now

        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, time_form)
                elif key != "__class__":
                    self.__dict__[key] = value

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        if storage_type == "db":
            self.updated_at = datetime.utcnow()
        else:
            self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get('_sa_instance_state'):
            dictionary.pop('_sa_instance_state')
        if 'amenity_ids' in dictionary:
            # Make a deep copy of the list
            dictionary['amenity_ids'] = dictionary['amenity_ids'].copy()

        return dictionary

    def delete(self):
        """Deletes an instance from storage"""
        from models import storage
        storage.delete(self)
