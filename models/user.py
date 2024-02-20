#!/usr/bin/python3
"""This module defines a class User"""
import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
    The user attributes:
      email (str)
      password (str)
      first_name (str)
      last_name (str)
    """

    __tablename__ = "users"

    if storage_type == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")

    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
