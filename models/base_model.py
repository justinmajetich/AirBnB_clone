#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from models import storage

fmt = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for i, j in kwargs.items():
                if i != "__class__":
                    setattr(self, i, j)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], fmt)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], fmt)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        tmp_dict = self.__dict__.copy()
        if "created_at" in tmp_dict:
            tmp_dict["created_at"] = tmp_dict["created_at"].strftime(fmt)
        if "updated_at" in tmp_dict:
            tmp_dict["updated_at"] = tmp_dict["updated_at"].strftime(fmt)
        tmp_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in tmp_dict:
            del tmp_dict["_sa_instance_state"]
        return tmp_dict
