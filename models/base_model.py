#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, DATETIME, Column

import models

Base = declarative_base()


class BaseModel:
    """This class will define all common attributes/methods
     for other classes
    """
    id = Column(String(60), unique=True, nullable=False, primery_key=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, dafault=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates of bae model class
        Args:
            -args:the first parameter
            -kwargs: the second argument for BaseModel construction
        Attributes:
            -id:id generator
            -created_at:date of created
            -updated_at:update date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value,
                                              "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created-at", time)
            if "update_at" not in kwargs.keys():
                setattr(self, "update-at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Create dic of thr class and returns
           Return:
               -return thr dictionary value of the class
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        key_list = list(dictionary.keys())
        if '_sa_instance_state' in key_list:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__': (str(type(self))
                            .split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """Delete the current instance from the
        storage by calling  methods delete"""
        models.storage.delete(self)
