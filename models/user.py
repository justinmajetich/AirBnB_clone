#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
<<<<<<< HEAD

    __tablename__ = "users"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
=======
    __tabelname__="users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship("Places", cascade="all, delete-orphan", backref="user")


>>>>>>> jose
