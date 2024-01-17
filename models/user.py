#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column


class User(BaseModel):
    """This class defines a user by various attributes"""
    if models.storage_t == "db":
        __tablename = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
