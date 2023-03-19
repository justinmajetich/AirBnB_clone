#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # TODO add or replace class attribute
    id = Column(
        String(60),
        nullable=False,
        primary_key=True
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # ! no more need for import storage here
        # // from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        # TODO move models.storage.new to save(self)
        # // storage.new(self)
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        # ! moved from __init__ to here
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
        # TODO remove the key _sa_instance_state from dictionary
        if "_sa_instance_state" in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    # TODO add a new public instance method delete
    def delete(self):
        """Deletes the current instance"""
        from models import storage
        storage.delete(self)
