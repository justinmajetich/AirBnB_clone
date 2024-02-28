#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
import models


Base = declarative_base()


class State(BaseModel, Base):
    """This class defines all common attributes/methods for other classes"""
    __tablename__ = 'base_model'
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiation of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """Returns a string representation"""
        return self.__str__()

    def save(self):
        """Updates the public instance attribute updated_at to current"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary representation of the class"""
        my_dict = dict(self.__dict__)
        my_dict.pop('_sa_instance_state', None)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def delete(self):
        """Deletes the object"""
        models.storage.delete(self)
