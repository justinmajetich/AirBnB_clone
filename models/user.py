#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String, column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.place import Place


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    places = relationship("Place", cascade="all, delete", backref="user")
__tablename__ = User
email = Column(String(128), nullable=False)
password = Column(String(128), nullable=False)
name = Column(String(128), nullable=False)
first_name = column(String(128),nullable = False)
last_name = column(String(128), nullable = False)
