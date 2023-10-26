#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if (os.getenv("HBNB_TYPE_STORAGE") == 'db'):
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship(
            "Review", cascade='all, delete', backref='user')
        places = relationship(
                'Place', cascade='all, delete, delete-orphan', backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
