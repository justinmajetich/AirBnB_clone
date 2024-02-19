#!/usr/bin/python3
"""This module defines a class User"""

import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Colum(String(128), nullable=True)
    password = Colum(String(128), nullable=True)
    first_name = Colum(String(128), nullable=True)
    last_name = Colum(String(128), nullable=True) 
