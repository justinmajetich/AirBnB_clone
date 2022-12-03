#!/usr/bin/python3
''' Base Module for python interpreter'''


import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import os
Base = declarative_base()


class BaseModel:
    '''Parent class to store data'''

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        '''BaseModel Constructor'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if kwargs:
            self.update(*args, **kwargs)

    def __str__(self):
        '''Method to change print output of the instance'''
        dictInst = self.__dict__.copy()
        dictInst.pop("_sa_instance_state", None)
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, dictInst))

    def save(self):
        '''
        Public method to update public instance and store the
        change in the public instance attribute <updated_at>
        '''
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        '''Used to return a dict of all attribute of the instance'''
        # Create the dict
        dictInst = self.__dict__.copy()
        # Add a key '__class__' with value: the class name of the object
        dictInst['__class__'] = self.__class__.__name__
        dictInst['created_at'] = datetime.isoformat(dictInst['created_at'])
        dictInst['updated_at'] = datetime.isoformat(dictInst['updated_at'])
        dictInst.pop("_sa_instance_state", None)
        return dictInst

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute(keys) in kwargs
        """
        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                value = datetime.fromisoformat(value)
            elif key != '__class__' and "id" not in key:
                try:
                    value = int(value)
                except Exception:
                    try:
                        value = float(value)
                    except Exception:
                        try:
                            value = value.replace('_', ' ')
                        except Exception:
                            pass
            setattr(self, key, value)

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage

        storage.delete(self)
