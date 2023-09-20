#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from models.base_model import BaseModel, Base



class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

        @property
        def password(self):
            return self._password

        @password.setter
        def password(self, pwd):
            """hashes password"""
            self._password = pwd