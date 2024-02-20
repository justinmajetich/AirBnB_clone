#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import uuid
from datetime import datetime


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    
    """_summary_
        1.Have id Represent a column containing a Unique string (60 chars)
            Can't be null
            Primary key
        2.Create_at column containing Datetime
            can't be null
            default value of time use (datetime.utcnow())
        3.Updated_at column conatining datetime
            can't be null
            default value is current time (datetime.utcnow())
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        self.id = str(uuid.uuid4())
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            """_summary_
            Updated to handle creation of custom attributes
            """
            if 'id' not in kwargs:
                self.id =str(uuid.uuid4())
                self.created_at = datetime.utcnow()
                self.updated_at = datetime.utcnow()
            for k, v in kwargs.items():
                if k != '__class__':
                    # Check if the Key exits, if not create custom key
                    setattr(self,k , v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        # """Convert instance into dict format"""
        # dictionary = {}
        # dictionary.update(self.__dict__)
        # dictionary.update({'__class__':
        #                   (str(type(self)).split('.')[-1]).split('\'')[0]})
        # dictionary['created_at'] = self.created_at.isoformat()
        # dictionary['updated_at'] = self.updated_at.isoformat()
        # return dictionary
        
        d = dict(self.__dict__)
        d['__class__'] = self.__class__.__name__
