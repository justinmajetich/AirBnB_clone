#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


# commented out code base for task 7
# class User(BaseModel):
#     """File Storage Method for User"""
#     email = ''
#     password = ''
#     first_name = ''
#     last_name = ''

class User(BaseModel, Base):
    """
    Database Storage Method for User
    """
    __tablename__ = "users"
    email = Column(string(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(string(128), nullable=False)
    last_name = Column(string(128), nullable=False)
