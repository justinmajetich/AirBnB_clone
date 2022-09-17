#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column
from sqlalchemy import String
from models.place import Place
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="users", cascade="delete")
    reviews = relationship('Review', backref='users')
    