#!/usr/bin/python3
"""
Defines the BaseModel class.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value,
                                                          '%Y-%m-%dT%H:%M:%S.%f'))
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            time = datetime.utcnow()
            if 'created_at' not in kwargs:
                self.created_at = time
            if 'updated_at' not in kwargs:
                self.updated_at = time
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of a BaseModel."""
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                      self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__."""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = type(self).__name__
        if '_sa_instance_state' in dict_copy:
            del dict_copy['_sa_instance_state']
        return dict_copy

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)