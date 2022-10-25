#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# commented out code base for task 7
# class User(BaseModel):
#     """File Storage Method for User"""
#     email = ''
#     password = ''
#     first_name = ''
#     last_name = ''

class User(BaseModel, Base):
    """
    Database Storage Method for User
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship("Place", backref="user", cascade="all delete-orphan")
