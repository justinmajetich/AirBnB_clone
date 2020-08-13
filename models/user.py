#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel):
    """This class defines a user by various attributes"""


    __tablename__ = 
    email = Column(String(128), nullable 
    password = ''
    first_name = ''
    last_name = ''
