#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.place import Place
import os
import sqlalchemy


class User(BaseModel, Base):
    """Defines a user by various attributes"""
    __tablename__ = "users"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place",
                              cascade='all, delete, delete-orphan',
                              back_populates="user")
        reviews = relationship("Review",
                               cascade='all, delete, delete-orphan',
                               back_populates="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
