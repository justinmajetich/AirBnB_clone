#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models."""

    id = Column(String(60), unique=True, nullable=False,
                primary_key=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiate a new model."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            if 'updated_at' in kwargs.keys():
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs.update({'updated_at': datetime.now()})

            if 'created_at' in kwargs.keys():
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                kwargs.update({'created_at': datetime.now()})

            if 'id' not in kwargs.keys():
                kwargs.update({'id': str(uuid.uuid4())})

            if '__class__' in kwargs.keys():
                del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Return a string representation of the instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current time when instance is changed."""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        """public delete method, to delete the current instance from
        the storage (models.storage) by calling the method delete.
        """
        from models import storage
        storage.delete(self)
