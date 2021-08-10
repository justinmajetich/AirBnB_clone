#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import os
import uuid
import os
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    '''
        Base class for other classes to be used for the duration.
    '''

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=False)

    def __init__(self, *args, **kwargs):
        '''
            Initialize public instance attributes.
        '''
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            try:
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                         time_format)
                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                         time_format)
            except KeyError:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        '''
            Return string representation of BaseModel class
        '''
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)

        try:
            del dictionary['_sa_instance_state']
        except KeyError:
            pass

        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.\
                                   strftime('%Y-%m-%dT%H:%M:%D.%f')
        dictionary['updated_at'] = self.updated_at.\
                                   strftime('%Y-%m-%dT%H:%M:%D.%f')
        return dictionary

    def delete(self):
        '''
            Deletes the current instance from the storage
                by calling the method delete.
        '''
        models.storage.delete(self)
