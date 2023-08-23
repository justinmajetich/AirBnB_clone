#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

fmt = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    if models.engine_type == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow(),
                            nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        now = datetime.utcnow()
        self.id = str(uuid.uuid4())
        self.created_at = now
        self.updated_at = now

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
                if key in ["created_at", "updated_at"]:
                    try:
                        tm = datetime.strptime(kwargs[key], fmt)
                        self.__dict__[key] = tm
                    except Exception as e:
                        print(e)
#        model.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        value = str(type(self)).split('.')[-1]
        dictionary.update({'__class__': value.split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if "_sa_instance_state" in dictionary.keys():
            del (dictionary["_sa_instance_state"])
        return dictionary

    def delete(self):
        """
        delete the current instance from the storage (models.storage)
        """
        models.storage.delete(self)
