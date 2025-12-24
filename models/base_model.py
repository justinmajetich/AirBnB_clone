#!/usr/bin/python3
"""This is the base model class"""
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
import models

Base = declarative_base()


class BaseModel:
    """Defines common attributes and methods that all
       models will inherit from
    """

    id = Column(
        String(60), primary_key=True,
        nullable=False, default=lambda: str(uuid.uuid4())
    )
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)

            # Ensure defaults exist even if missing in kwargs
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # models.storage.new(self) Moved to def save(self)

    def __str__(self):
        """returns a string representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current session to database"""
        self.updated_at = datetime.now()
        models.storage.new(self)  # Moved here
        models.storage.save()

    def to_dict(self):
        """
           - Copies everything python stores inside __objects including
             SQLAlchemy's objects.
           - The _sa_instance_state is filtered out since json library can't
             serialize it
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        # Remove SQLAlchemy internal attribute if present
        my_dict.pop('_sa_instance_state', None)
        return my_dict

    def delete(self):
        """ delete the  object"""
        storage.delete(self)
