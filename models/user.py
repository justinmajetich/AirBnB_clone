#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = Column(str(128), nullable=False)
    password = Column(str(128), nullable=False)
    first_name = Column(str(128), nullable=True)
    last_name = Column(str(128), nullable=True)
    __tablename__ = 'users'
