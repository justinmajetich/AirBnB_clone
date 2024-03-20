#!/usr/bin/python3
"""This module defines a class User"""
import string
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import  BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  relationship
from models.review import  Review


class User(BaseModel):
    """This class defines a user by various attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name  """
    
    __tablename__ = "users "
    email = Column(String(128), nullable=False)
    password = Column(string (128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    place = relationship("place", cascade= 'all, delete, delete-orphan', backref="user")
    reviews = relationship("Review", cascade= 'all, delete, delete-orphan', backref="user")