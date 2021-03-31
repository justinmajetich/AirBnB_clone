#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = 'Column(String(128), nullable=False)'
    password = 'Column(String(128), nullable=False)'
    first_name = 'Column(String(128), nullable=False)'
    last_name = 'Column(String(128), nullable=False)'
    __tablename__ = 'users'
    places = 'Place'
    places_ = relationship("Place", backref="user")
