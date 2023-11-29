#!/usr/bin/python3
"""
Module base_model
Contains a Class that defines all common attributes or
methods for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage
import uuid
import json
import sys
import os.path


class BaseModel():
    ''' a base class for other classes '''

    def __init__(self, *args, **kwargs):
        '''
        initializes the values
        '''
        if kwargs:
            dtf = '%Y-%m-%dT%H:%M:%S.%f'
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if ("created_at" == key or "updated_at" == key):
                    k_dict[key] = datetime.strptime(k_dict[key], dtf)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        print in "[<class name>] (<self.id>) <self.__dict__>" format
        '''
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__class__.__dict__))

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keysvalues
        of __dict__ of the instance
        '''
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

    def to_json(self):
        '''
        returns a json containing all keysvalues
        of __dict__ of the instance
        '''
        my_json = self.__dict__.copy()
        my_json.update({'created_at': self.created_at.strftime(self.dtf)})
        my_json.update({'__class__': str(self.__class__.__name__)})
        if hasattr(self, 'updated_at'):
            my_json.update({'updated_at': self.updated_at.strftime(self.dtf)})
        return my_json
