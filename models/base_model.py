#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwrgs):
        """Instatntiates a new model"""
        if not kwrgs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            if 'updated_at' in kwrgs:
                kwrgs['updated_at'] = datetime.strptime(kwrgs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            if 'created_at' in kwrgs:
                kwrgs['created_at'] = datetime.strptime(kwrgs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwrgs:
                del kwrgs['__class__']
            self.__dict__.update(kwrgs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        instance_dict = {key: value for key, value in
                         self.__dict__.items() if key != '_sa_instance_state'}
        return '[{}] ({}) {}'.format(cls, self.id, instance_dict)

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
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage (models.storage) by
        calling the method delete."""
        from models import storage
        storage.delete(self)
