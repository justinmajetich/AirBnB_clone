#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, Relationship
from models import storage_type
from sqlalchemy import (
    Column,
    String
)


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_type == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = Relationship(
            'Review', cascade='all, delete', backref="user")
        places = Relationship(
            'Place', cascade='all, delete', backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
