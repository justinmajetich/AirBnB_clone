#!/usr/bin/python3
"""This module defines a class User"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
storage_type = os.getenv('HBNB_TYPE_STORAGE', 'file')

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_type == 'db':
        __tablename__ = 'users'
        email = Column('email', String(128), nullable=False)
        password = Column('password', String(128), nullable=False)
        first_name = Column('first_name', String(128))
        last_name = Column('last_name', String(128))
    
        places = relationship('Place', back_populates='user', cascade='all, delete-orphan')
        reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
