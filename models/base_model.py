#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from models import storage_type


Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models
    Attributes:
        id (sqlalchemy String): Basemodel Id
        created_at (sqlalchemy DateTime): Datetime of creation
        updated_at (sqlalchemy DateTime): Datetime of last update
    """
    
    id == Column(String(60),
                 nullable=False,
                 primary_key=True,
                 unique=True)
    
    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])
                    
            if storage_type == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

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
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        for k in dict:
            if type(dict[k]) is datetime:
                dict[k] = dict[k].isoformat()
        if '_sa_instance_state' in dict.keys():
            del(dict['_sa_instance_state'])
        return dict
    
    def delete(self):
        """
            Performs a destruction of the current instance in storage
        """
        from models import storage
        storage.delete(self)
