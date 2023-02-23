#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__='users'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        email = column(String(128), nullable=False)
        password = column(String(128), nullable=False)
        first_name = column(String(128))
        last_name = column(String(128))
        places = relationship("Place", backref="user", cascade="delete")
        reviews = relationship("Review", backref="user", cascade="delete")
    else:
        email =""
        password =""
        first_name =""
        last_name = ""
