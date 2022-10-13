#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from os import getenv
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

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
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)

        if self.id is None:
            self.id = str(uuid4())

        if getenv('HBNB_TYPE_STORAGE') != 'db':
            if self.created_at is None:
                self.created_at = datetime.utcnow()
            if self.updated_at is None:
                self.updated_at = datetime.utcnow()

    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        new_dict = {key: value for key, value in self.__dict__.items()
                    if key != "_sa_instance_state"}
        return "[{}] ({}) {}".format(type(self).__name__, self.id, new_dict)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """deletes the current instance from the storage
        """
        models.storage.delete(self)

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        new_dict = {key: value for key, value in self.__dict__.items()
                    if key != "_sa_instance_state"}
        new_dict["__class__"] = str(type(self).__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
