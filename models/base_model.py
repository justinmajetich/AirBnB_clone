#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DATETIME, String
import models

if models.storage_t != "db":
    Base = object
else:
    Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DATETIME, default=datetime.utcnow())
        updated_at = Column(DATETIME, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("updated_at") is None\
                    or kwargs.get("created_at") is None:
                self.updated_at = self.created_at = datetime.now()
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "updated_at" or k == "created_at":
                    v = datetime.fromisoformat(v)
                setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if dictionary.get("_sa_instance_state") is not None:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """
        deleting an obj from storage
        """
        models.storage.delete(self)
