#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade="all, delete", backref="user")
        review = relationship("Review", cascade="all, delete", backref="user")

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
