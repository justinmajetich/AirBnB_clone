#!/usr/bin/python3
"""This module defines the BaseModel class"""

import uuid
from datetime import datetime
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()

class BaseModel:
    """This class defines common attributes/methods for other classes"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            storage.new(self)
        else:
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        """Saves the current instance to the storage"""

        self.updated_at = datetime.utcnow()
        storage.save()
        storage.new(self)

    def delete(self):
        """Deletes the current instance from the storage"""

        storage.delete(self)

    def to_dict(self):
        """Returns a dictionary representation of the instance"""

        result = self.__dict__.copy()
        result.pop('_sa_instance_state', None)
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

