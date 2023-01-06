#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


# Note: BaseModel does NOT imherit from Base
# it only defines the common attributes
class BaseModel:
    """A base class for all hbnb models"""
    # define the field properties of the attributes (for sqlalchemy)
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(), nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime(), nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if ('updated_at' and 'created_at' in kwargs.keys()):
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                # a totally new instance, not a reload: set attributes
                kwargs['updated_at'] = datetime.now()
                kwargs['created_at'] = datetime.now()
                kwargs['id'] = str(uuid.uuid4())
            if ('__class__' in kwargs.keys()):
                del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        # add object to __objects & save to storage
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the current instance (self) from storage"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # remove dictionary['_sa_instance_state'] if it exists
        if '_sa_instance_state' in dictionary.keys():
            del (dictionary['_sa_instance_state'])
        return dictionary
