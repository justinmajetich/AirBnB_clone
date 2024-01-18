#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel:
    """Defines common attributes for other classes"""
    id = Column(string(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """
        Instatntiates BaseModel class
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
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "create_at" not in kwargs:
                self.create_at = datetime.now()
            if "update_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string of class id, name, dictionary"""
        return "[{}] ({}) {}".format(
                type(self).__name__, seld.id, self.__dict__)

        def __repr__(self):
            """returning a string representation"""
            return self.__str__()

    def save(self):
        """updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates and returns dictionary class"""
        dictionary = dict(self.__dic__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in dicttionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """deletes objects"""
        models.storage.delete(self)
