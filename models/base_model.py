#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
import models
Base = declarative_base()


if models.env_stroage == "db":
    class BaseModel:
        """A base class for all hbnb models"""

        id = Column(String(60), primary_key=True,
                    unique=True, nullable=False)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

        def __init__(self, *args, **kwargs):
            """
            init method for baseModel instances
            """
            if kwargs:
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                for key in kwargs.keys():
                    if key == '__class__':
                        continue
                    if key == 'created_at' or key == 'updated_at':
                        formatOfdate = '%Y-%m-%dT%H:%M:%S.%f'
                        dateetime = datetime.strptime(kwargs[key],
                                                      formatOfdate)
                        setattr(self, key, dateetime)
                        continue
                    setattr(self, key, kwargs[key])
            else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

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
            dictionary = {}
            dictionary.update(self.__dict__)
            dictionary.update({'__class__': (str(type(self)).
                              split('.')[-1]).split('\'')[0]})
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
            # if '_sa_instance_state' in dictionary.keys():
            #     dictionary.pop('_sa_instance_state')
            return dictionary

        def __str__(self):
            """
            :return:Return the print/str
            representation of the BaseModel instance.
            """
            if '_sa_instance_state' in self.__dict__.keys():
                self.__dict__.pop('_sa_instance_state')
            return str(self.__dict__)

        def delete(self):
            """
            calling the method delete
            """
            from models import storage
            storage.delete(self)
else:
    class BaseModel:
        """A base class for all hbnb models"""

        id = str(uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

        def __init__(self, *args, **kwargs):
            """
            init method for baseModel instances
            """
            if kwargs:
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                for key in kwargs.keys():
                    if key == '__class__':
                        continue
                    if key == 'created_at' or key == 'updated_at':
                        formatOfdate = '%Y-%m-%dT%H:%M:%S.%f'
                        dateetime = datetime.strptime(kwargs[key],
                                                      formatOfdate)
                        setattr(self, key, dateetime)
                        continue
                    setattr(self, key, kwargs[key])
            else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

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
            dictionary = {}
            dictionary.update(self.__dict__)
            dictionary.update({'__class__':
                              (str(type(self)).split('.')[-1]).split('\'')[0]})
            dictionary['created_at'] = self.created_at.isoformat()
            dictionary['updated_at'] = self.updated_at.isoformat()
            # if '_sa_instance_state' in dictionary.keys():
            #     dictionary.pop('_sa_instance_state')
            return dictionary

        def __str__(self):
            """
            :return:Return the print/str
            representation of the BaseModel instance.
            """
            if '_sa_instance_state' in self.__dict__.keys():
                self.__dict__.pop('_sa_instance_state')
            return str(self.__dict__)

        def delete(self):
            """
            calling the method delete
            """
            from models import storage
            storage.delete(self)
