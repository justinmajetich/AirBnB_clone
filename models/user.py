#!/usr/bin/python3
"""Defines the User class."""

# Importing necessary modules
import string
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.review import Review

class User(BaseModel):
    """Represents a user in the system.
    
    Attributes:
        email: The email address of the user.
        password: The password for user login.
        first_name: The first name of the user.
        last_name: The last name of the user.
    """
    
    # Database table name
    __tablename__ = "users"
    
    # User attributes
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    # Relationships
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
