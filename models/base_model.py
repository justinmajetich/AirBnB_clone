#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os
from models import storage

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        from models import storage"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                u = 'updated_at'
                c = 'created_at'
                k = kwargs
                k[u] = datetime.strptime(kwargs[u], '%Y-%m-%dT%H:%M:%S.%f')
                k[c] = datetime.strptime(kwargs[c], '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs['__class__']
            except KeyError:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            self.__dict__.update(kwargs)
            storage.save()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        new_dict = self.to_dict()
        new_dict.pop('__class__')
        return '[{}] ({}) {}'.format(cls, self.id, new_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed
        from models import storage"""
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
        try:
            dictionary.pop('_sa_instance_state')
        except KeyError:
            pass
        return dictionary

    def delete(self):
        """method to delete an object from the storage engine
        from models import storage"""
        stored_objects = storage.all()
        obj_id = self.id
        for key, val in stored_objects.items():
            val_id = (key.split('.', 1))[1]
            if val_id == obj_id:
                stored_objects.pop(key)
                storage.save()
                return
