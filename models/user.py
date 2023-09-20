#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from models.base_model import Base


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place",  backref="user", cascade="delete")
    reviews = relationship("Review",  backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """User class init
        """
        super().__init__(*args, **kwargs)
