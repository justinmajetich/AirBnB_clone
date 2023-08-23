#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import storage_type


Base = declarative_base()


class BaseModel:
    id = Column(String(60), nullable=False,
                primary_key=True, default=str(uuid4()))
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        '''
            create new base model instance
            or recreate base model instance from dictionary
        '''
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()

        if kwargs == {}:
            return

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                value = datetime.fromisoformat(value)
            if key != '__class__':
                self.__dict__[key] = value

    def __str__(self):
        ''' defines custom string representation of object '''
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        ''' updates the updated_at attribute when called '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''
            creates custom dictionary from __dict__
            (i.e dictionary of instance attributes)
        '''
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        # the __class__ key is needed to recreate the object
        my_dict['__class__'] = self.__class__.__name__
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict

    def delete(self):
        ''' deletes the current instance from the storage '''
        models.storage.delete(self)
