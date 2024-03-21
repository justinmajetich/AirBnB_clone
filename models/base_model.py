#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import sqlalchemy
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False
                        )
    updated_at = Column(DateTime,
                        default=datetime.utcnow(),
                        nullable=False
                        )

    def __init__(self, *args, **kwargs):
        """
        Initializes object attributes:
            - id: randomly generated string
            - created_at: current datetime
            - updated_at: same as created_at initially
        """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        if kwargs:
            for key, val in kwargs.items():
                if key in ("created_at", "updated_at"):
                    val = datetime.strptime(kwargs['updated_at'],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        dictt = self.to_dict()
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return "[{:s}] ({:s}) {}".format(cls, self.id, dictt)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """
        purge the object from storage
        """
        models.storage.delete(self)

