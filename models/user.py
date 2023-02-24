#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
    This class defines a user by various attributes
    """
    __tablename__ ='users'
    email = column(String(128), nullable=False)
    password = column(String(128), nullable=False)
    first_name = column(String(128))
    last_name = column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

