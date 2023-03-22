#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes

    Attributes:
            __tablename__(str): The name of the table in the database
            email(sqlalchemy String): user's email
            password(sqlalchemy String): user's password
            first_name(sqlalchemy String): user's first name
            last_name(sqlalchemy String): user's last name
    """

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
