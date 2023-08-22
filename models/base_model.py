#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id (Column(String(60), primary_key=True, nullable=False, unique=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default value=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    # skip this attribute
                    continue
                if key == "created_at" or key == "updated_at":
                    # convert value from string to datetime object
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                # set attribute of object using key & value
                setattr(self, key, value)
           else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.utcnow()     

        storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
       
        """Updates `updated_at` and saves the model"""
        self.updated_at = datetime.datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
       """dictionary['created_at'] = self.created_at.isoformat()"""
        """dictionary['updated_at'] = self.updated_at.isoformat()"""
        """return dictionary"""
      
        """Returns a dictionary representation of the instance"""
        new_dict = self.__dict__.copy()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

