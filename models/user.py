#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="delete")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
