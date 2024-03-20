#!/usr/bin/python3
"""This module defines a class User"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from os import getenv

class User(BaseModel, Base):
    __tablename__ = 'users'

    # Columns
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Relationships
    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship('Place', backref='user', cascade='all, delete')
        reviews = relationship("Review", backref='user', cascade="all, delete")
