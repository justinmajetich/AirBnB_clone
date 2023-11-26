#!/usr/bin/python3
'''module for Base class:
for subclassing
this module defines a base class for all models in our hbnb clone'''

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    '''A base class for all hbnb models'''

    defaults = {}
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialization"""
        for k, v in self.__class__.defaults.items():
            if k not in kwargs:
                kwargs.update({k: v})
        if kwargs:
            forbidden_keys = ['__class__']
            datetime_keys = ['created_at', 'updated_at']
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            now = kwargs['created_at'] = datetime.now().isoformat()
            if 'created_at' not in kwargs:
                kwargs['created_at'] = now
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = now
            if '_sa_instance_state' in kwargs:
                del kwargs['_sa_instance_state']
            for k, v in kwargs.items():
                if k in forbidden_keys:
                    continue
                if k in datetime_keys:
                    # convert to datetime object
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            now = datetime.now()
            self.created_at = now
            self.updated_at = now

    def __str__(self):
        '''returns a string representation of the instance'''
        cls = self.__class__.__name__
        attributes = {k: v for k, v in self.__dict__.items()
                      if k != '_sa_instance_state'}
        return '[{}] ({}) {}'.format(cls, self.id, attributes)

    def save(self):
        '''
        updates updated_at with current timestamp when instance is changed
        '''
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        '''converts instance into dict format'''
        dictionary = self.__dict__.copy()
        dictionary.pop('_sa_instance_state', None)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        '''deletes the current instance from storage'''
        from models import storage
        storage.delete(self)
