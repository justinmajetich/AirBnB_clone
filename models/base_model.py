#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
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
        else:
            for attr in ['updated_at', 'created_at']:
                if attr in kwargs:
                    kwargs[attr] = datetime.strptime(
                        kwargs[attr], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    kwargs[attr] = datetime.now()

            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())

            if '__class__' in kwargs:
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
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
