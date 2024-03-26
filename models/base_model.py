#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
# base_model.py updated
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import models
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            kwargs['id'] = str(uuid4()) if 'id' not in kwargs else kwargs['id']
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f') if 'created_at' in kwargs else datetime.utcnow()
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f') if 'updated_at' in kwargs else datetime.utcnow()
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        dic = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = dic['created_at'].isoformat()
        dic['updated_at'] = dic['updated_at'].isoformat()
        return dic
