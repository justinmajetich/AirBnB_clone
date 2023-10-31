#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone
"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """
    A base class for all hbnb models
    """
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Instantiation of BaseModel object """
        self.id = kwargs.get('id', str(uuid4()))
        self.created = kwargs.get('created', datetime.now())
        self.updated = kwargs.get('updated', self.created)
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created", "updated"]:
                    self.__dict__[key] = datetime.strptime(
                        value,
                        "%Y-%m-%dT%H:%M:%S.%f"
                    )
                elif key != '__class__':
                    self.__dict__[key] = value

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates updated with current time when instance is changed
        """
        from models import storage
        self.updated = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Convert instance into dict format
        """
        d = {}
        d.update(self.__dict__)
        d.update({
            '__class__': (str(type(self)).split('.')[-1]).split('\'')[0]
        })
        d['created'] = self.created.isoformat()
        d['updated'] = self.updated.isoformat()
        if '_sa_instance_state' in d.keys():
            d.pop('_sa_instance_state')
        return d

    def delete(self):
        """
        Deletes the current instance from the storage
        """
        from models import storage
        storage.delete(self)
