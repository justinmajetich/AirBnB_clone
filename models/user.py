#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represent a User.
    Attributes:
        __tablename__ (str): Name of the table
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship('Place', cascade='all, delete-orphan',
                          back_populates='user')
    reviews = relationship('Review', cascade='all, delete-orphan',
                           back_populates='user')
