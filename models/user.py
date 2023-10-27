#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

__tablename__= users

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = Column(string(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(string(128), nullable=False)
    last_name = Column(string(128), nullable=False)
