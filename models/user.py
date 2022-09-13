#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a MySQL database
    Attributes:
        __tablename__ (str) : The name of the MySQL table to store users
        email: (sqlalchemy String): The user's email
        password: (sqlalchemy String): The user's password
        first_name: (sqlalchemy String): The user's first name
        last_name: (sqlalchemy String): The user's last name
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship('Place', backref="user", cascade='delete')
