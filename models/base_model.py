#!/usr/bln/python3
""" BaseModel class """
from uuid import uuid4
from datetime import datetime
import models
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(object):
    """ Definition for BaseModel class """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """ Initializes the attributes of the BaseModel class """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if "id" not in kwargs.keys():
                    self.id = str(uuid4())
                if "updated_at" not in kwargs.keys():
                    self.updated_at = datetime.now()
                if "created_at" not in kwargs.keys():
                    self.created_at = datetime.now()

                setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Returns the string representation of the BaseModel class """
        return f"[{type(self).__name__}] ({str(self.id)}) {str(self.__dict__)}"

    def save(self):
        """ Updates to the current datetime and saves it """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
        __dict__ of the instance """
        temp_dict = self.__dict__.copy()
        temp_dict["__class__"] = self.__class__.__name__
        temp_dict["created_at"] = self.created_at.isoformat()
        temp_dict["updated_at"] = self.updated_at.isoformat()
        if "_sa_instance_state" in temp_dict:
            del temp_dict["_sa_instance_state"]
        return temp_dict

    def delete(self):
        """ Delete the current instance from the storage """
        models.storage.delete(self)
