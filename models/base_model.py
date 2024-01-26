#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            #  from models import storage
            """The behaviour of __init__: The method __init__ here is what
            is called first by default in all of our child class that
            inherits from BaseModel,
            before inheriting from the sqlalchemy `Base` Class.

            However, when the dot-notation below is then called, it will call
            the setattr in return. The setattr of the children class has
            however been overwritten by the `Base` that each children class
            inherits from. The sqlalchemy `Base` setattr behaviour actually
            sets attributes to become Column values like we normally know/do
            for typical sqlalchemy objects, according to their
            respective columns defined as class attributes

            Thus, for instance, the `self.id` notation below will be
            used by the `Base` to set the `id` column defined above as
            class attributes.
            """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if (kwargs.get("updated_at", None)):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                kwargs["updated_at"] = datetime.now()
            if (kwargs.get("created_at", None)):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                kwargs["created_at"] = datetime.now()
            if (kwargs.get("__class__", None)):
                del kwargs["__class__"]
            if os.getenv("HBNB_TYPE_STORAGE") != "db":
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split(".")[-1]).split("'")[0]
        return "[{}] ({}) {}".format(
            cls,
            self.id,
            {k: v for k, v in self.__dict__.items()
                if k != "_sa_instance_state"},
        )

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
        dictionary.update(
            {"__class__": (str(type(self)).split(".")[-1]).split("'")[0]},
        )
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if dictionary.get("_sa_instance_state", None) is not None:
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """Public method to delete instance"""
        storage.delete(self)
