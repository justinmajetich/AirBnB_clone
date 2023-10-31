#!/usr/bin/python3
# KASPER edited @ 10/30 11:40pm
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import (
    Column,
    String,
    DateTime,
    Uuid
)


Base = declarative_base()


class BaseModel():
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            # If it is a dictionary, change timestamps to DateTime objects
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            if kwargs is not None and len(kwargs) != 0:
                for key in kwargs:
                    if key == "created_at" or key == "updated_at":
                        value = kwargs.get(key)
                        new_value = datetime.strptime(value, date_format)
                        setattr(self, key, new_value)
                    elif key != "__class__":
                        setattr(self, key, kwargs.get(key))

    def __str__(self):
        """Returns a string representation of the instance"""
        # Self is <class 'models.base_model.BaseModel'>
        # Splits by . and takes "BaseModel'>"
        # Splits by ' and makes just BaseModel

        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        # from models import storage
        self.updated_at = datetime.utcnow()
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
        if '_sa_instance_state' in dictionary:
            dictionary.pop('_sa_instance_state')
        return dictionary

    def delete(self):
        storage.delete(self)
