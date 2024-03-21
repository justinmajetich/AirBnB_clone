#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime
import models

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
        String(60),
        nullable=False,
        unique=True,
        primary_key=True,
        default=str(uuid.uuid4()),
    )
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

        if kwargs:
            try:
                kwargs["updated_at"] = datetime.fromisoformat(
                    kwargs["updated_at"]
                )
                kwargs["created_at"] = datetime.fromisoformat(
                    kwargs["created_at"]
                )
            except (KeyError, ValueError):
                kwargs["updated_at"] = kwargs["created_at"] = datetime.now()

            kwargs.pop("__class__", None)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.get_dict_without_sa_instance()}"
        )

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.get_dict_without_sa_instance()

        dictionary.update({"__class__": self.__class__.__name__})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def delete(self):
        """Deletes the object."""
        models.storage.delete(self)

    def __repr__(self):
        """Return the string representation of the object."""
        return self.__str__()

    def get_dict_without_sa_instance(self):
        """Remove the sqlalchemy state from the dictionary"""
        dictionary = self.__dict__.copy()
        dictionary.pop("_sa_instance_state", None)
        return dictionary
