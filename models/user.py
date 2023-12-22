#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', cascade='all, delete, delete-orphan',
                              backref='user')
        reviews = relationship('Review', cascade='all, delete, delete-orphan',
                               backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
