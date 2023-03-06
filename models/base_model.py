#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['update_at'] = datetime.strptime(kwargs['update_at'],
                                                    '%Y-%m,-%dT%H:%M:%S.%f')
            kwargs['create_at'] = datetime.strptime(kwargs['create_at'],
                                                    '%Y-%m,-%dT%H:%M:%S.%f')
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
        dictionary |= self.__dict__
        dictionary['__class__'] = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary['create_at'] = self.created_at.isoformat()
        dictionary['update_at'] = self.updated_at.isoformat()

        dict_copy = dictionary.copy()
        if "_sa_instance_state" in dict_copy:
            del dict_copy["_sa_instance_state"]
        return dict_copy

    def delete(self):
        """
        delete the current instance from the storage
        (models.storage) by calling the method delete
        """
        from models import storage
        storage.delete(self)
