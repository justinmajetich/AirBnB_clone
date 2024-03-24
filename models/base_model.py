#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models

    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """
    id = Column(
        String(60),
        primary_key=True,
        nullable=False
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow()
    )

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            # Correctly assign updated_at and created_at
            self.updated_at = (datetime.utcnow() if kwargs.get('updated_at') is None
                               else datetime.strptime(kwargs['updated_at'],
                                                      '%Y-%m-%dT%H:%M:%S.%f'))
            self.created_at = (datetime.utcnow() if kwargs.get('created_at') is None
                               else datetime.strptime(kwargs['created_at'],
                                                      '%Y-%m-%dT%H:%M:%S.%f'))
            # Remove '__class__' key from kwargs
            kwargs.pop('__class__', None)
            # Ensure id is generated if not provided
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes an instance from storage"""
        from models import storage
        storage.delete(self)
