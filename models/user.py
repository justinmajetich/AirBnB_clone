#!/usr/bin/python3

"""
Module for the User class.
"""

from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """
        Class representing a user in the application.
        Inherits from BaseModel and Base.
        """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """
         Initializes a new User instance.
         Args:
             *args: Variable length argument list.
             **kwargs: Arbitrary keyword arguments.
         """
        super().__init__(*args, **kwargs)
