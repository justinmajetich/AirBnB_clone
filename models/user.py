#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base import Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = ''
    password = ''
    first_name = ''
    last_name = ''
