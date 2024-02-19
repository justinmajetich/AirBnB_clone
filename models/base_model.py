#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = Column(String(60), nullable=False,
                             primary_key=True, default=str(uuid.uuid4),
                             unique=True)

            self.created_at = Column(
                DateTime, nullable=False, default=datetime.utcnow())

            self.updated_at = Column(
                DateTime, nullable=False, default=datetime.utcnow())

            from models import storage
            storage.new(self)
        else:
            kwargs['updated_at'] = Column(DateTime, nullable=False,
                                          default=datetime.strptime(
                                              kwargs['updated_at'],
                                              '%Y-%m-%dT%H:%M:%S.%f'))

            kwargs['created_at'] = Column(DateTime, nullable=False,
                                          default=datetime.strptime(
                                              kwargs['created_at'],
                                              '%Y-%m-%dT%H:%M:%S.%f'))
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        from models import storage
        storage.delete(self)
