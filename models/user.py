#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ""
    password = ""
    first_name = ""
