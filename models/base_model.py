#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """
        A base class for all hbnb models

        ATTRIBUTS:
        ============
            id : string 60char max, not null, unique
                Primary Key
            created_at : datetime, not null,
                default: datetime now
            updated_at : datetime, not null,
                default: datetime now

    """

    id = Column(
        String(60),
        unique=True,
        nullable=False,
        primary_key=True
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

    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
        for key, value in kwargs:
            if key == "name":
                self.id = value
            elif key == "create_at":
                self.created_at = value
            elif key == "update_at":
                self.updated_at = value

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
        for key in dictionary.keys():
            if key == "_sa_instance_state":
                del dictionary[key]
        return dictionary

    def delete(self):
        """ Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
