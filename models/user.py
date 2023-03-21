#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    places = relationship('Place', back_populates='user',
                          cascade='all, delete')
    reviews = relationship('Review', back_populates='user',
                           cascade='all, delete')

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
