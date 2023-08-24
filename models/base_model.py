#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if len(kwargs) != 0:
            self._assign_att(kwargs)
            storage.new(self)
        else:
            storage.new(self)
    def _assign_att(self, att):
        """
        Assigns in attrubutes for kwargs
        """
        str_format = "%Y-%m-%dT%H:%M:%S.%f"
        for key, value in att.items():
            if key == "created_at" or key == "updated_at":
                t = self.__dict__[key]
                t = datetime.strptime(value, str_format)
            else:
                t = value

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
    
    def delete(self):
        """
        Delete instance from storage by calling its delete method
        """
        models.storage.delete(self)

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": (str(type(self)).split(".")[-1]).split("'")[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
