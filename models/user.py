#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import column, String


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__='users'

    email = column(String(128), nullable=False)
    password = column(String(128), nullable=False)
    first_name = column(String(128))
    last_name = column(String(128))
