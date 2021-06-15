#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class BaseModel():
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            # self.__dict__ = kwargs
            if '__class__' in kwargs.keys():
                del kwargs['__class__']
            if 'updated_at' in kwargs.keys():
                self.updated_at = datetime.strptime(kwargs.get("updated_at"),
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            if 'created_at' in kwargs.keys():
                self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)
            
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """delete the current instance from model.storage"""
        from models import storage
        storage.delete(self)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        the_dict = {}
        the_dict.update(self.__dict__)
        the_dict.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        the_dict['created_at'] = self.created_at.isoformat()
        the_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in the_dict.keys():
            del the_dict['_sa_instance_state']
        return the_dict
