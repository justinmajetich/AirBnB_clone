#!/usr/bin/python3
"""Defines the User class."""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """Represents a user."""
    
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Establishes one-to-many relationship with Place
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")

    # Establishes one-to-many relationship with Review
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
