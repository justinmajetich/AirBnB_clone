#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", cascade="all, delete")
    reviews = relationship("Review", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize new instances
        Args:
            args: list of arguments
            kwargs: key/value dictionary of arguments
        """
        super().__init__(args, kwargs)
