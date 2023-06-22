#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
        Represents a user in the database.

        Attributes:
            __tablename__ (string): The name of the table.
            email (sqlalchemy string): The email address of the user.
            first_name(sqlalchemy string): The first name of the user.
            last_name (sqlalchemy string): The last_name of the user.
    """

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship('Place', backref='user',
                          cascade="delete")
    reviews = relationship('Review', backref='user',
                           cascade="delete")
