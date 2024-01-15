#!/usr/bin/python3
"""This is the user class"""

from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user
    Attributes:
        email: email address (string, 128 chars, not null)
        password: password for login (string, 128 chars, not null)
        first_name: first name (string, 128 chars, nullable)
        last_name: last name (string, 128 chars, nullable)
        places: relationship with Place objects
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationship with Place objects
    places = relationship('Place', backref='user', cascade='all, delete-orphan')
