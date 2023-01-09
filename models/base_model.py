#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from models import storage_type
import models

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60),
            unique = True,
            primary_key =True,
            nullable =False)
    created_at = Column(DATETIME,
            nullable =False,
            default=datetime.utcnow())
    updated_at = Column(DATETIME,
            nullable =False,
            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

            if 'created_at' not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)


    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""

        self.updated_at = datetime.now()
        models.stroage.new(self)
        models.storage.save()


    def delete(self):
        """Delete current instance from storage
        """
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = dict(self.__dict__)

        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']

        my_dict["__class__"] = str(type(self).__name__)

        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        
        return my_dict
