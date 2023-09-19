#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
form sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', back_populates='users',
                          cascade='all, delete, delete-orphan')

    # email = ''
    # password = ''
    # first_name = ''
    # last_name = ''
