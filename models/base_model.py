#!/usr/bin/python3
<<<<<<< HEAD
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


if getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
=======
"""
Module base_model
Contains a Class that defines all common attributes or
methods for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage
import uuid
import json
import sys
import os.path


class BaseModel():
    ''' a base class for other classes '''

    def __init__(self, *args, **kwargs):
        '''
        initializes the values
        '''
        if kwargs:
            dtf = '%Y-%m-%dT%H:%M:%S.%f'
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if ("created_at" == key or "updated_at" == key):
                    k_dict[key] = datetime.strptime(k_dict[key], dtf)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        print in "[<class name>] (<self.id>) <self.__dict__>" format
        '''
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__class__.__dict__))

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
>>>>>>> master
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
=======
        '''
        returns a dictionary containing all keysvalues
        of __dict__ of the instance
        '''
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

    def to_json(self):
        '''
        returns a json containing all keysvalues
        of __dict__ of the instance
        '''
        my_json = self.__dict__.copy()
        my_json.update({'created_at': self.created_at.strftime(self.dtf)})
        my_json.update({'__class__': str(self.__class__.__name__)})
        if hasattr(self, 'updated_at'):
            my_json.update({'updated_at': self.updated_at.strftime(self.dtf)})
        return my_json
>>>>>>> master
