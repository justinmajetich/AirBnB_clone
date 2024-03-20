#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    from sqlalchemy import Column, String, DateTime
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            created_at = kwargs.get('created_at', datetime.now().isoformat())
            updated_at = kwargs.get('updated_at', datetime.now().isoformat())
            kwargs['created_at'] = datetime.strptime(created_at,
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(updated_at,
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['id'] = kwargs.get('id', str(uuid.uuid4()))

            for key, value in kwargs.items():
                if key != '_sa_instance_state' and key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        from hashlib import sha256
        """Returns a string representation of the instance"""

        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        if '_sa_instance_state' in self.__dict__:
            del self.__dict__['_sa_instance_state']
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
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__': (str(type(self)).
                                         split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

    def delete(self):
        """
        delete the current instance from the storage (models.storage)
        by calling the method delete
        """
        from models import storage
        storage.delete(self)
        storage.save()
