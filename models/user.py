#!/usr/bin/python3
"""User class for AirBnb project"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """User class that creates users table"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", cascade="all, delete-orphan",
                          backref='user')
    reviews = relationship("Review", cascade="all, delete-orphan",
                           backref='user')