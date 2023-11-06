#!/usr/bin/python3
# KASPER edited 12:55pm 10/31/2023
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    String
)


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user",
                          cascade="all, delete-orphan")
    # reviews = relationship("Review", backref="user",
    # cascade="all, delete-orphan")
