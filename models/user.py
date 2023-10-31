#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Defines relationship with the Review class
    reviews = relationship("Review", back_populates="user",
                           cascade="all, delete-orphan")

    # Defines relationship with the Place class
    places = relationship("Place", backref="user", cascade="all, delete")


class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="reviews")
