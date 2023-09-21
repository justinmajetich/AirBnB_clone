#!/usr/bin/python3
"""This module defines a class User"""
import models
import sqlalchemy
import hashlib
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade='all, delete-orphan',
                            backref="user")
        reviews = relationship("Review", cascade='all, delete-orphan',
                            backref="user")

    else:
        email = ""
        _password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """returns password"""
        return self._password
    
    @password.setter
    def password(self, value):
        """sets password"""
        self._password = value
