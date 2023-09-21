#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True, default="")
        last_name = Column(String(128), nullable=True, default="")

        places = relationship("Place", backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete-orphan")
