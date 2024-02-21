#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    __tablename__ = 'base_model'
    __defaults = [0, 0.0, "", []]

    id = Column(String(60), nullable=False, primary_key=True,
                default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow(),
                        onupdate=datetime.now())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models import storage
        if getenv("HBNB_TYPE_STORAGE") != "db":
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            if kwargs:
                for key, value in kwargs.items():
                    if not hasattr(self, key):
                        setattr(self, key, value)

                if '__class__' in kwargs:
                    del kwargs['__class__']

                self.__dict__.update(kwargs)

                if 'updated_at' in kwargs:
                    self.updated_at = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if 'created_at' in kwargs:
                    self.created_at = datetime.strptime(kwargs['created_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        new_dict = {k: v for (k, v) in self.__dict__.items()
                    if v not in BaseModel.__defaults}
        new_dict.pop("_sa_instance_state", None)
        return '[{}] ({}) {}'.format(cls, self.id, new_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        """Deletes the curent instance"""
        from models import storage
        storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary
