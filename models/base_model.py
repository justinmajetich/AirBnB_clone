#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import uuid

Base = declarative_base()

class BaseModel:
    """Represents the BaseModel class.
    Attributes:
        id (str): The UUID of the BaseModel.
        created_at (datetime): The creation date of the BaseModel.
        updated_at (datetime): The last update date of the BaseModel.
    """
    id = Column(String(60), nullable=False, unique=True, primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """Deletes the current instance from storage."""
        models.storage.delete(self)

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        new_dict = dict(self.__dict__)
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict

    def __str__(self):
        """Returns a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

