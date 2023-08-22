#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, Nullable
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    
    __tablename__ = "users"
    
    if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
        email = column(String(128), Nullable=False)
        password = column(String(128), Nullable=False)
        first_name = column(String(128), Nullable=True)
        last_name = column(String(128), Nullable=True)
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")
    else:    
        email = ''
        password = ''
        first_name = ''
        last_name = ''
