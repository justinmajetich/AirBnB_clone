#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
import sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models
    Attributes:
        id(sqlalchemy string): the id
        created_at(sqlalchemy datetime): time stamp at creation
        updated_at(sqlalchemy datetime): time stamp at update
    """

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model
        Args(any): argument to pass
        kwargs(dict): create instance attr from dict
        """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.now()
            else:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
            else:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if "__class__" in kwargs:    
                del kwargs['__class__']
            
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(type(self).__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        """return string representation"""
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = str(type(self).__name__)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict.pop("_sa_instance_state", None)
        return obj_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
