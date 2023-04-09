#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), primary_key=True, nullable=True)
    password = Column(String(128), primary_key=True, nullable=True)
    first_name = Column(String(128), primary_key=True, nullable=True)
    last_name = Column(String(128), primary_key=True, nullable=True)
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")


