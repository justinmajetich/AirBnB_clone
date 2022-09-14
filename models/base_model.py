#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from venv import create
from sqlalchemy import (
    Column,
    String,
    DateTime
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import models

if models.storage_type == 'db':
    Base = declarative_base()
else:
    Base = object
Relationship = relationship


class BaseModel:
    """A base class for all hbnb models"""
    if models.storage_type == 'db':
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            try:
                kwargs['updated_at'] = datetime.fromisoformat(
                                        kwargs['updated_at'])
                kwargs['created_at'] = datetime.fromisoformat(
                                        kwargs['created_at'])
            except KeyError:
                self.id = str(uuid.uuid4())
                kwargs['created_at'] = datetime.now()
                kwargs['updated_at'] = datetime.now()
                self.__dict__.update(kwargs)

            self.__dict__.update(kwargs)

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
        if models.storage_type is None:
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Deletes current instance from storage"""

        models.storage.delete()
