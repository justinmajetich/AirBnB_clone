#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
        This is the class modele
        Inherits:
                BAseModel
                Base

        Attributes:
            __tablename__: table name in the database
            places: user's  places, relationship with place
            email: user's email.
            password: user's password.
            first_name: user's first name.
        last_name: user's last name.
    """
    __tablename__ = "users"
    places = relationship("Place", backref="user", cascade="all, delete-orphan")
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

