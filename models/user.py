#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
import os

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
    This class defines a user by various attributes. The user
    has differnt attributes:
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
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
