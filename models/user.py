#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)  # NUEVO REVISAR
    password = Column(String(128), nullable=False)  # NUEVO REVISAR
    first_name = Column(String(128), nullable=True)  # NUEVO REVISAR
    last_name = Column(String(128), nullable=True)  # NUEVO REVISAR
    places = relationship("Place", cascade="all, delete", backref="user")
    reviews = relationship("Review", cascade="all, delete", backref="user")
