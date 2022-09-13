#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Represents a User for MySQL DB, containing various attributes

    Inherits the BaseModel and Base(from sqlalchemy) and links to the mysql table users

    Attributes:
      __tablename__(str): name of the MySQL table
      email(sqlalchemy String): email for the User
      password(sqlalchemy String): password for the User
      first_name(sqlalchemy String): first_name for the User
      last_name(sqlalchemy String): last_name for the User 
    """
    if models.storage_type == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        def __init__(self, email = "", password = "", first_name = "", last_name = ""):
            """ if storage type is not db (FileStorage) instantiate values """
            self.email = email
            self.password = password
            self.first_name = first_name
            self.last_name = last_name
            super().__init__()
