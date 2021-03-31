#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column('id', String(60), primary_key=True, nullable=False)
    created_at = Column('created_at', DateTime, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column('updated_at', DateTime, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # converts from str back to datetime
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != "__class__":
                    setattr(self, key, value)
            if 'id' not in kwargs or self.id is None:
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        final_dict = dict(self.__dict__)
        # created_at and updated_at are converted to str() iso format
        final_dict["created_at"] = self.created_at.isoformat()
        final_dict["updated_at"] = self.updated_at.isoformat()
        final_dict["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in final_dict:
            del final_dict['_sa_instance_state']
        return final_dict

    def delete(self):
        """calls the storage method delete"""
        models.storage.delete(self)
