#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    which will be mapped to columns on a users table
    in the database
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # establishing relationship with place and city models
        places = relationship(
            "Place", backref="user", cascade="all, delete-orphan")
        reviews = relationship(
            "Review", backref="user", cascade="all, delete-orphan")

    def __init__(self, *args, **kwargs):
        """ constructor for user """
        valid_user_param = {key: value for key, value in kwargs.items()
                            if hasattr(self, key) or key == 'id'}
        super().__init__(*args, **valid_user_param)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
