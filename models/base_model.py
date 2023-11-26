#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

id = Column(String(60), nullable=False, primary_key=True)
created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())


class BaseModel(Base):
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at' or k == 'updated_at':
                        v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

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
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary.keys():
            del (dictionary['_sa_instance_state'])

        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
