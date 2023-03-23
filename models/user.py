#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'User'
    email = Column(String(128), primary_key=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
