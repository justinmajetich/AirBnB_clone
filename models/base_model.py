#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import storage_type

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
            String(60), nullable=False, primary_key=True, unique=True,
            default=str(uuid.uuid4())
            )
    created_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow()
            )
    updated_at = Column(
            DateTime,
            nullable=False,
            default=datetime.utcnow()
            )

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, v)
            if not hasattr(self, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(self, 'created_at'):
                setattr(self, 'created_at', datatime.now())
            if not hasattr(self, 'updated_at'):
                setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Converts instance into dict format"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        for k, v in dct.items():
            if isinstance(v, datetime):
                dct[k] = v.isoformat()
        dct.pop('_sa_instance_state', None)
        return dct

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
