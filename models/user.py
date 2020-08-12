#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place',
                              backref='user', cascade='all, delete-orphan',
                              passive_deletes=True,
                              single_parent=True)

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
