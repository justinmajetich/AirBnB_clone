#!/usr/bin/python3
"""This is the base model class for AirBnB"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from hashlib import md5


Base = declarative_base()


class BaseModel():
    """This class will defines all common attributes/methods
    for other classes
    """

    id = Column(String(60), unique=True, primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

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
        updated_set = created_set = False
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    created_set = True
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    updated_set = True
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        if not created_set:
            self.created_at = datetime.now()
        if not updated_set:
            self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        my_dict = self.to_dict().copy()
        del my_dict["__class__"]
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, my_dict)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = {k: v for k, v in dict(
            self.__dict__).items() if k != "_sa_instance_state"}
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def delete(self):
        """deletes the object from FileStorage.__objects
        """
        models.storage.delete(self)
