#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
import models

Base = declarative_base()
<<<<<<< HEAD
=======

import sqlalchemy
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

import models

Base = declarative_base()

time = "%Y-%m-%dT%H:%M:%S.%f"
now = datetime.now()
>>>>>>> origin/chalo


class BaseModel:
    """ A base class for all hbnb models """
    id = Column(String(60), nullable=False, primary_key=True)
<<<<<<< HEAD
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    Updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
=======
    created_at = Column(datetime, default=datetime.utcnow(), nullable=False)
    Updated_at = Column(datetime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
<<<<<<< HEAD
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
=======
>>>>>>> origin/chalo
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            if kwargs.get('created_at'):
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if kwargs.get('updated_at'):
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
<<<<<<< HEAD
=======
>>>>>>> d110871 (Update class and database engine models)
>>>>>>> origin/chalo
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
<<<<<<< HEAD
        models.storage.new(self)
        models.storage.save()
=======
<<<<<<< HEAD
        storage.save()
=======
        models.storage.new(self)
        models.storage.save()
>>>>>>> b065d2f (Update class models)
>>>>>>> origin/chalo

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
<<<<<<< HEAD
        if dictionary.get('_sa_instance_state'):
            del dictionary['_sa_instance_state']
=======
<<<<<<< HEAD
=======
        if dictionary.get('_sa_instance_state'):
            del dictionary['_sa_instance_state']
>>>>>>> b065d2f (Update class models)
>>>>>>> origin/chalo
        return dictionary

    def delete(self):
        """ Delete the current instance from storage """
        models.storage.delete(self)
