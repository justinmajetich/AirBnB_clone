#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_type == 'db':
        __tablename__ = "users"

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship("Place", cascade="all, delete", backref="user")
        reviews = relationship("Review", cascade="all, delete", backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
