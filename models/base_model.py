#!/usr/bin/python3
'''This is a base class for all classes'''


import uuid
from datetime import datetime
import models


class BaseModel():
    ''' Defines all common attributes/methods for other classes '''

    def __init__(self, *args, **kwargs):
        ''' Instantiate an object with id, created_at and updated_at
        unless kwargs are passed'''
        dtformat = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:

            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, dtformat)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, dtformat)
                elif key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        '''return string representation'''
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''updates the public instance attribute updated_at
        with the current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of the instance'''
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        mydict["created_at"] = self.created_at.isoformat()
        mydict["updated_at"] = self.updated_at.isoformat()
        return mydict
