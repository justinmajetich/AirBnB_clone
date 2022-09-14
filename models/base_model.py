#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime, date, time
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

Base = declarative_base()


class BaseModel:
    """class BaseModel that defines all methods"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(
        DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = created_at

    def __init__(self, *args, **kwargs):
        """Initializing BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(str(type(self).__name__),
                                     str(self.id), str(self.__dict__))

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of th class"""
        new_dictionary = self.__dict__.copy()
        if '_sa_instance_state' in new_dictionary.keys():
            del new_dictionary['_sa_instance_state']
        new_dictionary.update({'__class__': str(type(self).__name__)})
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()
        return new_dictionary

    def delete(self):
        """
        delete the current instance from the storage
         (models.storage) by calling the method delete
         """
        models.storage.delete(self)
