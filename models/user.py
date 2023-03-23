#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes

    Attributes:
        email (string): contains the user's email
        password (string): contains the user's password
        first_name (string): contains the user's first name
        last_name (string): contains the user's last name
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place",
                              backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review",
                               backref="user",
                               cascade="all, delete, delete-orphan")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
