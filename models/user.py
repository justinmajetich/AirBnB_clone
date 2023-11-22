#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=Flase)
    password = Column(String(128), nullable=Flase)
    first_name = Column(String(128), nullable=Flase)
    last_name = Column(String(128), nullable=Flase)
    places = relationship("Place", backref='user', cascade='all, delete')
    reviews = relationship("Review", backref='user', cascade='all, delete')
