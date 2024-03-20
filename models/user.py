#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    from sqlalchemy import Column, String, ForeignKey
    from sqlalchemy.orm import relationship

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user",
                          cascade="all, delete")
    reviews = relationship("Review", backref="user",
                           cascade="all, delete")
