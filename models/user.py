#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.reviews import Review


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    reviews = relationship(
        "Review",
        backref="user",
        cascade="all, delete-orphan"
    )
