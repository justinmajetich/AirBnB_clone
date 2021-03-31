#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()


class BaseModel():
    """ BaseModel class """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Initializated Method """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            if "create_at" not in kwargs.keys():
                self.created_at = datetime.now()
            if "update_at" not in kwargs.keys():
                self.updated_at = datetime.now()
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    fmt = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, k, datetime.strptime(v, fmt))
                elif k != "__class__":
                    setattr(self, k, v)

    def save(self):
        """ Save Method """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Convert to dictionary """
        attr = vars(self).keys()
        dic = {"__class__": self.__class__.__name__}
        for k in attr:
            if k in ["created_at", "updated_at"]:
                dic.update({k: getattr(self, k).isoformat()})
            else:
                dic.update({k: getattr(self, k)})
            if "_sa_instance_state" in dic:
                del(dic['_sa_instance_state'])
        return dic

    def __str__(self):
        """ String method"""
        dic = self.__dict__.copy()
        dic.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, dic)

    def delete(self):
        """
        Delete the current instance from the storage (models.storage)
        by calling the method delete
        """
        models.storage.delete(self)
