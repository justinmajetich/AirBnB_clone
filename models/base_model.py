#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = sqlalchemy.Column(
        'id',
        sqlalchemy.String(60),
        unique=True,
        nullable=False,
        primary_key=True
    )
    created_at = sqlalchemy.Column(
        'created_at',
        nullable=False,
        default=datetime.utcnow()
    )
    updated_at = sqlalchemy.Column(
        'updated_at',
        nullable=False,
        default=datetime.utcnow()
    )

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            # from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)
        else:
            for key, value in kwargs.items(): 
                if key == "updated_at":
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                            '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "created_at":
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                            '%Y-%m-%dT%H:%M:%S.%f')
                elif key != "__class__":
                    setattr(self, key, value)
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self) #New object before saving it
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary

    def delete(self):
        from models import storage
        storage.delete(self)
