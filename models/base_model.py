#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import declarative_base, Column, String, DateTime
from models import storage

# create a new SQLAlchemy declarative base class called Base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    # Add or replace the following class attributes:
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

            # moved the call to storage.new() from here to just before
            # storage.save() on the save() method
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()

        # move the call to storage.new() to just before self.save() is called
        storage.new(self)
        storage.save()

    # Add the public instance method def delete(self) to delete the current
    # instance from the storage (models.storage) by calling the method
    # delete(self) from the storage engine
    def delete(self):
        """Delete the current instance from the storage"""
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        # update the to_dict() method of your BaseModel class to remove the
        # key _sa_instance_state from the dictionary returned by this method
        # only if this key exists
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary
