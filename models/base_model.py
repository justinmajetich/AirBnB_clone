#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime

storage_engine = getenv('HBNB_TYPE_STORAGE')
if storage_engine is None:
    storage_engine = "db"

Base = object
if storage_engine == "db":
    Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    storage_engine = getenv('HBNB_TYPE_STORAGE')
    if storage_engine is None:
        storage_engine = "db"

    if storage_engine == "db":
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime,
                            nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime,
                            nullable=False, default=datetime.utcnow())
    else:
        id = None
        created_at = None
        updated_at = None

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        now = datetime.now()

        if len(kwargs) > 0:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())

            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = now
            else:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

            if 'created_at' not in kwargs:
                kwargs['created_at'] = now
            else:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

            if '__class__' in kwargs:
                del kwargs['__class__']

            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = now
            self.updated_at = now

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models.__init__ import storage
        self.updated_at = datetime.now()

        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = (str(type(self)).split('.')[-1]).split('\'')[0]

        if "_sa_instance_state" in new_dict:
            new_dict.pop("_sa_instance_state")

        return new_dict

    def delete(self):
        """Removes current instance reference from within objects and saves it
        """
        from models.__init__ import storage
        storage.delete(self)
        storage.save()
        