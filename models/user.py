#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, String, ForeignKey


class User(BaseModel, Base):
    """Name of table in database to link to"""
    __tablename__ = 'users'

    """This class defines a user by various attributes"""
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
